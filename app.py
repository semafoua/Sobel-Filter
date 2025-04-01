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
        img = []
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
        return (img)


def sobel_img(img): #an array of [row][pixel][value,value,value]
    for y in range(len(img)):
        for x in range(len(img[y])): #pixels
            pixelLeft = img[y][x-1]
            pixel = img[y][x]
            pixelRight = img[y][x+1]
            if (x == 0 or x == len(img) - 1):
                newPixelVal == pixel[0] #assuming greyscale

            else:
                left = pixelLeft[0] * -1
                center = pixel[0]
                right = pixelRight[0] * 1
                newPixelVal = abs(left + center + right)

            pixel[0] = newPixelVal
            pixel[1] = newPixelVal
            pixel[2] = newPixelVal
    
    return img

    



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


