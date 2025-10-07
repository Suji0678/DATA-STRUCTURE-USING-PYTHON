num_keys = int(input("Enter number of keys in the dictionary: "))
my_dict = {}
keys = []
for i in range(num_keys):
    key = input(f"Enter key {i+1}: ")
    values = input(f"Enter letters for key '{key}' separated by spaces: ").split()
    my_dict[key] = values
    keys.append(key) 
def generate_combinations(index, current):
    if index == len(keys):
        print(''.join(current))
        return
    for letter in my_dict[keys[index]]:
        generate_combinations(index + 1, current + [letter])
print("\nAll combinations of letters:")
generate_combinations(0, [])

