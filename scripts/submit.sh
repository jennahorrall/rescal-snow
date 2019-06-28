#!/bin/bash

# Set up this run in the correct directory
#Configured for LL CPU not RC

# go into test directory
output_root="../snow_data"
echo ${output_root}

output_dirs=(${output_root}/*)

# "loop" through each subdirectory and start run in each
output_dir="${output_dirs[${PMI_RANK}]}"
cd ${output_dir}
echo "Process ${PMI_RANK} in  ${output_dir}"

# Need to be able to read and execute this directory
chmod u+rwx *

./run.run
