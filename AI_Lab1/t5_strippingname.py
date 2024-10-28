name = input("Enter your name: ")
print(name)

def name_stripping(name):
    print("Full Stripping: ")
    print(name.strip())

def left_stripping(name):
    print("Left side stripping: ")
    print(name.lstrip())
    
def right_stripping(name):
    print("Right side stripping: ")
    print(name.rstrip())
    
def main():
    name_stripping(name)
    left_stripping(name)
    right_stripping(name)
    
if __name__ == "__main__":
    main()