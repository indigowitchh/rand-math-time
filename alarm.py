def alarm (hour, minu):
    if minu < 40:
        hour -=1
        if hour < 0:
            hour = 23
    minu -=40
    if minu < 0:
        minu +=60
    print ("Mirko needs to set an alarm at ", hour, ":", minu)



input1= int(input("What hour does Mirko need to get out of bed?"))
input2= int(input("What minute does Mirko need to get out of bed?"))

alarm (input1, input2)
