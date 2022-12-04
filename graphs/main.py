import os 
print("Welcome from the MatGraphPy Community!")
disp= input("do you want to see all graphs? (y/n)")

if disp == "y":
    files = os.listdir("./graphs")
    for file in files:
        if not file == "main.py":
            os.system(f"python ./graphs/{file}")