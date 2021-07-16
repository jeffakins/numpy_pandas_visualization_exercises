# Pandas Exercises

import pandas as pd
fruit_series = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

# Type and output of the fruit_series
type(fruit_series)
fruit_series

# 1. Determine the number of elements in fruits.
fruit_series.size                                       # Answer: 17

#2. Output only the index from fruits.
fruit_series.index                                      # RangeIndex(start=0, stop=17, step=1)
fruit_series.index.tolist()

# 3. Output only the values from fruits.
fruit_series.values                                     # Complete

# 4. Confirm the data type of the values in fruits.
fruit_series.dtype

# 5. Output only the first five values from fruits. 
fruit_series.head(5)
#    Output the last three values. 
fruit_series.tail(3)
#    Output two random values from fruits.
fruit_series.sample(2)

# 6. Run the .describe() on fruits to see what information it returns when called on a Series with string values
fruit_series.describe()

# 7. Run the code necessary to produce only the unique string values from fruits.
fruit_series.unique()                                   # This method needs parenthasis to work

# 8. Determine how many times each unique string value occurs in fruits.
fruit_series.unique().size                              # Answer: 13

# 9. Determine the string value that occurs most frequently in fruits.
fruit_series.value_counts().head(1)                     # Kiwi

# 10. Determine the string value that occurs least frequently in fruits.
fruit_series.value_counts().nsmallest(n=1, keep="all")                             

#



