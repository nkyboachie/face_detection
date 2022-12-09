import cv2
from random import randrange


#load a pretrained data face frontals opencv algorithm
trained_face_data= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#choose image to detect faces
#img = cv2.imread('nana.jpg')
#to capture video from webcam
webcam = cv2.VideoCapture(0)

#Iterate forever over frames
while True:
  #read current frame
  succesful_framread, frame =webcam.read()



  #convert to greyscale
  grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  
    
 
  #detect faces
  #multiscale, any scale
  face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
  
  #draw rectangles around faces
  for (x, y, w, h) in face_coordinates: 
    cv2.rectangle(frame,(x,y), (x+w, y+h) , (randrange(128,256),randrange(128,256),randrange(128,256)), 10)

  #show grayscale image
  cv2.imshow('Clever Face Detector', frame)
  #wait for key to be pressed
  key=cv2.waitKey(1)
  #stop if q is pressed
  if key ==81 or key==113:
    break
# release the videocapture request
webcam.release()
cv2.destroyAllWindows()

"""
  #detect faces
  #multiscale, any scale
  face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

#draw rectangles around faces
for (x, y, w, h) in face_coordinates: 
  cv2.rectangle(img,(x,y), (x+w, y+h) , (randrange(128,256),randrange(128,256),randrange(128,256)), 10)



#print(face_coordinates)




#show image with the faces
#wait for key to be pressed
cv2.imshow('Clever Programmer Face Detector', img)
cv2.waitKey()

"""
print("code completed")

