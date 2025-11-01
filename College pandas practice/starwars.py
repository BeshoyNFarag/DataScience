'''
### Start pandas notes ###
df = df.set_index("column name", drop = False) --> this sets the index to a value of one our columns
np.random.standard_normal(size) --> this gives you a random number array of "size" and with standard dev =1 and mean = 0
usually these values are between -3 and 3
df.head(number of rows ) --> this return the first 5 rows
df.tail(number of rows) --> this retirns the last 5 rows
starwars.info() --> returns each column name and how many n0n-null values it has also the data type of it
starwars.describe() --> it works the same as in numpy it returns the statistical analysis like mean, median, max,min (only numerical columns)
starwars.shape() --> it returns also the the shape of your dataframe
starwars.to_excel("starwars.xlsx", sheet_name="people", index=False)
starwars.loc["Height"] --> access the column called height
****** starwars.loc[starwars["mass"] > 77] --> this line here returns the data and information where the mass is greater than
77

starwars.index --> prints what is the start and end indices are and also prints the steps between them
starwars[starwars["height"] < 180]  # height < 180 --> return the data frame where the condition is met
starwars[(starwars["height"] < 180) & (starwars["sex"] == "male")] return the data frame where the condition is met
starwars[starwars["eye_color"].isin(["red","blue"])] return the data frame where the condition is met
starwars[starwars["homeworld"].isna()] -->return the data frame where the condition is met
starwars.loc[starwars["height"] < 180, "name"] --> the first input chooses the row, the second chooses the column
starwars.loc["R2-D2"]      --> you can choose the row based on its name
starwars.loc[:, "height"]   --> you should always pass the rows,evne if you want to choose based on the columns 
starwars.loc["R2-D2":"Chewbacca", ["mass","homeworld"]] --> choosing rows and column ranges


starwars["BMI"] = starwars["mass"] / (starwars["height"]/100)**2  --> we can just create a new column by selecting it
using this ["name"] then assign =  a value to it.
starwars["col1"] = 7  --> here we assing a value to an entire column
starwars["col2"] = np.random.randint(0,100, starwars.shape[0]) --> creating a random value for each column
starwars = starwars.drop(columns=["col1","col2"]) --> deleting entire columns
starwars_renamed = starwars.rename(columns={"eye_color":"Augenfarbe","sex":"Geschlecht"}) --> rename by just renaming



###end Pandas notes###

###start matplot lib notes###
'''


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

arrayx = np.array([10, 20, 30, 50, 60])
arrayy = np.array([140, 240, 340, 540, 460])

plt.plot(arrayx, arrayy)
plt.show()
