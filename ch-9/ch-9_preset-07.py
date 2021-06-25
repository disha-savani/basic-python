content=True
i=1
with open("log_file.txt") as f:
    while content:
        content=f.readline()
        if "python" in content.lower():
            print(content)
            print(f"yes python is present in line number of {i}")
        i+=1