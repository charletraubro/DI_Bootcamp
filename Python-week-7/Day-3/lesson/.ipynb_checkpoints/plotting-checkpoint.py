import pandas as pd
import numpy as np
import ssl
import seaborn as sns
ssl._create_default_https_context = ssl._create_unverified_context
import matplotlib.pyplot as plt
titanic_df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
# print(titanic_df.head())
# print(titanic_df.columns.values)
# print(titanic_df.describe())
# print(titanic_df[['Sex', 'Survived']].groupby('Sex').mean())
# print(titanic_df[['Sex', 'Pclass', 'Survived']].groupby(['Sex', 'Pclass']).mean())
# print(titanic_df[['Parch','Survived']].groupby(['Parch']).mean())
# print(plt.hist(titanic_df, col = 'Survived'))
g = sns.FacetGrid(titanic_df, col='Survived')
print(g.map(plt.hist,'Age'))
print(plt.show())

