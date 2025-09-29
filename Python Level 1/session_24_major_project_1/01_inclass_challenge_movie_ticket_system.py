# Movie Ticket Booking System
import sys

# Sample movies data
movies = {
    "1": {"name": "Inception", "price": 150, "seats": [[0]*5 for _ in range(5)]},
    "2": {"name": "Interstellar", "price": 180, "seats": [[0]*5 for _ in range(5)]},
    "3": {"name": "The Dark Knight", "price": 200, "seats": [[0]*5 for _ in range(5)]}
}

def display_movies():
    print("\nAvailable Movies:")
    for key, movie in movies.items():
        print(f"{key}. {movie['name']} - ₹{movie['price']} per ticket")

def display_seats(seats):
    print("\nSeat Layout (0 = Available, X = Booked):")
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            if seat == 0:
                print("0", end=" ")
            else:
                print("X", end=" ")
        print(f" <- Row {i+1}")
    print("Cols:  1 2 3 4 5\n")

def book_tickets(movie_key):
    movie = movies[movie_key]
    seats = movie["seats"]
    price = movie["price"]

    display_seats(seats)
    try:
        num = int(input("How many tickets do you want to book? "))
        booked = 0
        total_cost = 0

        while booked < num:
            row = int(input(f"Enter row (1-5) for ticket {booked+1}: ")) - 1
            col = int(input(f"Enter column (1-5) for ticket {booked+1}: ")) - 1

            if 0 <= row < 5 and 0 <= col < 5:
                if seats[row][col] == 0:
                    seats[row][col] = 1
                    booked += 1
                    total_cost += price
                    print(f"Seat ({row+1}, {col+1}) booked successfully.")
                else:
                    print("Seat already booked. Try a different seat.")
            else:
                print("Invalid seat location.")
        
        print(f"\nBooking complete! Total amount to pay: ₹{total_cost}")
        display_seats(seats)

    except ValueError:
        print("Invalid input. Please enter numeric values.")

def main():
    total_bill = 0
    while True:
        display_movies()
        choice = input("\nEnter movie number to book tickets or 'q' to quit: ").strip()
        if choice.lower() == 'q':
            print("\nThank you for using the Movie Ticket Booking System!")
            break
        elif choice in movies:
            book_tickets(choice)
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
