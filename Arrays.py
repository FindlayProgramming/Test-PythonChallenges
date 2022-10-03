import array as arr
f = arr.array('i', [2, 4, 6, 8, 10])

print("First element:", f[0])
print("Second element:", f[1])
print("Third element:", f[2])

def arrays():
    f = input("What element would you like?")
    if f == 6:
        print(f[2])
    else:
        break

arrays()
