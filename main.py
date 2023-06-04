import qrcode

img = qrcode.make('https://github.com/RiderMC126') # The site to which the qr code leads
type(img)
img.save('qrcode.png')
