import pickle


myDict = {'a':'b', 'c':'d', 'e':'f'}

with open("dict.txt", 'wb') as f:
    f.write(pickle.dumps(myDict))
