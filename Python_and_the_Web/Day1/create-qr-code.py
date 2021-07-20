import pyqrcode #pip install pyqrcode 
                #pip install pypng
import sys

# python3 create-qr-code.py msg
print("--- Command Line:", sys.argv)

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} [msg]")
    exit(1)

msg = sys.argv[1]

qrcode = pyqrcode.create(msg)

qrcode.png("QRmsg.png", scale=8)

print("Your QR Code is now created and located in QRmsg.png")