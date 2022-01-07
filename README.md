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
Make sure you have every mandatory library installed. Launch *setup.py* with the *python setup.py py2exe* command.
Your executable file will be located in the subdirectory *dir* and will have the name *main.exe*.
# Primary Features
- Set and change the distortion probability of the communication channel in any window.
- Send a binary vector of length 12 and compare raw data with encrypted then decoded values.
- Transfer and receive a block of text, compare the Golay Code algorithm's effectiveness.
- Test the method's capabilities with .bmp files sent through the channel.
# Notice
All code comments are written in Lithuanian, but the GUI is English.
# Screenshots
## Initial launch and main menu
![image](https://user-images.githubusercontent.com/43152072/148556095-f64b3204-e812-4fa6-9b0b-dc8735861faa.png)
## Sending a vector
![Vector](https://user-images.githubusercontent.com/43152072/148556114-718942f8-a664-45ae-bfea-616f5f4e2d76.jpg)
## Sending a block of text
![Text](https://user-images.githubusercontent.com/43152072/148556140-79f0e0b2-ad0c-43f7-b832-62056638ac94.jpg)
## Sending an image
![Saturn](https://user-images.githubusercontent.com/43152072/148556158-ed573c71-04e9-4007-9b6d-830a2e95b81b.jpg)
