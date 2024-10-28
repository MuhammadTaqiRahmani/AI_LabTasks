x = int(input("Enter a numerical value: "))
def absolute_value(x):
    if x < 0:
        x = -x
    return x

def main():
    print(absolute_value(x))
    
if __name__ == "__main__": 
    main()