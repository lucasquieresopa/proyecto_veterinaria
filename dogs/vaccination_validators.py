from datetime import date, datetime

from accounts import forms

def dosis_validator(actual, total):
    if actual>total:
        return False
    return True


def dog_age(dog_dob):
    return (datetime.now() - dog_dob).days/365


def diff_month(d1, d2):
    months = (d1.year - d2.year) * 12 + d1.month - d2.month
    #print(months)
    return months


def age_validator(vaccine_dop, dog, vaccine_type):
    #print(vaccine_type)
    if vaccine_type=="Antirrabica":
        if diff_month(vaccine_dop, dog.date_of_birth) < 4:
            raise forms.ValidationError('No se pudo registrar la vacuna: el perro debe tener más de 4 meses para recibir una antirrabica')
    if vaccine_type=="Antimoquillo":
        if diff_month(vaccine_dop, dog.date_of_birth) < 2:
            raise forms.ValidationError('No se pudo registrar la vacuna: el perro debe tener más de 2 meses para recibir una antimoquillo')
    return True


