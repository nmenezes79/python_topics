# Vehicle Management System

# Store data as list of tuples: [(vehicle_number, duration, entry_time)]
parking_data = []

def entry():
    print("\n--- Vehicle Entry ---")
    vehicle_number = input("Enter Vehicle Number: ")
    duration = float(input("Enter Duration (in hours, e.g., 1.5, 2.0): "))
    entry_time = float(input("Enter Entry Time (24-hour format, e.g., 9.30, 14.00): "))
    
    # Calculate fees (₹20 per half hour)
    fee = (duration / 0.5) * 20
    print(f"Parking Fee: ₹{fee:.2f}")
    
    # Save vehicle data
    parking_data.append((vehicle_number, duration, entry_time))

def exit():
    print("\n--- Vehicle Exit ---")
    vehicle_number = input("Enter Vehicle Number: ")
    exit_time = float(input("Enter Exit Time (24-hour format, e.g., 12.30): "))
    
    # Search for vehicle entry
    for i in range(len(parking_data)):
        if parking_data[i][0] == vehicle_number:
            duration = parking_data[i][1]
            entry_time = parking_data[i][2]
            
            actual_duration = round(exit_time - entry_time, 2)
            paid_duration = duration
            
            print(f"Paid Duration: {paid_duration} hours")
            print(f"Actual Duration: {actual_duration} hours")

            if actual_duration <= paid_duration:
                print("No extra charges. Thank you!")
            else:
                extra_time = actual_duration - paid_duration
                # Round to nearest 0.5
                extra_time_rounded = round((extra_time + 0.25) // 0.5 * 0.5, 2)
                extra_fee = (extra_time_rounded / 0.5) * 30
                print(f"Overstay Detected! Extra Fee: ₹{extra_fee:.2f}")
            
            # Remove the vehicle record
            parking_data.pop(i)
            return
    
    print("Vehicle not found!")

# Main program
while True:
    print("\n==== Vehicle Parking System ====")
    print("1. Entry")
    print("2. Exit")
    print("3. Exit Program")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        entry()
    elif choice == '2':
        exit()
    elif choice == '3':
        print("Exiting Program. Have a great day!")
        break
    else:
        print("Invalid choice. Try again.")
