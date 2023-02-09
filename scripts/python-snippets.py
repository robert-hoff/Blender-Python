


# create an empty list and add integers to it
mylist = []
for myint in range(1,11):
    mylist.append(myint)

# Python doesn't have a problem mixing integers and strings
mylist.append('hello')

# tuples are valid Python objects
mylist = []
for myint in range(1,11):
    mylist.append((myint,myint))


# print all the properties of an object
light_properties = light.__dir__()
light_properties.sort()
for prop in light_properties:
    print(prop)

# data is usually the more useful to operate on
light_data = light.data__dir__()





