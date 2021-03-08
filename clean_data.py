import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def create_list(l):
    d = {}
    r = []
    c = 0
    for i in l:
        if i not in d:
            d[i] = c
            c += 1
        r.append(d[i])
    return r

class cleaned_data:
    def clean():
        #read pulled data
        data = pd.read_csv('data/hotels_data.csv')
        df = pd.DataFrame(data)
        #remove entries missing rate plan info
        df = df[df['geoBullets'] == "[]"]
        cols = [0,1,2,6,9,10]
        df = df[df.columns[cols]]
        #format rate plan without "$" or ","
        df['ratePlan'] = df['ratePlan'].map(lambda x: x.lstrip('$').replace(',',''))
        #ensure numeric categories are numbers
        df['ratePlan'] = df['ratePlan'].astype(int)
        df['guestReviews'] = df['guestReviews'].astype(float)
        df['starRating'] = df['starRating'].astype(float)
        #convert neighbourhood names to enumerated values
        df['enumNeighbourhoods'] = create_list(df['neighbourhood'])
        #write to new CSV
        df.to_csv('data/cleaned_hotels_data.csv')
        
    def plot_data():
        data = pd.read_csv('data/cleaned_hotels_data.csv')
        df = pd.DataFrame(data)
        #df.hist(column='ratePlan',density=1)
        #df = df.groupby('neighbourhood')['ratePlan'].mean().plot(kind='bar')
        df.plot(x='starRating',y='ratePlan',kind='scatter')
        df.plot(x='guestReviews',y='ratePlan',kind='scatter')
        #plot correlation heat map
        #cmap = sns.diverging_palette(150, 275, as_cmap=True)
        sns.heatmap(df.corr()[['ratePlan']], annot=True)
        
        plt.show()


c = cleaned_data
c.clean()
c.plot_data()

    
