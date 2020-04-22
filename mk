#!/bin/bash

filename=invitation
if [[ $# -gt 0 ]]; then
   filename="$1"
fi
xelatex $filename  
xelatex $filename 
rm -f  $filename.aux *.log $filename.bbl $filename.blg $filename.dvi $filename.ps  $filename.nav  $filename.out  $filename.snm  $filename.toc $filename.lof $filename.tdo $filename.pbsdat $filename.run.xml $filename.bcf
rm -f *.*~ .*.un~ *~ *.aux
