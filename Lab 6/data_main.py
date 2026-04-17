from data_package import remove_duplicates, strip_whitespaces, calculate_mean, find_maximum, find_minimum


def main():
    user_input = input("Enter a comma-separated list of numbers (e.g., 12, 5, 12, 8): ")

    raw_list = user_input.split(",")

    clean_strings = strip_whitespaces(raw_list)

    number_list = []
    for item in clean_strings:
        if item != "":
            number_list.append(float(item))


    final_data = remove_duplicates(number_list)

    print(f"Cleaned Dataset: {final_data}")
    print(f"Mean: {calculate_mean(final_data)}")
    print(f"Maximum: {find_maximum(final_data)}")
    print(f"Minimum: {find_minimum(final_data)}")


if __name__ == "__main__":
    main()