#Choosing between sort() and sorted():
#Use list.sort() when you need to modify the original list and don't require a new one.
#Use sorted() when you need a new sorted list and want to preserve the original list.

lst1 = [10,18,13,100,65,37]
lst = [1,5,2,10,12,37]



lst1.sort()
print(lst1)

res = map(lambda x: x*x, lst)
print(list(res))

sorted_lst =  sorted(lst)  
print(sorted_lst)

#sort dict by value
d = {'one':1,'three':3,'five':5,'two':2,'four':4}
print(d.items())
a = sorted(d.items(), key=lambda x: x[1])    
print(a)

#sort list of dict
data =  [{"id" : 1, "name" : "Ramesh", "weight": 70},
         {"id" : 2, "name" : "Anand", "weight": 85},
         {"id" : 3, "name" : "Dravid", "weight": 56},
         {"id" : 4, "name" : "Ullas", "weight": 92}]
         
         

print(list(sorted(data, key = lambda x: x['name'])))