num = input("Enter numbers separated by space: ").split() #split le space anusar list of string banauxa 
l1 = [int(num) for num in num] 
# using builtin function  
max_num=max(l1) 
min_num=min(l1) 
print(f"{max_num} is maximum and {min_num} is minimum") 
print(sorted(l1)) 
print("List without duplication") 
noduplicate=set(l1) 
print(noduplicate) 


n= int(input("Enter the value of numbers you want to store: ")) 
l1=[] 
for i in range(n): 
j=int(input("Enter the value: ")) 
l1.append(j) 
for i in range(n): 
for j in range(n-1): 
if(l1[i]>l1[j+1]): 
l1[j],l1[j+1]=l1[j+1],l1[j] 
print(f"Maximum is {l1[-1]} and minimun is {l1[0]}") 
print(f"Sorted list is {l1}") 
l2=[] 
for i in l1: 
if i not in l2: 
l2.append(i) 
print(f"without duplicate{l2}")


l1=[1,2,4,3,2,4,24,5] 
l2=[3,2,4,2,4,2,1,3,5] 
mergedList=l1+l2 
print(f"Merged list is {mergedList}") 
l3=mergedList.copy() 
for i in l3: 
if i in l1 and i in l2: 
l3.remove(i) 
print(l3) 


string = input("Enter string separated by space: ")#split le space anusar list of string banauxa 
l1 = string.split() 
unique=[] 
print(l1) 
for word in l1: 
if word  not in unique: 
unique.append(word) 
6 
for word in unique: 
print(word,l1.count(word)) 



stack = [] 
while True: 
choice = input("enter 1 push 2 pop 3 display") 
if choice == "1": 
num = int(input("Enter a number: ")) 
stack.append(num) 
elif choice == "2": 
if (len(stack) == 0): 
print("stack is empty") 
continue 
print(f"Deleted element is: {stack.pop()}") 
elif choice == "3": 
if (len(stack) == 0): 
print("stack is empty") 
continue 
print(f"elements are: {stack}") 
else: 
print("invalid choice") 
break 


queue = [] 
while True: 
choice = input("enter 1 eqQ 2 deQ 3 display") 
if choice=="1": 
num = int(input("Enter a number: ")) 
queue.append(num) 
elif choice=="2": 
if(len(queue)==0): 
print("queue is empty") 
continue 
print(f"Deleted element is: {queue.pop(1)}") 
elif choice=="3": 
if(len(queue)==0): 
print("queue is empty") 
continue 
print(f"elements are: {queue}") 
else: 
print("invalid choice") 
break 



n= int(input("Enter the value of numbers you want to store: ")) 
l1=[] 
for i in range(n): 
j=int(input("Enter the value: ")) 
l1.append(j) 
even_indices = range(0,len(l1),2) 
print(even_indices) 
for index in even_indices: 
count = 0 
for i in range(1,l1[index]+1): 
if (l1[index]%i==0): 
count +=1 
if count==2: 
print(l1[index]) 



n=int(input("Enter the number of elements: ")) 
l1=[] 
for i in range(n): 
num=int(input("Enter the value: ")) 
l1.append(num) 
t1=tuple(l1) 
average=(sum(t1)/n) 
print(f"the average is {average}") 
t2=(sorted(t1)) 
if(n%2==0): 
median=(t2[(n-1)//2]+t2[((n-1)//2)+1])/2 
else: 
median=t2[(n-1)//2] 
print(f"Median is {median}") 
#mode 
max_count=0 
mode=None 
for num in t2: 
count=t2.count(num) 
if (count>max_count): 
max_count=count 
mode=num 
print(f"The mode of the tuple is {mode} with frequency {max_count}")



def straight(l1): 
if(len(l1)<=2): 
print("They form straight line") 
x0,y0=l1[0] 
x1,y1=l1[1] 
dx=x1-x0 
dy=y1-y0 
#points form straight line if the slope is constant 
for i in range(2,len(l1)): 
xi,yi=l1[i] 
dx_i = xi - x0 
dy_i = yi - y0 
if dy * dx_i != dy_i * dx: 
print("Not straight line") 
return 
n=int(input("Enter the number of points: ")) 
l1=[] 
for i in range(n): 
x=int(input("Enter x coordinate: ")) 
y=int(input("Enter y coordinate: ")) 
l1.append((x,y)) 
print(l1) 
straight(l1)



n=int(input("Enter a total number of student: ")) 
universal=set() 
for i in range(n): 
roll=int(input("Enter the roll number of student: ")) 
universal.add(roll) 
c=int(input("Enter number of student who play cricket:")) 
cricket=set() 
for i in range(c): 
roll=int(input("Enter cricket player's roll no: ")) 
cricket.add(roll) 
f=int(input("Enter the number of football players: ")) 
football=set() 
for i in range(f): 
roll=int(input("Enter the roll no of football players: ")) 
football.add(roll) 
print(f"The roll number of students who play both sports are {cricket & football}") 
print(f"The roll number of students who play neither sports are { universal-(cricket | football)}") 
print(f"The roll number of students who play only one sports are {cricket ^ football}")



import random 
num=set() 
while len(num)<10: 
num.add(random.randint(1,100)) 
print(f"Set with 10 unique numbers: {num}") 
smallest=min(num) 
largest=max(num) 
num.remove(smallest) 
num.remove(largest) 
print(f"Set after removing smallest and largest numbers:{num} ")



#to find unique vowels in a sentence 
vowel={'a','e','i','o','u'} 
unique=set() 
string=input("Enter a sentence: ") 
for char in string.lower(): 
if char in vowel: 
unique.add(char) 
print("the unique vowels used are",unique)



l=[1,2,3,4,3,2,1,31,4,5,89,900,78] 
unique=set(l) 
print(l) 
print("no duplicate") 
print(unique) 
sortedset=sorted(unique) 
print("Sorted set  is ",sortedset)




students={} 
n=int(input("Enter the number of students:")) 
for i in range(n): 
name=input("Enter student name:") 
marks=[] 
for j in range(1,4): 
mark=int(input("Enter marks for student: ")) 
marks.append(mark) 
students[name]=marks 
def displayAverage(stds): 
for k,v in stds.items(): 
average = sum(v) / len(v) 
print("The average is", average) 
#to find topper 
def displayTopper(stds): 
topper = "" 
highest = 0 
for k, v in stds.items(): 
average = sum(v) / len(v) 
if average > highest: 
highest = average 
topper = k 
print(f"the topper is {topper} and highest average mark is {highest}") 
def updateMarks(stds): 
name = input("Enter student name you want to update:") 
if name in stds: 
newMarks = [] 
for i in range(1, 4): 
mark = int(input("Enter marks for student: ")) 
newMarks.append(mark) 
stds[name] = newMarks 
print("Updated!!") 
else: 
print("Student not found") 
while True: 
print("1. Display average marks") 
print("2. Display topper") 
print("3. Update marks") 
print("4. Exit") 
choice=int(input("Enter choice:")) 
if choice==1: 
displayAverage(students) 
elif choice==2: 
displayTopper(students) 
elif choice==3: 
updateMarks(students) 
elif choice==4: 
print("Exiting") 
break 
else: 
print("Invalid choice") 
continue



string=input("enter a string: ") 
freq={} 
for char in string.lower(): 
if char.isalpha(): 
freq[char]=freq.get(char,0)+1 
print(freq)




products={} 
def addProduct(product): 
name=input("enter product name: ") 
if name  not in product: 
price=int(input("enter product price: ")) 
product[name]=price 
print("product added") 
def update(product): 
name=input("enter product name to update: ") 
if name in product: 
newprice=int(input("enter new product price: ")) 
product[name]=newprice 
print("product price updated") 
else: 
print("product not found") 
def findproduct(product): 
ll=int(input("Enter product lower limit: ")) 
ul=int(input("Enter product upper limit: ")) 
found = False 
for k,v in product.items(): 
if (v>=ll and v<=ul): 
print(f"product {k} is {v}") 
found=True 
if not(found): 
print("product not found") 
while True: 
print("1. Add new product") 
print("2. Update product price") 
print("3. Find product") 
print("4. Exit") 
choice = input("Enter your choice: ") 
if choice == "1": 
addProduct(products) 
if choice == "2": 
update(products) 
if choice == "3": 
findproduct(products) 
if choice == "4": 
exit()




def report_card(local_roll,local_student): 
output = f""" 
{local_student["name"]}'s Report Card 
Name: {local_student["name"]} 
Roll number: {local_roll} 
<--Marks in various subjects -->           
""" 
print(output) 
for local_subject in subjects: 
print(f"{local_subject}: {local_student['marks'][local_subject]}") 
print( 
f"TOTAL MARKS: {local_student['total']} \nPercentage: {local_student['percentage']}% \n") 
print(" Welcome to Student Report Card Management System") 
data = {} 
subjects = ["Physics", "English", "Maths", "Chemistry", "Computer"] 
while True: 
print("What do you want to do?") 
task = input("Add -> Add new student data \nView -> View all student data\n" 
"Topper -> Display the class topper \nSearch -> Search student by roll no.\n" 
"Failures -> Display the data of failed students\n" 
"Update -> Update student marks\n" 
"Exit -> Exit program\n") 
if task == "Add": 
name = input("Enter student name: ") 
roll_no = input("Enter student roll no: ") 
marks = {} 
for subject in subjects: 
mark = int(input(f"Enter student's marks in {subject}: ")) 
marks[subject] = mark 
total = sum(marks.values()) 
percentage =  total / len(subjects) 
data[roll_no] = {"name": name, "marks": marks, "total":total,"percentage": percentage} 
elif task == "View": 
for roll_no, student in data.items(): 
report_card(roll_no, student) 
elif task == "Topper": 
topper = [] 
highest = max([student['total'] for student in data.values()]) 
for student in data.values(): 
if student['total'] == highest: 
topper.append(student['name']) 
print("The list of topper(s) is:") 
for item in topper: 
print(item) 
print("\n") 
elif task == "Search": 
roll = input("Enter the student's roll number: ") 
report_card(roll, data[roll]) 
elif task == "Failures": 
failures = [] 
for student in data.values(): 
for mark in student["marks"].values(): 
if mark < 40: 
failures.append(student["name"]) 
break 
print("The list of failures is:") 
for item in failures: 
print(item) 
print("\n") 
elif task == "Update": 
change = input("Enter the student's roll number and subject to update: ") 
roll, subject = change.split(" ") 
new_marks = int(input("Enter the new mark: ")) 
data[roll]['marks'][subject] = new_marks 
total = sum(data[roll]['marks'].values()) 
percentage = total / len(subjects) 
data[roll]['total'] = total 
data[roll]['percentage'] = percentage 
print("Updated successfully!!") 
print("\n") 
elif task == "Exit": 
break
