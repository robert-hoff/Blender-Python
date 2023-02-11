
# list all objects
for obj in bpy.data.objects:
    print(obj)

# get object by its name
my_object = bpy.data.objects['object_name']

# print all the properties of an object
# I used to have `members = obj.__dir__` maybe that was an older syntax
members = dir(obj)
members.sort()
print('\n\n--- object properties')
for name in members:
    print('{:40s} {}'.format(name, getattr(obj, name)))

# the data is often the more useful to operate on
my_object_data_properties = my_object.data.__dir__()

# check if an object with a given name exists
if 'Camera' in bpy.data.objects:
    print('camera exists')





