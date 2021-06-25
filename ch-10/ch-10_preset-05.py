class Train():
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def getStatus(self):
        print("***********")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
        print("***********")

    def fareInfo(self):
        print(f"The price of the ticket is:{self.fare}Rs.")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! your seats number is {self.seats}")
            self.seats=self.seats-1
            print(f"Total seats are avaible {self.seats}")

        else:
            print("Sorry this train is full! kindly try in next time")

        

    def cancleTicket(self,seatno):
        if(seatno<10):
            print(f"Your ticket is succesfully canceled!")
            self.seats+=1
            print(f"Total seats are avaible {self.seats}")

        else:
            print("Sorry your seats are not canceled")
            
            


intercity=Train("Tntercity Express : 1405",90,10)
intercity.getStatus()
intercity.fareInfo()
intercity.bookTicket()
#intercity.bookTicket()
intercity.cancleTicket(5)

