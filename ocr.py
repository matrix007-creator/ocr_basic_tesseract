gitimport cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd='C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
#tessdata_dir_config='C:/Program Files (x86)/Tesseract-OCR/tessdata/eng.traineddata'
img=cv2.imread('assets/t1.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#detecting charcters
hImg=img.shape[0]
wImg=img.shape[1]
boxes=pytesseract.image_to_data(img)
for x,b in enumerate(boxes.splitlines()):
    if x!=0:
        b=b.split()

        
        if len(b)==12:
            x,y,w,h=int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),3)
            cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),1)
    
    
#print(pytesseract.image_to_string(img))
cv2.imshow('result',img)

cv2.waitKey(0)