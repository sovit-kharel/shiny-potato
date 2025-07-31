records = [
    {'name': "rice", 'price': 120, 'category': "grocery"},
    {'name': "sugar", 'price': 220, 'category': "grocery"},
    {'name': "wheat", 'price': 320, 'category': "grocery"},
    {'name': "rcereal", 'price': 420, 'category': "grocery"},
]

# Writing to the file
f = open("grocery.txt", "w")
f.write("ID   NAME       PRICE     CATEGORY\n")

i = 0
while i < len(records):
    id = i + 1
    name = records[i]['name']
    price = records[i]['price']
    category = records[i]['category']
    line = f"{id:<5}{name:<10}{price:<10}{category}\n"
    f.write(line)
    i = i + 1

f.close()

# Reading from the file and displaying
print("File Contents:")
f = open("grocery.txt", "r")
line = f.readline()
while line:
    print(line.strip())
    line = f.readline()
f.close()




f = open("demo.txt", "w")
f.write("Python file handling example.")
f.close()

f = open("demo.txt", "r")
print(f.read(6))     # Output: Python
f.seek(0)            # Move pointer to beginning
print(f.read(4))     # Output: Pyth
f.seek(7)            # Move to 7th byte
print(f.read(4))     # Output: file
f.close()
