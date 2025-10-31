'''
# start series notes
some series notes
series.dropna() --> drops the empty values
series.fillna(any type of data) --> fills any empty data
series3 =  s1 + s2 --> this addes the values of the 2 series into one series when they have matching index, 
any none matching index get a nan value and no index is excluded!
series.mean() --> gives you the mean of the series
series.loc['value of index'] --> this returns a value at the index based on the index name
series.iloc[numerical index] --> this retunrs a value ar the index based on the index value (normal slicing)
series.values -> to fetch the values
series.index -> to fetch the indices
series.shape --> returns the dimensions of the series
print(s.get('x', "nah")) --> here is safely fetches the data at index 'x' and throws a message if not found called nah
print(s.mean())       # Average
print(s.median())     # Middle value
print(s.std())        # Standard deviation
print(s.describe())   # Summary of all statical values
s = pd.concat([s, pd.Series({'Hannah': 50})]) --> concats 2 series
s.sort_values(ascending=True)) --> this sorts the series ascendingly

# end series notes

Create a Series called temperatures using this dictionary:
{'Mon': 30, 'Tue': 32, 'Wed': 31, 'Thu': 29, 'Fri': 28}
Do the following:
Print the temperature on Wednesday.
Add 2 to all temperatures (imagine it got hotter).
Find the average temperature.
Filter and display days with temperatures above 30°C.

import pandas as pd
series = {'Mon': 30, 'Tue': 32, 'Wed': 31, 'Thu': 29, 'Fri': 28}
temp = pd.Series(series)
print(temp)
print(f"temprature on Wednesday: {temp['Wed']}")
temp = temp + 2
print(temp)
print(f"the mean of this is: {(temp - 2).mean()}")
print(f"filtered:\n{temp.loc['Wed']}")


import pandas as pd

series = [10, 20, 30, 40, 50]

s = pd.Series(series, index=['a', 'b', 'c', 'd', 'e'])
s2 = pd.Series([20, 30, 40, 50, 80], index=['a', 'f', 'e', 'x', 'b'])
print(s)
print(s.values)
print(s.index)
print(s.dtype)
print(s.shape, "\n")

print(s.get('x', "nah"))

s3 = s + s2
print(s3)
print(s3.dropna())
print(s3.fillna("x"))
print(s3.describe())





🧩 Your Task:
Create a Series called grades from the dictionary.
Display:
The average score
The highest and lowest score (and which student got them)
Add 5 bonus points to everyone and show the updated Series.
Replace any score above 100 with 100 (since scores cap at 100).
Display only the students who passed (score ≥ 70).
Add a new student “Hannah” with a score of 78.
Sort the Series by score (ascending order).
Find how many students scored above the average.
import pandas as pd

scores = {
    'Alice': 88,
    'Bob': 95,
    'Charlie': 67,
    'David': 72,
    'Eva': 90,
    'Frank': 59,
    'Grace': 83
}

s = pd.Series(scores)
print(f"the avergae score for this class was: {s.mean()}")
print(f"the minimum score was: {s.min()}")
print(f"the highest score was: {s.max()}")
print(f"the student with the max score is: {s.loc[s == s.max()]}")
print(f"the student with the max score is: {s.loc[s == s.min()]}")

s = s + 5
print(s)
print(f"studnets who passed: {s.loc[s >= 70]}")
s = pd.concat([s, pd.Series({'Hannah': 78})])

print(s)


print(f"the new avergae score for this class was: {s.mean()}")
print(s.sort_values(ascending=True))
print(s.loc[s > s.mean()].count())

'''
