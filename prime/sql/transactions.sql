select @@autocommit;

SET autocommit = 0;

create database prime;

use prime;

create table accounts (
id int primary key auto_increment,
name varchar(50),
balance decimal(10, 2)
);

insert into accounts (name, balance) values
('Adam', 500.0) ,
('Bob', 300.0),
('Charlie', 1000.00);

select * from accounts;

start transaction;
update accounts set balance = balance - 50 where id = 1;
commit;
update accounts set balance = balance + 50 where id = 2;

rollback;

start transaction;
update accounts set balance = balance + 1000 where id = 1;
savepoint after_wallet_topup;
update accounts set balance = balance + 50 where id = 2;
-- error

rollback to after_wallet_topup;
commit;


select * from accounts;

