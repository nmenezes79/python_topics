# Recursive Functions = Functions calling themselves.

def count_toys(box):
	# Check if the box is empty
	if not box:
		print("Zero toys! Done!")
		return 0 # No toys left, so return 0
	
	# Take out one toy and count it
	toy = box.pop()
	print("One toy!", toy) # Say "One toy"

	# Recursively count the remaining toys in the box
	remaining_toys = count_toys(box)

	# Return the Total Count
	return 1 + remaining_toys

# Let's play with our magical toy counter friend Recursy!
toys_box = ["Teddy Bear", "LEGOs", "Doll", "Action Figure"]
total_toys = count_toys(toys_box)
print("Total toys in the box:", total_toys)