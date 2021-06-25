def replace_and_split(string, word):
    newStr=string.replace(word,"")
    return newStr.strip()

this="    Harry is a good    "
n=replace_and_split(this,"is")
print(n)