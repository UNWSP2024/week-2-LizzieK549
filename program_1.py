'''Program #1: Personal Information Write a program that displays the following information.
Your name Your address with city, state and ZIP Your telephone number Your college major'''
def personal_information():
    name=("Elizabeth Kerr")
    city= ("Inver Grove Heights")
    state=("Minnesota")
    zip_code= 55077
    phoneNumber=("612-963-8605")
    major=("Physics")
    print('Hello, my name is', name+". I am from", city, zip_code, "in", state + ".")
    print("My phone number is", phoneNumber + ". In college I want to study", major + "!")


# Line which calls the above function.
personal_information()