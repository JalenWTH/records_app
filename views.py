from django.shortcuts import render
from django.http import HttpResponse
from app_3.models import records
from app_3.models import record_jalen

def homepage(response):
    return render(response, 'app_3/homepage.html', {})

def base(response):
    return render(response, 'app_3/base.html', {})

def record(response, firstname):
    #firstname is a variable containing the name entered into the url by the user
    #the function will check if a record model with that first name is in records
    #records is a list containing all record models

    foundmodel = False

#checks to see if the entered name is in the datbase
    for i in range(len(records)):
        firstname = firstname[0].upper() + firstname[1:] #Makes first letter uppercase
        if firstname == records[i].objects.values_list('first_name', flat=True)[0]:
            modelname = records[i]
            data = modelname.objects.all()

#modelname will be passed to the template so the correct model can be referenced

            foundmodel = True
            break
        else:
            modelname = None
            continue

#the loop will keep iterating until a match is found or there are no more record models to try

    def any(firstname):
        for char in firstname:
            if char.isdigit():
                return True
        return False

    if len(firstname) <= 1 or any(firstname) == True:
        validname = False
        foundmodel = None
        return render(response, 'app_3/homepage.html', {'foundmodel':foundmodel, 'validname':validname})

#Makes sure the name is neither a number nor is less than 2 characters
    else:

        if foundmodel == True:
            validname = True
            return render(response, 'app_3/base2.html', {'modelname':modelname, 'validname':validname, 'data':data})

#the template will be rendered with the information from the correct model if a model with the 
#entered name is found

        if foundmodel == False:
            validname = True
            return render(response, 'app_3/homepage.html', {'foundmodel':foundmodel, 'validname':validname})

#if a model with the entered name is not found, this page will be rendered