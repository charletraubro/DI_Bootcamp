-- -- Database: postgres

-- -- DROP DATABASE IF EXISTS postgres;

-- CREATE DATABASE postgres
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'C'
--     LC_CTYPE = 'C'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1;

-- COMMENT ON DATABASE postgres
--     IS 'default administrative connection database';

-- create table countries
-- (id serial primary key,
-- name varchar (100) );

-- insert into countries
-- values
-- (default,'USA' ),
-- (default, 'Mexico'),
-- (default, 'Canada'),
-- (default, 'Israel'),
-- (default, 'England'),
-- (default, 'France'),
-- (default, 'Belgium'),
-- (default, 'Brazil');

-- select a.actor_id, c.id
-- from actors as a 
-- inner join countries as c
-- on a.actor_id = c.id;

-- select actor_id from actors;

CREATE TABLE cars (
car_id SERIAL PRIMARY KEY,
car_color INTEGER REFERENCES colors (color_id) ON DELETE CASCADE,
car_name TEXT);

insert into cars values
(default,
(select color_id from colors where nam ilike '%black%'),
'Mitsubishi')