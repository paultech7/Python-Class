# get the amount in USD currency
sourceCurr = float(input("Enter an amount in USD currency: "))

exchangeRate = 0.92
destCurr = sourceCurr * exchangeRate

print("")
print(sourceCurr, "USD = ", destCurr, "EUR")
