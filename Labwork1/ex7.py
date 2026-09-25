def remove_dollar_sign(s):
    return s.replace('$', '')
test_string = "$100"
result = remove_dollar_sign(test_string)
print(result)  