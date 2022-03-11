import csv
from re import S
import plotly.figure_factory as pf
import plotly.graph_objects as pg
import pandas as pd
import statistics
import random

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

population_mean = statistics.mean(data)
print("The population mean is: ",population_mean)

population_std_dev = statistics.stdev(data)
print("The standard deviation of population is: ",population_std_dev)

fig=pf.create_distplot([data],["temp"],show_hist=False)
fig.show()

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean
    #print("The sample mean is: ",mean)

    #std_dev = statistics.stdev(dataset)
    #print("The standard deviation of sample_population is: ",std_dev)

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig=pf.create_distplot([df],["temp"],show_hist=False)
    fig.add_trace(pg.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)

    show_fig(mean_list)

    mean= statistics.mean(mean_list)
    print("The mean of sampling distribution is:-",mean)

setup()

def std_dev():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)

    sample_std_dev= statistics.stdev(mean_list)
    print("The standard deviation of sampling distribution is:-",sample_std_dev)

std_dev()