import sys

type = sys.argv[1]

if type == "t2.micro":
    print("ok! it will be create a instance for u")
elif type =="t5.xlarge":
    print("ok! it will be charge you 4 $")   
elif type == "t3.medium":
    print("ok! it will be charge u 8 $")     
else:
    print("it will not create instance for u")    