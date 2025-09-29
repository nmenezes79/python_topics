def rental_car_cost(days):
    cost_per_day = 50
    discount = 0
    if days >= 7:
        discount = 50
    elif days >= 3:
        discount = 20
    total = (cost_per_day * days) - discount
    return total

def plane_ride_cost(city):
    city_fares = {
        "Delhi": 5000,
        "Mumbai": 4500,
        "Bangalore": 4000,
        "Kolkata": 5500,
        "Chennai": 4800
    }
    return city_fares.get(city, 5000)  # default if city not found

def hotel_cost(nights):
    cost_per_night = 100
    return cost_per_night * nights

def trip_cost(city, days, nights):
    total = rental_car_cost(days) + plane_ride_cost(city) + hotel_cost(nights)
    return total

# ---- Input Section ----
print("Welcome to Jack's Travel Cost Calculator!")

city = input("Enter the city you are traveling to (Delhi, Mumbai, Bangalore, Kolkata, Chennai): ")
days = int(input("Enter number of days you need a rental car: "))
nights = int(input("Enter number of nights you will stay in a hotel: "))

# ---- Output Section ----
print("\nCalculating your trip cost...\n")

print(f"Plane ride to {city}: ₹{plane_ride_cost(city)}")
print(f"Rental car for {days} days: ₹{rental_car_cost(days)}")
print(f"Hotel stay for {nights} nights: ₹{hotel_cost(nights)}")

total = trip_cost(city, days, nights)
print(f"\nTotal trip cost: ₹{total}")
