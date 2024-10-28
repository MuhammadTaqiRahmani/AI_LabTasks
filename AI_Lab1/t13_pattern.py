def pattern():
    for i in range(1,6):
        print()
        for j in range(1, i + 1):
            if i % 5 == 0 and j == 2:
                print(' ', end='')
            
            print(i, end='')
                
                
def main():
    pattern()   

if __name__ == "__main__":
    main()
                
                
                