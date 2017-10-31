from PIL import Image

#isEven is used to to determine the least significant bit for binary values. Even have 0, odd have 1.
def isEven(val):
	if val%2==0:
		return True
	else:
		return False
# File inputs and checks. fil is the file name, ima is the image name. Check to make sure there are enough bits
# in the image to decode with
print("Enter the file you wish to encode")
fil = raw_input()
with open(fil) as f:
	tex = f.read()
f.closed
print("Enter the image name you wish to encode with")
ima = raw_input()
tmm = Image.open(ima)
pixels = list(tmm.getdata())
width, height = tmm.size
if width*height <= len(tex)*3:
	print("File is to large to fit into the picture, try again")
	quit()
	
#fr is the binary string of the length of the text. Cut off the 0b at the start, and add 0 to the front to make it
# the right size.
fr = bin(len(tex))
fr = fr[2:]
for bn in range(0, 32-len(fr)):
	fr = '0' + fr
ad = 1
#Look at the first 10 bits and change the red, blue and green pixels when necessary for decoding. If the binary of
# the text length is 0, only change the bit value if its odd by subtracting one. Likewise, add a bit when the
#binary value is odd and the bit is even. This prevents other bit changes. Pixel position is checked by the
# value ad, while which r,g,b value is checked by the increment "on" mod 3.
for on in range(0, 32):
	r, g, b = pixels[width*height-ad]
	if on%3 == 0:
		if isEven(int(fr[on])):
			if isEven(r) != True:
				pixels[width*height-ad] = ((r-1), g, b)
				
			
		else:
			if isEven(r):
				pixels[width*height-ad] = ((r+1), g, b)
				
		
	if on%3 == 1:
		if isEven(int(fr[on])):
			if isEven(g) != True:
				pixels[width*height-ad] = (r, (g-1), b)
				
		else:
			if isEven(g):
				pixels[width*height-ad] = (r, (g+1), b)
				
		
	if on%3 == 2:
		if isEven(int(fr[on])):
			if isEven(b) != True:
				pixels[width*height-ad] = (r, g, (b-1))
				
				
		else:
			if isEven(b):
				pixels[width*height-ad] = (r, g, (b+1))
				
		ad += 1

#The list i used was not changing the image, so load the image with pixe and change the pixels. widt is used
# for the width position of and heigh for the height position
pixe = tmm.load()
heigh = 1
widt = 1
for sm in range(1,12):
	if (width-widt) < 0:
		he += 1
		wi = 1
	
	pixe[width-widt, height-heigh] = pixels[width*height-sm]
	widt +=1

#for the actual text to binary encoding, we start by turning a character into binary, then going through each 0 
# or 1, and changing the values the same way as the text length earlier. mn acts as our binary charracter holder
# nm is our entire text in binary, being trimmed of its 0b headers, pos is used to know which r,g,b value to check
# and pla is used to indicate which pixel is being changed.
mn = "0"
pos = 0
pla = 12
nm = ''.join(map(bin,bytearray(tex,'ascii')))

for inc in range(0, len(tex)):
	nm = ''.join(map(bin,bytearray(tex[inc],'ascii')))
	for onc in range(0, 9-len(nm)):
		mn += '0'
	mn += nm[2:]
	for eig in range(0,8):
		r, g, b = pixels[width*height-pla]
		if pos == 0:
			
			if isEven(int(mn[eig])):
				
				if isEven(r) != True:
					pixels[width*height-pla]= ((r-1),g, b)
			else: 
				if isEven(r):
					pixels[width*height-pla]= ((r+1),g, b)
			pos += 1
		elif pos == 1:
			if isEven(int(mn[eig])):
				if isEven(g) != True:
					pixels[width*height-pla]= (r,(g-1), b)
			else: 
				if isEven(g):
					pixels[width*height-pla]= (r,(g+1), b)
			pos += 1
		else:
			if isEven(int(mn[eig])):
				if isEven(b) != True:
					pixels[width*height-pla]= (r,g, (b-1))
			else: 
				if isEven(b):
					pixels[width*height-pla]= (r,g, (b+1))
			pos = 0
			pla += 1
					 
	
	mn = '0'
# Place the pixels into the image, wi and he are used for the actual pixel positions. It is run from 12 to
#pla +1	because pla indicates the last pixel that was changed. The image is saved as the original 
#image name +"-en.png"

wi = 12
he = 1
for la in range(12, pla+1):
	r, g, b = pixels[width*height-la]
	if (width-wi) < 0:
		he += 1
		wi = 1
	pixe[width-wi, height-he] = pixels[width*height-la]
	wi += 1
ima += '-en.png'
tmm.save(ima, 'PNG')	
	
