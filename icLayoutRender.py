#!/bin/tcsh -f
# IC-layout Rendering tool
# Authors: João R. R. O. Martins & Pietro M. Ferreira
# Affiliation: 
#	Université Paris-Saclay, CentraleSupélec, CNRS, Lab. de Génie Électrique et Électronique de Paris,91192,Gif-sur-Yvette,France
#	Sorbonne Université, CNRS, Lab. de Génie Électrique et Électronique de Paris, 75252, Paris, France
# IC-Layout Render: Image rendering using LuaTEX compiler

import gdspy
import pandas as pd
import math
from gds2pdf import gds2pdf
from GDSLatexConverter import GDSLatexConverter
import os
import sys, getopt

def main(argv):
   cellName = ''
   layerColors = ''
   pdfTex=False
   

   try:
      opts, args = getopt.getopt(argv,"hXg:m:",["cellNameFile=","layerColorsFile="])
   except getopt.GetoptError:
      print("Help: icLayoutRender.py -h\n")
      sys.exit(1)
   for opt, arg in opts:
      if opt == '-h':
         print("Usage: icLayoutRender.py -g <cellNameFile> -m <layerColorsFile>\n")
         print("For pdfTex compiler do: icLayoutRender.py -X -g <cellNameFile> -m <layerColorsFile>\n")
         sys.exit()
      if opt == '-X':
         pdfTex = True
      elif opt in ("-g", "--gds"):
         cellName = arg
      elif opt in ("-m", "--map"):
         layerColors = arg
      #elif opt in ("-o", "--opacity"):
      #   opacity = arg
      else:
         assert False, "unhandled option"
   return (pdfTex,cellName,layerColors)

if __name__ == "__main__":
   pdfTex, cellName, layerColors =main(sys.argv[1:])


#files = os.listdir()   
if bool(cellName)==False:   
    print("Please enter the cell name:")
    cellName = input()

if os.path.isfile(cellName)==False:
    print("The file %s does not exist.\n Please check the filename and restart icLayoutRender\n"% cellName)
    sys.exit(2)
    
if bool(layerColors)==False:
    print("Please enter the layer colors:")
    layerColors = input()
print(layerColors)
if os.path.isfile(layerColors)==False:
    print(f"The file %s does not exist.\n Please check the filename and restart icLayoutRender\n"% layerColors)
    sys.exit(2)

pdfName = cellName.replace(".gds","")
print("Converting %s to %s.pdf with %s layer colors\n"% (cellName,pdfName,layerColors))
print("Do you want to continue ? [yes|no]:")
response = input()
if response != "yes":
   sys.exit(3)
    
gds2pdf(cellName,pdfName,layerColors, pdfTex)
