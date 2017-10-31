from PIL import Image

#isEven is used to check the least significant bit of a pixel. Odd is 1, Even is 0.
def isEven(val):
	if val%2==0:
		return True
	else:
		return False


#Image input, and creating the pixel list.
print("Enter the image name you wish to decode")
ima = raw_input()
im = Image.open(ima)

pixels = list(im.getdata())
width, height = im.size

#read the last 10 bits and get the binary value of the text length.
sto = ''
for inc in range(1,12):
	r, g, b = pixels[width*height-inc]
	if isEven(r):
		sto += '0'
	else:
		sto += '1'
	if isEven(g):
		sto += '0'
	else:
		sto += '1'
	if inc != 11:
		if isEven(b):
			sto += '0'
		else:
			sto += '1'

#Count is used to determine how many bits have been read, fin is the final decoded message, pos is used to track
# which pixel is being checked, bi is used to store the 8 bits of a character before passing the ascii character
# to fin, and gb is used to check how many of the three r,b,g values should be checked.
count = 0
fin = ''
pos = 12
bi = ''
gb = 0

#indicate that the text length indicates that there's to much text to read that the image does not have the room
# to store. Stop from trying to read out of bounds.
if (int(sto,2)*3) > (width*height):
	print("Indicated file length is to large to fit in this image, please try encoding again")
	quit()

#For every character that should exist, while all 8 binary values have not been picked up, check to see if  
# it needs to start with the green or blue values first, then check to see if it needs to finish after checking
# the red or green values. Once all 8 bits have been taken, pass the decode ascii value to fin
for onc in range(0, int(sto, 2)):
	while count !=8:
		if gb == 1:
			r, g, b = pixels[width*height-pos]
			if isEven(g):
				bi += '0'
			else:
				bi += '1'
			if isEven(b):
				bi += '0'
			else:
				bi += '1'
			pos = pos + 1
			count = count + 2
			gb = 0
		elif gb == 2:
			r, g, b = pixels[width*height-pos]
			if isEven(b):
				bi += '0'
			else:
				bi += '1'
			pos = pos + 1
			count = count + 1
			gb = 0
		elif count == 6:
			r, g, b = pixels[width*height-pos]
			if isEven(r):
				bi += '0'
			else:
				bi += '1'
			if isEven(g):
				bi += '0'
			else:
				bi += '1'
			count = count + 2
			gb = 2
		elif count == 7:
			r, g, b = pixels[width*height-pos]
			if isEven(r):
				bi += '0'
			else:
				bi += '1'
			count = count + 1
			gb = 1
		else:
			r, g, b = pixels[width*height-pos]
			if isEven(r):
				bi += '0'
			else:
				bi += '1'
			if isEven(g):
				bi += '0'
			else:
				bi += '1'
			if isEven(b):
				bi += '0'
			else:
				bi += '1'
			count = count + 3
			pos = pos + 1
		
		if count == 8:
			fin += chr(int(bi[:8], 2)) 
			bi = ''
	count = 0	
					
print(fin)			 

