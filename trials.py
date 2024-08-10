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
    #snakecase= snake_case camelcase = camelCaseBro
    #check that string exists
    if not string:
        return string
        #if not, return the string

    #create empty string var
    only_camel = ''

    #create arr var to hold arr of string words split on'_'
    arr_of_str = string.split('_')
    #loop over arr of str words
    for word in arr_of_str:
        #add current word with the first letter capitalized to only_camel
        only_camel += word.capitalize()
    #return camel str
    return only_camel

    # for word in string.pop('')

print(snake_to_camel('this_is_snake'))
print(snake_to_camel('this_is_snake_so_is_this'))

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

#given two strings return third string that contains odd index items from 1st lst
#and even index items fron 2nd lst
def mix_lists(list_1, list_2):
    #create empty lst to hold odd indexs items from list 1
    odd = []
    #create empty lst to even index items from lst 2
    even = []
    #loop over lst 1 using enumerate
    for i, num in enumerate(list_1):
        #if index is not even using modulu
        if i % 2 != 0:
            #add to odd lst
            odd.append(num)
    #loop over lst_2 using enumerate
    for j, num_2 in enumerate(list_2):
        #if index is even
        if j % 2 == 0:
            #add to even lst
            even.append(num_2)

    #return third lst
    return (odd + even)

print(mix_lists([0, 1, 2, 3, 4], [0, 9, 8, 7, 6]))


def chop_and_attach(list_1):
    new_lst = [0, 1, 2, 3, 4, 5, 4, 5, 6, 7]
    list_1[2] = list_1[4]
    list_1[-1] = list_1[4]
    list_1.pop(list_1[4])
    return list_1

print(chop_and_attach([0, 1, 2, 3, 4, 5, 6]))