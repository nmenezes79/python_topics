# We have 3 rods: Source (A), Auxiliary (B), and Destination (C).
# The rule is: move n disks from Source to Destination using Auxiliary as helper.
# Recursive Logic:
# 1. Move n-1 disks from Source → Auxiliary (using Destination as helper).
# 2. Move the nth (largest) disk from Source → Destination.
# 3. Move n-1 disks from Auxiliary → Destination (using Source as helper).

def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    # Step 1: Move n-1 disks from source to auxiliary
    tower_of_hanoi(n-1, source, destination, auxiliary)
    
    # Step 2: Move the nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")
    
    # Step 3: Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n-1, auxiliary, source, destination)

# Example: Play with 3 disks
num_disks = 3
print(f"\nTower of Hanoi solution for {num_disks} disks:\n")
tower_of_hanoi(num_disks, 'A', 'B', 'C')
