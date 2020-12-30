import png
import numpy as np
import numpngw
from PIL import Image
import random
import cv2
import os

def to_png(path):
  image_type = path.split('.')
  if image_type[-1] != 'png':
    try:
      im = Image.open(path)
      new = ''
      for i in image_type:
        if i == image_type[-1]:
          continue
        new = new + i + '.'
      new = new + 'png'
      im.save(new)
      return new
    except FileNotFoundError:
      print("[x] File: '"+str(path)+"' is not defined!")
      raise SystemExit
  else :
    return path
  

def int_to_bin16(number):
  return "{0:016b}".format(number)

def int_to_bin8(number):
  return "{0:08b}".format(number)

def int_to_bin13(number):
  return "{0:013b}".format(number)

def int_to_bin26(number):
  return "{0:026b}".format(number)

def bin_to_int(binary):
  return int(binary, 2)

def image_to_array(path):
  try:
    im = Image.open(path)
    q = np.array(im)
    return q
  except IOError:
    print("[x] File: '" + str(path) + "' is not found!")
    raise SystemExit

def uint8_to_uint16(path):
  array = image_to_array(path)
  if array.dtype == 'uint16':
    return array
  else:
    new = (array*256).astype('uint16')
    del array
    return new ##array

def xor(number, random):
    number = int_to_bin8(number)
    random = int_to_bin8(random)
    new = ''
    for i in range(8):
        if number[i] == "0" and random[i] == "0":
            new += "0"
        if number[i] == "0" and random[i] == "1":
            new += "1"
        if number[i] == "1" and random[i] == "0":
            new += "1"
        if number[i] == "1" and random[i] == "1":
            new += "0"
    return bin_to_int(new)

def encryptDecrypt(path):
  try:
    array = image_to_array(path)
    l = []
    k = 0
    q = 0
    for i in array.flat:
      if k == 253:
        k = 0
      q = xor(i, k)
      l.append(q)
      k += 1
    new = np.array(l, dtype = 'uint8').reshape(array.shape[0], array.shape[1], array.shape[2])
    del array
    return new ##array
  except KeyboardInterrupt:
    raise SystemExit

def merge_numbers(number1, number2):
  return bin_to_int(int_to_bin16(number1)[:4] + int_to_bin8(number2)[:4] + int_to_bin16(number1)[8:])

def merge(img1, img2):
  try:
    array1 = uint8_to_uint16(img1)
    array2 = encryptDecrypt(img2)
    for matrix in range(array2.shape[0]):
      for list in range(array2.shape[1]):
        for element in range(array2.shape[2]):
          array1[matrix][list][element] = merge_numbers(array1[matrix][list][element], array2[matrix][list][element])
    del array2
    q = 'merged.png'
    numpngw.write_png(q, array1)
    return q
  except KeyboardInterrupt:
    raise SystemExit
  
def unmerge_number(number):
  return bin_to_int(int_to_bin16(number)[4:8] + '0000')

def unmerge(path, l):
  try:
    array = uint8_to_uint16(path)
    new = np.empty((l[0], l[1], l[2]), dtype = "uint8")
    for matrix in range(l[0]):
      for list in range(l[1]):
        for element in range(l[2]):
          new[matrix][list][element] = unmerge_number(array[matrix][list][element])
    del array
    q = 'unmerged.png'
    numpngw.write_png(q, new)
    return q
  except KeyboardInterrupt:
    raise SystemExit

def shape(path):
  array = image_to_array(path)
  return array.shape

"""
key = random.randint(230, 255)
print(key)
key = 240
image1 = to_png("G:\\Desktop\\26-06-2019_11-30-48\\the.png")
image2 = to_png("G:\\Desktop\\26-06-2019_11-30-48\\extract.png")
l = shape(image2)
merged = merge(image1, image2)
encryptDecrypt(unmerge(merged, l))
"""



