
#DICTIONARIES

my_dict = {'JOHN':'001','RYE':'002','BSCS':'003'}
# print(my_dict) #the print syntax don't tab it it will be an error
# type(my_dict)
#
# new_dict = dict()
# print(new_dict)
# type(new_dict) #it shows empty bracket
#
# new_dict = dict(JOHN='001',RYE='002')
# print(new_dict)

#NESTED DICTIONARIES |  my_dict = {'JOHN':'001','RYE':'002','BSCS':'003'}

emp_details = {'Employee':{'JOHN':{'ID':'001','SALARY':'2000','DESIGNATION':'TEAM LEAD'},
                           'RYE':{'ID':'002','SALARY':'2500','DESIGNATION':'ASSOCIATE'}}}
print(emp_details)
print("")

#ACCESING ITEMS

print(my_dict['JOHN']) #it shows only 001
print([my_dict.get("JOHN")]) #it shows ['001']
print("")

print([my_dict])
print([my_dict.keys()]) #it shows the primary key or the names
print([my_dict.values()]) #it shows the value or the right side next to key
print("")

for x in my_dict:
    print(x) #the names shows are constant .keys
print("")
for x in my_dict.values():
    print(x) #you can use same variable 'x' above in every for loop syntax
print('')
for x,y in my_dict.items():
    print(x,y) #x and y are the left and right value


#UPDATING VALUE
    my_dict['JOHN'] = '888'
    my_dict['RYE'] = '513'
    my_dict['BRIZ'] = '104'
    print(my_dict)  #it shows the updated version

    print("")
    for x,y in my_dict.items():
        print(x,y)


print("")
#DELETING     |   {'JOHN': '888', 'RYE': '513', 'BSCS': '003', 'BRIZ': '104'}

print(my_dict.pop('JOHN')) #some syntax are not shown in pycharm console only in jupyter
print(my_dict.popitem()) #same no syntax are shown

del my_dict['JOHN']