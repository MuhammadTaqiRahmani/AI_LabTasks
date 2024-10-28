number = int(input("Enter a number: "))
def multiplication_table(number):
    for i in range(1, 11):
        print(number, "x", i, "=", number*i)
    
def main():
    multiplication_table(number)
    
if __name__ == "__main__": 
    main()