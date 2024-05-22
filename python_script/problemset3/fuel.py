def remaining():
    control = True
    while control:
        rem_fuel = inputFuel()
        try:
            per_fuel = 100*rem_fuel
            if per_fuel <= 100 and per_fuel >= 0:
                if per_fuel >= 0 and per_fuel <= 1:
                    return "E"
                elif per_fuel >= 99 and per_fuel <= 100:
                    return "F"
                else:
                    return per_fuel
            else:
                raise ValueError("Invalid Input: Please enter valid values.")
        except ValueError as ve:
            print(ve)
            
            
    
def inputFuel():
    control = True
    while control:
        try:
            fuel = eval(input("Fuel: "))
            return fuel
        except ZeroDivisionError:
            print("Invalid Input: Please avoid Zero in denominator.")
        except NameError:
            print("Invalid Input: Please enter fractional values only (2/4).")

            
def main():
    remaining_fuel = remaining()
    if isinstance(remaining_fuel, str):
        print("Remaining Fuel(%): ", remaining_fuel)
    else:
        print("Remaining Fuel(%): ", round(remaining_fuel),"%")
    
main()




        

    
    
    
