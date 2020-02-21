import cv2
img_path = 'D:\\MachineLearning\\fake_ai_faces.0.png'
casc_path = 'D:\\MachineLearning\\opencv-master\\opencv-master\\data\\haarcascades\\haarcascade_frontalface_default.xml'

#https://docs.opencv.org/2.4/modules/objdetect/doc/cascade_classification.html
faceCas = cv2.CascadeClassifier(casc_path)
pic =  cv2.imread(img_path)
bw =  cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY) #Opencv operates more in grayscale
# Detect faces in the image
faces = faceCas.detectMultiScale(
    bw, #Provide the grayscale image as input
    scaleFactor=1.8, #This compensates the zoom factor in the picture
    minNeighbors=4, #Number of objects detected  near the current one before it is identified as face
    minSize=(30, 30) #Size of each window
    )
for (a,b,c,d) in faces :
    cv2.rectangle(pic,(a,b), (a+c,b+d), (0,255,0),2)
print(len(faces))
cv2.imshow("Faces found", pic)
cv2.waitKey(0)