
# This program runs a game that awards points to the user for each correctly translated
# random number from binary to decimal and decimal to binary. For each incorrect answer
# the computer is awarded a point.

import random
FINAL_SCORE = 10

def main():
  print("Greetings, this program will generate random numbers in either")
  print("binary or base ten, from 1-100.  your objective is to enter the")
  print("corresponding value in the opposite number base.")
  print()
  print("For each correct answer, you'll get 1 point, for each incorrect ")
  print("answer the computer will recieve 1 point.")
  print()
  print("The first to 10 points wins.")
  print()
  print("Here is your first question.")

  player = 0
  computer = 0

  # This keeps score, and uses the score to exit the loop
  while player < FINAL_SCORE and computer < FINAL_SCORE:
    print() 
    points = dec_or_bin()
    if points:
      player+=1
      print("Player: ",player," Computer: ",computer)    
    elif not points:
      computer+=1
      print("Player: ",player," Computer: ",computer)   

  if player == 10:
      print()
      print("Congratulations! You win!")
  elif computer == 10:
      print()
      print("The computer won.")
      print("Better luck next time...")

# This function randoms either decimal or binary and generates the random question
# for the user.  It also stores whether it was correct or not.
def dec_or_bin(): 
   rand = random.randint(1,2)
   dec,ans = rand_dec()
   bi = rand_bi(dec)
   if rand == 1:
     response = entry_bi(dec,bi)
     return response
   else:
     response = entry_dec(ans,bi)
     return response
   

def rand_dec(): # Random decimal number generator that will later be converted to binary
  num = random.randint(1,100)
  ans = str(num)
  return num,ans

def rand_bi(num): # Random binary number converter
  bi = bin(num)
  bi = str(bi[2:])
  return bi

def entry_bi(dec,bi): # Player input function for binary values
  resp = input("What is the binary value for the decimal number {}? ".format(dec))
  resp = str(resp)
  if resp == bi:
    print("Correct")
    return True
  else:
    print("I'm sorry, that is incorrect.")
    print("The correct answer is {}.".format(bi))
    return False
  
def entry_dec(dec,bi): #Player input function for decimal values
  resp = input("What is the decimal value for the binary number {}? ".format(bi))
  if resp == dec:
    print("Correct")
    return True
  else:
    print("I'm sorry, that is incorrect.")
    print("The correct answer is {}.".format(dec))
    return False    

main()
