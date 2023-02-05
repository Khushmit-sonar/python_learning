import qrcode
import image

data = input("past the link of any your social media to make qr code")

qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5
)




qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill ="black",back_color="white")
img.save("test.png")