city = input("Enter the name of a city: ").strip().lower()
country = "Pakistan"

list = ["Karachi", "Lahore", "Islamabad", "Quetta", "Peshawar"]
list = [i.lower() for i in list]
def describe_city(city, country):
    if city in list:
        print(city, "is in", country)
    else:
        print("City not found")

def main():
    describe_city(city, country)
    
if __name__ == "__main__": 
    main()    
    
