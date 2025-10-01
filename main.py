#######################################################################################
## PROJECT 1: CALCULATING WIND TURBINE POWER OUTPUT BASED ON POWER CURVE ASSUMPTIONS ##
#######################################################################################

## This file includes the functions and code to solve project 1

## We define a function for the power curve
def power_calc(v, p_rated=15, v_in = 3, v_ratd = 11, v_out = 25, interpol = "linear"):
    """We define a function that calculates power output based on user inputs"""
    
    # We check for errors in user input and raise errors if any
    inputs = {'v': v, 'p_rated': p_rated, 'v_in': v_in, 'v_ratd': v_ratd, 'v_out': v_out}

    for name, value in inputs.items():
        if not isinstance(value, (int, float)): 
            raise ValueError(f"Invalid input: {value} is not a number")  
    
    if not interpol == "linear" or interpol == "cubic":
        raise ValueError(f"Invalid input: {interpol}. Interpolation should be either 'linear' or 'cubic'.")  

    # We define g(v) based on linear or cubic interpolation assumption
    if interpol == "linear":
        g = (v-v_in)/(v_ratd-v_in)
    elif interpol == "cubic":
        g = v**3/v_ratd**3

    # We calculate the power output P(v) based on power curve assumptions
    if v < v_in or v >= v_out:
        p = 0
    elif v_in <= v < v_ratd:
        p = g*p_rated
    elif v_ratd <= v < v_out:
        p = p_rated
        
    return p

#We use the power function to calculate and print the power output
if __name__ == '__main__':
    # We call the power output function to calculate power output based on user defined inputs:
    power = power_calc(10, 15, 4, 12, 25, "linear")

    # We print the calculated power output: 
    print(f"Power Output is: {power:.2f} MW")

