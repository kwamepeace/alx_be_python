CREATE DATABASE IF NOT EXISTS alx_book_store;
USE alx_book_store;

CREATE TABLE IF NOT EXISTS books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(130) NOT NULL,
    author_id  INT AUTO_INCREMENT FOREIGN KEY REFERENCES authors(author_id),
    price DOUBLE,
    publication_date DATE
);


CREATE TABLE IF NOT EXISTS authors (
    author_id  INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(215) NOT NULL,
    
);

CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) NOT NULL UNIQUE,
    address TEXT
);


CREATE TABLE IF NOT EXISTS orders (
    order_detail_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT AUTO_INCREMENT FOREIGN KEY REFERENCES customers(customer_id),
    order_date DATE,
);



CREATE TABLE IF NOT EXISTS order_Details (
    order_detail_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT AUTO_INCREMENT FOREIGN KEY REFERENCES orders(order_detail_id),
    book_id INT AUTO_INCREMENT FOREIGN KEY REFERENCES books(book_id),
    quantity DOUBLE
);