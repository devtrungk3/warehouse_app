USE WAREHOUSE;

create table role (
	id int primary key identity(1,1),
	name nvarchar(50) not null
)

create table account (
	id int primary key identity(1,1),
	username varchar(50) unique not null,
	fullname nvarchar(255),
	password nvarchar(255) not null,
	role_id int foreign key references role(id),
	created_at datetime default getdate()
)

create table category (
	id int primary key identity(1,1),
	name nvarchar(255) not null unique,
	created_at datetime default getdate()
)

create table product (
	id int primary key identity(1,1),
	name nvarchar(255) not null,
	unit nvarchar(10) not null,
	category_id int foreign key references category(id),
	created_at datetime default getdate()
)

create table inventory (
	id int primary key identity(1,1),
	product_id int foreign key references product(id) unique,
	quantity int not null,
	updated_at datetime default getdate()
)

create table partner (
	id int primary key identity(1,1),
	name nvarchar(50) not null,
	description nvarchar(255)
)

create table [order] (
	id int primary key identity(1,1),
	partner_id int foreign key references partner(id),
	type bit not null, -- 0: import, 1: export
	status int check (status>=0 and status<=2) not null, -- 0: accepted, 1: waiting, 2: canceled
	order_date datetime default getdate(),
	staff_id int foreign key references account(id)
)

create table order_item (
	id int primary key identity(1,1),
	order_id int foreign key references [order](id) on delete cascade,
	product_id int foreign key references product(id) on delete cascade,
	unit nvarchar(10) not null,
	quantity int not null
)

insert into role values (N'quản trị viên', N'Nhân viên')
insert into account (username, fullname, password, role_id) values ('admin', 'admin', '1234', 1)

SELECT 
    MONTH(order_date) AS month_number,
    COUNT(id)
FROM [order]
WHERE type = 0 -- 1 = export
    AND YEAR(order_date) = YEAR(GETDATE()) -- current year
GROUP BY MONTH(order_date), DATENAME(MONTH, order_date)