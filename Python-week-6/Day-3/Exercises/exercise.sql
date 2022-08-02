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

--  CREATE TABLE customer(
--  id SERIAL PRIMARY KEY,
--  first_name VARCHAR (100),
--  last_name VARCHAR(100) NOT NULL);
 
--  insert into customer values
--  (default, 'John', 'Doe'),
--  (default,'Jerome','Lalu'),
--  (default,'Lea','Rive')
 
-- CREATE TABLE Customer_profile(
-- id serial,
-- isLoggedIn boolean DEFAULT False,
-- customer_id int,
-- Foreign Key (customer_id)  References customer(id),
-- constraint customer_constraint primary key (customer_id))
 
 insert into Customer_profile
 (default, 'John is loggedIn', default),
 (default, 'Jerome is not logged in', default)
 