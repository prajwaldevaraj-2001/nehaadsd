-- 1NF: Create the Bookings table with atomic values
CREATE TABLE Bookings (
    BookingID TEXT,
    CustomerID TEXT,
    FlightID TEXT,
    Date TEXT,
    Price INTEGER,
    SeatNumber TEXT
);

-- 2NF: Create Customers, Flights, and Airlines tables
CREATE TABLE Customers (
    CustomerID TEXT PRIMARY KEY,
    CustomerName TEXT
);

CREATE TABLE Flights (
    FlightID TEXT PRIMARY KEY,
    FlightName TEXT,
    AirlineID TEXT
);

CREATE TABLE Airlines (
    AirlineID TEXT PRIMARY KEY,
    AirlineName TEXT
);

-- Insert data into the tables
-- Repeat similar commands for each table (Bookings, Customers, etc.)
