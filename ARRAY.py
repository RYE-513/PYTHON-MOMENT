# import array
import ARRAY as arr
#from array import *

#1. simple array

# a = array.array('i', [1,2,3,4,5,6])
# print(a)

#2. arr

# a = arr.array('i', [1,2,3,4,5,6])
# print(a)

#3. import *

#                       -2-1
# a = array('i', [1,2,3,4,5,6])
# print(a[-2]) #it shows '5' because 6 is correspond as -1
#
# a.extend([7,8,9,10])
# print(a) #don't forget to add [] inside of parameter .extend meaning to add another value at the end
#
# #current array: array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#
# print(a.pop()) # .pop shows the last number of array
# print(a.pop(2)) # .pop(2) it shows number 3. because putting a specific number will start counting at first left to right
# print(a.pop(-1)) # it shows '9' because negative will start counting from right to left
#
# print(a.remove(1)) # it shows none in console so type only the print(a) below
# print(a) #its literally remove the num '1' in the array

#4. array concatenation

a = arr.array('i', [1,2,3,4,5,6,7])
b = arr.array('i', [3,5,7,5,3,2,1])
c = arr.array('i')

c = a+b
print(c) #don't forget to on """import array as arr""" / the console shows the combine the array a and b

#ARRAY SLICING
print(c[0:8]) # it shows the specific array or range which is [0:8] meaning print only the first number up to 8th.
print(c[0:-2]) # the negative corresponds to remove only the last specific range number.
print(c[::-2]) # the double :: shows the console reverse.

#FOR LOOP ARRAY
for x in c:
    print(x)

print("")

for x in c[0:-3]:
    print(x) #it removes the last number specific range

#WHILE LOOP ARRAY *this syntax is not working in pycharm in jupyter only
# temp = 0
#     while temp<c[2]:
#         print(c[temp])
#         temp = temp+1







