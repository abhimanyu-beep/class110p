import pandas as p 
import csv 
import plotly.figure_factory as ff 
import statistics 
import plotly.graph_objects as go
import random
df=p.read_csv("datesof.csv")
datesof= df["date"].tolist()
mean=statistics.mean(datesof)
print(mean)
sd1=statistics.stdev(datesof)
print(sd1)
def randomsetofmeans(counter):
    dataset=[]
    for i in range(0,counter):
        randomindex=random.randint(0,len(datesof
    )-1)
        value=datesof
    [randomindex]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def showfigure(meanlist):
    df=meanlist
    figure=ff.create_distplot([datesof
],["date"],show_hist=False)
    figure.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    figure.show()
def setup():
    meanlist=[]
    for i in range(0,1000):
        setofmeans=randomsetofmeans(100)
        meanlist.append(setofmeans)
    showfigure(meanlist)
setup()-9