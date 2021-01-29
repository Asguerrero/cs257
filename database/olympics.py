# Author: Valentina Guerrero

import argparse
import psycopg2

# database = ' '
# user = ' '
# password = ' '


'''
Import the information about the database in question from a file called config.py
'''
from config import password
from config import database
from config import user



def connect_database():
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
        return connection
    except Exception as e:
        print(e)
        exit()


def search_athletes_by_noc(string):
    '''
    This method connects to the olympics database, searches for all the athletes from a specific national olympic committee
    and returns the results through a cursor.  
    '''

    # Given that all the entries in the database are capitalized, 
    # capitalize the first letter of the input given by the user
    search_string = string.capitalize()
    connection = connect_database()
    query = '''SELECT DISTINCT
                athletes.full_name,
                national_olympic_committees.country
            FROM 
                athletes,  
                linking_table, 
                national_olympic_committees
            WHERE 
                linking_table.national_olympic_committee_id = national_olympic_committees.id AND
                national_olympic_committees.country = %s AND
                linking_table.athlete_id = athletes.id
            ORDER BY 
                athletes.full_name;'''

    try:
        cursor = connection.cursor()
        cursor.execute(query, (search_string,))
        return cursor
    except Exception as e:
        print(e)
        exit()



def search_gold_medals_by_noc(string):
    '''
    This method connects to the olympics database and returns a cursor with all the NOCs 
    and the number of gold medals they have won, in decreasing order of the number of gold medals.  
    '''

    season_string = string.split(' ')
    season_capitalized = season_string[1].capitalize()
    search_string = season_string[0] + season_capitalized


    connection = connect_database()
    query = '''SELECT 
                    national_olympic_committees.country,
                    COUNT(*) AS gold_medals
                FROM
                    national_olympic_committees,
                    linking_table,
                    medals
                WHERE 
                    linking_table.medal_id = medals.id AND
                    medals.medal = 'Gold' AND
                    linking_table.national_olympic_committee_id = national_olympic_committees.id
                GROUP BY 
                    national_olympic_committees.country
                ORDER BY 
                    gold_medals DESC;'''

    try:
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor
    except Exception as e:
        print(e)
        exit()

def search_athletes_by_olympic_game(string):
    '''
    This method connects to the olympics database and returns a cursor with the name of all athletes
    that participated in the olympic game entered by the user  
    '''

    search_string = string
    connection = connect_database()
    query = '''SELECT DISTINCT
                athletes.full_name,
                olympic_games.game
                FROM 
                    athletes,  
                    linking_table, 
                    olympic_games
                WHERE 
                    linking_table.olympic_game_id = olympic_games.id AND
                    olympic_games.game = %s AND
                    linking_table.athlete_id = athletes.id
                ORDER BY 
                    athletes.full_name;'''

    try:
        cursor = connection.cursor()
        cursor.execute(query, (search_string,))
        return cursor
    except Exception as e:
        print(e)
        exit()


def print_results(cursor):
    for row in cursor:
        print(f'{row[0]}: {row[1]}')
    print()


def get_arguments():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a", "--athletes", action="store_true", help="Displays the names of all the athletes from a specified National Olympic Committee. \n " 
                                                                    "Accepts as input one string that should represent the name of a national olympic committee \n"
                                                                    "Example: --athletes Colombia or -a Colombia")

    group.add_argument("-gm", "--gold", action="store_true", help="Displays all the NOCs and the number of gold medals they have won in decreasing order of the number of gold medals. \n " 
                                                                "This command does not requiere any additional input. \n"
                                                                "Example: --gold or -gm")
    group.add_argument("-g", "--game", action="store_true", help="Displays the names of all athletes that participated in an specified instance of the Olympic Games.\n " 
                                                                "Accepts as input the year and season of an specific Olympic Game. \n"
                                                                "Both values should be between quotes. The year should go first and the season second.\n"
                                                                "Example: --game '2012 Summer' or -g '2012 Summer' ")
    parser.add_argument("Input", nargs="*", type=str, help="The search string")

    args = parser.parse_args()

    return args


def main():
    args = get_arguments()

    if args.athletes and args.Input[0]:
        print(f'All athletes from {args.Input[0]}')
        print('----------------------------------------------')
        results = search_athletes_by_noc(str(args.Input[0]))
        print_results(results)

    elif args.gold:
        print(f'Gold medals of all National Olympic Committees')
        print('----------------------------------------------')
        results = search_gold_medals_by_noc()
        print_results(results)

    elif args.game and args.Input[0]:
        print(f'All athletes that participated in {args.Input[0]}')
        print('----------------------------------------------')
        results = search_athletes_by_olympic_game(str(args.Input[0]))
        print_results(results)




main()
