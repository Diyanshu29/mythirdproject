print("Sum of Digit...")
no=int(input("Enter Any Number"))
sum=0
rem=0
rev=0

while no>0:
	rem=no%10
	sum+=rem
	rev=rev*10+rem
	no//=10
print("Sum of Given Number is:",sum)
print("The Reverse Number is:",rev)
