
"""

import random

computer_guess=random.randint(1,20)
c=1   #counter to count term

print("chalo bhai game start krte hai")
user_guess=int(input("bhai 1 se 20 tak koi number socho: "))

while computer_guess!=user_guess:

  if user_guess<computer_guess:
    user_guess=int(input("bhai yaar bda socho: "))
  else:
    user_guess=int(input("bhai chhota socho: "))
  c=c+1
print("bhai sahi socha aap to genius ho yaar: ")
print("apne itne bar try kiya: ",c)