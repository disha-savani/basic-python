class Programmer:
    company="Microsoft"

    def __init__(self,name,product):
        self.name=name
        self.product=product

    def getInfo(self):
        print(f"The programmer Name is {self.name} and the product is {self.product}")

disha=Programmer("Disha","Skype")
ravi=Programmer("Ravi","GitHub")
disha.getInfo()
ravi.getInfo()
