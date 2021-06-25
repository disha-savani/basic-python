post="abc def ghi jkl mno pqr stu vwx yz"
    
post1=input("Enter the text \n")


if post1.lower() or post1.upper():
   spam=True

else :
    spam=False

if(spam):
    print("this text in post")
else:
    print("this text is not in post")
