

def add_new_number_to_tuple(previous_numbers, new_number):

	new_numbers = previous_numbers +(new_number)
	return new_numbers


def change_index_in_tuple():

	numbers = (1, 2, [3, 4],5)
	numbers[2][1] = 99
	return numbers

def convert_tuple_to_list_and_back():

	fruits = ('apple', 'banana', 'cherry')
	fruits_list = list(fruits)
	fruits_list.append('mango')
	updated_fruits = tuple(fruits)
	return updated_fruits

	

def unpack_tuple():

	numbers = (10, 20, 30, 40)
	
	return index_zero, index_one, first_index


def sum_each_array ():
	row_total = []

	for row in table:
		row_sum = sum(row)
		row_total.append(row_sum)

	return row_total


def sum_every_column(table)

	column_total = []
	number_of_colums = len(table)

	for column_index in range(number_of_colums):
		column_sum = 0

		for row in table:
			column_sum = column_sum + row[column_index]

		column_total.append(column_sum)

	return column_total

def is_even(number):
    return number % 2 == 0
 
 
def is_longer_than_five_letters(word):
    return len(word) > 5
 
 
def has_first_number_greater_than_two(pair):
    first_number = pair[0]
    return first_number > 2
 
 
def is_divisible_by_three_and_five(number):
    return number % 3 == 0 and number % 5 == 0
 
 
def is_palindrome(word):
    reversed_word = word[::-1]
    return word == reversed_word
 
 
def is_greater_than_five(number):
    return number > 5
 
 
def is_only_digits(text):
    return text.isdigit()
 
def get_even_numbers():
	numbers = range(1,21)
	even_numbers = filter(is_even, numbers)
	return list(even_numbers)

def get_words_greater_than_five(words):
	long_words = filter(is_longer_than_five_letters, words)
	return list(long_words)

def get_tuple_values_greater_than_two(pairs):
	matching_pairs = filter(has_first_value_greater_than_two, pairs)

def get_numbers_divisible_by_three_and_five():
	numbers = range(1,51)
	matching_numbers = filter(is_divisible_by_three_and_five, numbers)
	return list(matching_numbers)

def get_palindromes(words):
	palindromes = filter(is_palindrome, words)
	return list(palindromes)
	



 
def make_uppercase(word):
    return word.upper()
 
 
def square(number):
    return number * number
 
 
def capitalize_name(name):
    # "john" -> "John"
    return name.capitalize()
 
 
def add_ten_percent_tax(price):
    tax = price * 10 / 100
    return price + tax
 
 
def add_pair_together(pair):
    # (1, 2) -> 1 + 2 = 3
    return pair[0] + pair[1]
 
 
def convert_to_integer(text):
    # "123" -> 123
    return int(text)



def convert_to_uppercase(languages):
    uppercase_languages = map(make_uppercase, languages)
    return list(uppercase_languages)
 
 
def square_one_to_ten():
    numbers = range(1, 11)                        
    squared_numbers = map(square, numbers)
    return list(squared_numbers)
 
 
def capitalize_names(names):
    capitalized_names = map(capitalize_name, names)
    return list(capitalized_names)
 
 
def add_tax_to_prices(prices):
    prices_with_tax = map(add_ten_percent_tax, prices)
    return list(prices_with_tax)

def add_two_numbers(first_number, second_number):
    return first_number + second_number
 
 
def multiply_two_numbers(first_number, second_number):
    return first_number * second_number
 
 
def get_larger_number(first_number, second_number):
    if first_number > second_number:
        return first_number
    return second_number
 
 
def join_with_space(first_word, second_word):
    return first_word + " " + second_word
	

def sum_one_to_fifty():
    numbers = range(1, 51)
    total = reduce(add_two_numbers, numbers)
    return total
 

def find_maximum(numbers):
    largest_number = reduce(get_larger_number, numbers)
    return largest_number
 
 

def join_words(words):
    sentence = reduce(join_with_space, words)
    return sentence
 
 
def product_of_squares(numbers):
    squared_numbers = map(square, numbers)
 
    product = reduce(multiply_two_numbers, squared_numbers)
    return product
 
 

 
def get_pair_sums_above_five(pairs):
    pair_sums = map(add_pair_together, pairs)
 
    large_sums = filter(is_greater_than_five, pair_sums)
    return list(large_sums)
 
 
def sum_numeric_strings(data):
    numeric_strings = filter(is_only_digits, data)
 
    whole_numbers = map(convert_to_integer, numeric_strings)
 
    total = reduce(add_two_numbers, whole_numbers)
    return total






	