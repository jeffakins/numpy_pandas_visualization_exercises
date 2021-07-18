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

# 4. How many consonants are in the Series?
letter_series.value_counts().sum() - letter_series[letter_series.isin(vowels)].value_counts().sum()
#                                                               # Answer: 166

# 5. Create a Series that has all of the same letters but uppercased
letter_series.str.upper()

# 6. Create a bar plot of the frequencies of the 6 most commonly occuring letters.
import matplotlib.pyplot as plt
letter_series.value_counts().head(6).plot.bar()
plt.show()                                                      # Vertical bar plot of top 6

# New Series
numbers = pd.Series(list(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']))
numbers

# 1. What is the data type of the numbers Series?
numbers.dtype                                                   # Object

# 2. How many elements are in the number Series?
numbers.value_counts().sum()                                    # 20

# 3. Perform the necessary manipulations by accessing Series attributes and methods to convert the numbers Series to a numeric data type.
num_no_dollar = numbers.str.replace("$", "")                    # Remove $
just_numbers = num_no_dollar.str.replace(",", "")               # Remove commas
just_numbers = just_numbers.astype(float)                       # Convert to float type
just_numbers                                                    # dtype: float64

# 4. Run the code to discover the maximum value from the Series.
just_numbers.max()                                              # Answer: 4789988.17

# 5. Run the code to discover the minimum value from the Series.
just_numbers.min()                                              # Answer: 278.6

# 6. What is the range of the values in the Series?


# 7. Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.

# 8. Plot the binned data in a meaningful way. Be sure to include a title and axis labels.