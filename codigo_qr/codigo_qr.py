import pyqrcode

from pyqrcode import QRCode

url = 'https://youtu.be/rtUpj8DLzgg'
qr = pyqrcode.create(url)

qr.png('data\mi_codigo.png', scale=8)