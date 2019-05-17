#importing the library
import cv2
#image is the numpy array 1 is for coloured image , 0 is for black and white
#printing the shape of numpy array
#print(img.shape)
# Resizing Image
'''resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
    cv2.imshow('face.jpg',resized_image)
    print(resized_image.shape)

    # Window will wait for 2000ns
    cv2.waitKey(2000)
    cv2.destroyAllWindows()'''

# Creating the Face Detection

# Create the cascade classifier

# Haar Cascade is used for detecting the frontal face 
face_cascade = cv2.CascadeClassifier(r'C:\Users\KIIT\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_frontalcatface.xml')
img = cv2.imread(r'D:\programs\python\mface.jpg',1)

# Reading the image as gray scALE image or black and white image
resized = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Search the coordinates of the image , search the face rectangle coordinates

faces = face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5 )

print(faces)

for x,y,w,h in faces:
    #Image Object ,  RGB value of the rectangle output , WIdth of rectangle
    
    img=cv2.rectangle(img ,(x,y),(x+w,y+h),(102,251,0),3)


cv2.imshow("Gray",img)

cv2.waitKey(0)

cv2.destroyAllWindows()
