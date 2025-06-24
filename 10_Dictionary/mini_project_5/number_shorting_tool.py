number = input("enter number sepearted by comma: ")

num = number.split()

number_list = []

for i in num:
    number_list.append(i)

num_dict = {
    "original": number_list,
    "sorted": sorted(number_list)
}

print("Original numbers:", num_dict["original"])
print("Sorted numbers:  ", num_dict["sorted"])