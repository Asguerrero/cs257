import csv

def read_athlete_csv():
    """
    Reads athlete_events.csv and returns lists.
    """
    athlete_events = []

    with open("athlete_events.csv", mode="r") as file:
        csvFile = csv.reader(file, delimiter=",")
        for line in csvFile:
            athlete_events.append(line)

    return (athlete_events)


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
            athlete_table.append([row[15], row[1], row[2], row[3], row[4], row[5]])

    with open('athlete.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(athlete_table)

    return athlete_events


def add_sport_ids(athlete_events):
    dict = {}
    counter = 0
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

    return athlete_events


def add_events_ids(athlete_events):
    dict = {}
    counter = 0
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

    return athlete_events


def add_games_ids(athlete_events):
    dict = {}
    counter = 0
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
    return athlete_events


def add_medal_ids(athlete_events):
    dict = {}
    counter = 0
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

    return athlete_events


def add_noc_id(athlete_events):
    dict = {}
    counter = 0
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
    print(dict)
    return athlete_events


def create_all_csv(athlete_events):
    id_fields = []
    for row in athlete_events:
        id_fields.append([row[15], row[16], row[17], row[18], row[19], row[20]])

    with open('all.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(id_fields)


test = read_athlete_csv()
second = add_athlete_ids(test)
third = add_sport_ids(second)
fourth = add_events_ids(third)
five = add_games_ids(fourth)
six = add_medal_ids(five)
seven = add_noc_id(six)
create_all_csv(seven)
