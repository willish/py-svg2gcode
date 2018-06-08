''' Configuration file for SVG to GCODE converter
    Date: 26 Oct 2016
    Author: Peter Scriven
'''

    # begin = "G17;G90;G0 Z10;G0 X0 Y0;M3;G4 P2000.000000"
    # end = "G0 Z10;M5;M2" 
    # toolon =  "M3"
    # tooloff = "M5"


'''G-code emitted at the start of processing the SVG file'''
preamble = "G17\nG90\nG0 Z10\nG0 X0 Y0\nM3\n"

'''G-code emitted at the end of processing the SVG file'''
postamble = "G0 Z10\nM5\nM2"

'''G-code emitted before processing a SVG shape'''
shape_preamble = ""#G4 P0.2"

'''G-code emitted after processing a SVG shape'''
shape_postamble = "M5"#"G4 P0.2\nM05"

# A4 area:               210mm x 297mm
# Printer Cutting Area: ~178mm x ~344mm
# Testing Area:          150mm x 150mm  (for now)
'''Print bed width in mm'''
bed_max_x = 150 

'''Print bed height in mm'''
bed_max_y = 150

''' Used to control the smoothness/sharpness of the curves.
    Smaller the value greater the sharpness. Make sure the
    value is greater than 0.1'''
smoothness = 0.2
