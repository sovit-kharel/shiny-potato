import random
random_list
[random.randit(1,100) for_in range(15)]

list1= random_list[0:5]
list2=random_list[5:10]
list3=random_list[10:15]

sum1=sum(list1)
sum2 =sum(list2)
sum3=sum(list3)

print('list3:',list1)
print('list2:',list2)
print('list3:',list3)

print("largest sum among the three lists is:", max(sum1, sum2, sum3))
print("smallest sum among the three lists is:", min(sum1, sum2, sum3))
