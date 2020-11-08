import json 
import collections
from collections import defaultdict 

# bar_chart_data = collections.defaultdict(lambda: collections.defaultdict(int))
# # Opening CA JSON file 
# f1 = open('./data/data_ca.json',) 
# data1 = json.load(f1) 
# for i,v in data1['job'].items(): 
#     bar_chart_data[v][data1['name'][i]] += data1['count'][i]
# f1.close() 

# # Opening TX JSON file 
# f2 = open('./data/data_tx.json',) 
# data2 = json.load(f2) 
# for i,v in data2['job'].items(): 
#     bar_chart_data[v][data2['name'][i]] += data2['count'][i]
# f2.close() 

# # Opening NY JSON file 
# f3 = open('./data/data_ny.json',) 
# data3 = json.load(f3) 
# for i,v in data3['job'].items(): 
#     bar_chart_data[v][data3['name'][i]] += data3['count'][i]
# f3.close() 

# print(bar_chart_data)

map_data = collections.defaultdict(int)
# Opening CA JSON file 
# f1 = open('./data/data_ca.json',) 
# data1 = json.load(f1) 
# for i,v in data1['job'].items(): 
#     map_data[data1['name'][i]] += data1['count'][i]
# f1.close() 

# Opening TX JSON file 
# f2 = open('./data/data_tx.json',) 
# data2 = json.load(f2) 
# for i,v in data2['job'].items(): 
#     map_data[data2['name'][i]] += data2['count'][i]
# f2.close() 

# # Opening NY JSON file 
f3 = open('./data/data_ny.json',) 
data3 = json.load(f3) 
for i,v in data3['job'].items(): 
    map_data[data3['name'][i]] += data3['count'][i]
f3.close() 

print(map_data)