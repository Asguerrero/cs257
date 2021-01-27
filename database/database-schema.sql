CREATE TABLE athletes(
  id integer,
  full_name text
);

CREATE TABLE national_olympic_committees(
  id integer,
  abbreviation text, 
  country text
);

CREATE TABLE olympic_games(
  id integer, 
  game text
);


CREATE TABLE sports(
  id integer,
  sport text
);

CREATE TABLE events(
	id integer,
	event_title text
);

CREATE TABLE medals(
  id integer,
  medal text
);

CREATE TABLE linking_table(
  athlete_id integer,
  sport_id integer,
  event_id integer,
  olympic_game_id integer,
  medal_id integer,
  national_olympic_committee_id integer
);
