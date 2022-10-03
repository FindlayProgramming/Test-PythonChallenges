n = int(input("Enter numbers:"))

a = list(map(int,input("\nEnter the numbers:").strip().split()))[:n]

print("\nList is - ", a)

Num = 20

while n == Num:
    print("Number Found")
    break
else:
    print("Number not found")
    print(n)
    print("\nList is -", a)

my_list = [2, 4, 6, 9, 10]

max_listNum = max(my_list)

print(max_listNum)

xs =[1, 2, 7, 9, 10]
print(sum(xs))


list1 = [10, 20, 100, 40, 50]

list1.sort()

print("Smalles number:", list1[0])


def ProductList(List2):
    result = 1
    for x in List2:
        result = result * x
    return result

ListExample = [4, 6, 10]
ListExamp = [9, 5, 12]
print(ProductList(ListExample))
print(ProductList(ListExamp))
