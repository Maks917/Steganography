import desktop
import rsa
import random
import numpngw
import os

os.chdir("G:\\Desktop\\Практика Python")
mode = input("[E]ncrypt, [D]ecrypt : ").upper()
if mode == 'E':
    coverImage = input("Cover file name : ")
    hideImage = input("File name which you want to hide : ")
    image1 = desktop.to_png(coverImage)
    image2 = desktop.to_png(hideImage)
    key = desktop.shape(image2) ## 2 element
    print("Your keys : " + str(key[0]) + ", " + str(key[1]))
    print("Merge process . . .")
    mergedPath = desktop.merge(image1, image2)
    print("FILES ARE MERGED ( " + str(mergedPath) + " )")
    os.remove(hideImage)
    os.remove(coverImage)

elif mode == 'D':
    image = input("File name : ")
    key1 = int(input("First key : "))
    key2 = int(input("Second key : "))
    l = (key1, key2, 3)
    print("Unmerge process . . .")
    unmerged = desktop.unmerge(image, l)
    unmergedArray = desktop.encryptDecrypt(unmerged)
    numpngw.write_png("Decrypted.png", unmergedArray)
    print("Your file : " + str("Decrypted.png"))

