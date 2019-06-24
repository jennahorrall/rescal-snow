# python3 txt_to_par.py ALTI0000.txt
# creates a .par file based on HLD in .data file
# uses INPUT_ELEVATION template in genesis.c to set up cell space
import sys

txt_filename = sys.argv[1]
#print(txt_filename)

txt_file = open(txt_filename, "r")
txt_text = txt_file.read()
# print(txt_text)
txt_file.close()

numbers = [int(number) for number in txt_text.split()]
# print(numbers)
lines = [line.split() for line in txt_text.split("\n") if line.split()]
#print(lines)

Length = len(lines[0])#i
Depth = len(lines) #k
Height = 50 * round(max(numbers)/50) #j

par_filename = txt_filename.split(".")[0] + ".par"
par_file = open(par_filename, "w")

par_file.write("## PARAMETER FILE \n")
par_file.write("## INPUT_ELEVATION TEMPLATE: .txt file to .par file \n")
par_file.write("\n")
par_file.write("Model = SNO\n")
par_file.write("\n")
par_file.write("#Bin_file = TE_50_200_200.bin\n")
par_file.write("#Bin_file = DUN_{}_{}_{}.bin\n".format(Length, Depth, Height))
par_file.write("Csp_file = DUN_{}_{}_{}.csp\n".format(Length, Depth, Height))
par_file.write("#Hpp_file = HPP.bin\n")
par_file.write("H = %d\n" % Height)
par_file.write("L = %d\n" % Length)
par_file.write("D = %d\n" % Depth)
par_file.write("\n")
par_file.write("## CSP template (genesis)\n")
par_file.write("Csp_template = INPUT_ELEVATION(%s)" % txt_filename)
par_file.write("\n")
par_file.write("## Boundary conditions\n")
par_file.write("Boundary = PERIODIC\n")
par_file.write("\n") 

par_file.write("## Initial time\n")
par_file.write("Time = 0.0\n")
par_file.write("\n") 
par_file.write("## Physical parameters file\n")
par_file.write("Phys_prop_file = real_data/desert_earth.prop\n")
par_file.write("\n")

par_file.write("## Qsat data file\n")
par_file.write("Qsat_file = real_data/PDF.data\n")
par_file.write("\n")

par_file.write("## Erosion rate\n")
par_file.write("Lambda_e = 4\n")
par_file.write("\n")


par_file.write("## Erosion ratio for cohesive snow\n")
par_file.write("Lambda_F = 400\n")
par_file.write("\n")

par_file.write("## Sintering rate - PARAMETER TO VARY\n")
par_file.write("Lambda_S = 0.02\n")
par_file.write("\n")

par_file.write("## Deposition rate\n")
par_file.write("Lambda_C = 2\n")
par_file.write("\n")

par_file.write("## Transport rate\n")
par_file.write("Lambda_T = 30\n")
par_file.write("\n")

par_file.write("## Coefficient for the vertical transport of mobile grains\n")
par_file.write("Coef_A = 1.6\n")
par_file.write("\n")

par_file.write("## Coefficient for the deposition against an obstacle\n")
par_file.write("Coef_B = 1\n")
par_file.write("\n")

par_file.write("# Coefficient for the deposition behind an obstacle\n")
par_file.write("Coef_C = 3\n")
par_file.write("\n")

par_file.write("## Probability of the transition links\n")
par_file.write("Prob_link_ET = 0.5\n")
par_file.write("Prob_link_TT = 1.0\n")
par_file.write("\n")

par_file.write("## Higher mobility of grains\n")
par_file.write("High_mobility = 1\n")
par_file.write("\n")

par_file.write("## Diffusion rate\n")
par_file.write("Lambda_D = 0.06\n")
par_file.write("\n")

par_file.write("## Injection rate\n")
par_file.write("Lambda_I = 1\n")
par_file.write("\n")

par_file.write("## Gravity\n")
par_file.write("Lambda_G = 1000 #1000\n")
par_file.write("\n")

par_file.write("## Mode of avalanches\n")
par_file.write("Ava_mode = TRANS\n")
par_file.write("\n")

par_file.write("## Avalanches rate in TRANS mode\n")
par_file.write("Lambda_A = 1\n")
par_file.write("\n")

par_file.write("## Delay between avalanches\n")
par_file.write("#Ava_delay = 10.0\n")
par_file.write("\n")

par_file.write("## Duration of avalanches\n")
par_file.write("#Ava_duration = 1.0\n")
par_file.write("\n")

par_file.write("## Angle of avalanches (degrees)\n")
par_file.write("Ava_angle = 35.0 #35.0\n")
par_file.write("\n")

par_file.write("## Height limit in avalanches (cells)\n")
par_file.write("Ava_h_lim = 1\n")
par_file.write("\n")

par_file.write("## Global flow forcing coefficient\n")
par_file.write("#Lgca_gfor = 0.002\n")
par_file.write("\n")

par_file.write("## Delay between flow cycles\n")
par_file.write("Lgca_delay = 1.0\n")
par_file.write("\n")

par_file.write("## Initial number of flow cycles without transitions\n")
par_file.write("Init_ncycl = 150\n")
par_file.write("\n")

par_file.write("## Speedup of the stabilization of the flow\n")
par_file.write("Lgca_speedup = 1000\n")
par_file.write("\n")

par_file.write("## Min shear stress value\n")
par_file.write("Tau_min = 0\n")
par_file.write("\n")

par_file.write("## Max shear stress value\n")
par_file.write("Tau_max = 1000\n")
par_file.write("\n")

par_file.write("## Automatic centering\n")
par_file.write("Centering_delay = 200\n")

print("%s file created successfully!" % par_filename)

par_file.close()
