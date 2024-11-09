import qrcode
from PIL import Image

maps_url = "Link de lo que necesitas"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data(maps_url)
qr.make(fit=True)

qr_img = qr.make_image(fill="black", back_color="white")

logo = Image.open("python_logo.png")
logo = logo.resize((60, 60))

qr_width, qr_height = qr_img.size
logo_position = ((qr_width - logo.size[0]) // 2, (qr_height - logo.size[1]) // 2)

qr_img.paste(logo, logo_position, mask=logo)

qr_img.save("Codigo QR.png")
print("Código QR generado y guardado como 'Codigo QR.png'")




