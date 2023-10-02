from math import factorial

def get_factorial(number):
    if  str(number).isdigit():
        output = f'The factorial is {factorial(int(number))}' 
    else:
        output = 'Not a valid input!'

    return output

def is_palindrome(word):
    if word == word[::-1]:
        output =  f'The word: {word} is a palindrome!'
    else:
        output = f'The word: {word} is not a palindrome!'
    
    return output

greeter = lambda str: 'Hello, %s' %str
