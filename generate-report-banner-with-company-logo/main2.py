from PIL import Image, ImageDraw

def hex_to_rgb(hex_color):
    """Mengonversi warna hex ke RGB."""
    hex_color = hex_color.lstrip('#')  # Menghapus karakter '#' jika ada
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_custom_banner_with_logo(background, logo, hex_color):
    # Ukuran A4 dalam piksel (300 DPI)
    a4_width, a4_height = 2480, 3508
    
    # Membuat kanvas berukuran A4 dengan warna putih
    a4_canvas = Image.new("RGB", (a4_width, a4_height), "white")
    
    if(background == None):
        custom_box_width, custom_box_height = 2480, 1579  # Ukuran kotak kustom
        # Warna kustom dalam format hex
        custom_color = hex_to_rgb(hex_color)  # Mengonversi ke RGB
        draw = ImageDraw.Draw(a4_canvas)
        draw.rectangle([0, 0, custom_box_width, custom_box_height], fill=custom_color)
    else:
        # Mengubah ukuran gambar background agar sesuai dengan lebar kertas A4, menjaga rasio aslinya
        background_ratio = a4_width / background.width
        new_bg_size = (a4_width, int(background.height * background_ratio))
        background = background.resize(new_bg_size, Image.ANTIALIAS)
        
        background_position = (0, 0)
        a4_canvas.paste(background, background_position)


    #background = Image.open("default_banner.png")  # Gambar background
    #logo = Image.open("logo2.png")  # Gambar logo

    logo_size = (int(logo.width * 3), int(logo.height * 3)) 
    logo = logo.resize(logo_size, Image.ANTIALIAS)

    logo_position = (100, 100)  # Jarak dari pojok kiri atas

    a4_canvas.paste(logo, logo_position, logo)

    return a4_canvas

logo = Image.open("logo2.png")
background = Image.open("default_banner.png")
a4_canvas = create_custom_banner_with_logo(background,logo , None)

a4_canvas.save("result_imagev2.png")
