import dropbox
import time
import random
import cv2

start_time=time.time()

def take_snapShot():
    number=random.randint(1, 100)
    #initialising cv2
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        #read the frames while camera is on
        ret,frame=videoCaptureObject.read()
        print(ret)
        #cv2.imwrite (is a method used to save an image to any storage device)
        imgName="img"+str(number)+'.png'
        cv2.imwrite(imgName, frame)
        start_time=time.time()

        result=False
    return imgName
    print('snapShot Taken')

    #closes the webcam
    videoCaptureObject.release()
    #closes all the windows that might be opened while cv2 was on
    cv2.destroyAllWindows()

def uploadFile(imgName):
    access_token = 'JlXMijE_9M4AAAAAAAAAAc_6JI1baOvUxsbt5Z-CN71ARu4HQ5qoy-OfwQoWeWtn'

    file_from = imgName
    file_to = '/test/'+(imgName)  

    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print('file uploaded')


def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapShot()
            uploadFile(name)

main()



