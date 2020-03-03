def main():
    userInteger = 0
    userInteger = int(input('Please enter an even integer. '))
    while userInteger % 2 != 0:
        userInteger = int(input('Please enter an even integer. '))
    if userInteger % 2 == 0:
        print('Thank you.')
main()
    
