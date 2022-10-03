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

#sampleDict = {
    #"class":{
        #"student":{
            #"name":"Mike",
            #"marks":{
                #"physics":70,
                #"history":80
            #}
        #}
    #}
#}

#print(sampleDict)


sampleDict = {
    "name": "Kelly",
    "age":25,
    "salary": 8000,
    "city": "New york"
}
keysToRemove = ["name", "salary"]

print(sampleDict)
