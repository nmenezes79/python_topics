# Movie Ticket Booking System with Enhanced Features

# Sample movies data with 5x10 seat layout (50 seats total)
movies = {
    "1": {"name": "Inception", "price": 150, "seats": [[0]*10 for _ in range(5)]},
    "2": {"name": "Interstellar", "price": 180, "seats": [[0]*10 for _ in range(5)]},
    "3": {"name": "The Dark Knight", "price": 200, "seats": [[0]*10 for _ in range(5)]},
    "4": {"name": "Avatar", "price": 170, "seats": [[0]*10 for _ in range(5)]},
    "5": {"name": "Tenet", "price": 160, "seats": [[0]*10 for _ in range(5)]}
}

def display_movies():
    print("\n🎬 Available Movies:")
    for key, movie in movies.items():
        seats_left = count_available_seats(movie["seats"])
        print(f"{key}. {movie['name']} - ₹{movie['price']} per ticket | Available Seats: {seats_left}")

def display_seats(seats):
    print("\n🪑 Seat Layout (0 = Available, X = Booked):")
    for i, row in enumerate(seats):
        for seat in row:
            print("X" if seat else "0", end=" ")
        print(f" <- Row {i+1}")
    print("Cols:  1 2 3 4 5 6 7 8 9 10\n")

def count_available_seats(seats):
    return sum(row.count(0) for row in seats)

def book_tickets(movie_key):
    movie = movies[movie_key]
    seats = movie["seats"]
    price = movie["price"]
    available = count_available_seats(seats)

    if available == 0:
        print("Sorry, all seats are booked for this movie.")
        return

    display_seats(seats)
    print(f"🎟️ Total available seats: {available}")
    
    try:
        num = int(input("How many tickets do you want to book? "))
        if num > available:
            print("❌ Not enough seats available.")
            return

        booked = 0
        total_cost = 0
        booked_positions = []

        while booked < num:
            row = int(input(f"Enter row (1-5) for ticket {booked+1}: ")) - 1
            col = int(input(f"Enter column (1-10) for ticket {booked+1}: ")) - 1

            if 0 <= row < 5 and 0 <= col < 10:
                if seats[row][col] == 0:
                    if (row, col) not in booked_positions:
                        seats[row][col] = 1
                        booked_positions.append((row, col))
                        booked += 1
                        total_cost += price
                        print(f"✅ Seat ({row+1}, {col+1}) booked.")
                    else:
                        print("⚠️ You already selected this seat. Choose a different one.")
                else:
                    print("❌ Seat already booked by someone. Choose another seat.")
            else:
                print("⚠️ Invalid seat location. Try again.")

        print(f"\n💰 Booking complete! Total amount to pay: ₹{total_cost}")
        display_seats(seats)

    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")

def main():
    while True:
        display_movies()
        choice = input("\nEnter movie number to book tickets or 'q' to quit: ").strip()
        if choice.lower() == 'q':
            print("\n🎉 Thank you for using the Movie Ticket Booking System!")
            break
        elif choice in movies:
            book_tickets(choice)
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
