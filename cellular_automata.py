# This program is a one dimensional cellular automata model.  It checks that
# the cells adjacent to the index cell are equal to the index cell, and prints
# a + if they are all equal, and a space if they are not.

LEFT_BOUNDARY = 0
RIGHT_BOUNDARY = 0
LENGTH = 65
def main():
    number = iterations()

    cell = [1 for i in range(LENGTH)] # prints translation of first line
    trans(cell)
          
    for i in range(number): # prints the rest of the function.
        trans(update(cell))
        cell = update(cell)

def iterations():  # This function allows the user to input the number
                   # of iterations  they would like the program to run
    num = 0        # and prompts the user to enter a valid value if they don't.
    while num < 1:
        try:
            num = int(input("Please enter how many iterations you would like: "))
            if num < 1:
                print("Please enter a value greater than 0.")
        except: 
            print("Please enter a value greater than 0.")

    return num-1 # The first line is printed prior to the loop, so there
                 # will be 1 less entry.

def trans(final): # This translates the code into the final output (+ and ' ')
    for c in final:
            if c == 1:
                print('+',end='')
            else:
                print (' ', end='')
    print()

def update(cell): # This function updates the new cells, and changes the values. 
    
    newCell = []
    for i in range(len(cell)): # This iterates down the length of the list.
        if i == 0 or i == LENGTH-1: # This controls for the edges of the list.
            if i == 0:
                if cell[0] == cell[1] and cell[0] == LEFT_BOUNDARY:
                    newCell.append(1)
                else:
                    newCell.append(0)
            else:
                if cell[i] == cell[i-1] and cell[i] == RIGHT_BOUNDARY:
                    newCell.append(1)
                else:
                    newCell.append(0)
        else:  # This checks that i is the same in all adjacent cells.  
            if cell[i+1] == cell[i-1]:
                newCell.append(1)
            else:
               newCell.append(0)

    return newCell
   
main()
