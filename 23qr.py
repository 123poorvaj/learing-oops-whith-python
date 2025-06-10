import qrcode

# Replace this URL with the actual link to your uploaded image
image_url = ("E:/qrcode.py")

# Create a QR Code object
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data(image_url)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill="black", back_color="white")

# Save the QR code image
img.save("image_qr_code.png")
