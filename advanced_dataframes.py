# Advanced Exercises

import pandas as pd
import numpy as np
from env import hostname, username, password


# 1. Create a function named get_db_url. 
#    It should accept a username, hostname, password, and database name and return a url connection string
#    formatted like in the example at the start of this lesson.

# Function to get a url:
# def get_db_url(hostname, username, password, database_name):
#     url = f'mysql+pymysql://{username}:{password}@{hostname}/{database_name}'
#     return url

# 2. Use your function to obtain a connection to the employees database.
#url = f'mysql+pymysql://{username}:{password}@{hostname}/employees'

# employee_employees = pd.read_sql('SELECT * FROM employees', get_db_url(hostname, username, password,'employees'))
# employee_employees.head()

# 3. Once you have successfully run a query:
#    a. Intentionally make a typo in the database url. What kind of error message do you see?
        # A long list of error messages
#    b. Intentionally make an error in your SQL query. What does the error message look like?
        # Another long list of error messages

# 4. Read the employees and titles tables into two separate DataFrames.
# titles_employees = pd.read_sql('SELECT * FROM titles', get_db_url(hostname, username, password,'employees'))
# titles_employees

# 5. How many rows and columns do you have in each DataFrame? Is that what you expected?
#employee_employees.shape                                        # (300024, 6)


# 6. Display the summary statistics for each DataFrame.
#employee_employees.describe()
#titles_employees.describe()

# 7. How many unique titles are in the titles DataFrame?
#print(titles_employees.head())
#print(titles_employees.title.unique())                      # 7

# 8. What is the oldest date in the to_date column?
#print("oldest date: ", titles_employees.to_date.min())      # 1985-03-01

# 9. What is the most recent date in the to_date column?
#print("most recent date: ", titles_employees.to_date.max()) # 9999-01-01

#----------------------------------------------------------------------------------------
# Exercises II

# 1. Copy the users and roles DataFrames from the examples above.
users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles

# 2. What is the result of using a right join on the DataFrames?
users_roles_right = users.merge(roles, left_on='role_id', right_on='id', how='right', indicator=True)
users_roles_right

# 3. What is the result of using an outer join on the DataFrames?
users_roles_outer = users.merge(roles, left_on='role_id', right_on='id', how='outer', indicator=True)
users_roles_outer

# 4. What happens if you drop the foreign keys from the DataFrames and try to merge them?
roles_no_id = roles.drop(columns='id')
roles_no_id
# test_no_role_id = users.merge(roles_no_id, left_on='role_id', right_on='id', how='outer', indicator=True)
# test_no_role_id                 # Answer: It does't work because there is no foreign key to join on

# 5. Load the mpg dataset from PyDataset.
from pydataset import data
mpg = data('mpg')

# 6. Output and read the documentation for the mpg dataset.
#data('mpg', show_doc=True)

# 7. How many rows and columns are in the dataset?
len(mpg)
#mpg.describe()
mpg.loc[:,:]                                            # [234 rows x 11 columns]
mpg.shape                                               # (234, 11)

# 8. Check out your column names and perform any cleanup you may want on them.
print(mpg.head())
mpg.rename(columns={'drv': 'drive'}, inplace=True)
mpg

# 9. Display the summary statistics for the dataset.
# mpg.info()
# mpg.describe()
mpg.manufacturer.mode()

# 10. How many different manufacturers are there?
# mpg.count('')                                          # 7
mpg.manufacturer.unique().size

# 11. How many different models are there?               # 38
mpg.model.unique().size

# 12. Create a column named mileage_difference like you did in the DataFrames exercises; 
#     this column should contain the difference between highway and city mileage for each car.
mpg.hwy - mpg.cty

# 13. Create a column named average_mileage like you did in the DataFrames exercises; 
#     this is the mean of the city and highway mileage.
mpg['average_milage'] = mpg[["cty", "hwy"]].mean(axis=1)
mpg

# 14. Create a new column on the mpg dataset named is_automatic that holds boolean values denoting 
#     whether the car has an automatic transmission.
mpg['is_automatic'] = mpg.trans.str.contains("auto")
mpg

# 15. Using the mpg dataset, find out which which manufacturer has the best miles per gallon on average?
mpg.groupby(by='manufacturer').mean().sort_values(by='average_milage', ascending=False).head(1)

# 16. Do automatic or manual cars have better miles per gallon?
mpg.groupby(by='is_automatic').mean()   #manual

# mpg["is_automatic"] = np.where(mpg.trans.str.contains('auto'), True, False)



#-------------------------------------------------------------------------------------------------------
#Exercises III

# 1. Use your get_db_url function to help you explore the data from the chipotle database.
# chipotle = pd.read_sql('SELECT * FROM orders', get_db_url(hostname, username, password,'chipotle'))
# chipotle.head(20)
# chipotle.info()

# 2. What is the total price for each order?
#chip_tab = pd.crosstab(chipotle.order_id, chipotle.item_price, margins=True)

#chip_tab = chipotle.groupby(['order_id', 'quantity']).item_price.sum()
#print(chip_tab)

# 3. What are the most popular 3 items?
#pop = chipotle.groupby(['item_name', 'quantity']).quantity.sum()
#print(pop)
# 4. Which item has produced the most revenue?

# 5. Join the employees and titles DataFrames together.

# 6. For each title, find the hire date of the employee that was hired most recently with that title.

# 7. Write the code necessary to create a cross tabulation of the number of titles by department. 
#    (Hint: this will involve a combination of SQL code to pull the necessary data and python/pandas 
#    code to perform the manipulations.)