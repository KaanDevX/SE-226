def calculate_mean(num_list):
    if len(num_list) == 0:
        return "Error: The list is empty!"
    return sum(num_list) / len(num_list)

def find_maximum(num_list):
    if len(num_list) == 0:
        return "Error: The list is empty!"
    return max(num_list)

def find_minimum(num_list):
    if len(num_list) == 0:
        return "Error: The list is empty!"
    return min(num_list)