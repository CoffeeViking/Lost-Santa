bin = input("Hello, please offer me a binary number to convert!")
dec = 0
tempBin = list(str(bin))
l = len(tempBin) - 1

# For Zero
if tempBin == ['0']:
    print("Not Zero! You know what that is, silly you.")
    quit()

#Check for non 0 or 1, length
for x in tempBin:
    if x != '1' and x != '0':
        print("Sorry mate, 1s and 0s only baby")
        print("Bai!")
        quit()
    if len(tempBin) > 8:
        print("Sorry, limited to 8 digits!")
        quit()
#Calculate decimal from binary
for x in tempBin:
    if x == '1':
        formula = 2 ** l
        l = l - 1
        dec = dec + formula
    else:
        l = l - 1

print("Your number in decimal form is " + str(dec) + "!")
