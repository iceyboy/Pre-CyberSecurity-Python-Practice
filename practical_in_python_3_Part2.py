print("1. Austria\n2. Singapore\n3. UK")
country = int(input("Select your country ..."))

if country >= 1 and country <= 3:
    age = int(input("Please enter your age : "))


Austria = 16
Singapore = 21
UnitedKingdom = 18

countryName = ""

if age >= 1 or age <= 120:
    
    if country == 1:
        votingAge = Austria
        countryName = "Austria"
    elif country == 2:
        votingAge = Singapore
        countryName = "Singapore"
    elif country == 3:
        votingAge = UnitedKingdom
        countryName = "United Kingdom"
    else:
        print("This should not be possible! Error detected in the country - should be 1, 2 or 3. You selected: " + str(country)) 

    if age >= votingAge:
        print("You are old enough to vote in " + countryName)
    else:
        print("You are not old enough to vote in " + countryName + ". You can vote in " + str((votingAge - age)) + " year(s)")
        
    