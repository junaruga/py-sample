keys = ['a', 'b']
values = ['A', 'B']

for key, value in iter(zip(keys, values)):
    print("key: {}, value: {}".format(key, value))
