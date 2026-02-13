def validate_atm_pin_code(pin):
    length=len(pin)
    if(length==4 or length==6):
        for i in range(length):
            if(pin[i].isdigit()):
                result="Valid PIN Code"
            else:
                result="Invalid PIN Code"
                break
    else:
        result="Invalid PIN Code"
    print(result)


pin = input()
# Call the validate_atm_pin_code function
validate_atm_pin_code(pin)
