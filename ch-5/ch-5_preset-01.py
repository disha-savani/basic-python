mydict={
    "Pankha":"Fan",
    "Dabba":"Box",
    "Vastu":"Item"
}
print("options are ",mydict.keys())
a=input("Enter the hindi word \n")
#print("The Meaning of your word is : ",mydict[a])
print("The meaning of your word is : ",mydict.get(a))