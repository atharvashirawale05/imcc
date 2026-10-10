num=int(input("input number:"))
sum=0
n=num
while(num>0):
    sum=sum*10+(num%10)
    num//=10
if(n==sum):
    print("number is pallindrome")
    
