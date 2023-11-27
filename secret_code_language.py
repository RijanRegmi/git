import random
import string

print("........Secret Code Language Ex..........")
message = input("Enter your  for Coding or Decoding message: ")

# Code for generating 3 random string characters
letters = string.ascii_letters
rand3_start = ''.join(random.choice(letters) for i in range(3))
rand3_end = ''.join(random.choice(letters) for i in range(3))
# print(rand3_start)
# print(rand3_end)

def coding(m):
    if len(m) >= 3:
        first = m[0]
        up_a1 = m[1:] + first       # deleting the first character and appending it to the end of the string
        up_a2 = rand3_start + up_a1 + rand3_end

        print(up_a2)
    else:
        reverse_string = m[::-1]
        print(reverse_string)


def decoding(m):
    if len(m) >= 3:
        up_a1 = m[3:-3]
        first = up_a1[len(up_a1)-1]
        up_a2 = first + up_a1[0:-1]

        print(up_a2)
    else:
        reverse_string = m[::-1]
        print(reverse_string)


num = int(input("Press '1'for CODING and '2'for DECODING: "))
if num == 1:
    coding(message)
elif num == 2:
    decoding(message)
else:
    raise ValueError("Invalid number!!!!")







