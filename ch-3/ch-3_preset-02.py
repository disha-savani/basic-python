letter=''' Dear <|name|>
You are selected!
<|date|>'''
name=input("Enter your name \n")
date=input("enter date \n")
letter=letter.replace("<|name|>",name)
letter=letter.replace("<|date|>",date)
print(letter)