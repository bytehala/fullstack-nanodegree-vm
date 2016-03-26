-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


create table players (
    id SERIAL PRIMARY KEY,
    name varchar(40)
);

create table matches (
    player_a integer REFERENCES players(id),
    player_b integer REFERENCES players(id),
    winner integer REFERENCES players(id)
);