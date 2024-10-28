age = int(input("Enter your age: "))

def ageF(age):
    if age < 2:
        print("This is a baby")
    elif age >= 4 and age < 13:
        print("Its a kid")
    elif age >= 13 and age < 20:
        print("He is a teenager")
    elif age >= 20 and age < 65:
        print("He is an adult")
    elif age >= 65:
        print("He is elder")
    else:
        print("Alien")
        
def main():
    ageF(age)
    
    
if __name__ == "__main__":
    main()