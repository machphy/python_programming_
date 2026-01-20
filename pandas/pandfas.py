import numpy as np
import pandas as pd 

dict={
    "name":['ajay', 'vijay', 'mohan', 'jadish', 'krishna'],
    "marks":['45','10','42','45','36'],
    "city":['gorakhpur','kushingar','kasia','lucknow', 'odisha ']

}

#     data farama
df=pd.DataFrame(dict)


df.to_csv('mere_dost.csv')

# for index need no need 
df.to_csv('mere_dost.csv', index=False)    

df.head(2)

df.tail(2)

df.describe()

print(df.describe)