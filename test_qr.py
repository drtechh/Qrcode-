import qrcode
import os

# تست با لینک سایت دیگر
url = 'https://www.github.com'

folder_name = "generated_qrcodes"
os.makedirs(folder_name, exist_ok=True)
full_path = os.path.join(folder_name, "github_qr.png")

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="lightyellow")
img.save(full_path)
print(f"QR code saved successfully to: {os.path.abspath(full_path)}")
