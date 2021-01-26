import csv

def read_athlete_csv():
    athlete_events = []

    with open("athlete_events.csv", mode="r") as file:
        csvFile = csv.reader(file, delimiter=",")
        for line in csvFile:
            athlete_events.append(line)

    return (athlete_events)

def read_noc_csv():
    noc_regions = []
    with open("noc_regions.csv", mode="r") as file:
        csvFile = csv.reader(file, delimiter=",")
        for line in csvFile:
            noc_regions.append(line)
    return (noc_regions)


def add_athlete_ids(athlete_events):
    athlete_events.pop(0)
    dict = {}
    athlete_table = []
    counter = 0
    for row in athlete_events:
        name = row[1]
        try:
            dict[name]
            id = dict[name]
            row.append(id)
        except:
            counter = counter + 1
            dict[name] = counter
            row.append(counter)
            athlete_table.append([row[15], row[1]])

    return athlete_events, athlete_table


def add_sport_ids(athlete_events):
    dict = {}
    counter = 0
    sports_table = []
    for row in athlete_events:
        name = row[12]
        try:
            dict[name]
            id = dict[name]
            row.append(id)

        except:
            counter = counter + 1
            dict[name] = counter
            row.append(counter)
            sports_table.append([row[16], row[12]])

    return athlete_events, sports_table


def add_events_ids(athlete_events):
    dict = {}
    counter = 0
    events_table = []
    for row in athlete_events:
        name = row[13]

        try:
            dict[name]
            id = dict[name]
            row.append(id)

        except:
            counter = counter + 1
            dict[name] = counter
            row.append(counter)
            events_table.append([row[17], row[13]])

    return athlete_events, events_table


def add_games_ids(athlete_events):
    dict = {}
    counter = 0
    games_table = []
    for row in athlete_events:
        name = row[8]
        try:
            dict[name]
            id = dict[name]
            row.append(id)

        except:
            dict[name] = counter
            counter = counter + 1
            row.append(counter)
            games_table.append([row[18],row[8]])

    return athlete_events, games_table


def add_medal_ids(athlete_events):
    dict = {}
    counter = 0
    medals_table =[]
    for row in athlete_events:
        name = row[14]
        try:
            dict[name]
            id = dict[name]
            row.append(id)

        except:
            dict[name] = counter
            counter = counter + 1
            row.append(counter)
            medals_table.append([row[19], row[14]])

    return athlete_events, medals_table


def add_noc_id(athlete_events):
    dict = {}
    counter = 0
    noc_table = []
    for row in athlete_events:
        name = row[7]
        try:
            dict[name]
            id = dict[name]
            row.append(id)

        except:
            dict[name] = counter
            counter = counter + 1
            row.append(counter)
            noc_table.append([row[20], row[7]])

    return athlete_events, noc_table


def create_csv(table, file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(table)
    

def create_all_ids_csv(athlete_events):
    id_fields = []
    for row in athlete_events:
        id_fields.append([row[15], row[16], row[17], row[18], row[19], row[20]])

    with open('all.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(id_fields)

def create_athlete_table(athlete_table):
    with open('athlete.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(athlete_table)

def create_sports_table(sports_table):
    with open('sports.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(sports_table)

def create_events_table(events_table):
    with open('events.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(events_table)

def create_medal_table(medal_table):
    with open('medal.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(medal_table)

def create_games_table(games_table):
    with open('games.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(games_table)

def create_noc_table(noc_table, noc_regions):
    for row in noc_table:
        for noc in noc_regions:
            if row[1] == noc[0]:
                row.append(noc[1])
    with open('noc.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(noc_table)

def create_updated_athlete_events(updated_table):
    with open('updated_athlete_events.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(updated_table)




def main():
    athlete_events = read_athlete_csv()
    noc_regions = read_noc_csv()
    updated_athlete_events, athlete_table = add_athlete_ids(athlete_events)
    updated_athlete_events, sports_table = add_sport_ids(updated_athlete_events)
    updated_athlete_events, events_table = add_events_ids(updated_athlete_events)
    updated_athlete_events, games_table = add_games_ids(updated_athlete_events)
    updated_athlete_events, medals_table = add_medal_ids(updated_athlete_events)
    updated_athlete_events, noc_table = add_noc_id(updated_athlete_events)
    create_all_ids_csv(updated_athlete_events)
    create_athlete_table(athlete_table)
    create_sports_table(sports_table)
    create_events_table(events_table)
    create_updated_athlete_events(updated_athlete_events)
    create_medal_table(medals_table)
    create_games_table(games_table)
    create_noc_table(noc_table, noc_regions)

main()
