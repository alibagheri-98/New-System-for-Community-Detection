from dtaidistance import innerdistance
from dtaidistance import dtw,dtw_ndim
import numpy as np
"""_summary_
This code defines a set of functions to calculate the similarity/distance between time series of stock prices.
The innerdistance module provides the dtw distance calculation functionality,
which calculates the Dynamic Time Warping distance between two time series.
The my_dist class is a custom implementation of innder distance calculation,
accoding to the paper "A similarity measurement for time series and its application to the stock market https://doi.org/10.1016/j.eswa.2021.115217"


The function get_most takes two series and returns the shorter series and its corresponding portion from the end of the longer series.
This function is used to compare the most recent stock prices.

The function calc_proprty takes two stock prices and a timestamp and calculates a set of properties:
distance, mid (the average of two prices), s1_jumped (if the first stock price is greater than 5),
s2_jumped (if the second stock price is greater than 5),
and all_gone (if both stocks are greater than 4.5, the timestamp is greater than 3.5, or both stocks are less than -4.5, the timestamp is less than -3.5).

The function arenan takes a variable number of arguments and returns True if any argument is NaN.

The function calc_edge takes two series and a list of timestamps and returns a similarity score based on the given type.
 If type is 1, it calculates a semi-correlation score between the two series based on their properties.
 If type is 2, it calculates the DTW distance between the two series.
 If type is 3, it also calculates the DTW distance but with a custom inner distance class my_dist.
 If type is 4, it calculates a distance score based on the difference between the two stocks, normalized by the number of days.
 If type is 5, it calculates a similarity score based on the absolute difference of the stock prices, normalized by the number of days.

The validate_adj function takes a list of stock names, an adjacency matrix adj that measures the similarity between the stocks,
a type of similarity metric, a list of stock names to compare with (my_stock),
a number of stocks to randomly compare (n), and showall flag to print all the comparisons.
"""

# proposed by "A similarity measurement for time series and its application to the stock market https://doi.org/10.1016/j.eswa.2021.115217"
class my_dist(innerdistance.CustomInnerDist):
    @staticmethod
    def inner_dist(x, y):
        if(x!=0 and y!=0):
          return abs(x - y)/(abs(x)+abs(y))
        return 0
    @staticmethod
    def result(x):
        return x
#
#
def get_most(ser1,ser2):
    s = min(len(ser1.dropna()),len(ser2.dropna()))
    s1 = ser1[-s:]
    s2 = ser2[-s:]
    return s1,s2,s
#
#this is mostly customized for Iran Stock but it can be used for others as well by just some tuning
def calc_proprty(s1,s2):
    dist = abs(s1-s2)
    mid = (s1-s2)/2
    s1_jumped = s1>5
    s2_jumped = s2>5
    return dist, mid,s1_jumped,s2_jumped
#
#
def arenan(*args):
    for i in args:
        if np.isnan(i):
            return True
    return False
#
#this is mostly customized for Iran Stock but it can be used for others as well by just some tuning
def calc_edge(ser1,ser2,type,tresh = 1.2):
    # assert len(ser1.index) == len(ser2.index) == len(totindex),"should have the same len"
    s1, s2, s = get_most(ser1,ser2)
    if s==0 :
        return -1
    if type == 1:
        semi_cor = 0
        for i , j ,in zip(s1,s2):
            dist ,mid,s1_jumped,s2_jumpled = calc_proprty(i,j)
            if dist < tresh:
                semi_cor+=1
        return semi_cor/s
    elif type == 2:
        # needs C library
        return  dtw.distance_fast(s1.to_numpy(),s2.to_numpy(),window=4,penalty=1,use_pruning=True,only_ub=True,max_step=4)
    elif type == 3:
        # customized and more speed efficent than defult
        if s==0:
            return -1
        return dtw.distance(s1.to_numpy(),s2.to_numpy(),window=4,inner_dist=my_dist(),penalty=1,use_pruning=True,only_ub=True,max_step=4)/s
    elif type == 4:
        days = 0
        tot_dist = 0
        for i , j in zip(ser1,ser2):
            if not arenan(i,j):
                dist ,mid,s1_jumped,s2_jumpled = calc_proprty(i,j)
                if(not s1_jumped and not s2_jumpled):
                    tot_dist+=dist
                else :
                    tot_dist+=min(dist,5)
            else:
                continue
        return tot_dist/s
    elif type == 5:
        dist = 0
        days = 0
        for i , j  in zip(ser1,ser2):
            if not arenan(i,j):
                dist+=-abs(i-j)
                days+=1
        return -dist/days
# multi_dim proposed by  "A Novel Time-Sensitive Composite Similarity Model for Multivariate Time-Series Correlation Analysis  https://doi.org/10.3390/e23060731"
# def calc_multi_edge(ser1,ser2):
#     # ser1,ser2 = nanMulti_Fix(ser1,ser2)
#     ser1 = np.nan_to_num(ser1)
#     ser2 = np.nan_to_num(ser2)
#     # print(ser1)
#     return dtw_ndim.distance(ser1, ser2,window=4,penalty=1,use_pruning=True,only_ub=True,max_step=4)
#     # pass
# def nanMulti_Fix(ser1,ser2):
#     for index,(el1,el2 )in enumerate(zip(ser1,ser2)):
#         if contains_nan(el1) or contains_nan(el2):
#             np.delete(ser1, index,axis=0)
#             np.delete(ser2, index,axis=0)
#     return ser1 ,ser2
# def contains_nan(ser):
#     for i in ser:
#         if np.isnan(i):
#             return True
#     return False
def validate_adj(stock_list,adj,type,my_stock=None,n=10,showall=False):
    if my_stock == None:
        random_list = np.random.randint(0,50,n)
    else:
        random_list = [int(np.where(stock_list == stock)[0]) for stock in my_stock]
    if type == 0 :
        dialog = 'distnaced'
    else :
        dialog = 'similarity'
    for i in random_list:
        for j in random_list:
                if showall:
                    print(f'{stock_list[i]:10} and {stock_list[j]:10} are {adj[i][j]:.3f} {dialog}') 
        if type == 0:
            this_adj = np.argsort(adj[i])[0:4]
            this_adj2 = np.argsort(adj[i])[-4:]
            print(f'{stock_list[i]:10} is most like {stock_list[this_adj]} with {dialog} of {adj[i][this_adj]}')
            print(f'{stock_list[i]:10} is less like {stock_list[this_adj2]} with {dialog} of {adj[i][this_adj2]}')
        else:
            this_adj = np.argsort(adj[i])[-5:]
            this_adj2 = np.argsort(adj[i])[0:4]
            print(f'{stock_list[i]:10} is most like {stock_list[this_adj]} with {dialog} of {adj[i][this_adj]}')
            print(f'{stock_list[i]:10} is less like {stock_list[this_adj2]} with {dialog} of {adj[i][this_adj2]}')
        print('-----------------------\n')

# print('hi')