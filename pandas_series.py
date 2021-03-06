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
import pandas as pd
fruit_series = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

#1. Capitalize all the string values in fruits.
fruit_series.str.capitalize()

# 2. Count the letter "a" in all the string values (use string vectorization).
fruit_series.str.count("a").sum()                       # Answer: 14

# 3. Output the number of vowels in each and every string value.
vowels = list('aeiou')
fruit_series[fruit_series.isin(vowels)]                 # No worky

# 4. Write the code to get the longest string value from fruits.
max(fruit_series, key=len)                              # 'honeycrisp apple'

# 5. Write the code to get the string values with 5 or more letters in the name.
fruit_series.str.len() >= 5

# 6. Use the .apply method with a lambda function to find the fruit(s) containing the letter "o" two or more times.
fruit_series[fruit_series.apply(lambda fruit: fruit.count('o') > 1)]

# 7. Write the code to get only the string values containing the substring "berry".
fruit_series[fruit_series.str.contains('berry')]

# 8. Write the code to get only the string values containing the substring "apple".
fruit_series[fruit_series.str.contains('apple')]

# 9. Which string value contains the most vowels?
fruit_series[fruit_series.str.count('[aeiou]').max()]   # 'honeycrisp apple'      

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
# or
numbers.size                                                    # 20

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
just_numbers.shape

# 7. Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.
bin_just_numbers = pd.cut(just_numbers, 4).value_counts()
bin_just_numbers

# 8. Plot the binned data in a meaningful way. Be sure to include a title and axis labels.
bin_just_numbers.plot.bar(title='Frequency of Numbers',
                          color='steelblue').set(xlabel='Numeric Grouping',
                                                ylabel='Frequency')
plt.show()

# New Series
exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])

# 1. How many elements are in the exam_scores Series?
exam_scores.size                                                # Answer: 20

# 2. Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.
exam_scores.min()                                               # Answer: 60
exam_scores.max()                                               # Answer: 96
exam_scores.mean()                                              # Answer: 78.15
exam_scores.median()                                            # Answer: 79

# 3. Plot the Series in a meaningful way and make sure your chart has a title and axis labels.
bins = pd.IntervalIndex.from_tuples([(60, 69), (70, 79), (80, 89), (90, 100)])      # Grouped/binned by letter grade 
pd.cut(exam_scores, bins).value_counts(sort=False).plot.bar(title='Exam Grades', color='steelblue').set(xlabel='Grade', ylabel='Frequency')
plt.show()                                                      # Got it to work!

# 4. Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades. 
#    Add the necessary points to the highest grade to make it 100, and add the same number of points to every other score in the Series as well.
curved_exam_scores = exam_scores + 4                            # Curved the grades by adding 4 points to all scores
pd.cut(curved_exam_scores, bins).value_counts(sort=False).plot.bar(title='Exam Grades', color='steelblue').set(xlabel='Grade', ylabel='Frequency')
plt.show()                                                      # Bar plot showes a shift right

# 5. Use a method to convert each of the numeric values in the curved_grades Series into a categorical value of letter grades. 
#    For example, 86 should be a 'B' and 95 should be an 'A'. Save this as a Series named letter_grades.
def score_to_letter_grade(score):
    if score >= 0 and score <= 59:
        return "F"
    elif score >= 60 and score <= 69:
        return "D"
    elif score >= 70 and score <= 79:
        return "C"
    elif score >= 80 and score <= 89:
        return "B"
    elif score >= 90 and score <= 100:
        return "A"
    else:
        return "Not a valid score"

curved_letter_grade = curved_exam_scores.apply(score_to_letter_grade)
curved_letter_grade

# 6. Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.
curved_letter_grade.value_counts()
curved_letter_grade.value_counts(sort=False).sort_index(ascending=False).plot.bar(title='Exam Grades', color='steelblue').set(xlabel='Grade', ylabel='Frequency')
plt.show()