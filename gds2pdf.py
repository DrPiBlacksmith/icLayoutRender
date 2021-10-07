#!/usr/bin/python3
# gds2pdf Rendering tool
# Authors: João R. R. O. Martins & Pietro M. Ferreira
# Affiliation: 
#	Université Paris-Saclay, CentraleSupélec, CNRS, Lab. de Génie Électrique et Électronique de Paris,91192,Gif-sur-Yvette,France
#	Sorbonne Université, CNRS, Lab. de Génie Électrique et Électronique de Paris, 75252, Paris, France
# Primary version using LuaTEX compiler

import gdspy
import pandas as pd
import math
from GDSLatexConverter import GDSLatexConverter
import os

def gds2pdf(cellName,pdfName,layerColors, pdfTex=False, opacity=0.2):

    gdsii = gdspy.GdsLibrary()
    lib = gdsii.read_gds(infile=cellName)#gds file open

    Colors = pd.read_map(layerColors,sep='!',dtype={'GDSNumber':int,'Layer':str,'Color':str})#map file open
    #GDS layer numbers and names are mapped to the colors
    Colors.set_index('GDSNumber',inplace = True)
    Colors.drop(columns=['Layer'],inplace = True)
    #Create converter
    conv = GDSLatexConverter(lib)

    # Display all available layers:
    containedLayers = conv.all_layer
    containedColors = Colors.reindex(index=containedLayers)
    colorscheme = containedColors.to_dict()['Color']
    drawopt = colorscheme.copy()
    for key in drawopt:
        c = drawopt[key]
        if str(c) == "nan":
            drawopt[key] = "fill={}, fill opacity={}".format('none',0)
            colorscheme[key] = "none"
        else:
            drawopt[key] = "fill={}, fill opacity={}".format(c,opacity)

    print(containedLayers)


    def save_and_plot(converter, filename):
        converter.compile(filename=filename, overwrite=True)

        # Show the output pdf
        try:
            from pdf2image import convert_from_path
            
            images = convert_from_path(filename,dpi=200)
        except:
            img = 'PDF could not be displayed. Please install the library wand (pip install wand).'
        return img

    conv = GDSLatexConverter(lib)
    conv.scale = 2.0 #Set a convienient scale for line-thickness
    conv.layer_drawcolor = colorscheme
    
    if pdfTex :
        conv.textype = GDSLatexConverter.PDFLATEX

    conv.layer_drawopt = drawopt     

    save_and_plot(converter=conv, filename=pdfName)
