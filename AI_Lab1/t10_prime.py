number = int(input("Enter a numerical value: "))

def prime_number(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(number, "is not a prime number.")
                break
            else:
                print(number, "is a prime number.")
                break
    else:
        print(number, "is not a prime number.")
        
def main():
    prime_number(number)
    
if __name__ == "__main__":
    main()