i = int(input("Enter the number: "))
even=1
odd=0
a=lambda i: 1 if i%2==0 else 0
if a(i)==1:
    print('Number is even')
else:
    print("it is odd")