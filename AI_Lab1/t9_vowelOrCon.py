alphabet = input("Enter a letter of the alphabet: ")

def vowelOrCon(alphabet):
    if alphabet == 'a' or alphabet == 'e' or alphabet == 'i' or alphabet == 'o' or alphabet == 'u':
        print("This is a vowel.")
    else:
        print("This is a consonant.")
    
def main():
    vowelOrCon(alphabet)    
    
if __name__ == "__main__":        
    main()