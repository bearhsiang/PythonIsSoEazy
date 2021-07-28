import cv2
from pyzbar import pyzbar

def read_barcode(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        #1
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        
        #2
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)

    return frame


cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    
    frame = read_barcode(frame)
    cv2.imshow('Barcode/QR code reader', frame)
    
    k = cv2.waitKey(1)
    if k == ord(' '):
        break

cap.release()
cv2.destroyAllWindows()
