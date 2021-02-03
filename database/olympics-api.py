#Auhtors:
#Valentina Guerrero
#Songyan Zhao

import sys
import argparse
import flask
import json
import psycopg2


from config import password
from config import database
from config import user


def run_query_no_search_string(query):
    connection = connect_database()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor
                
    except Exception as e:
        print(e)
        exit()

def run_query_one_search_string(query, search_string_one):
    connection = connect_database()
    
    try:
        cursor = connection.cursor()
        cursor.execute(query,(search_string_one,))
        return cursor
            
    except Exception as e:
        print(e)
        exit()
        
def run_query_two_search_strings(query, search_string_one, search_string_two):
    connection = connect_database()
    try:
        cursor = connection.cursor()
        cursor.execute(query,(search_string_one, search_string_two,))
        return cursor
            
    except Exception as e:
        print(e)
        exit()
        
                

def connect_database():
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
        return connection
    except Exception as e:
        print(e)
        exit()

app = flask.Flask(__name__)

@app.route('/games')
def games():
    games_list = []
    query = '''SELECT * FROM olympic_games
            ORDER BY 
                    olympic_games.year;'''

    cursor = run_query_no_search_string(query)
    
    for row in cursor:
        dictionary = {
            'id': row[0],
            'year': row[2],
            'season': row[3],
            'city': row[4]
        }
        games_list.append(dictionary)

    return json.dumps(games_list)

@app.route('/medalists/games/<games_id>')
def get_actor(games_id):
    athletes_list = []
    noc = flask.request.args.get('noc')
    query = ""
    search_string_one = games_id
    
    if noc is None:
        query = '''SELECT DISTINCT
                    athletes.id,
                    athletes.full_name,
                    athletes.sex,
                    medals.medal,
                    events.event_title,
                    sports.sport
                    FROM 
                        athletes,  
                        linking_table, 
                        olympic_games,
                        events,
                        medals,
                        sports
                    WHERE 
                        linking_table.olympic_game_id = olympic_games.id AND
                        olympic_games.id = %s AND
                        linking_table.athlete_id = athletes.id AND
                        linking_table.sport_id = sports.id AND
                        linking_table.medal_id = medals.id AND
                        medals.id != 1 AND 
                        linking_table.event_id = events.id
                    ORDER BY 
                        athletes.full_name;'''
        cursor = run_query_one_search_string(query, search_string_one)
        
        for row in cursor:
            athlete_dic = {
                'athletes':  row[0],
                'athlete_name': row[1],
                'athletes_sex': row[2],
                'medal':        row[3],
                'events':       row[4],
                'sports':       row[5]
            }
            athletes_list.append(athlete_dic)
    else:

        noc_upper = str(noc).upper()
        search_string_two = noc_upper
        query = '''SELECT DISTINCT
                athletes.id,
                athletes.full_name,
                athletes.sex,
                medals.medal,
                events.event_title,
                sports.sport
                FROM 
                    athletes,  
                    linking_table, 
                    olympic_games,
                    national_olympic_committees,
                    events,
                    medals,
                    sports
                WHERE 
                    linking_table.olympic_game_id = olympic_games.id AND
                    olympic_games.id = %s  AND
                    linking_table.athlete_id = athletes.id AND
                    linking_table.sport_id = sports.id AND
                    linking_table.medal_id = medals.id AND
                    medals.id != 1 AND 
                    linking_table.event_id = events.id AND
                    national_olympic_committees.abbreviation = %s AND
                    linking_table.national_olympic_committee_id = national_olympic_committees.id
                    
                ORDER BY 
                    athletes.full_name;'''
        cursor = run_query_two_search_strings(query, search_string_one, search_string_two)
        
        for row in cursor:
            athlete_dic = {
                'athletes':  row[0],
                'athlete_name': row[1],
                'athletes_sex': row[2],
                'medal':        row[3],
                'events':       row[4],
                'sports':       row[5]
            }
            athletes_list.append(athlete_dic)

    
    return json.dumps(athletes_list)

@app.route('/nocs')
def get_nocs():
    
    nocs_list = []
    query = '''SELECT * FROM national_olympic_committees'''

    cursor = run_query_no_search_string(query)
    
    for row in cursor:
        dictionary = {
            'abbreviation': row[1],
            'name': row[2]
        }
        nocs_list.append(dictionary)

    return json.dumps(nocs_list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('A sample Flask application/API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)