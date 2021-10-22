# Read the Inputs
balance = float(input("Account Balance ($): "))
risk_percentage = int(input("Risk Percentage (%): "))
stop_loss = float(input("Stop-Loss (pips): "))
pip_value = float(input("Pip Value: "))

# Calculation and Formula
needed_lots_0 = ( balance * risk_percentage) / (stop_loss * pip_value * 100 )

# Rounding to 2 Decimals
needed_lots = round( needed_lots_0 , 2) 

# Display the result
print("Your ideal position size is: ", needed_lots, "Lot(s)")