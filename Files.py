#from tabulate import tabulate
f = open("FileTest.txt", "w")
data = "3"
g = 'Work in Progress'

#mydata = [
    #["Is it mutable?", "Yes","Yes","No"],
    #["Can we change the size after creation?", "Yes", "No", "No"],
    #["Can items in the list be changed?", "Yes", "No", "No",],
    #["How many different types of data can be stored", "Any", "Any", "Any",]
#]

#head = ["","List", "Array", "Tuple"]

#with open('FileTest.txt', 'w') as file:
    #file.write(data + g + '\n')
    #file.write(tabulate(mydata, headers=head, tablefmt="grid" + '\n'))
    #file.close()



with open('FileTest.txt', 'a') as file:
    file.write("Hi" + data + g + '\n')
    file.close()
