color = input("Enter a color: ")
gap = " "
def color_selection(color, gap):
    for i in range(1, 8):
        print(color, end='')
    print('\n')
    
    for i in range(1):
        print(color, end='')
        
    for i in range(20):
        print(gap, end='')
        
    for i in range(1):
        print(color, end='')
        
    print('\n')
    
    for i in range(1, 8):
        print(color, end='')
        
        
def main():
    color_selection(color,gap)
    
if __name__ == "__main__":
    main()
