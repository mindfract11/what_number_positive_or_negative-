def filter_numbers(number_list):
    positive_numbers = []
    negative_numbers = []
    even_numbers = []
    odd_numbers = []

    for number in number_list:
        if number > 0:
            positive_numbers.append(number)
        elif number < 0:
            negative_numbers.append(number)
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    return positive_numbers, negative_numbers, even_numbers, odd_numbers
all_numbers = []
for i in range(10):
    user_input = int(input(f"Enter number {i+1}: "))
    all_numbers.append(user_input)
pos_list, neg_list, even_list, odd_list = filter_numbers(all_numbers)
print("All numbers:", all_numbers)
print("Positive numbers:", pos_list)
print("Negative numbers:", neg_list)
print("Even numbers:", even_list)
print("Odd numbers:", odd_list)