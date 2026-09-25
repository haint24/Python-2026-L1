def extract_even (l):
    even_numbers = []
    for num in l:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
sample_list = [1, 4, 5, -1, 10]
result = extract_even(sample_list)
print(result)
