#Ignacio Hernandez
#CST 205
#Project 1 Images
#https://github.com/ighernandez/cst205project1: Link to project.
#used examples instructed by professor
#Abstract: taking out the annoying photo bomber from 9 images


# using pillow to import image
from PIL import Image
from PIL import Image


#defined variables and made some calculations
def MedianValueOdd(myList):
    ListLength = len(myList)
    sortedValues = sorted(myList)
    middleIndex = (ListLength + 1)//2 - 1
    return sortedValues[middleIndex]

#set up list using square brackets
imgList = []

#giving it a range using tuples
for i in range(9):
    imgList.append(Image.open("pics/ProjectImages/" + str (i + 1) + ".png"))
    
    
picW, picH = imgList[0].size

RedPixelList = []
GreenPixelList = []
BluePixelList = []

Red, Green, Blue = imgList[6].getpixel((2,3))

print(Red, Green, Blue)

canvas = Image.new("RGB", (picW, picH), "white")


#giving ranges to x and y to pic widtg and to pic height
for x in range(picW):
    for y in range(picH):
        for myImage in imgList:
            Red, Green, Blue = myImage.getpixel((x,y))
            RedPixelList.append(Red)
            GreenPixelList.append(Green)
            BluePixelList.append(Blue)
            
            
        medianRed = MedianValueOdd(RedPixelList)
        medianGreen = MedianValueOdd(GreenPixelList)
        medianBlue = MedianValueOdd(BluePixelList)
        
        canvas.putpixel((x,y), (medianRed, medianGreen, medianBlue))
        
        RedPixelList = []
        GreenPixelList = []
        BluePixelList = []
        
#saved picture as newpic2.png        
        
canvas.save("newpic2.png")