age= int(input("enter your age : "))
if age > 0 and age<100 :
    age_str = str(age)
    reversed_str=""
    for char in age_str:
        reversed_str=char+reversed_str
        
else:
    reversed_str=""
    print("pleas enter a true number (your age)")
if reversed_str !="":
    print(f"reversed your age :{reversed_str}")