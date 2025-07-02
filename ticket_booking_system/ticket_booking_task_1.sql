-- 1
-- create database
create database ticketbookingsystem;

use ticketbookingsystem;

-- create table venue

create table venue
(
venue_id int primary key auto_increment,
venue_name varchar(100) not null,
address varchar(100) not null
);

desc venue;

-- create table booking

create table booking
(
booking_id int primary key auto_increment,
customer_id int references customer(customer_id),
event_id int references event(event_id),
num_tickets int not null,
total_cost decimal(10,2),
booking_date date
);

desc booking;

-- create table customer

create table customer
(
customer_id int primary key auto_increment,
customer_name varchar(100) not null,
email varchar(100) not null unique,
phone_number varchar(20) not null,
booking_id int references booking(booking_id)
);

desc customer;

-- create table event

create table event
(
event_id int primary key auto_increment,
event_name varchar(100) not null,
event_date date not null,
event_time time not null,
venue_id int references venue(venue_id),
total_seats int not null,
available_seats int not null,
ticket_price decimal(10,2),
event_type enum ('Movie','Sports','Concert'),
booking_id int references booking(booking_id)
);

desc event;







