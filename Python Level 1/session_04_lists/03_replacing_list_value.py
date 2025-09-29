# Replacing a single value by index
numbers = [10, 20, 30, 40, 50]
numbers[2] = 99 # Replacing the value at index 2
print(numbers) # Output: [10, 20, 99, 40, 50]

# Replacing a specfic value by searching
fruits = ["Apple", "Banana", "Cherry", "Grapes"]
fruits = ["Orange" if fruit == "Banana" else fruit for fruit in fruits]
print(fruits) # Output: ["Apple", "Orange", "Cherry", "Grapes"]

# Replacing multiple values using map()
nums = [1, 2, 3, 4, 5]
nums =list(map(lambda x : 99 if x == 3 else x, nums))
print(nums) # Output: [1, 2, 99, 4, 5]
