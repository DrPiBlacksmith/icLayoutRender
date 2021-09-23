
# gds2pdf

Havin a high quality layout image for publishing is a painfull process. And usually published layouts have poor quality.

This library intends to make this process as straight forward as possible. By inputing a .gds file the script outputs a .tex and a pdf file ready for publication.



## API Reference

### Generating a GDS File on CADENCE Virtuoso 

Open the Virtuoso Window, and go to File->Export->Stream

Configure the stream file to be: cellName.gds

Select your library and the topcell to be exported
  - Library: Mylib
  - Cell: cellName
  - View: Layout

Click **Apply**

### LayerColor File

The LayerColors.map file is created for a specific Process Design Kit (PDK)

If the available PDK has the layers:
- diffusion is lime,
- poly-Si is red, 
- n-type implantation is gold, 
- p-type implantation is pink...

File format is:

- GDSNumber!Layer!Collor
- 4!DIFF!{rgb:red,0;green,255;blue,0}
- 5!POLY!{rgb:red,255;green,0;blue,0}
- 6!NIMP!{rgb:red,217;green,204;blue,0}
- 7!PIMP!{rgb:red,255;green,191;blue,242}

### Creating LayerColors file

Obtain the GDS layer number using 
  > Technology Tool Box->Manager->Dump…->Save

The layer numbers can also be obtained when exporting the .gds file as shown on the image bellow:
![](/Images/LayerNumbers.png)


Obtain the colors from Virtuoso layout using
  > Display Resources Tool Box->Edit->File->Save
![](/Images/LayerColors.png)

Compare the *.tf file and the *.drf

Write a new layerColors_PDK.map according to the example

Missing layers will be neglected

```bash
  python gds2pdf
  Please enter the cell name: **INPUT FILE** # No GDS extention
  Please enter the layer colors: **LayerColor** # No CSV extention
```



  
## Authors

- [J. R. R. O. Martins](https://www.github.com/Rapos0)
- [Pietro M. Ferreira](https://www.github.com/DrPiBlacksmith)


  
## Installation

### Linux
Please first make sure that python 3 is installed on your machine with the devel extension, otherwise please run

For CentOs:
```bash
  sudo yum install python3-devel
```
For Ubuntu:
```bash
  sudo apt install python3-devel
```
#### Dependencys Installation

```bash
  python -m pip install --user gdspy
  python -m pip install pandas
  python -m pip install:l git+https://github.com/Aypac/GDSLatexConverter.git
```
#### Installing TeXLive

```bash
  cd /~
  mkdir TeXLiveInstall
  cd TeXLiveInstall
  wget https://mirrors.chevalier.io/CTAN/systems/texlive/tlnet/install-tl-unx.tar.gz
  tar -xzvf install-tl-unx.tar.gz
  cd install-tl
  pearl install-tl -gui
```

Installation is completed at /usr/local/texlive/2021
Please check if the 2021 version is installed in the default path using

```bash
tex --version
```

### Windows

Please first make sure that ```PYTHON_INSTALLATION_FOLDER/include``` is in your PATH. 

Download the precompiled release of [gdspy](https://github.com/heitzmann/gdspy/releases)

Once downloaded open your command prompt

```cmd 
cd *DOWNLOAD_PATH*
python -m pip install ****.whl
python -m pip install pandas
pip install git+https://github.com/Aypac/GDSLatexConverter.git
```
For installing latex compiler we sugest [MiKTeX](https://miktex.org/download) 


## Screenshots
### Miller Operational Transconductance Amplifier
![OTA_Miller](Examples/OTA_Miller.svg)

### Strong Arm Comparator
![SA_Razavi2015](Examples/SA_Razavi2015.svg)

  
## License

[GNU](https://choosealicense.com/licenses/agpl-3.0)

  
