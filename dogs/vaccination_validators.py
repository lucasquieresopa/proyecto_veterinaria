from datetime import date, datetime

def dosis_validator(actual, total):
    if actual>total:
        return False
    return True

def dog_age(dog_dob):
    return (datetime.now() - dog_dob).days/365



def age_validator(vaccine_dop, dog_dob, vaccine_type):

    if vaccine_type=="Antirrabica":
        if ((vaccine_dop - dog_dob).days/12) > 4:
            return True
    if vaccine_type=="Antimoquillo":
        if ((vaccine_dop - dog_dob).days/12) > 2:
            return True
    return False