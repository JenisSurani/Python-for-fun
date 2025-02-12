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
    
 words=message.split(" ")
 finalMessage=[]
 for word in words:
        if(len(word)<3):
            finalMessage.append(word[::-1])
        else:
            word=word[1:]+word[0]
            # Random lowercase letter
            message1 = "".join([random.choice(string.ascii_lowercase) for _ in range(3)])
            message2 = "".join([random.choice(string.ascii_lowercase) for _ in range(3)])
            finalMessage.append(message1+word+message2)
 return " ".join(finalMessage)

def Decode(message:str)->str:

 words=message.split(" ")
 finalMessage=[]
 
 for word in words:   
        if(len(word)<3):
            finalMessage.append(word[::-1])
        else:
            word=word[3:-3]
            word=word[-1] + word[:-1]
            finalMessage.append(word)             
 return " ".join(finalMessage)
 
 
a=input("Please Enter the message to Encode:\n")
print("Your Encoded message is:\n"+Encode(a))

print()

b=input("Please Enter the message to Decode:\n")
print("Your Decoded message is:\n"+Decode(b))



# Author: Jenis Surani
# Topic: Encoding-Decoding_OfMessage
# Date: 10/02/2025