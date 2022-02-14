-- Disable foreign keys
PRAGMA foreign_keys = OFF;

DROP TABLE IF EXISTS order_status;
DROP TABLE IF EXISTS customer_ord_lines;
DROP TABLE IF EXISTS customer_orders;
DROP TABLE IF EXISTS weather;

-- Enable foreign keys
PRAGMA foreign_keys = ON;


-- Create the tables

CREATE TABLE order_status (
    order_status_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE customer_ord_lines (
    customer_ord_lines_id INTEGER PRIMARY KEY,
    order_number TEXT NOT NULL,
    item_name TEXT NOT NULL,
    order_status_id INTEGER NOT NULL,
    FOREIGN KEY (order_status_id)
        REFERENCES order_status ( order_status_id )
);

CREATE TABLE customer_orders (
    ord_id TEXT NOT NULL,
    ord_dt TEXT NOT NULL,
    qt_ordd INTEGER NOT NULL
);

CREATE TABLE weather (
    "date" TEXT NOT NULL,
    was_rainy INTEGER NOT NULL
);

-- Populate the tables

INSERT INTO order_status (order_status_id, name)
VALUES
    (1, "CANCELLED"),
    (2, "SHIPPED"),
    (3, "PENDING");

INSERT INTO customer_ord_lines (order_number, item_name, order_status_id)
VALUES
    ("ORD_1567", "LAPTOP", 2),
    ("ORD_1567", "MOUSE", 2),
    ("ORD_1567", "KEYBOARD", 3),
    ("ORD_1234", "GAME", 2),
    ("ORD_1234", "BOOK", 1),
    ("ORD_1234", "BOOK", 1),
    ("ORD_9834", "SHIRT", 2),
    ("ORD_9834", "PANTS", 1),
    ("ORD_7654", "TV", 1),
    ("ORD_7654", "DVD", 1);

INSERT INTO customer_orders (ord_id, ord_dt, qt_ordd)
VALUES
    ("113-8909896-6940269", date("2019-09-23"), 1),
    ("114-0291773-7262677", date("2020-01-01"), 1),
    ("114-0291773-7262697", date("2019-12-05"), 1),
    ("114-9900513-7761000", date("2020-09-24"), 1),
    ("112-5230502-8173028", date("2020-01-30"), 1),
    ("112-7714081-3300254", date("2020-05-02"), 1),
    ("114-5384551-1465853", date("2020-04-02"), 1),
    ("114-7232801-4607440", date("2020-10-09"), 1);

INSERT INTO weather ("date", was_rainy)
VALUES
    (date("2020-01-01"), 0),
    (date("2020-01-02"), 1),
    (date("2020-01-03"), 1),
    (date("2020-01-04"), 0),
    (date("2020-01-05"), 0),
    (date("2020-01-06"), 1),
    (date("2020-01-07"), 0),
    (date("2020-01-08"), 1),
    (date("2020-01-09"), 1),
    (date("2020-01-10"), 1);
