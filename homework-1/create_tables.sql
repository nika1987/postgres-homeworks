-- SQL-команды для создания таблиц
CREATE TABLE employees
(
  employee_id serial PRIMARY KEY,
  first_name varchar(100) NOT NULL,
  last_name varchar(100),
  title text,
  birth_date date,
  notes text
);
CREATE TABLE customers
(
	customer_id varchar(30) PRIMARY KEY,
	company_name char (50),
	contact_name char (50)
);

CREATE TABLE orders
(order_id int PRIMARY KEY,
customer_id varchar(20) REFERENCES customers(customer_id),
 employee_id int REFERENCES employees(employee_id),
 order_date date,
 ship_city varchar(20)
)
