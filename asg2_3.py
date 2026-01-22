print("Hello, my lovely teacher ")

def vvv(sex,hemo):
    if sex == "Males":
        if hemo >=134 and hemo<= 167:
            print("So great")
    elif sex == "Females":
        if hemo >=117 and hemo<= 155:
            print("So great")
    elif sex == "Males" or sex == "Females":
        print("need to pay more attention to our health.")

sex=input("Are you Males/ Females: ")
hemo= float(input("the user's biological sex and hemoglobin value (g/l): " ))
vvv(sex,hemo)