-- create role for project
create role atimaanav_bot with password 'password' with login;
grant all privileges on database atimaanav to atimaanav_bot;

-- create user table
create table user (id serial primary key, name character varying(200), password character varying(200), created timestamp with time zone, updated timestamp with time zone, ended timestamp with time zone);