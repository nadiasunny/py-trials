"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    """ loop over items list and print each item"""
    for item in items:
        print(item)


def get_all_evens(nums):
    """ Given nums, return an arr of only even numbers in num"""
    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums


def get_odd_indices(items):
    """ Given items list, return list of elements at odd indices"""
    odd_indices = []

    for i in range(len(items)):
        if i % 2 != 0:
            odd_indices.append(items[i])

    return odd_indices


def print_as_numbered_list(items):
    """ Given a list, output a numbered list
    1. items[0] etc.
    """
    list_num = 1

    for item in items:
        print(f'{list_num}. {item}')
        list_num+=1


def get_range(start, stop):
    """ given a start & stop, return list of numbers from start(inclusive-stop(exclusive)"""
    nums = []

    for num in range(start, stop):
        nums.append(num)
    
    return nums

def censor_vowels(word):
    """given a word string, for each vowel in string, replace w/'*'"""
    chars = []

    for letter in word:
        if letter in 'aeiou':
            chars.append('*')
        else:
            chars.append(letter)

    return ''.join(chars)


def snake_to_camel(string):
    """Given a string in snake case, return a string in camel case"""
    pass
    # camelCase = []

    # for char, i in string:
    #     if string[i] == ''

    # for word in string.pop()

def longest_word_length(words):
    biggest = words[0]
    for word in words:
        if len(word) > len(biggest):
            biggest = word
    return biggest

    
print(longest_word_length(['I', 'am', 'cool', 'my', 'man', 'coooool']))


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
