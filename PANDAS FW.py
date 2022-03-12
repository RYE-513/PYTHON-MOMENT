import pandas as pd


emp_details = {'Employee':{'JOHN':{'ID':'001','SALARY':'2000','DESIGNATION':'TEAM LEAD'},
                           'RYE':{'ID':'002','SALARY':'2500','DESIGNATION':'ASSOCIATE'}}}


df = pd.DataFrame(emp_details['Employee'])
print(df)