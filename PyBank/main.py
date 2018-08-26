
# coding: utf-8

# In[1]:

import pandas as pd
import os


# In[4]:

filename = os.path.join("Pybank/Resources/budget_data.csv")
filename
df = pd.read_csv(filename)
df.head()


# In[7]:

# The total number of months included in the dataset
print("The total number of months included in the dataset: ", df["Date"].count())


# In[39]:

# The total net amount of "Profit/Losses" over the entire period
total = df["Profit/Losses"].sum()
print("The total net amount of Profit/Losses over the entire period is $%0.2f" %total)


# In[32]:

# The average change in "Profit/Losses" between months over the entire period
df['shifted_column'] = df['Profit/Losses'].shift(1)
df['difference'] = df['Profit/Losses'] - df['shifted_column']
df['difference']
#df['difference'] = df['difference'].abs()
average = df['difference'].mean()
print("The average change in Profit/Losses between months over the entire period is $%0.2f" %average)


# In[33]:

# The greatest increase in profits (date and amount) over the entire period
maximum = df['difference'].max()

print("The greatest increase in profits over the entire period is $%0.2f" %maximum)


# In[35]:

# The greatest decrease in losses (date and amount) over the entire period
minimum = df['difference'].min()
print("The greatest decrease in profits over the entire period is $%0.2f" %minimum)


# In[47]:

# Summary
print("Financial Analysis")
print("-"*30)
print("Total Months: " , df['Date'].count())
print("Total: $" ,total)
print("Average  Change: $", average)
print("Greatest Increase in Profits: $" , maximum)
print("Greatest Decrease in Profits: $" , minimum)


# In[ ]:



