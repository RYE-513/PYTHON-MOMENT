# #ARITHMETIC OPERATOR
#
# # a = 5
# # a += 5 # '+=' meaning add to it self number e.g. 5 + 5 = 10
#
# aa = 45 #they are connected
# aa += 45 #they are connected  or 'aa = aa + 45'
# print(aa)
#
# bb = 5
# bb **= 5
# print(bb)
#
# #COMPARISON OPERATOR
#
# '''
# a == b //equal
# a != b // not equal
# a > b // greater than
# a < b // less than
# a >= b // greater than or equal to
# a <= b // less than or equal to
# '''
#
# a = 52
# b = 60
#
# result = a == b
# print(result)
#
# result = a != b
# print(result)
#
# result = a < b
# print(result)
#
# #LOGICAL OPERATOR
# #A. CONDITION OR CONTROL STATEMENTS
#
# if a == b:
#     print('NICE')
# elif a < b:          #'elif' means else if, another if declaration or true statements
#     print('SUS')
# else :
#     print('AMOGUS')
#
# #B. AND, OR, NOT    // IN JAVA &&,||,!
#
# '''
# AND - MAJORITY FALSE
# OR - MAJORITY TRUE
# NOT - VICE VERSA
# '''
#
# rye_balance = 58
# bscs_balance = 64
#
# #                       T,                         T,                     F               = false: because of 'and'
# result1 = (rye_balance < bscs_balance) and (bscs_balance != 64) and (rye_balance <= 678)
# print(result1)
#
# #                       F,                 T,                  T,                  = true: because of 'or'
# result2 = (541 <= rye_balance) or (65 > bscs_balance) or (not(bscs_balance != 64))
# print(result2)
#
# #                       F,                 T,                  T,                  = true: because of 'or' is first to declare operator than 'and'
# result2 = (541 <= rye_balance) or (65 > bscs_balance) and (not(bscs_balance != 64))
# print(result2)

#C. IDENTIFY OPERATORS

aaa = 10
bbb = 30

list1 = [10,20,30]
list2 = [10,20,30]

print(aaa is list1)   # false: 'is' consider as 'false' but 'in' consider as 'true' which is vice versa.
print(list1 is list2) # false: yes they are both same values, but they are different object 'variable name'.
print(list1 is list1) # true: same variable which is object.

print(list1 is not list1) # false: vice versa answer
print('')

#D. MEMBERSHIP OPERATORS

print(aaa in list1)  # true: 'in' consider as 'true' but 'is' consider as 'false' which is vice versa.
print(list1 in list2) # false: yes they are both same values, but they are different object 'variable name'.
print(list1 == list2) # true: same equal value
print('')

#E. BITWISE OPERATORS |  & - and, | - or

print(10&12) # AND
''' BINARY CONVERT
      8   4  2  1      
10 = (1)  0  1  0
12 = (1)  1  0  0

* the answer is '8' because the 1 are same align with 10 and 12.
'''

print(10|12) # OR
''' BINARY CONVERT
      8   4  2  1      
10 =  1  0  1  (0) become 1  0  1 (1) become 1  1  1  1
12 =  1  1  0  (0) become 1  1  0 (1) become 1  1  1  1

* the zero both allign will become 1 
* it turning all in '1'
* the answer is '14'
'''

print(10 >> 2) # RIGHT SHIFT
'''
      8   4   2    1      
10 =  1   0  (1)  (0)  = out 2:  *the binary of '10' which is 1 0 1 0 the (1) (0) 1 0 will disregard because it's left shift
'''

print(10 << 2) # LEFT SHIFT
'''
10 = 1 0 1 0 THEN ADD 2 zero of end because of (10 << '2')
finally it become 1 0 1 0 (0 0)

32  16  8   4   2   1 
1   0   1   0   0   0  = 32 and 8 are in '1' so 32+8 = 40
'''

print(10^2) # XOR * sets each bit to 1 if only one of the bits is 1.

