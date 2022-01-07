# GolayCodePython
A Golay Code decoding and encoding method implementation using Python.
The GUI was created with the tkinter library.
This is a simulation of a real communication channel with a specified distortion probability.
It allows the user to send data through the channel and showcases, how effectively the Golay Code algorithm would try to recover erroneous data.
# Required libraries
- Python 3.9 or higher with tkinter
- py2exe
- bitarray
- Pillow
# Instructions
## Quickstart
Launch the *GolayCode.bat* file to open the already generated executable file in the *dist* folder.
## Generate new .exe file
Make sure you have everything installed. Launch *setup.py* with the *python setup.py py2exe* command.
Your executable file will be located in the subdirectory *dir* and will have the name *main.exe*.
# Main Features
- Set and change the distortion probability of the communication channel in any window.
- Send a binary vector of length 12 and compare raw data with encrypted then decoded values.
- Transfer and receive a block of text, compare the Golay Code algorithm's effectiveness.
- Test the method's capabilities with .bmp files sent through the channel.
# Notice
All code comments are written in Lithuanian, but the GUI is English.
# Screenshots
## Initial launch and main menu

## Sending a vector

## Sending a block of text

## Sending a .bmp file
