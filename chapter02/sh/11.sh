#!/bin/bash
sed -e "s/    / /g" hightemp.txt > tab2space_sed_hightemp.txt
cat hightemp.txt | tr "\t" " " > tab2space_tr_hightemp.txt
expand -t 1 hightemp.txt > tab2space_expand_hightemp.txt
