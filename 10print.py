from random import random as rnd

while True:
    print(chr(47 + int(0.5 + rnd()) * 45), end="")

#
# while True:
#   if 0.5 + rnd() > 1:
#       print("\\", end="")
#   else:
#       print("/", end="")
#

