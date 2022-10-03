from tabulate import tabulate

mydata = [
    ["Is it mutable?", "Yes","Yes","No"],
    ["Can we change the size after creation?", "Yes", "No", "No"],
    ["Can items in the list be changed?", "Yes", "No", "No",],
    ["How many different types of data can be stored", "Any", "Any", "Any",]
]

head = ["","List", "Array", "Tuple"]

print(tabulate(mydata, headers=head, tablefmt="grid"))



