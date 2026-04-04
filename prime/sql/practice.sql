create database college;
create database xyz_company;

drop database xyz_company;
use college;

create table student (
rollno int,
name varchar(30),
age int
);

insert into student
values (101, "Adam", 12),
(102, "Bob", 14);

select * from student;

drop database if exists student;

create database if not exists instagram;

use instagram;

create table users (
	id int,
    age int,
    name varchar(20) not null,
    email varchar(30) unique,
    followers int default 0,
    following int default 0,
    constraint age_check check (age >= 13),
    primary key (id)
);

drop table  if exists users;

create table post (
id int primary key,
content varchar(100),
user_id int,
foreign key (user_id) references users(id)
);

insert into user
(id, name, email, following)
values 
(10,  "adam", "ada@yahoo.in", 145),
(11,  "Bob", "bob12@gmail.com",  200),
(12,  "Casey", "cae@gmail.com",  306),
(13,  "Donald", "doal@gmail.com",  105);

select id, name from users;

select * from users;

select distinct age from users;

select name, age
from users
where age < 16;

select name, age
from users
where age + 1 = 18;

select name, age, followers 
from users
where age > 15 and followers > 200;

select name, age, followers 
from users
where age > 15 or followers > 200;

select name, age, followers
from users
where age between 15 and 17;

select name, age, followers
from users
where email in ("donald@gmail.com", "bob123@gmail.com", "abc@gmail.com");

select name, followers, email
from users
where age in (14, 16);

select name, followers, email
from users
where age not in (14, 16);

select name, followers, email
from users
where age > 14 
limit 2;

select name, age, followers
from users
order by followers asc;


select max(followers) from users;

select max(age) from users;

select count(age)
from users
where age = 14;

select min(age)
from users;

select avg(age) 
from users;

select sum(age)
from users;

select count(id)
from users 
group by age;

select age, max(followers)
from users
group by age;

select age, max(followers)
from users
group by age
having max(followers) > 200
order by age desc; -- applies filter only on the group whereas where applies on all rows

update users
set followers = 600
where age = 16;

set sql_safe_updates = 0;

select * from users;

delete from users
where age = 14;

alter table users 
add column city varchar(25) default "Delhi";

alter table users
rename to user;

alter table user
drop column age;

alter table user
change column followers subs int default 0;

alter table user
modify subs int default 5;

select * from user;

drop table post;

truncate table user;

drop table user;

-- practice q

create database if not exists college2;

create table teacher (
id int,
name varchar(50),
subject varchar(50),
salary int

);

insert into teacher (id , name , subject, salary ) values 
(23, 'ajay', 'math', 50000),
(47, 'bharat', 'english', 60000),
(18, 'chetan', 'chemistry', 45000),
(9, 'divya', 'physics', 75000);

select * from teacher;

select * from teacher 
where salary > 55000;

alter table teacher
change column salary ctc int;

update teacher 
set ctc = ctc + ctc * 0.25;

alter table teacher
add column city varchar(50) default "Gurgaon";

alter table teacher
drop column ctc;

create table student (
rollno int primary key,
name varchar(30),
city varchar(30),
marks int
);

insert into student 
(rollno, name, city, marks)
values
(110, "adam", "Delhi", 76),
(108, "bob", "Mumbai", 65),
(124, "casey", "Pune", 94),
(112, "duke", "Pune", 80);

select * from student;

select * from student
where marks > 75;

select distinct city from student;

select city, max(marks)
from student
group by city;


select avg(marks) 
from student;

alter table student
add column grade varchar(2);

update student
set grade = "O"
where marks >= 80;

update student
set grade = "A"
where marks >= 70 and marks < 80;

update student
set grade = "B"
where marks >= 60 and marks < 70;









