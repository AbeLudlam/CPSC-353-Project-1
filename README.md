# CPSC-353-Project-1

Writer: Abraham Ludlam

My encoding and decoding software is split into two different programs, one for encoding and the other for decoding. Encoding takes
a file and an image, then converts the text into binary and changes the least significant bits of the last pixels in the image.
Decoding reads the last 11 bits to determine the length of the message, and then reads the indicated amount of pixels to get the message.


As for running the software, it requires python 3 and python pillow. My installation for both is based on the "Building on Linux" 
section on the Pillow website here https://pillow.readthedocs.io/en/latest/installation.html. To run in the command terminal
use "python ./encode.py" for encoding and "python ./decode.py" for decoding. Encoding asks for a file and an image name, decoding only
asks for an image; make sure to input the correct file or image names



For Professor Razul:

I have a encode10 and decode10 program as well. These were made to be compatible with the test image you gave us. In the test image, the text length only is encoded to the last 10 bits, ignoring the 11th, and encoding the message 12 onwards. As the test image was made and read by your encoder, the 10 version of the programs and images were made to fit the same conditions as the test image.
