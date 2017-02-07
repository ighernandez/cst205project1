#Ignacio Hernandez
#CST 205
#Project 1 Images

#print("heelo world")
# this is a comment
from PIL import Image
from PIL import Image

def medianOdd(myList):
    listlength = len(myList)
    sortedValues = sorted(myList)
    middleIndex = (listlength + 1)//2 - 1
    return sortedValues[middleIndex]

imgList = []

for i in range(9):
    imgList.append(Image.open("pics/ProjectImages/" + str (i + 1) + ".png"))
    
    
picW, picH = imgList[0].size

redPixelList = []
greenPixelList = []
bluePixelList = []

myRed, myGreen, myBlue = imgList[6].getpixel((2,3))

print(myRed, myGreen, myBlue)

canvas = Image.new("RGB", (picW, picH), "white")

for x in range(picW):
    for y in range(picH):
        for myImage in imgList:
            myRed, myGreen, myBlue = myImage.getpixel((x,y))
            redPixelList.append(myRed)
            greenPixelList.append(myGreen)
            bluePixelList.append(myBlue)
            
            
        medianRed = medianOdd(redPixelList)
        medianGreen = medianOdd(greenPixelList)
        medianBlue = medianOdd(bluePixelList)
        
        canvas.putpixel((x,y), (medianRed, medianGreen, medianBlue))
        
        redPixelList = []
        greenPixelList = []
        bluePixelList = []
        
canvas.save("newpic.png")