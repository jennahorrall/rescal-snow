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
Height = max(numbers) #j

par_filename = txt_filename.split(".")[0] + ".par"
par_file = open(par_filename, "w")

par_file.write("## PARAMETER FILE \n")
par_file.write("## INPUT_ELEVATION TEMPLATE: .txt file to .par file \n")
par_file.write("\n")
par_file.write("Model = SNO\n")
par_file.write("\n")
par_file.write("#Bin_file = TE_50_200_200.bin\n")
par_file.write("Bin_file = DUN_{}_{}_{}.bin\n".format(Length, Depth, Height))
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


print("%s file created successfully!" % par_filename)

par_file.close()
