# Code to track the blob in camera input.
# Heavily based on
# mouse-gestures http://code.google.com/p/mouse-gestures/
# Thanks: Jemshid K.K

import urllib
from opencv.cv import *
from opencv.highgui import *
from blobs.BlobResult import *
from blobs.Blob import *

# set filename.
file_name="shot.jpg"
path="http://192.168.1.44:8080/shot.jpg"

image = urllib.URLopener()

def track():
    # Testing.	
    #image.retrieve(path, filename)
    frame = cvLoadImage(file_name) 
    
    red = red = cvCreateImage (cvGetSize (frame), 8, 1)
    blue = cvCreateImage (cvGetSize (frame), 8, 1)
    green = cvCreateImage (cvGetSize (frame), 8, 1)

    # Extract red chanel.
    cvSplit(frame, blue, green, red, None)
    cvAdd(blue, green, green)
    cvSub(red, green, red)

    ## Perform an OTSU threshold to prepare a binary image.
    cvThreshold(red, red, 20, 255, CV_THRESH_OTSU)
    binary_image = cvCreateMat(red.rows,red.cols,red.type)
    cvThreshold(red, binary_image, 100, 255, CV_THRESH_OTSU)
    #cvNamedWindow("binary") 
    #cvShowImage("binary", binary_image) 
    #c = cvWaitKey(0)
    cvSaveImage("binary_im.jpg", binary_image)

    ## Get the frame size.
    frame_size = cvGetSize (red)
    
    ## Create necessary data structures for holding the blobs and masking the image.
    blob= cvCreateImage(frame_size, 8, 1)
    mask = cvCreateImage (frame_size, 8, 1)
    cvSet(mask, 255)

    ## Extracting the blobs
    myblobs = CBlobResult(binary_image, mask, 0, True)
    myblobs.filter_blobs(100,50000)

    ## Get the numberof blobs
    blob_count = myblobs.GetNumBlobs()

    #  CALCULATING CORDINATES FOR MOVEMENT
    if blob_count==0:
	wx = 0
	print(wx)
	#continue 
    else:
	cvSet(blob, 0)
	temp=[]

    # Finding the position of index finger	
    for i in range(blob_count):	
        my_enum_blob = myblobs.GetBlob(i)
	temp.append(my_enum_blob.maxx)
    for i in range(len(temp)):
	if temp[i]==max(temp):
		my_enum_blob = myblobs.GetBlob(i)
		my_enum_blob.FillBlob(blob,CV_RGB(255,0,255),0,0)
	

    #cvNamedWindow("Blob")
    # commented the next line as a show error is noticed
    #cvShowImage("Blob", blob)   
    #c = cvWaitKey(0)
    #cvSaveImage("blob_im.jpg", blob)

    ## Finding the centroid
    moments=CvMoments()
    cvMoments(blob,moments,1)
    M00 = cvGetSpatialMoment( moments, 0, 0 )
    M10 = cvGetSpatialMoment( moments, 1, 0 )
    M01 = cvGetSpatialMoment( moments, 0, 1 )
    ## Calculating X-cordinate on the window
    wx = int(M10/M00)
    ## Calculating Y-cordinate on the window
    wy = int(M01/M00)

    wx = wx - (frame_size.width / 2)

    return wx,wy


if __name__ == "__main__":
    x,y = track()

    print x,y
    
