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
