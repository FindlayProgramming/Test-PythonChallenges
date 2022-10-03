thisdict = {
    "Ten",
    "Twenty",
    "Thirty"
}
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

x = zip(keys, values)
type(x)
list(x)


print(thisdict)

j = ['R', 'F', 'G', 'P']
o = ['J', 'D', 'T', 'E']
dictionary = dict(zip(j, o))

print (dictionary)
