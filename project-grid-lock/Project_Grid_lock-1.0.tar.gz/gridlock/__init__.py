import tempfile
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
try:
    from PIL import Image
except ImportError:
    import Image
import pylab as plt
import io
import numpy
import base64
import PIL
from tempfile import TemporaryFile
from time import sleep

def grid(image_url):

    image = Image.open(image_url)
    img = plt.imread(image_url)

    height = image.height
    width = image.width

    if height >= 500 and height<2000 :
        my_dpi = 300
    elif height >= 2000 and height<4000:
        my_dpi = 600
    elif height >= 4000 and height<6000:
        my_dpi = 1000
    elif height >= 0 and height < 500:
        my_dpi = 100
    elif height > 6000:
        my_dpi = height/4
    else:
        print("error")

    if (width / height) > 1.28 and (width / height) < 1.4:
        dy, dx = round(width / 4), round(height / 4)
        #print(width, dx, dy, height)

        # Custom (rgb) grid color
        grid_color = [0,0,0]

        # Modify the image to include the grid
        img[:,::dy,:] = grid_color
        img[::dx,:,:] = grid_color
        #print("hi")


        # Set up figure
        fig=plt.figure(figsize=(float(image.size[0])/my_dpi,float(image.size[1])/my_dpi),dpi=my_dpi)
        ax=fig.add_subplot(111)

        # Remove whitespace from around the image
        fig.subplots_adjust(left=0,right=1,bottom=0,top=1)

        # Set the gridding interval: here we use the major tick interval
        myInterval_x= round(height/4)
        myInterval_y = round(width/4)
        loc = plticker.MultipleLocator(base=myInterval_x)
        print(loc)
        ax.xaxis.set_major_locator(loc)
        ax.yaxis.set_major_locator(loc)


        # Add the image
        ax.imshow(img)

        # Find number of gridsquares in x and y direction
        nx=abs(int(float(ax.get_xlim()[1]-ax.get_xlim()[0])/float(myInterval_x)))
        ny=abs(int(float(ax.get_ylim()[1]-ax.get_ylim()[0])/float(myInterval_y)))

        # Add some labels to the gridsquares
        offset = 2
        for j in range(int(ny) + 2):
            y=myInterval_x/2+j*myInterval_x
            offset = offset - 1
            for i in range(int(nx) + 1):
                x=myInterval_y/2.+float(i)*myInterval_y
                ax.text(x,y,'{:d}'.format(i+j*nx + offset),color='w',ha='center',va='center')

        img = numpy.array(image)

        # Grid lines at these intervals (in pixels)
        dy, dx = round(width / 4), round(height / 4)
        print(width, dx, dy, height)

        # Custom (rgb) grid color
        grid_color = [0,0,0]

        # Modify the image to include the grid
        img[:,::dy,:] = grid_color
        img[::dx,:,:] = grid_color
        #print("hi")

        # Show the result
        #plt.imshow(img)
        img_buf = io.BytesIO()
        plt.savefig(img_buf, format='png')
        #print("hrer")

        im = Image.open(img_buf)
        #im.show()
        print(im.height)
        #im.show(title="My Image")
        #numbering(im)
        #img_buf.close()
        #print("closed")
        #print(plt.imshow(img))
        #print(plt.show())

        # Save the figure    
        #fig.savefig('xyz.jpg',dpi=my_dpi)
        buffered = io.BytesIO()
        rgb_im = im.convert('RGB')
        rgb_im.save(buffered, format="JPEG")
        output = base64.b64encode(buffered.getvalue()).decode("utf-8")
        #buffered.close()
    elif (width / height) > 0.9 and (width / height) < 1.1: #---------------------------------
        dy, dx = round(width / 4), round(height / 4)
        print(width, dx, dy, height)

        # Custom (rgb) grid color
        grid_color = [0,0,0]

        # Modify the image to include the grid
        img[:,::dy,:] = grid_color
        img[::dx,:,:] = grid_color


        # Set up figure
        fig=plt.figure(figsize=(float(image.size[0])/my_dpi,float(image.size[1])/my_dpi),dpi=my_dpi)
        ax=fig.add_subplot(111)

        # Remove whitespace from around the image
        fig.subplots_adjust(left=0,right=1,bottom=0,top=1)

        # Set the gridding interval: here we use the major tick interval
        myInterval_x= round(height/4)
        myInterval_y = round(width/4)
        loc = plticker.MultipleLocator(base=myInterval_x)
        print(loc)
        ax.xaxis.set_major_locator(loc)
        ax.yaxis.set_major_locator(loc)


        # Add the image
        ax.imshow(img)

        # Find number of gridsquares in x and y direction
        nx=abs(int(float(ax.get_xlim()[1]-ax.get_xlim()[0])/float(myInterval_x)))
        ny=abs(int(float(ax.get_ylim()[1]-ax.get_ylim()[0])/float(myInterval_y)))

        # Add some labels to the gridsquares
        offset = 1
        for j in range(int(ny) + 2):
            y=myInterval_x/2+j*myInterval_x
            for i in range(int(nx) + 1):
                x=myInterval_y/2.+float(i)*myInterval_y
                ax.text(x,y,'{:d}'.format(i+j*nx + offset),color='w',ha='center',va='center')

        img = numpy.array(image)
        #print(img.length)

        width = image.width
        height = image.height
        # Grid lines at these intervals (in pixels)
        # dx and dy can be different
        dy, dx = round(width / 4), round(height / 4)
        print(width, dx, dy, height)

        # Custom (rgb) grid color
        grid_color = [0,0,0]

        # Modify the image to include the grid
        img[:,::dy,:] = grid_color
        img[::dx,:,:] = grid_color

        # Show the result
        img_buf = io.BytesIO()
        plt.savefig(img_buf, format='png')

        im = Image.open(img_buf)

        # Save the figure    
        buffered = io.BytesIO()
        rgb_im = im.convert('RGB')
        rgb_im.save(buffered, format="JPEG")
        output = base64.b64encode(buffered.getvalue()).decode("utf-8")
        #buffered.close()
    else:
        dy, dx = round(width / 6), round(height / 3)
        print(width, dx, dy, height)

        # Custom (rgb) grid color
        grid_color = [0,0,0]

        # Modify the image to include the grid
        img[:,::dy,:] = grid_color
        img[::dx,:,:] = grid_color
        #print("hi")


        # Set up figure
        fig=plt.figure(figsize=(float(image.size[0])/my_dpi,float(image.size[1])/my_dpi),dpi=my_dpi)
        ax=fig.add_subplot(111)

        # Remove whitespace from around the image
        fig.subplots_adjust(left=0,right=1,bottom=0,top=1)

        # Set the gridding interval: here we use the major tick interval
        myInterval_x= round(height/3)
        myInterval_y = round(width/6)
        loc = plticker.MultipleLocator(base=myInterval_x)
        print(loc)
        ax.xaxis.set_major_locator(loc)
        ax.yaxis.set_major_locator(loc)


        # Add the image
        ax.imshow(img)

        # Find number of gridsquares in x and y direction
        nx=abs(int(float(ax.get_xlim()[1]-ax.get_xlim()[0])/float(myInterval_x)))
        ny=abs(int(float(ax.get_ylim()[1]-ax.get_ylim()[0])/float(myInterval_y)))

        # Add some labels to the gridsquares
        offset = 0
        for j in range(ny + 1):
            y=myInterval_x/2+j*myInterval_x
            offset = offset + 1
            for i in range(nx + 1):
                x=myInterval_y/2.+float(i)*myInterval_y
                ax.text(x,y,'{:d}'.format(i+j*nx + offset),color='w',ha='center',va='center')

        img = numpy.array(image)

        # Grid lines at these intervals (in pixels)
        dy, dx = round(width / 6), round(height / 3)
        print(width, dx, dy, height)

        # Custom (rgb) grid color
        grid_color = [0,0,0]

        # Modify the image to include the grid
        img[:,::dy,:] = grid_color
        img[::dx,:,:] = grid_color
        #print("hi")

        # Show the result
        img_buf = io.BytesIO()
        plt.savefig(img_buf, format='png')

        im = Image.open(img_buf)

        # Save the figure    
        buffered = io.BytesIO()
        rgb_im = im.convert('RGB')
        rgb_im.save(buffered, format="JPEG")
        output = base64.b64encode(buffered.getvalue()).decode("utf-8")
        #buffered.close()
    final_output = "data:image/jpeg;base64," + output
    print(final_output)
    return final_output


def pixel_selection(a, b, c, d, e, f):
    image = Image.open("C:\\Users\\shany\\Documents\\Python Scripts\\Img_encryption\\image 2.jpg")
    my_dpi=100.
    height = image.height
    width = image.width
    coords = []
    delay = 0 
    for i in range(6):
        sleep(delay)
        if i == 0:
            coordinate = a
        elif i == 1:
            coordinate = b
        elif i == 2:
            coordinate = c
        elif i == 3:
            coordinate = d
        elif i == 4:
            coordinate = e
        else:
            coordinate = f
        dx, dy = 0 , 0
        if coordinate == 1: 
            dx, dy = round(30), round(15)
        elif coordinate == 2:
            dx, dy = round((2*width / 3)-15), round((height / 4)-10)
        elif coordinate == 3:
            dx, dy = round((3*width / 3)-35), round((height / 4)-18)
        elif coordinate == 4: 
            dx, dy = round(36), round((2*height / 4)-9)
        elif coordinate == 5:
            dx, dy = round((2*width / 3)-29), round((2*height / 4)-36)
        elif coordinate == 6:
            dx, dy = round((3*width / 3)-54), round((2*height / 4)-24)
        elif coordinate == 7: 
            dx, dy = round(66), round((3*height / 4)-17)
        elif coordinate == 8:
            dx, dy = round((2*width / 3)-21), round((3*height / 4)-16)
        elif coordinate == 9:
            dx, dy = round((3*width / 3)-61), round((3*height / 4)-61)
        elif coordinate == 10: 
            dx, dy = round(23), round((4*height / 4)-17)
        elif coordinate == 11:
            dx, dy = round((2*width / 3)-11), round((4*height / 4)-26)
        elif coordinate == 12:
            dx, dy = round((3*width / 3)-9), round((4*height / 4)-31)
        else:
            print("error")
        #print(coordinate)
        coords.append( (dx,dy) )
    rgb_string = ""
    image = Image.open("C:\\Users\\shany\\Documents\\Python Scripts\\Img_encryption\\image 2.jpg")
    for i in range(6):
        r, g, b = image.getpixel(coords[i])
        rgb_string = rgb_string + str(r) + str(b) + str(g)
    print(rgb_string)