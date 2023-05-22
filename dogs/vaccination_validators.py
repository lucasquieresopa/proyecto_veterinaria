from datetime import date, datetime

def dosis_validator(actual, total):
    if actual>total:
        return False
    return True


def dog_age(dog_dob):
    return (datetime.now() - dog_dob).days/365


def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month


def age_validator(vaccine_dop, dog, vaccine_type):

    if vaccine_type=="Antirrabica":
        if diff_month(vaccine_dop, dog.date_of_birth) > 4:
            return False
    if vaccine_type=="Antimoquillo":
        if diff_month(vaccine_dop, dog.date_of_birth) > 2:
            return False
    return True


