x = int(input("Enter a number: "))

def sum(x):
    y = 3
    return x + y

def product():
    z = sum(x)
    y = 2
    return z * y

def diff():
    z = product()
    y = 4
    return z - y

def cal_sum():
    z = diff()
    y = 3
    return z + y

def main():
    z = cal_sum()
    print(z)
    
if __name__ == "__main__":
    main()
    

    