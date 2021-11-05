---
title: 'IC-Layout Render: Image rendering tool for integrated circuit layout in Python'
tags:
	- Python
	- Graphic Design System
	- integrated circuit
	- layout illustration
authors:
	- name: João R. R. O. Martins
	orcid: 
	affiliation: "1, 2"
	- name: Pietro M. Ferreira
	orcid: 0000-0002-0038-9058
	affiliation: "1, 2"
affiliation:
	- name: Université Paris-Saclay, CentraleSupélec, CNRS, Lab. de Génie Électrique et Électronique de Paris,91192,Gif-sur-Yvette,France
	index: 1
	- name: Sorbonne Université, CNRS, Lab. de Génie Électrique et Électronique de Paris, 75252, Paris, France
	index: 2
date: 05 November 2021
bibliography: paper.bib
---

# Summary

Graphic Design System (GDSII) from [@Calma1987] is a common database file format to stream out integrated circuit (IC) masks, also called layout, before fabrication. 
Being an essential part of circuit development, designers are often familiarized in how to generate this binary file on computer-aided design (CAD) tools. 
This output file contains planar geometric shapes which represent physical 3D layers from a specific process design kit (PDK). 
Commercial PDK usually presents more than 50 layers, which are 2D visualized in CAD tools. 

Reading a layout in those CAD tools is not a simple task, however high-quality graphical image is available in such tool. 
Thus, an IC designer is capable to understand the data representation and point out improvements for the IC. 
Nevertheless, IC documentation is often delivered in a lower quality 2D image depicted in a PDF file. 
Once the PDF is generated; the circuit layout becomes hardly readable even for experienced IC designers.

Scientific communications require accurate and repeatable results to be considered prior publication. 
In microelectronics research field, a layout picture is mandatory. 
While illustrations should be a vectorial graph like, IC layout is often depicted from a low-quality bitmap obtained from a screenshot or an image saving through the CAD tool. 
In this scenario, having an accurate, readable, and reproducible layout result is a challenge. 
Most publications illustrate IC layouts in lower standards than the other illustration results, which hinds the required physical solution to address state-of-the-art IC performance.

The tool icLayoutRender aims to a user-friendly transcription of a GDSII file in a pdf file. 
Developed in Python 3, the image rendering requires an input GDSII file <cellName.gds> and the PDK layer color file <LayerColor_PDK.map> to produce an output PDF file <cellName.pdf>. 
The GDSII layers will be rendered using the available PDK layer colors. Missing layers will be neglected.

The tool icLayoutRender does:
	1. confirm the entered values;
	2. item convert the *.gds to a *.tex file;
	3. call LuaTeX or pdflatex to generate a *.aux, and *.pdf.

The tool icLayoutRender requires:
	1. Python3 installed with devel options;
	2. gdspy, pandas, math, and GDSLatexConverter [@Vollmer2020] Python libraries installed;
	3. TexLive for a Linux installation, or  MikTEX for a Windows installation;
	4. tikz LaTEX package to compile the output *.pdf  file.

Several examples using icLayoutRender are freely available on the official website. 
Layer color file generation is also explained in the user manual, as installation procedure and the tool operation in Linux and Windows. 
The icLayoutRender image rendering tool has been used in recent scientific communication [@Martins2021] and the illustration readability is remarkable.

# Overview of icLayoutRender tool

In commercial CAD tools, the GDSII file is obtained following a common procedure File->Export->Stream. 
The output stream file should be named as <cellName.gds> and selected as the top cell to be exported from an available layout. 
The GDSII file should be saved in the same folder as the proposed tool for a user-friendly operation.

The LayerColors.map file is created for a specific PDK. 
Commercially available PDK, as [@XFAB:019], has the layers: diffusion in lime, poly-Si in red, n-type implantation in gold, p-type implantation in pink, and others. 
The layer color file format is depicted in the \autoref{ver:LayerMAP} One may notice that lime, red, gold, and pink colors are represented in RGB color code. 
GDS layer number and name are available in the PDK layer map file (see \ref{fig:LayerNumbers}), while the color and its code are obtained in the technology file. 
A user-friendly layer window (LSW) is often available aid both files translation in the requested LayerColors.map. 
One may implement an automation tool for such translation. However, this procedure is only run once per PDK. GDS number, layer name, and color do not change between different PDK versions. 
Moreover, CAD tools usually uses the color code proposed in the example \autoref{ver:LayerMAP}. Thus, this procedure is only required in the installation of a new PDK and the layer colors are usually the same. 
The GDS number is the data that mostly change between different PDK files.
![Checking layer numbers in a commercial PDK as [@XFAB2019]. \label{fig:LayerNumbers}](Images/LayerNumbers.png){ width=40% }
![Checking layer collors in a commercial PDK as [@XFAB2019]. \label{fig:LayerColors}](Images/LayerColors.png){ width=40% }
\begin{verbatim}
\label{ver:LayerMAP} 
GDSNumber!Layer!Collor
4!DIFF!{rgb:red,0;green,255;blue,0}
5!POLY!{rgb:red,255;green,0;blue,0}
6!NIMP!{rgb:red,217;green,204;blue,0}
7!PIMP!{rgb:red,255;green,191;blue,242}
\end{verbatim} 

To prove the advantage of using icLayoutRender tool, the authors have rendered the IC layout known as StrongArm latched comparator and proposed in [@Fonseca2017]. 
The original image file is reproduced in Fig \autoref{fig:SA_Fonseca} using a grey color scale. Figure \autoref{fig:SA_ColorRendering} depicts the same IC layout 
rendered by the proposed tool in a colored version, and \autoref{fig:SA_GrayRendering} is a gray scaled version of the rendering. 
A full color version of this example is depicted in Fig. \autoref{fig:SA_original} and \autoref{fig:SA_ColorRendering}.
Another example of IC layout known as OTA Miler is compared in Fig \autoref{fig:OTA_original}, using standard tools, and in Fig \autoref{fig:OTA_ColorRendering}, using the icLayoutRender solution.
Both illustration examples are obtained from an IC design using the PDK of [@XFAB2019]. 
The authors invite the reader to now increase zoom over Fig. \autoref{fig:SA_original} and \autoref{fig:SA_ColorRendering}, or over  \autoref{fig:OTA_original} and \autoref{fig:OTA_ColorRendering}
to assert the vectorial graphical rendering obtained by the proposal in which the standard tool is unable to attain. 

![Original StrongArm latched comparator layout proposed in [@Fonseca2017]. \label{fig:SA_Fonseca}](Images/SA_Fonseca.png){ width=40% }
![StrongArm latched comparator layout rendered by the proposed tool (gray scaled version). \label{fig:SA_GrayRendering}](Images/SA_GrayRendering.svg){ width=40% }

![Original StrongArm latched comparator layout in full color. \label{fig:SA_original}.](Images/SA_original.png){ width=40% }
![StrongArm latched comparator layout rendered by the proposed tool (colored version). \label{fig:SA_ColorRendering}](Images/SA_ColorRendering.svg){ width=40% }

![Original OTA Miler amplifier layout.\label{fig:OTA_original}.](Images/OTA_original.png){ width=40% }
![OTA Miler amplifier layout rendered by the proposed tool (colored version). \label{fig:OTA_ColorRendering}](Images/OTA_ColorRendering.svg){ width=40% }

# References
