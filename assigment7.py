def writedata(file="datad.txt"):
    try:
        with open(file,"a") as f:
            roll_no=input("enter your roll no")
            name=input("enter your name")
            class_name=input("enter your class")
            f.writelines([roll_no+ "\n",name +"\n", class_name +"\n" ])
            with open(filr,"r") as f:
                print (f.read())
    except FileNotFoundError as e:
        print("An error occurred",str(e))
writedata()
