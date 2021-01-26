import csv

def read_athlete_csv():
    athlete_events = []
    with open("athlete_events.csv", mode="r") as file:
        csvFile = csv.reader(file, delimiter=",")
        for line in csvFile:
            athlete_events.append(line)
    # Eliminate first row of the table with labels
    athlete_events.pop(0)
    return athlete_events


def read_noc_csv():
    noc_regions = []
    with open("noc_regions.csv", mode="r") as file:
        csvFile = csv.reader(file, delimiter=",")
        for line in csvFile:
            noc_regions.append(line)
    return noc_regions


def add_athlete_ids(athlete_events):

    dictionary = {}
    athlete_table = []
    counter = 0
    for row in athlete_events:
        name = row[1]
        try:
            # If the dictionary has a key that matches the name of the athlete, assign the corresponding id
            dictionary[name]
            id = dictionary[name]
            row.append(id)
        except:
            # If the dictionary does not have any key that matches the name, create a key with its corresponding id
            counter = counter + 1
            dictionary[name] = counter
            row.append(counter)
            athlete_table.append([row[15], row[1]])

    return athlete_events, athlete_table


def add_sport_ids(athlete_events):
    dictionary = {}
    counter = 0
    sports_table = []
    for row in athlete_events:
        name = row[12]
        try:
            dictionary[name]
            id = dictionary[name]
            row.append(id)

        except:
            counter = counter + 1
            dictionary[name] = counter
            row.append(counter)
            sports_table.append([row[16], row[12]])

    return athlete_events, sports_table


def add_events_ids(athlete_events):
    dictionary = {}
    counter = 0
    events_table = []
    for row in athlete_events:
        name = row[13]

        try:
            dictionary[name]
            id = dictionary[name]
            row.append(id)

        except:
            counter = counter + 1
            dictionary[name] = counter
            row.append(counter)
            events_table.append([row[17], row[13]])

    return athlete_events, events_table


def add_games_ids(athlete_events):
    dictionary = {}
    counter = 0
    games_table = []
    for row in athlete_events:
        name = row[8]
        try:
            dictionary[name]
            id = dictionary[name]
            row.append(id)

        except:
            dictionary[name] = counter
            counter = counter + 1
            row.append(counter)
            games_table.append([row[18], row[8]])

    return athlete_events, games_table


def add_medal_ids(athlete_events):
    dictionary = {}
    counter = 0
    medals_table = []
    for row in athlete_events:
        name = row[14]
        try:
            dictionary[name]
            id = dictionary[name]
            row.append(id)

        except:
            dictionary[name] = counter
            counter = counter + 1
            row.append(counter)
            medals_table.append([row[19], row[14]])

    return athlete_events, medals_table


def add_noc_id(athlete_events):
    dictionary = {}
    counter = 0
    noc_table = []
    for row in athlete_events:
        name = row[7]
        try:
            dictionary[name]
            id = dictionary[name]
            row.append(id)

        except:
            dictionary[name] = counter
            counter = counter + 1
            row.append(counter)
            noc_table.append([row[20], row[7]])

    return athlete_events, noc_table

def replace_null_entries_noc_table(noc_table):
    for row in noc_table:
        try:
            row[2]
        except:
            row.append('NULL') 


def create_csv(table, file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(table)

def create_noc_table_csv(noc_table, noc_regions, file_name):
    for row in noc_table:
        for noc in noc_regions:
            if row[1] == noc[0]:
                row.append(noc[1])

    replace_null_entries_noc_table(noc_table)

    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(noc_table)


def create_linking_table_csv(athlete_events, file_name):
    id_fields = []
    for row in athlete_events:
        id_fields.append([row[15], row[16], row[17], row[18], row[19], row[20]])

    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(id_fields)


def main():
    athlete_events = read_athlete_csv()
    noc_regions = read_noc_csv()

    # Add ids to all entities that have their own table in the database
    updated_athlete_events, athlete_table = add_athlete_ids(athlete_events)
    updated_athlete_events, sports_table = add_sport_ids(updated_athlete_events)
    updated_athlete_events, events_table = add_events_ids(updated_athlete_events)
    updated_athlete_events, games_table = add_games_ids(updated_athlete_events)
    updated_athlete_events, medals_table = add_medal_ids(updated_athlete_events)
    updated_athlete_events, noc_table = add_noc_id(updated_athlete_events)

    create_csv(athlete_table, 'athletes.csv')
    create_csv(sports_table, 'sports.csv')
    create_csv(events_table, 'events.csv')
    create_csv(medals_table, 'medals.csv')
    create_csv(games_table, 'olympic_games.csv')
    create_noc_table_csv(noc_table, noc_regions, 'national_olympic_committees.csv')
    create_linking_table_csv(updated_athlete_events, 'liking_table.csv')


main()

