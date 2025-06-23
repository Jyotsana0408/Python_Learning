# we cannot directly change original tuple
# for that we need to convert tuple to list
# and then make changes 
# and then again convert list to tuple


countries = ("spain", "india","japan","china","korea","germany")
print(countries)

temp = list(countries)
temp.append("russia")
temp.pop(3)
temp[2] = "finland"

countries = tuple(temp)
print(countries)



# concatenation in tuple --> will return new tuple
countries1 = ("japan", "india")
countries2 = ("russia", "china")
asia_countries = countries1 + countries2
print(asia_countries)


# count methods

tup5 = (0,1,2,2,3,3,3,4,4,4,4,4)
res = tup5.count(3)
print(res)

# index method  --> will return the first occurence of item in tuple
#  it wll raise value error if item is not present in tuple
res1 = tup5.index(3)
print(res1)


res3 = tup5.index(3,5,8)  #slice the tuple from 5 to 8
print(res3)

res4 = len(tup5)
print(res4)
