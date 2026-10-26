#These are the test cases 

#TC 1 Temp 

#C1 tempertaure 
#1 40 
#2 35.01
#3 35 
#4 20 
#5 10 
#6 9.99 
#7 0

#C2 Expected 
#1 High temp alert 
#2 High temp alert 
#3 Temp acceptable 
#4 Temp acceptable 
#5 Temp acceptable 
#6 Low temp alert
#7 Low temp alert 

#C3 Purpose 
#1 Clearly high 
#2 Just above the boundary 
#3 At the boundary because the rule says above 35 
#4 Normal
#5 At the boundary because the rule says below 10 
# Just below the boundary 
#7 Clearly low 

#TC 2 Soil 

#C1 moisture 
#1 10 
#2 29.99 
#3 30 
#4 60 

#C2 Expected 
#1 Plants need water 
#2 Plants need water 
#3 Soial moisute acceptable 
#4 Soial moisture acceptable 

#C3 Purpose 
#1 Clealry dry 
#2 Just below the boundary 
#3 At the boundary because the rule says below 30 
#4 Normal 

#This is the pseudcose for each of the functions 

#Function check_temperature 
#If temp > 35 
#Reutrn "High temp alert"
#Else if temp < 10 
#Return "Low temp altert"
#Else 
#Return "Soil moisture acceptable"

#Function check_soil 
#If mositure < 30 
#Return "Plants need water"
#Else 
#Return "Soil mositure acceptable"

#Main 
#Ask use for temp and moisture 
#Set temp_result = check_temp 
#Set soild_result = check_soil
#Display both results 

#The Smart Greenhouse Monitoring System 

# Temp part 
from subprocess import check_call


def check_temperature(temperature):
    """Return a status message for the greenhouse temperature (Celsius)."""
    if temperature > 35:
        status = "High temperature alert"
    elif temperature < 10:
        status = "Low temperature alert"
    else:
        status = "Temperature acceptable"
    return status

#Soil Part
def check_soil(moisture):
    """Return a status message for soil moisture (percentage)."""
    if moisture < 30:
        status = "Plants need water"
    else:
        status = "Soil moisture acceptable"
    return status

#Main Part
temperature = float(input("Enter greenhouse temperature (Celsius): "))
moisture = float(input("Enter soil moisture (%): "))

temp_result = check_temperature(temperature)
soil_result = check_soil(moisture)

print(temp_result)
print(soil_result)