#Given two dictionaries, d1 and d2, where values are numbers, add values from both the dictionaries with
#common keys. Form a new dictionary with such key, value pairs.

d1= {'a':10, 'b':20,'c':30}
d2= {'b':20 , 'c':30, 'd':40}
d3={}
d4={}
for i in d1:
    for j in d2:
        if i==j:
            key = i
            value = d1[i] + d2[j]
            d3 = {key:value}
            d4.update(d3)

print("New dictionary: ",d4)