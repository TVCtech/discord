'''python discord tempalte'''

```Python

# Exercise 1: 
aLsit = [100, 200, 300, 400, 500]
print(aLsit[::-1])

#Exercise 6: 
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

for elm in list1 :
    if elm =='':
        list1.remove(elm)
print(list1)

#Exercise 7:
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

# Exercise 8: 
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list1[2][1][2].extend(["h", "i", "j"])
print(list1)

# Exercise 9: 
list1 = [5, 10, 15, 20, 25, 50, 20]
list1[list1.index(20)] = 200
print(list1)

```