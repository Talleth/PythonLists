#===================================================================
#    Purpose:   Demonstrate basic Python programming in 
#               for Lists and Functions
#===================================================================

# Function to to display temperatures
def DisplayTemperatures(HourlyTemperatures, AverageTemp):
    lowTemp = 0
    highTemp = 0

    # Get low temperature
    for value in HourlyTemperatures:
        if (lowTemp == 0) or (lowTemp > value):
            lowTemp = value

    # Get high temperature
    for value in HourlyTemperatures:
        if (highTemp == 0) or (highTemp < value):
            highTemp = value

    # Print all values =================

    print("")
    print("Hour\t\tTemperature")
    print("")

    for index in range(0, len(HourlyTemperatures)):
        print(str((index + 1)).rjust(2, "0"), ": 00\t\t", HourlyTemperatures[index])

    print("")
    print("High Temperature: \t", highTemp)
    print("Low Temperature: \t", lowTemp)
    print("Average Temperature: \t", AverageTemp) 
    print("") 

# Function to calculate average temperature
def ComputeAverageTemp(HourlyTemperatures):
    totalValue = 0

    for value in HourlyTemperatures:
        totalValue += value

    return round((totalValue / len(HourlyTemperatures)), 1)    

# Function to get temperatures from user
def GetTemperatures(HourlyTemperatures):

    print("")
    for index in range(0, 24):
        currentInput = int(input("Please enter value for slot " + str((index + 1)) + ": "))

        # Repeat call until we get the correct value
        while (currentInput < 50) or (currentInput > 130):
            currentInput = int(input("Please make sure the value is between 50 and 130 " + str((index + 1)) + ": "))

        HourlyTemperatures.append(currentInput)

# Main function
def main():
    HourlyTemperatures = []

    GetTemperatures(HourlyTemperatures)
    AverageTemp = ComputeAverageTemp(HourlyTemperatures)
    DisplayTemperatures(HourlyTemperatures, AverageTemp)    

main()