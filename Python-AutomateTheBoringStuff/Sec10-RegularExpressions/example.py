def isPhoneNumber(text): #415-555-5555
    if len(text) !=12:
        return False #not phone number sized
    for i in range(0,3):
        if not text(i).isdecimal():
            return False #no area code
        if text(3)!= '-':
            return False #missing dash
        for i in range(4,7):
            if not text(i).isdecimal():
                return Flase #no first 3 digits
        if text(7) != '-':
            return False #missing second dash
        for in in range(8,12):
            if not text(i).isdecimal():
                return Fals 
            