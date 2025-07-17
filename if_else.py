# 1. EVEN and odd number find
num = int(input("enter your number"))
if num%2 == 0:
    print("this is even number")
else:
    print("this is odd number")
   

#2. positive and negative number find
num = int(input("enter your neg and postive and zero"))
if num >0:
    print("this is postive number")
elif num == 0:
    print("this is zero equal")
else:
    print("this is negative number")


#3. able for vote and not able for vote
age = int(input("enter your age"))
if age<18:
    print("you are not able for vote")
else:
    print("you are able for vote") 
 

#4.  number is between 1 to 100
rang = int(input("enter your number"))
if rang >=100:
    print("you are in not range")
else:
    print("you are  in range")


#5. year is leap and not
year = int(input("enter year"))
if year%4 == 0:
    print("this is leap year")
else:
    print("this is not leap year")


#6. give the grade according to number
let = int(input("enter your number between 0 to 100"))
if let>=80:
    print("A + grade")
elif let>=60:
    print("B + grade")
elif let>=48:
    print("C +grade")
else:
    print("fail and e grade")
          


#7. password check 
pas  = int(input("enter your pass"))
val = 56
if pas == val:
    print("access grantrd")
else:
    print("not access")


#8. even and odd and also divilble
num  = int(input("enter your number"))
if num%2 ==0 and num%5==0:
  print("this is evene and divsilble")

else:
    print("this is odd number")
   

#9. find the triangle yes and not
a = int(input("enter value of triangle"))
b = int(input("enter value of triangle"))
c= int(input("enter value of triangle"))
if a==b and b==c and c==a:
    print("this is triangle")
else:
    print("this is not triangle")

#10.    check where you go according your age
age = int(input("enter your age"))
b = int(input("enter your salary"))
c = input("enter your sex")
m = "male"
f ="female"
if age<25 and b>30000 and c==m:
    print("you will go to thilend")
elif age<25 and b>30000 and c==f:
    print("you will go to bali")
elif age>26 and age<40:
    print("you will not go anyvery")
else:
    print("you will go to jk")


#11 . check string len
x =input("enter your city name")
y  =input("entr your home city name")
x1 = len(x)
y1=len(y)
if x1>y1:
    print("you will get promotion")
elif x1==y1:
    print("its depands to us")
else:
    print("you will not promotion")


#12.     how many discount you got

x = int(input("enter your first order rate"))
y = int(input("enter your second order rate"))
b = int(input("enter your third rate"))
a = int(input("enter your rate"))
su  = a+b+x+y
print(su)
if su<50000:
    print("you got no discount")
elif su<75000:
    print("you got 10% discount")
elif su<100000:
    print("you got 20% discount")
else:
    print("you got 30% discount")
