# Advanced Exercises

import pandas as pd
import numpy as np
from env import hostname, username, password


# 1. Create a function named get_db_url. 
#    It should accept a username, hostname, password, and database name and return a url connection string
#    formatted like in the example at the start of this lesson.

# Function to get a url:
def get_db_url(hostname, username, password, database_name):
    url = f'mysql+pymysql://{username}:{password}@{hostname}/{database_name}'
    return url

# 2. Use your function to obtain a connection to the employees database.
#url = f'mysql+pymysql://{username}:{password}@{hostname}/employees'

pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', get_db_url(hostname, username, password,'employees'))

# 3. Once you have successfully run a query:
#    a. Intentionally make a typo in the database url. What kind of error message do you see?
        # A long list of error messages
#    b. Intentionally make an error in your SQL query. What does the error message look like?
        # Another long list of error messages

# 4. Read the employees and titles tables into two separate DataFrames.
pd.read_sql('SELECT * FROM titles LIMIT 5 OFFSET 50', get_db_url(hostname, username, password,'employees'))
# 5. How many rows and columns do you have in each DataFrame? Is that what you expected?

# 6. Display the summary statistics for each DataFrame.

# 7. How many unique titles are in the titles DataFrame?

# 8. What is the oldest date in the to_date column?

# 9. What is the most recent date in the to_date column?


#----------------------------------------------------------------------------------------
# Exercises II

# 1. Copy the users and roles DataFrames from the examples above.

# 2. What is the result of using a right join on the DataFrames?

# 3. What is the result of using an outer join on the DataFrames?

# 4. What happens if you drop the foreign keys from the DataFrames and try to merge them?

# 5. Load the mpg dataset from PyDataset.

# 6. Output and read the documentation for the mpg dataset.

# 7. How many rows and columns are in the dataset?

# 8. Check out your column names and perform any cleanup you may want on them.

# 9. Display the summary statistics for the dataset.

# 10. How many different manufacturers are there?

# 11. How many different models are there?

# 12. Create a column named mileage_difference like you did in the DataFrames exercises; this column should contain the difference between highway and city mileage for each car.

# 13. Create a column named average_mileage like you did in the DataFrames exercises; this is the mean of the city and highway mileage.

# 14. Create a new column on the mpg dataset named is_automatic that holds boolean values denoting whether the car has an automatic transmission.

# 15. Using the mpg dataset, find out which which manufacturer has the best miles per gallon on average?

# 16. Do automatic or manual cars have better miles per gallon?