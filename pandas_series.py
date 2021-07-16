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

#--------------------------------------------------------------------------

# Exercises Part II

#1. Capitalize all the string values in fruits.

fruit_series.to_string().capitalize()

# 2. Count the letter "a" in all the string values (use string vectorization).

# 3. Output the number of vowels in each and every string value.

# 4. Write the code to get the longest string value from fruits.
max(fruit_series, key=len)

# 5. Write the code to get the string values with 5 or more letters in the name.

# 6. Use the .apply method with a lambda function to find the fruit(s) containing the letter "o" two or more times.

# 7. Write the code to get only the string values containing the substring "berry".

# 8. Write the code to get only the string values containing the substring "apple".

# 9. Which string value contains the most vowels?


#--------------------------------------------------------------------------

# Exercises Part III
import pandas as pd
letters = pd.Series(['hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'])
letters

# 1. Which letter occurs the most frequently in the letters Series?
split_letters = letters.str.split(pat="", n=0, expand=True)     # Splits the string into individual letters 
split_letters                                                   # Letters split into columns (one row)
transpose_letters = split_letters.transpose()                   # Turns the columns into rows
transpose_letters                                               # Display rows
transpose_letters.value_counts()                                # Groups the letters by number of occurence
transpose_letters.value_counts().head(1)                        # Answer: y; 13 

#      This is the (better) way...  (thanks to Eli's quesiton and Brandon's assist)
letter_list = list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy')
letter_series = pd.Series(letter_list)                          # Convert the list into a series
letter_series                                                   # Check outpu
letter_series.value_counts().head(1)                            # Answer: y; 13

# 2. Which letter occurs the Least frequently?
transpose_letters.value_counts().tail()                         # Answer: l; 4

# 3. How many vowels are in the Series?
vowels = list('aeiou')
letter_series[letter_series.isin(vowels)].value_counts().sum()

