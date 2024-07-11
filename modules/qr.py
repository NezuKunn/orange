
import qrcode

path = "temp/qr_code.png"

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return img

def qr_code(data):
    qr_img = generate_qr_code(data)
    qr_img.save(path)

async def qr(url):

    qr_code(url)