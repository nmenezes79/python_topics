# Copying a List
original_list = [1, 2, 3, 4]
copied_list = original_list.copy()
print("Original List:", original_list)
print("Copied List:", copied_list)

# Modifying the copied list won't affect the original list
copied_list.append(5)
print("After modifying Copied List:", copied_list)
print("Original List remains unchanged:", original_list)

# Copying a Dictionary
original_dict = {"a": 1, "b": 2, "c": 3}
copied_dict = original_dict.copy()
print("Original Dictonary:", original_dict)
print("Copied Dictonary:", copied_dict)

# Modifying the copied dictionary won't affect the original
copied_dict["d"] = 4
print("After modifying Copied Dictionary:", copied_dict)
print("Original Dictionary remains unchanged:", original_dict)