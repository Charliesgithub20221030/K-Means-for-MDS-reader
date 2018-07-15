#K-means practice for user to know step by step

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import data set
dataset = pd.read_csv('Consumer_data.csv')
x=dataset.iloc[:,[3,4]].values


#before clustering
plt.scatter(x=x[:,0],y=x[:,1],color='black')  
plt.title('Group of customers')
plt.xlabel('Age')
plt.ylabel('Income')
plt.scatter(x=ini1[0],y=ini1[1],color='greenyellow')# 第一類中心
plt.scatter(x=ini2[0],y=ini2[1],color='darkviolet')#  第二類中心
plt.show()


# We set a certain point for initialization, 
# but in real condition ,it's not necessary
ini1=[40000,2000]
ini2=[100000,8000]
c1=list()
c2=list()

for n1,n2 in zip(x[:,0],x[:,1]):
    d1=((n1-ini1[0])**2+(n2-ini1[1])**2)**0.5
    d2=((n1-ini2[0])**2+(n2-ini2[1])**2)**0.5
    if d1<d2:
        c1.append([n1,n2])
    else:
        c2.append([n1,n2])
s1x=0
s1y=0
s2x=0
s2y=0
plt.cla()
for i,j in c1: 
    plt.scatter(x=i,y=j,color='lightgreen')
    s1x+=i
    s1y+=j

for i,j in c2:    
    plt.scatter(x=i,y=j,color='pink')
    s2x+=i
    s2y+=j

plt.scatter(x=ini1[0],y=ini1[1],color='darkslategray')# 第一類中心
plt.scatter(x=ini2[0],y=ini2[1],color='darkviolet')#  第二類中心
plt.xlabel('Income')
plt.xlabel('Spending')
plt.show()


##central---repeat this step until it print 'Done'


ini1[0]=s1x/len(c1)
ini1[1]=s1y/len(c1)
ini2[0]=s2x/len(c2)
ini2[1]=s2y/len(c2)


c1=list()
c2=list()

for n1,n2 in zip(x[:,0],x[:,1]):
    d1=((n1-ini1[0])**2+(n2-ini1[1])**2)**0.5
    d2=((n1-ini2[0])**2+(n2-ini2[1])**2)**0.5
    if d1<d2:
        c1.append([n1,n2])
    else:
        c2.append([n1,n2])
s1x=0
s1y=0
s2x=0
s2y=0
plt.cla()
for i,j in c1: 
    plt.scatter(x=i,y=j,color='lightgreen')
    s1x+=i
    s1y+=j

for i,j in c2:    
    plt.scatter(x=i,y=j,color='pink')
    s2x+=i
    s2y+=j
plt.scatter(x=ini1[0],y=ini1[1],color='darkslategray')# 第一類中心
plt.scatter(x=ini2[0],y=ini2[1],color='darkviolet')#  第二類中心
plt.xlabel('Income')
plt.xlabel('Spending')
plt.show()


if ini1[0]==s1x/len(c1) and ini1[1]==s1y/len(c1) and ini2[0]==s2x/len(c2) and ini2[1]==s2y/len(c2):
    print('Done')
