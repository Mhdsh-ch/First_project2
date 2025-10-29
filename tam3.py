age= int(input("enter your age : "))
secend = 31536000
minutes = 525600
hours = 8760
if age > 0 and age < 100 :
    secend=secend*age
    print(f"your age secend :{secend}")
    minutes=minutes*age
    print(f"your age minutes :{minutes}")
    hours=hours*age
    print(f"your age hours :{hours}")
else:
    print("pleas enter a true number (your age)")