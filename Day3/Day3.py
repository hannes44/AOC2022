from functools import reduce
import string

# Today i solved the problem using cursed one liners
def partOne():
    return reduce(lambda x, y: 1+ x +string.ascii_lowercase.index(y) if not y.isupper() else x+string.ascii_uppercase.index(y) + 27 , reduce(lambda a, b: a+[b[0]], map(lambda x: list(filter(lambda y: y in x[1], x[0])) , [[line[0:int(len(line)/2)], line[int(len(line)/2):]] for line in [line.strip() for line in  open("input.txt", "r").readlines()]])),0)

def partTwo():

    parsedInput = [line for line in [line.strip() for line in open("input.txt", "r").readlines()]]
    return reduce(lambda x, y: 1+ x +string.ascii_lowercase.index(y) if not y.isupper() else x+string.ascii_uppercase.index(y) + 27 , list(map(lambda x: list(filter(lambda y: y in x[1] and y in x[2],x[0]))[0],[parsedInput[i:i+3] for i, line in enumerate(parsedInput) if i % 3 == 0])), 0) 
   
    
print(partOne())
print(partTwo())