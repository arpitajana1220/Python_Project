'''
Wonder where to use this?
Here are few examples

1. Generate a QR code with your message inside and attach it with physical gifts
2. Lucky draw game - Generate multiple QR code with random word and one "win" word who ever scans win voila winner found!

Feel free to experiment with ideas 
'''
import pyqrcode
import png

def qrcode():
   
    q=pyqrcode.create("You are a Lovely Person!\nHave a wonderful year!")
    q.png('qrcode.png',scale=6)
    print("Qr Code generated")

if __name__ == "__main__":
    qrcode()


