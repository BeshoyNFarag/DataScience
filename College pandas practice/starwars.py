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
starwars.sort_values(by="column_name", ascending =True or false) --> this helps ascendingly or descindengly ordered using column name
starwars.sort_values(by=["jedi", "height"], ascending=[True, False]) --> sorting using 2 columns
starwars.sort_values("height", ignore_index=True) --> during normal sort the index remain attached to its main value
this ignore_index = True resets the index to zero
starwars["mass"].mean() --> we can return the mean of an entire column
starwars[["mass", "height"]].max() --> returns the mean of 2 columns
starwars.groupby("eye_color")["height"].mean() --> we can group by the uniqeness of any value of a column, then we can 
choose another column and aggregate it
starwars.groupby("eye_color")[["height", "mass"]].mean() --> we can aggregate more than one column using the same group
starwars["sex"].value_counts() --> count how many times a certain unique value appear on the column


pd.merge(left=students, right = names, how = "left", left_on = "degree program", right_on = "short name") --> this is
to merge 2 tables, left addressing one dataframe and right is the otherone, how ="left,rigth,inner,outer" 
left means the matching of right to left will be added and if nothing matches we keep the data from left and fill the
rest with NaN. Right is just the opposite giving the right the main character.
Inner only joins the common data and outer keeps all rows from both tables, filling NaN where no match exists.
left_on and right_on indicates the values or column names that should be joined based on






###end Pandas notes###
plt.plot(arrayx, arrayy) --> this here is a line chart with x and y axis both as an array input
plt.show() --> wihtout this funtion you can really see nothing
plt.plot(arrayx, arrayy, marker = "character") --> this marker keywoard would make the point on the char as the line
plt.plot(arrayx, arrayy, marker = "character", markersize=10) --> this sets the point mark as something
plt.plot(arrayx, arrayy, markerfacecolor = "color") --> this sets the color of the line chart's points
plt.plot(arrayx, arrayy, markeredgecolor = "color") --> this sets the color of the line chart's outer points
plt.plot(arrayx, arrayy, linestyle = "dashed") --> the line chart style
plt.plot(arrayx, arrayy, linewidth = 2) --> this doubles the line size
plt.plot(arrayx, arrayy, color = "some color") --> this is for the color of the line
starwars.plot.scatter(x="height", y="mass", c="BMI", colormap="viridis", title="Star Wars") --> a scatter plot is 
a 2D graph that represents a relation between 2 values as dots. the x = "height" is the column for values this sets the x
title and value, the y = "mass" does the same for the y access. c="BMI" means the color follows the BMI value of numbers
title= "sets the title", s= some number sets the size of the dots. 
plot.scatter(marker= "x") --> makes the dots looks as x instead of dots
plot.scatter(edgecolor="blue", linewidth= number, alpha = number between 0 and 1) --> this gives an edge of color blue
with widht of number and the alpha makes the color a bit see through
for idx, row in starwars.iterrows():
    ax.annotate(row["name"], (row["height"], row["mass"])) --> annotates the name on the point god knows how
###start matplot lib notes###
'''


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

starwars = pd.read_csv(
    "E:\Year 2 college\Data Science\DataScience\College pandas practice\starwars.csv")
starwars["BMI"] = (starwars["mass"] / 100) / (starwars["height"] ** 2)

starwars = starwars.set_index("name", drop=False)

df1 = starwars[starwars["sex"] == "male"]
df2 = starwars[starwars["sex"] != "male"]

df3 = pd.concat([df1, df2])

print(df1)
print(df2)

print(df3)
