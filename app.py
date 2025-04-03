def read_img(filename):
    with open(filename) as f:
        offset = 0
        lines = f.readlines()
        if ("#" in lines[1]):
            offset=1
        #Finding dimensions
        dim = lines[1+offset]
        dim = dim.rstrip("\n")
        dim = dim.split()
        width = int(dim[0])
        height = int(dim[1])
        dim_report = f"Width: {width} px Height: {height} px"
        print (dim_report)
        
        #findng pixels into list
        pixel = []
        row  = []
        out = []
        for x in range(3+offset,len(lines)):
            lines[x] = lines[x].rstrip("\n")
            for val in lines[x].split():
                pixel.append(int(val))
                if (len(pixel) == 3):
                    row.append(pixel)
                    pixel = []
                    if (len(row) == width):
                        out.append(row)
                        row = []
        return (out)

def grey(img):
    for y in range(len(img)):
        for x in range(len(img[y])):
            pixel = img[y][x]
            total = pixel[0]+pixel[1]+pixel[2]
            pixel[0] = total//3
            pixel[1] = total//3
            pixel[2] = total//3


def sobel_img(img):
    out = []
    for y in range(len(img)):
        row = []
        row.append([0,0,0])
        for x in range(1 , len(img[y])-1):
            oldPixel = img[y][x]
            newPixel = []

            pixelLeft = img[y][x-1]
            pixelRight = img[y][x+1]

            left = pixelLeft[0] * -1
            center = oldPixel[0] *0
            right = pixelRight[0] * 1
            newPixelVal = abs(left + center + right)
            newPixelVal*= 2
            if newPixelVal > 255:
                newPixelVal = 255

            newPixel = [newPixelVal, newPixelVal, newPixelVal]

            row.append(newPixel)
        row.append([0,0,0])
        out.append(row)

    return out

def reduce_noise(img):
    out = []

    for y in range(len(img)):
        row = []
        for x in range(0, len(img[y])):
            oldPixel = img[y][x]
            newPixelVal = oldPixel[0]
            if (oldPixel[0] < 64):
                newPixelVal = 0  

            newPixel = [newPixelVal, newPixelVal, newPixelVal]
            row.append(newPixel)
        out.append(row)
    return out

"""
def sobel_img(img): #an array of [row][pixel][value,value,value]

    out = []
    for y in range(len(img)):
        row = []
        for x in range(1, len(img[y])-1): #pixels
            pixel = img[y][x]
            newPixel = []
            if (x == 0 or x == len(img) - 1):
                newPixelVal = pixel[0] #assuming greyscale
                

            else:
                pixelLeft = img[y][x-1]
                pixelRight = img[y][x+1]

                left = pixelLeft[0] * -1
                center = pixel[0]
                right = pixelRight[0] * 1
                newPixelVal = abs(left + center + right)

            newPixel = [newPixelVal, newPixelVal, newPixelVal]
            row.append(newPixel)
        out.append(row)
    
    return out """

    



def write_img(img, filename):
    with open(filename, "w") as f:
        f.write("P3 \n")
        height = str(len(img))
        width = str(len(img[0]))
        f.write(f"{width} {height}\n")
        f.write("255\n")
        for row in img:
            for px in row:
                for channel in px:
                    f.write(f"{channel} ")
            f.write("\n")

cats = read_img("jedi-cats.ppm")
grey(cats)
sobelCats = sobel_img(cats)
#noiseCats = reduce_noise(sobelCats) 
write_img (sobelCats, "sobel-cats.ppm")
read_img("sobel-cats.ppm")


clown = read_img("creative.ppm")
grey(clown)
sobelClown = sobel_img(clown)
write_img(sobelClown, "sobel-clown.ppm")


