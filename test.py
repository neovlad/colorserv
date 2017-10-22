from pafy import new
import cv2
import urllib

def getVideo(url, outfile):
    video = new(url)
    best = video.getbest()
    test = urllib.FancyURLopener()
    test.retrieve(best.url, outfile)


def modifyVideo(file, fileout):
    cap = cv2.VideoCapture(file)
    width = int(cap.get(3))
    height = int(cap.get(4))
    fourcc =cv2.VideoWriter_fourcc('M','J','P','G')
    vout = cv2.VideoWriter(fileout, fourcc, 24, (width, height))
    while(cap.isOpened()):
        ret,frame = cap.read()
        if ret == False:
            break
        b,g,r = cv2.split(frame)
        frame = cv2.merge((g,b,r))
        vout.write(frame)


