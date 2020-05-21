### iscan
Use Epson `iscan` utility for easy batch scanning.
Settings are as follow:

Document tab:
  - 600 DPI
  - Image type: Color Photo
  - Unsharp mask: unchecked

Image controls (tweak as needed):
  - Gamma: 1.52
  - Highlight: 255
  - Shadow: 19

### compose.sh
    cd DIRECTORY_WITH_SCANS
    ../compose.sh *.tiff

### GIMP
Use GIMP's selection tool to find out matching rectangle regions.
`regions.json` file should be created for each batch.

### autocrop.py
    cd DIRECTORY_WITH_SCANS
    ../autocrop.py *.tiff

