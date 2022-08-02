-- Database: hr.backup

-- -- DROP DATABASE IF EXISTS "hr.backup";

-- CREATE DATABASE "hr.backup"
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'C'
--     LC_CTYPE = 'C'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1;

--select first_name as "First Name", last_name as "Last Name" from employees;
--select distinct employee_id from employees 
--select * from employees order by first_name desc
--select first_name, last_name,salary, (salary*0.85) as PF from employees
--select employee_id, first_name, last_name, salary from employees order by salary asc
--select sum(salary) from employees
--select min(salary), max(salary) from employees
--select avg(salary) from employees
--select count(employee_id) from employees
--select UPPER(first_name) from employees
--select SUBSTRing(first_name, 1,3) from employees
--select Concat(first_name, ' ', last_name) as full_name from employees
--select first_name, last_name, LENGTH(first_name)+ LENGTH(last_name) from employees
--select first_name from employees where first_name like '%[0-9]%';
--select * from employees LIMIT 11

--select first_name, last_name, salary from employees where salary between 10000 and 15000
-- select first_name, last_name, hire_date from employees WHERE TO_CHAR(hire_date, 'YYYY')  LIKE '%87'
--select first_name from employees where first_name like '%c%' and first_name like '%e%'




