# python3 txt_to_par.py ALTI0000.txt
# creates a .par file based on HLD in .data file
# uses INPUT_ELEVATION template in genesis.c to set up cell space
import sys
import math

def with_data(data_filename):
    return with_data_and_LHD(data_filename)
    
def with_data_and_par(data_filename, par_filename):
    return with_data_par_and_LHD(data_filename, par_filename)

def with_data_and_height(data_filename, H):
    return with_data_and_LHD(data_filename, Height=H)

def with_data_and_LHD(data_filename, Length=None, Height=None, Depth=None): 
    data_file = open(data_filename, "r")
    data_text = data_file.read()
    data_file.close()

    numbers = [int(number) for number in data_text.split()]
    lines = [line.split() for line in data_text.split("\n") if line.split()]

    if Length == None: 
        Length = len(lines[0]) #i
    elif Length != len(lines[0]): 
        print("Error: Length of .data file does not match given length argument. \n")
        return None
    
    if Height == None: 
        # Height = max(numbers)
        Height = 50 * math.ceil(max(numbers)/50) #j
    elif Height < max(numbers): 
        print("Warning: given height argument is less than the tallest height (j) point. \n")
        
    if Depth == None: 
        Depth = len(lines) #k
    elif Depth != len(lines): 
        print("Error: Depth of .data file does not match given depth argument. \n")
        return None

    par_filename = data_filename.split(".")[0] + ".par"
    par_file = open(par_filename, "w")

    par_file.write(
"""
## PARAMETER FILE
## INPUT_ELEVATION TEMPLATE: .data file to .par file
Model = SNO

"""
    )
    par_file.write("Bin_file = DUN_{}_{}_{}.bin\n".format(Length, Depth, Height))
    par_file.write("Csp_file = DUN_{}_{}_{}.csp\n".format(Length, Depth, Height))
    par_file.write("\n")
    par_file.write("H = %d\n" % Height)
    par_file.write("L = %d\n" % Length)
    par_file.write("D = %d\n" % Depth)
    par_file.write("\n")
    par_file.write("## CSP template (genesis)\n")
    injection = 1
    par_file.write("Csp_template = INPUT_ELEVATION(%s, %d)\n" % (data_filename, injection))
    par_file.write(
"""
## Boundary conditions
#Boundary = REINJECTION
Boundary = OPEN 

## Initial time
Time = 0.0

## Physical parameters file
Phys_prop_file = real_data/desert_earth.prop

## Qsat data file
Qsat_file = real_data/PDF.data

## Erosion rate
Lambda_E = 4

## Deposition rate
Lambda_C = 2

## Transport rate
#Lambda_T = 6
Lambda_T = 30

## Coefficient for the vertical transport of mobile grains
#Coef_A = 0
Coef_A = 0.2
#Coef_A = 1

## Coefficient for the deposition against an obstacle
#Coef_B = 10
#Coef_B = 2
Coef_B = 1

# Coefficient for the deposition behind an obstacle
Coef_C = 3

## Probability of the transition links
Prob_link_ET = 0.5
Prob_link_TT = 1.0

## Higher mobility of grains
High_mobility = 1

## Diffusion rate
#Lambda_D = 0.02
Lambda_D = 0.06

## Injection rate
#Lambda_I = 0.1
Lambda_I = 1

## Gravity
Lambda_G = 1000 #1000

## Mode of avalanches
Ava_mode = TRANS

## Avalanches rate in TRANS mode
Lambda_A = 1

## Delay between avalanches
Ava_delay = 10.0

## Duration of avalanches
Ava_duration = 1.0

## Angle of avalanches (degrees)
Ava_angle = 35.0 #35.0

## Height limit in avalanches (cells)
Ava_h_lim = 1

## Global flow forcing coefficient
Lgca_gfor = 0.002

## Delay between flow cycles
Lgca_delay = 1.0

## Initial number of flow cycles without transitions
Init_ncycl = 150

## Speedup of the stabilization of the flow
Lgca_speedup = 1000

## Min shear stress value
Tau_min = 0

## Max shear stress value
Tau_max = 1000

## Automatic centering
Centering_delay = 200
"""
    )
    par_file.close()
    print("%s file created successfully! \n" % par_filename)
    return None

def with_data_par_and_LHD(data_filename, par_filename, Length=None, Height=None, Depth=None): 
    # read in data text
    data_file = open(data_filename, "r")
    data_text = data_file.read()
    data_file.close()

    # from data text, determine Length, Height, and Depth
    numbers = [int(number) for number in data_text.split()]
    lines = [line.split() for line in data_text.split("\n") if line.split()]
    data_Length = len(lines[0])
    data_Height = max(numbers)
    data_Depth = len(lines)
    
    # read in parameter file
    par_file = open(par_filename, "r")
    par_text = par_file.read()
    par_file.close()
    
    # parse parameter file to determine given Length, Height, and Depth
    parameters = {}
    par_lines = [line for line in par_text.split("\n")]
    for line in par_lines: 
        if "=" in line and len(line.split()) == 3 and "#" not in line.split()[0]: 
            parameters[line.split()[0]] = line.split()[2]
    par_Length = int(parameters.get("L", None))
    par_Height = int(parameters.get("H", None))
    par_Depth = int(parameters.get("D", None))
    
    if Length == None and par_Length != data_Length: 
        print("Error: par length does not match length of data file. \n")
        return None
    elif Length != None and (par_Length != data_Length or par_Length != Length): 
        print("Error: given length argument does not match either par length or data length. \n")
        return None
    
    if par_Height < data_Height: 
        print("Warning: par height is less than the tallest height (j) point in data. \n")
    elif Height != None and par_Height != Height: 
        print("Error: par height does not match given argument height. \n")
        return None
    
    if Depth == None and par_Depth != data_Depth: 
        print("Error: par depth does not match depth of data file. \n")
        return None
    elif Depth != None and (par_Depth != data_Depth or par_Depth != Depth): 
        print("Error: given depth argument does not match either par depth or data length. \n")
        return None
    
    print("Data, Par, and LHD all succesfully validated! \n")        
    return None

def usage():
    print("--- TEXT TO PAR ---\n")
    print("OPTIONS:\n")
    print("<data file>\n")
    print("<data file> <parameter file>\n")
    print("<data file> <H>\n")
    print("<data file> <H> <L> <D>\n")
    print("<data file> <parameter file> <H> <L> <D>\n")

def main(): 
    if len(sys.argv) - 1 == 1: 
        with_data(sys.argv[1])
    elif len(sys.argv) - 1 == 2:
        if sys.argv[2].endswith(".par"): 
            with_data_and_par(sys.argv[1], sys.argv[2])
        elif sys.argv[2].isdigit(): 
            with_data_and_height(sys.argv[1], int(sys.argv[2]))
        else: 
            usage()
    elif len(sys.argv) - 1 == 4: 
        with_data_and_LHD(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    elif len(sys.argv) - 1 == 5: 
        with_data_par_and_LHD(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
    else:
        usage()

main()
