name=input("Enter your Name: ")
marks=input("Enter your Marks: ")
phone=input("Enter your Phone number: ")

template="The name of student is {}, his marks are {} & phone number {}"
output=template.format(name,marks,phone)
print(output)