target = 100
n1, n2 = 1, 1
count = 0
num_list = []
if target <= 0:
   print("Please enter a positive integer")
elif target == 1:
   print("Fibonacci sequence upto",target,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < target:
       num_list.append(n1)
       summ = n1 + n2
       n1 = n2
       n2 = summ
       count += 1
print(num_list)