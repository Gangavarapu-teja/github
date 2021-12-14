
print("Welcome to the tip caluclator!")
bill=float(input("What was the total bill?"))
tip=input("How much tip would you like to give? 10, 12, or 15?")
totpep=int(input("How many people to split the bill?"))
tippercent=1+int(tip)/100
costperhead= round((bill/totpep)*tippercent,3)
print(f"Each person should pay:{costperhead}")
