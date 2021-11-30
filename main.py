
import pyqrcode
import png
from pyqrcode import QRCode
s = "https://www.kaggle.com/"

url = pyqrcode.create(s)

# Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale = 8)

# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale = 6)

