import pandas as pd

# Sample data representing the unnormalized table
data = {
    "BookingID": ["B001", "B001", "B002", "B003", "B003", "B003"],
    "CustomerID": ["C001", "C001", "C002", "C001", "C001", "C001"],
    "CustomerName": ["Alice Brown", "Alice Brown", "Bob White", "Alice Brown", "Alice Brown", "Alice Brown"],
    "FlightID": ["F001", "F001", "F002", "F003", "F003", "F003"],
    "FlightName": ["Flight A", "Flight A", "Flight B", "Flight C", "Flight C", "Flight C"],
    "Date": ["2024-10-12", "2024-10-12", "2024-10-13", "2024-11-01", "2024-11-01", "2024-11-01"],
    "Price": [300, 300, 250, 400, 400, 400],
    "SeatNumber": ["12A", "12B", "15C", "8A", "8B", "8C"],
    "AirlineID": ["A001", "A001", "A002", "A003", "A003", "A003"],
    "AirlineName": ["SkyHigh", "SkyHigh", "AirWings", "FlyAway", "FlyAway", "FlyAway"]
}

# Create DataFrame
df = pd.DataFrame(data)

# 1NF: Ensure atomic values (already done since SeatNumbers are separated)
print("1NF Table:")
print(df)

# Decompose into separate tables for 2NF
bookings = df[['BookingID', 'CustomerID', 'FlightID', 'Date', 'Price', 'SeatNumber']]
customers = df[['CustomerID', 'CustomerName']].drop_duplicates()
flights = df[['FlightID', 'FlightName', 'AirlineID']].drop_duplicates()
airlines = df[['AirlineID', 'AirlineName']].drop_duplicates()

# Show 2NF tables
print("\nBookings (2NF):")
print(bookings)

print("\nCustomers (2NF):")
print(customers)

print("\nFlights (2NF):")
print(flights)

print("\nAirlines (2NF):")
print(airlines)

