def camelize(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))

string = camelize('cool_wind')
print(string)
