#!/usr/bin/env python

# Authors: jtbisign and jliebowf

# Requirements: scipy, imagetk

import os
import numpy as np
import scipy.misc as misc

try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *
    
from PIL import Image, ImageTk

if (len(sys.argv) != 2 and len(sys.argv) != 3) or \
	(len(sys.argv) == 3 and sys.argv[1] != "--pre-cache"):
	print >> sys.stderr, "Usage:", sys.argv[0], "[--pre-cache] <jpeg-path>"
	exit(1)

pre_cache = len(sys.argv) == 3
img_path = sys.argv[1]
if pre_cache:
	img_path = sys.argv[2]
img_path = os.path.abspath(img_path)

# bias is a number in the range [0, 2],
# where 0 is completely unbiased, 1 is
# relatively biased, and 2 is completely
# biased (all 0s)
def generateStream(bias, rows, cols, channels=False):
	stream = []
	for i in range(rows):
		row = []
		for j in range(cols):
			if channels:
				col = []
				for k in range(channels):
					col.append(randomOffset(bias))
				row.append(col)
			else:
				row.append(randomOffset(bias))
		stream.append(row)
	return stream

def randomOffset(bias):
	exp = np.random.exponential(128)
	un = np.random.uniform(0, 256)
	if bias < 1:
		return ((bias * exp) + ((1 - bias) * un)) % 256
	bias = bias - 1
	# for bias = 2, the offset is 0
	return np.uint8(((1 - bias) * exp))

def encryptImage(img, stream):
	shape = img.shape
	rows, cols = shape[0], shape[1]
	new = 0
	if len(shape) == 2:
		new = np.zeros((rows, cols), np.uint8)
	else:
		new = np.zeros((rows, cols, shape[2]), np.uint8)
	for i in range(rows):
		for j in range(cols):
			if len(shape) == 3:
				for k in range(shape[2]):
					new[i][j][k] = (img[i][j][k] + stream[i][j][k])
			else:
				new[i][j] = (img[i][j] + stream[i][j])
	return new


#
# The UI
#
 
imread = misc.imread

img = imread(img_path)
h = img.shape[0]
w = img.shape[1]
d = img.shape[2]

image_cache = {}
def encryptImageCached(value):
	if value in image_cache:
		return image_cache[value]
	opt = generateStream(value, h, w, d)
	enc = encryptImage(img, opt)
	image_cache[value] = enc
	return enc

if pre_cache:
	for i in range(21):
		encryptImageCached(i/10.0)
		sys.stdout.write("\r{}%\033[K".format(i*5.0))
		sys.stdout.flush()
	print

def update_image(value):
	value = float(value) / 50 # Adjust value to be between 0 and 2

	enc = encryptImageCached(value)
	photo = ImageTk.PhotoImage(Image.fromarray(enc))
	label.config(image=photo)
	label.image = photo
	label.pack(anchor=CENTER)

root = Tk()

window_width = w + 50
window_height = h + 75
root.geometry(str(window_width)+"x"+str(window_height)+"+300+300")

var = DoubleVar()
scale = Scale( root, variable = var, from_ = 0, to = 100, resolution = 5, orient=HORIZONTAL, command=update_image )
scale.pack(anchor=CENTER)

label = Label(root)
label.pack(anchor=CENTER)

root.mainloop()
