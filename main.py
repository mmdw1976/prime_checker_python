check = True

while check:
    # function that takes a number and check if the number is a prime
    def check_prime(num):
        '''
        Takes a number as input and check if the number
        is a prime or not and print out the message
        '''
        # a prime number is not divisable by 2 and al numbers before that number
        for i in range(2, num):
            if num % i == 0:
                print("This is not a prime number!\n")
                # break out of the loop
                break
        else:
            print("This is a prime number\n")

    print("\n")
    check_prime(int(input("What's the number you want to check? ")))

    ask_check = input("do you want to check another number? Type 'y' or 'n' ")

    if ask_check == 'n':
        check = False