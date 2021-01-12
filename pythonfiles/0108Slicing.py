
family = ["Qiyu", "Di", "Derrick", "Lixin", "Wei", "Yuchong", "Tao", "Xiuxiang", "Zhao", "Xiang", "Meng", "Dan", "Lu", "Guang", "MengC", "Yi","Ping","Fan", "Mia","Qiong"]
for i in family:
  print("Hi" + ", " + i + "!")


for i in range(1,10):
  print(i)

numbers = list(range(1,20,2))
print(numbers)

list = []
numbers = int(input("Enter a number: "))
for numbers in list:
  if numbers % 2 == 0:
    print ("The number is even.")
  else:
    print("The number is odd.")
list.append(numbers)
print(list)

for num in range(2,101):
    if all(num%i!=0 for i in range(2,num)):
       print (num)

print(family[0:2])
print(family[0:5])
print(family[1:6])
print(family[5:20])
print(family[-5:])
print(family[-8:-2])
print(family[15:])
print(family[0:])
print(family[:10])
print(family[:])