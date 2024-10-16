import pandas as pd
import statsmodels.api as sm
import matplotlib as mpl
import matplotlib.pyplot as plt
#import sys
#sys.path.insert(0, '../toxicidade-sentimento/scripts')
#import response_to_dataframe as rd # type: ignore

df = pd.read_csv("dados/processed/teste100.csv")

def plot_qq(df):
    for column in df.columns:
        sm.qqplot(df[column], line='45')
        plt.title(f'Q-Q plot for {column}')
        plt.show()

#plot_qq(df)

def plot_pie(df):
    for column in df.columns:
        plt.figure(figsize=(6, 6))
        plt.pie(df[column], labels=df.index, autopct='%1.1f%%')
        plt.title(f'Pie Chart for {column}')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()

#plot_pie(df)

def plot_histograms(df):
    df.hist(bins=10, figsize=(12, 10), layout=(3, 2), edgecolor='black')
    plt.suptitle('Histograms for Each Column')
    plt.show()

plot_histograms(df)