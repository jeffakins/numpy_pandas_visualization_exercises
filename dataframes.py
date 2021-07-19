# For several of the following exercises, you'll need to load several datasets using the pydataset library. 
# (If you get an error when trying to run the import below, use pip to install the pydataset package.)

from pydataset import data
import pandas as pd
import numpy as np

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

type(df)
df

#All the datasets loaded from the pydataset library will be pandas dataframes.
# 1. Copy the code from the lesson to create a dataframe full of student grades.
#    a. Create a column named passing_english that indicates whether each student has a passing grade in english.
df['passing_english'] = df.english > 70
df

#    b. Sort the english grades by the passing_english column. How are duplicates handled?
df.sort_values(by='passing_english', ascending=False)

#    c. Sort the english grades first by passing_english and then by student name. 
#       All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. 
#       The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)
df.sort_values(by=['passing_english','name'], ascending=True)

#    d. Sort the english grades first by passing_english, and then by the actual english grade, 
#       similar to how we did in the last step.
df.sort_values(by=['passing_english', 'english'])

#    e. Calculate each students overall grade and add it as a column on the dataframe. 
#       The overall grade is the average of the math, english, and reading grades.
df['overall_grade'] = df[['math', 'english', 'reading']].mean(axis=1).round(1)
df.drop(columns='passing_english')


# 2. Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:
mpg = data('mpg')
#    a. How many rows and columns are there?
mpg.info()                                              # 234 Rows; 10 Columns
mpg.describe()

#    b. What are the data types of each column?
mpg.info()                                              # Run code to see answer

#    c. Summarize the dataframe with .info and .describe
mpg.info()                                              
mpg.describe()

#    d. Rename the cty column to city.
mpg.rename(columns={'cty': 'city'})                     # Complete

#    e. Rename the hwy column to highway.
#    f. Do any cars have better city mileage than highway mileage?
#    g. Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.
#    h. Which car (or cars) has the highest mileage difference?
#    i. Which compact class car has the lowest highway mileage? The best?
#    j. Create a column named average_mileage that is the mean of the city and highway mileage.
#    k. Which dodge car has the best average mileage? The worst?

