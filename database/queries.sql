--- List all the NOCs (National Olympic Committees), in alphabetical order by abbreviation. 

SELECT abbreviation, country FROM national_olympic_committees ORDER BY abbreviation;

---List the names of all the athletes from Kenya. 
SELECT DISTINCT
    athletes.full_name,
    national_olympic_committees.country
FROM 
    athletes,  
    linking_table, 
    national_olympic_committees
WHERE 
    linking_table.national_olympic_committee_id = national_olympic_committees.id AND

    national_olympic_committees.abbreviation = 'KEN' AND

    linking_table.athlete_id = athletes.id
ORDER BY 
    athletes.full_name;

---List all the medals won by Greg Louganis, sorted by year. 
SELECT  
    olympic_games.game,
    medals.medal, 
    sports.sport,
    events.event_title
FROM 
    athletes,
    olympic_games,
    medals,
    sports,
    events,
    linking_table
WHERE
    linking_table.athlete_id = athletes.id AND
    athletes.full_name = 'Gregory Efthimios "Greg" Louganis' AND

    linking_table.medal_id = medals.id AND 
    medals.medal != 'NA' AND

    linking_table.sport_id = sports.id AND
    linking_table.event_id = events.id AND

    linking_table.olympic_game_id = olympic_games.id
ORDER BY 
    olympic_games.game;
