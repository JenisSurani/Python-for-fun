# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode
import random
import string



def Encode(message:str)->str:
    
    if(len(message)<3):
       return message[::-1]
    else:
    
      my_array=list(message)
      
      my_array.append(my_array[0])
      my_array.pop(0)
      
      message="".join(my_array)
      
      # Random lowercase letter
      message1 = "".join([random.choice(string.ascii_lowercase) for _ in range(3)])
      message2 = "".join([random.choice(string.ascii_lowercase) for _ in range(3)])
      
      return message1+message+message2
  
def Decode(message:str)->str:
    
    if(len(message)<3):
       return message[::-1]
    else:
        my_list=list(message)
        my_list[:3]=[]
        my_list[-3:]=[]
        last_letter = my_list.pop()  # Remove the last letter
        my_list.insert(0, last_letter)  # Add it to the beginning
        
        return "".join(my_list)
 
a=input("Please Enter the message to Encode:\n")
print("Your Encoded message is:\n"+Encode(a))

print()

b=input("Please Enter the message to Decode:\n")
print("Your Decoded message is:\n"+Decode(b))


# Author: Jenis Surani
# Topic: Encoding-Decoding_OfMessage
# Date: 10/02/2025