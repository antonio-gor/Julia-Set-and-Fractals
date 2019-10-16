# Packages to be used
from PIL import Image
import time
import sys

def julia(w=1920, h=1080, zoom=1, R=2, cX=-0.7702, cY=0.1442,
          moveX=0.0, moveY=0.0, iterations=255, filename="desc", disp=False):
    '''
    Renders a fractal according to the Julia set. Can display the
    rendered image and/or save it as a png file.
    Args:
        w: image width
        h: image height
        zoom: zoom level
        R: escape radius
        cX: constant along the x axis
        cY: constant along the y axis
        moveX: shift the image along the x axis
        moveY: shift the image along the y axis
        iterations: maximum number of iterations
        filename: default filename is a description of the settings
        disp: display the fractal; default is False
    '''

    # Checking if descriptive filename was selected
    if filename == "desc":
        filename = str(w)+"_"+str(h)+"_"+str(zoom)+"_" \
        +str(cX)+"_"+str(cY)+"_"+str(moveX)+"_"+str(moveY)+"_"+str(iterations)

    # Creating new bitmap in RGB mode
    bitmap = Image.new(mode="RGB", size=(w, h), color="white")

    # Allocating the storage for the image and loading the pixel data
    pix = bitmap.load()

    for x in range(w):
        for y in range(h):
            iter = iterations
            zx = 1.5*(x - w/2)/(0.5*zoom*w) + moveX
            zy = 1.0*(y - h/2)/(0.5*zoom*h) + moveY
            while zx**2 + zy**2 < R**2 and iter > 1:
                zx, zy = zx**2 - zy**2 + cX, 2.0*zx*zy + cY
                iter -= 1

            # Converting byte to RGB (3 bytes)
            pix[x,y] = (iter << 21) + (iter << 10) + iter*8

    # Display the rendered fractal
    if disp:
        bitmap.show()

    # Saving the image
    bitmap.save("img/julia_" + str(filename) + ".png")

def runtype(args):
    ''' Checks for command line args or does a custom run '''
    if args[0] == 'sample':
        julia()
    elif args:
        julia(cX=float(args[0]), cY=float(args[1]), filename=args[2])
    else:
        # Custom function calls
        for i in range(20):
            julia(cX=-0.8702+i/1000, filename=i, disp=False)

def begin():
    ''' Command line args are optional; arg0, arg1, ag2 = cX, cY, filename '''
    start = time.time()
    runtype(sys.argv[1:])
    end = time.time()

    print('Rendered image(s) in ' + str(round(end-start, 4)) + ' seconds' \
            + " / " + str(round((end-start)/60, 4)) + " minutes")

begin()
