#!/bin/bash

data_directory="/home/dave/Dropbox/Professional/Tutoring/Satvika/SEC-Edgar/SEC-Edgar-Data"
curr_directory=$(pwd)
output_file="./data.txt"

for i in `find $data_directory` ;
do
	if [ -f "$i" ]
	    then
	    	echo "Parsing: " $i
			python parser.py $i >> data.txt;     	
	    fi
done