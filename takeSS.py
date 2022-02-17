
import cv2
import dropbox
import time
import random

startTime=time.time()
def takeSS():
    no=random.randint(0,100)
    VideoCaptureObj=cv2.VideoCapture(0)
    result=True

    while(result):
      ret,frame=VideoCaptureObj.read()
      imageName='img'+str(no)+'.png'
      cv2.imwrite(imageName,frame)
      result=False
    
    return imageName
    print('Image captured')
    VideoCaptureObj.release()
    cv2.destroyAllWindows()

def UploadFiles(imageName):
    acessToken='LCmSViI6eP4AAAAAAAAAAdYviwwZUxA2WM72JWeXFN-oxHj0tlrYtPtiJCeo2ntA'
    file=imageName
    fileFrom=file
    fileTo='/myPictures/'+imageName
    dbx=dropbox.Dropbox(acessToken)

    with open(fileFrom,'rb') as f:
      dbx.files_upload(f.read(),fileTo,mode=dropbox.files.WriteMode.overwrite)
      print("files have been uploaded")

def main():
  while (True):
    if((time.time()-startTime)>=0):
      name=takeSS()
      UploadFiles(name)

main()




    