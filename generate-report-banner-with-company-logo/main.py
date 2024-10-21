from PIL import Image, ImageDraw

# Ukuran A4 dalam piksel (300 DPI)
a4_width, a4_height = 2480, 3508

# Buka gambar background dan logo
background = Image.open("default_banner.png")  # Gambar background
logo = Image.open("logo2.png")  # Gambar logo

# Membuat kanvas berukuran A4 dengan warna putih
a4_canvas = Image.new("RGB", (a4_width, a4_height), "white")

# Mengubah ukuran gambar background agar sesuai dengan lebar kertas A4, menjaga rasio aslinya
background_ratio = a4_width / background.width
new_bg_size = (a4_width, int(background.height * background_ratio))
background = background.resize(new_bg_size, Image.ANTIALIAS)

print(new_bg_size)

background_position = (0, 0)
a4_canvas.paste(background, background_position)

logo_size = (int(logo.width * 3), int(logo.height * 3)) 
logo = logo.resize(logo_size, Image.ANTIALIAS)

logo_position = (100, 100)  # Jarak dari pojok kiri atas

a4_canvas.paste(logo, logo_position, logo)

a4_canvas.save("result_image.png")

a4_canvas.show()

