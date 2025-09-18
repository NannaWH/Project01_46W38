#######################################################################################
## PROJECT 1: CALCULATING WIND TURBINE POWER OUTPUT BASED ON POWER CURVE ASSUMPTIONS ##
#######################################################################################

## This file includes the main code to solve project 1

# We ask the user to define input for the power output calculation
v_user = input("Input wind speed in m/s:")
p_rated_user = input("Input rated power in Mw:")
v_in_user = input("Input cut-in wind speed in m/s:")
v_ratd_user = input("Input rated wind speed in m/s:")
v_out_user = input("Input cut-out wind speed in m/s:")
interpol_user = input("Input interpolation option (linear or cubic):")

# We define the variables based on the user input. If no user input we use the default value
v = v_user or 10 # m/s
p_rated = p_rated_user or 15 # MW
v_in = v_in_user or 3 # m/s
v_ratd = v_ratd_user or 11 # m/s
v_out = v_out_user or 25 # m/s
interpol = interpol_user or "linear" # linear or cubic

# We define g(v)
if interpol == "linear":
    g = (v-v_in)/(v_ratd-v_in)
else:
    g = v^3/v_ratd^3

# We calculate the power output P(v)
if v < v_in or v >= v_out:
    p = 0
elif v_in <= v < v_ratd:
    p = g*p_rated
else: 
    p = p_rated

# We print the calculated power output: 
print("Power Output is:", p)