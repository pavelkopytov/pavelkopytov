age = int(input())
if age < 0:
    print("Error, age cannot be negative")
else:
    if  age < 2:
        print ("baby")
    elif age < 4:
        print ("kid")
    elif age < 13:
        print ("child")
    elif age < 20:
        print ("teenager")
    elif age < 65:
        print ("adult")
    else:
        print ("elderly")
