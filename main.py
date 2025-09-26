#######################################################################################
## PROJECT 1: CALCULATING WIND TURBINE POWER OUTPUT BASED ON POWER CURVE ASSUMPTIONS ##
#######################################################################################

## This file includes the functions and code to solve project 1

## We define the power function
def power_calc(v, p_rated=15, v_in = 3, v_ratd = 11, v_out = 25, interpol = "linear"):
    """We define a function that calculates power output based on user inputs"""
    
    # We define g(v)
    if interpol == "linear":
        g = (v-v_in)/(v_ratd-v_in)
    elif interpol == "cubic":
        g = v**3/v_ratd**3

    # We calculate the power output P(v)
    if v < v_in or v >= v_out:
        p = 0
    elif v_in <= v < v_ratd:
        p = g*p_rated
    else: 
        p = p_rated
        
    return p

if __name__ == '__main__':
    # Write the main script to use the function here:
    power = power_calc(10, 15, 3, 11, 25, "linear")

    # We print the calculated power output: 
    print(f"Power Output is: {power:.2f} MW")

