# Bit-Clock

A MicroPython binary clock for the BBC micro:bit.

The clock uses the top four rows of the micro:bit's LED array to display the time in binary. The fifth row is not used and is given a background glow to distinguish it from the pixels that make up the binary numbers.

Each column represents one digit of the time in 24 hour format "HH.MM". Where:

* Column 1 gives the first decimal digit of the hours in binary
* Column 2 gives the second decimal digit of the hours in binary
* Column 3 contains a single pixel that flashes at one second intervals
* Column 4 gives the first decimal digit of the minutes in binary
* Column 5 gives the second decimal digit of the minutes in binary

The time defaults to 12:34. Press button A to set the hours and button B to set the minutes.

The application uses the Micro:Bit's internal clock as a time source and so will be accurate.
