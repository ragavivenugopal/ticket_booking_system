-- 2.1 insert at least 10 sample records into each table.

insert into venue (venue_name,address) values
('Marina Hall','Chennai'),
('Abraham Hall','Nammakal'),
('Bombay Hall','Mumbai'),
('Catherine Hall','Coimbatore'),
('D Hall','Delhi'),
('Ethereum Hall','Andhra'),
('City Hall','Banglore'),
('Kerala Hall','Kerala'),
('Mary Hall','Chennai'),
('Cathy Hall','Namakkal');

select * from venue;

-- insert values into booking table

insert into booking(customer_id,event_id,num_tickets,total_cost,booking_date) values
(1, 1, 2, 4000.00, '2025-06-01'),
(2, 2, 3, 2250.00, '2025-06-02'),
(3, 3, 1, 1500.00, '2025-06-03'),
(4, 4, 5, 6000.00, '2025-06-04'),
(5, 5, 2, 2000.00, '2025-06-05'),
(6, 6, 4, 10000.00, '2025-06-06'),
(7, 7, 1, 1800.00, '2025-06-07'),
(8, 8, 3, 2700.00, '2025-06-08'),
(9, 9, 2, 3400.00, '2025-06-09'),
(10, 10, 1, 2100.00, '2025-06-10');

select * from booking;

-- insert values into customer table

insert into customer (customer_name,email,phone_number,booking_id) values
('Anbu','anbu@gmail.com','9999999999',1),
('Babu','babu@gmail','8888888888',2),
('Cam','cam@gmail.com','7777777777',3),
('Evan','evan@gmail.com','6666666666',4),
('Deva','deva@gmail.com','5555555555',5),
('Sam','sam@gmail.com','8989765789',6),
('Ram','ram@gmail.com','9898767898',7),
('Som','soom@gmail.com','9878987657',8),
('Sona','sona@gmail.com','9876898765',9),
('Mona','mano@gmail.com','7898765789',10);

select * from customer;

-- insert values into event table

insert into event(event_name,event_date,event_time,venue_id,total_seats,available_seats,ticket_price,event_type,booking_id) values
('Rock Concert', '2025-07-15', '19:00:00', 1, 5000, 3500, 2000.00, 'Concert',1),
('Comedy Play', '2025-07-10', '18:00:00', 2, 800, 600, 750.00, 'Movie',2),
('Indie Music Fest', '2025-08-01', '20:00:00', 3, 2000, 1800, 1500.00, 'Concert',3),
('Football Finals', '2025-07-25', '17:30:00', 4, 15000, 14000, 1200.00, 'Sports',4),
('Dance Drama', '2025-07-18', '18:30:00', 5, 700, 500, 1000.00, 'Movie',5),
('Cricket Cup', '2025-08-20', '16:00:00', 6, 25000, 20000, 2500.00, 'Sports',6),
('Jazz Night', '2025-08-05', '20:30:00', 7, 1000, 950, 1800.00, 'Concert',7),
('Stage Play: Hamlet', '2025-07-22', '18:00:00', 8, 600, 480, 900.00, 'Movie',8),
('Wrestling Mania', '2025-08-10', '19:00:00', 9, 10000, 9800, 1700.00, 'Sports',9),
('Rock Revival', '2025-09-01', '20:00:00', 10, 3000, 2500, 2100.00, 'Concert',10);

select * from event;

-- 2.2 list all Events.

select * from event;
select event_name from event;

-- 2.3 select events with available tickets.

select * from event
where available_seats > 0;

-- 2.4 select events name partial match with ‘cup’ 'com'

select * from event
where event_name like '%com%';

-- 2.5 select events with ticket price range is between 1000 to 2500ww

select * from event
where ticket_price between 1000 and 2500;

-- 2.6 retrieve events with dates falling within a specific range.

select * from event
where event_date between '2025-07-15' and '2025-08-10';

-- 2.7 retrieve events with available tickets that also have "Concert" in their name.

select * from event
where available_seats>0 and event_type='Concert';

-- 2.8 retrieve users in batches of 5 (3), starting from the 6th user.

select * from customer
limit 3 offset 5;

-- 2.9 retrieve bookings details contains booked no of ticket more than 4.

select * from booking
where num_tickets>4;

-- 2.10 retrieve customer information whose phone number end with ‘000’ '666'

select * from customer
where phone_number like '%_______666%';

select * from customer
where phone_number like '%666';


-- 2.11 retrieve the events in order whose seat capacity more than 15000 (800)

select * from event
where total_seats>800
order by total_seats;

-- 2.12 select events name not start with ‘x’, ‘y’, ‘z’ -> 'r'

select * from event
where event_name not like 'x%' 
and event_name not like 'y%' 
and event_name not like 'r%';

select * from event
where event_name not regexp '^[xXyYrR]';