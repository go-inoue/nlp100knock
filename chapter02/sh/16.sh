#!/bin/bash
/bin/echo -n "Input N: "
read N
split -l $N hightemp.txt 16_
