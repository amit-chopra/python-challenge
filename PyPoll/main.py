
# coding: utf-8

# In[1]:

import os
import pandas as pd


# In[27]:

filename = os.path.join("PyPoll/Resources/election_data.csv")
df = pd.read_csv(filename)
df.head


# In[13]:

# The total number of votes cast

print("Total votes: ", df["Voter ID"].count())


# In[29]:

# A complete list of candidates who received votes
df.columns
df_khan = df.loc[df["Candidate"] == "Khan"]
df_khan.count()


# In[30]:

df.columns
df_Correy = df.loc[df["Candidate"] == "Correy"]
df_Correy.count()


# In[31]:

df.columns
df_OTooley = df.loc[df["Candidate"] == "O'Tooley"]
df_OTooley.count()


# In[32]:

df.columns
df_Li = df.loc[df["Candidate"] == "Li"]
df_Li.count()


# In[41]:

# The percentage of votes each candidate won
Khan_votes = df_khan.count()/df["Voter ID"].count()
Khan_votes
#print("Khan won %.2f" %Khan_votes) 


# In[43]:

Correy_votes = df_Correy.count()/df["Voter ID"].count()
Correy_votes


# In[44]:

OTooly_votes = df_OTooley.count()/df["Voter ID"].count()
OTooly_votes


# In[45]:

Li_votes = df_Li.count()/df["Voter ID"].count()
Li_votes


# In[50]:

# The total number of votes each candidate won
print("Khan won:" ,df_khan["Voter ID"].count(), "votes")
print("Correy won:" ,df_Correy["Voter ID"].count(), "votes")
print("O'Tooley won:" ,df_OTooley["Voter ID"].count(), "votes")
print("Li won:" ,df_Li["Voter ID"].count(), "votes")


# In[ ]:

# The winner of the election based on popular vote
print("The winner of the election based on popular vote is " )


# In[63]:

# Summary

print("Election Results")
print("-"*30)
print("Total Votes: ", df["Voter ID"].count())
print("-"*30)
print("Khan won:  {0:.0%}".format(df_khan["Voter ID"].count()/df["Voter ID"].count()), "(",(df_khan["Voter ID"].count()),")")
print("Correy won:  {0:.0%}".format(df_Correy["Voter ID"].count()/df["Voter ID"].count()), "(",(df_Correy["Voter ID"].count()),")")
print("Li won:  {0:.0%}".format(df_Li["Voter ID"].count()/df["Voter ID"].count()), "(",(df_Li["Voter ID"].count()),")")
print("O'Tooley won:  {0:.0%}".format(df_OTooley["Voter ID"].count()/df["Voter ID"].count()), "(",(df_OTooley["Voter ID"].count()),")")
print("-"*30)
print("Winner: Khan")
print("-"*30)


# In[ ]:



