
import pyqrcode
import png

def qrcode():
   
    q=pyqrcode.create("You are a Lovely Person!\nHave a wonderful year!")
    q.png('qrcode.png',scale=6)
    print("Qr Code generated")

if __name__ == "__main__":
    qrcode()


