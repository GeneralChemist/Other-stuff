# Dustin Titus
# 6/2/15
#
# This program will use a key to encode a text file to make it unreadable.
# It will also decode a file that has been previously encrypted using the
# same key.
# 

PLAIN_TXT = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
             'O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b',
             'c','d','e','f','g','h','i','j','k','l','m','n','o','p',
             'q','r','s','t','u','v','w','x','y','z','1','2','3','4',
             '5','6','7','8','9','0',' ', '\n'] #64 positions

KEY =       ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G',
             'H','J','K','L','Z','X','C','V','B','N','M','1','2','3','4',
             '5','6','7','8','9','0','a','s','d','f','j','k','l','g','h',
             'q','w','e','r','t','y',' ','u','i','o','p','z','x','c','v',
             'b','n','m','\n']

# These allow for easy changes to the menu.
INSTRUCTIONS = '1'
ENCRYPTION = '2'
DECRYPTION = '3'
QUIT = '4'

def main():

  # This loop takes the input from the menu function, and applies it to
  # the corresponding function.
  decision = menu()
  if decision == INSTRUCTIONS:
     instruction()
  elif decision == ENCRYPTION:
    encrypt(get_file())
  elif decision == DECRYPTION:
    decrypt(get_file())
  elif decision == QUIT:
    print("Thank you.")
    quit()
  else:
    menu()
    
def menu(): # This function displays a with options that the user can choose
  # from, and returns that value.
  print('Please choose from the following menu options:')
  print('Press ',INSTRUCTIONS, 'for instructions.')
  print('Press ',ENCRYPTION,' for encryption.')
  print('Press ', DECRYPTION,' for decryptions.')
  print('Press ',QUIT,' to exit.')
  choice = input('Please choose from the menu above. ')
  return choice
    
def instruction():  # This function will display a simple set of instructions
  # on how to use the program.
  print()
  print("This program will encrypt a new text file so that it is not readable.")
  print()
  print('If you would like to encrypt a file, press 2, this will take the text,')
  print('and scramble it, so that it will be unreadable.')
  print()
  print('If you would like to decrypt a file that has previously been encrypted')
  print('by this program, select 3 from the menu.')
  print()
  menu()

def get_file(): # This function gets the file name, and returns it.
  file = input("Please enter the file name: ")
  return file

# This function takes a given file name, opens and reads the file, and indexes
# each character, then appends that character to a new list, after translating
# it to the key. Once the list is  complete, it is joined in a new file. 
def encrypt(file): 
  en_file = open(file,'r')
  pos = file.replace('.','E.')
  new_file = open(pos,'w')
  new_line = 0
  while new_line != '':
    new_line = en_file.readline()
    
    encrypted_characters = []
    for char in new_line:
      if char not in PLAIN_TXT:
        encrypted_characters.append(char)
      else:  
        index = PLAIN_TXT.index(char)
        encrypted_characters.append(KEY[index])      
    new_file.write("".join(encrypted_characters))      

  
  en_file.close()
  new_file.close()
  print()
  print(file,'has been encrypted.')
  
# This function takes a given file name, opens and reads the file, and indexes
# each character, then appends that character to a new list, after translating
# it to the plain text. Once the list is  complete, it is joined in a new file.  
def decrypt(file):  
  de_file = open(file,'r')
  pos = file.replace('.','D.')
  new_file = open(pos,'w')
  new_line = 0
  while new_line != '':
    new_line = de_file.readline()
    decrypted_characters = []
    for char in new_line:
      if char not in KEY:
        decrypted_characters.append(char)
      else:
        index = KEY.index(char)
        decrypted_characters.append(PLAIN_TXT[index])
    new_file.write(''.join(decrypted_characters))

  de_file.close()
  new_file.close()
  print()
  print(file,'has been decrypted.')  


main()
  
