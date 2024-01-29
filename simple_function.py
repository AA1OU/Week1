def add_two_numbers(number1, number2):
    """
    Add two numbers and print the results in a formatted manner.
    
    keyword arguements:
    number1 - left operand
    number2 - right operand
    """
    summed = number1 + number2
    print(f'{number1} + {number2} = {summed}')

if __name__ == '__main__':
    add_two_numbers(4, 5)