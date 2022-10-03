#def online_count(PeopleDictionary):
    #return sum(status == 'online' for status in PeopleDictionary.values()) #returns the status of people that are online from the parameter PeopleDictionary.

#statuses = { #People who are offline/online.
    #"Alice": "online",
    #"Bob": "offline",
    #"Eve": "online",
#}
#print(online_count(statuses))

#n=45 #set value for n.
#f="GDSDGFH" #set value for f.

#def only_ints(n, f): #This function takes two parameters n and f.
    #if isinstance(n, int): #Says that if n is an integer it is to return True.
        #return True
    #if isinstance(f, int): #Same with n.
        #return True
    #else:
        #return False #If the values have been change from int to string it will print False regardless of what is put.
#print(isinstance(n, int)) #Prints out True.
#print(isinstance(f, int)) #Prints out False.

#only_ints(n, f) #Returns whole function.

#def double_letters(Duffy):
    #for i in range (len(Duffy)-1):
        #if Duffy[i] == Duffy[i+1]:
            #return True
        #return False

#print(double_letters("Error")) #This is my first example of the double letters task. I have left it here incase.

#def double_letters(str1): #string parameter.
    #return any(c1 == c2 for c1, c2 in zip(str1, str1[1:])) #If one letter in the string is repeated then it will store the letter and then return True.
#str = "Duffy"
#print("Original string:", str)
#print("Check for consecutive similar letters!", double_letters(str)) #Returns True.
#str = "Dufy"
#print("\nOriginal string:", str)
#print("Check for consecutive similar letters!", double_letters(str)) #Returns False.
#str = "Dufyy"
#print("\nOriginal string:",str)
#print("Check for consecutive similar letters! ", double_letters(str)) #Returns True. If a letter is repeated then it will return as false no matter the string (this includes if a letter has more than one repeating letter).


#def count(metaphor): #New Function.
    #metaphor == metaphor.lower() #
    #count = 0 #Count starts at zero.
    #vowels = "aeiouy" #Set vowels.
    #if metaphor[0] in vowels:
        #count +=1
    #for index in range(1, len(metaphor)):
        #if metaphor[index] in vowels and metaphor[index - 1] not in vowels:
            #count += 1
    #if metaphor.endswith("e"):
        #count -= 1
    #if count == 0:
        #count += 1
    #return count

#print(count('met-a-phor'))
