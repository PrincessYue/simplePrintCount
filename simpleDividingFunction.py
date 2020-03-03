def main():
    firstNumber = int(input('Please enter the first number. '))
    secondNumber = int(input('Please enter the second number. '))
    divide(firstNumber, secondNumber)

def divide(firstNumber, secondNumber):
    quotientOfNumbers = firstNumber / secondNumber
    print('The quotient of the two numbers you entered is ', format(quotientOfNumbers,',''.1f'),sep='')
main()
