number= input("enter number : ")
if len(number) ==2 and number.isdigit():
    number1=int(number[0])
    number2=int(number[1])
    result1=number1**number2
    result2=number2**number1
    print(f"first digit to the power of second digit : {result1}")
    print(f"secend digit to the power of first digit : {result2}")
else :
    print("pleas enter a true number (2 digit)")