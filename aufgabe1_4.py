
# import pandasspd

# importing the package

import pandas as pd
import nltk
import pdpipe as pdp
# creating a empty dataframe named dataset
dataset = pd.DataFrame()

# Creating a simple dataframe
dataset['name'] = ['Reema', 'Shyam', 'Jai',
                   'Nimisha', 'Rohit', 'Riya']

dataset['gender'] = ['Female', 'Male', 'Male',
                     'Female', 'Male', 'Female']

dataset['age'] = [31, 32, 19, 23, 28, 33]

dataset['department'] = ['Accounts', 'Management',
                         'IT', 'IT', 'Management',
                         'Advertising']

dataset['index'] = [1, 2, 3, 4, 5, 6]

# View dataframe
dataset


print(dataset)


##### Pipeline #############

# creating a pipeline and
# dropping the unwanted column
dropCol = pdp.ColDrop("index").apply(dataset)

# display the new dataframe
# after column drop
dropCol

print("")
print("HIER DAS geDROPte-Dataset")
print("")

print(dropCol)

#####   Weg 2 um Spalte zu entfernen   #####

# creating a pipeline and
# dropping the unwanted column
dropCol2 = pdp.ColDrop("index")

# applying the ColDrop to dataframe
df2 = dropCol2(dataset)

# display dataframe

print("")
print("WEITERES ERGENIS: ")
print("")

print(df2)
