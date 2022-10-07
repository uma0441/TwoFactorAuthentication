# Importing library
import qrcode

# Data to encode
data = "person20"
attributes = "two"

# Creating an instance of QRCode class
qr = qrcode.QRCode(version = 1,
				box_size = 10,
				border = 5)

# Adding data to the instance 'qr'
qr.add_data(data)
qr.add_data(attributes)

qr.make(fit = True)
img = qr.make_image(fill_color = 'red',
					back_color = 'white')

img.save('Person20.png')
