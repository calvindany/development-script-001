from PIL import Image, ImageDraw, ImageFont

def create_progress_bar(percentage, color, bg_color, width_cm=70, height_cm=0.7, dpi=100, line_width=10, border_radius=100):
    # Convert dimensions from cm to pixels
    width = int(width_cm * dpi / 2.54)  # 1 inch = 2.54 cm
    height = int(height_cm * dpi / 2.54)
    
    # Ensure border_radius is not too large
    border_radius = min(border_radius, height // 2)
    

    # Create a blank image with white background
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)

    # Define the bar colors
    bar_color = color
    background_color = bg_color
    line_color = (255, 255, 255)  # White color

    # Calculate the length of the progress bar
    bar_length = int(width * (percentage / 100))
    
    if bar_length <= 0:
        border_radius = 0
   

    # Helper function to draw a rounded rectangle
    def draw_rounded_rectangle(draw, xy, radius, fill):
        x0, y0, x1, y1 = xy
        draw.rectangle([x0 + radius, y0, x1 - radius, y1], fill=fill)
        draw.rectangle([x0, y0 + radius, x1, y1 - radius], fill=fill)
        draw.ellipse([x0, y0, x0 + 2 * radius, y0 + 2 * radius], fill=fill)
        draw.ellipse([x1 - 2 * radius, y0, x1, y0 + 2 * radius], fill=fill)
        draw.ellipse([x0, y1 - 2 * radius, x0 + 2 * radius, y1], fill=fill)
        draw.ellipse([x1 - 2 * radius, y1 - 2 * radius, x1, y1], fill=fill)

    # Draw the background rounded rectangle
    draw_rounded_rectangle(draw, [0, 0, width, height], border_radius, background_color)

    # Draw the progress bar rounded rectangle
    draw_rounded_rectangle(draw, [0, 0, bar_length, height], border_radius, bar_color)

    # Draw the separating white line in the middle
    middle_x = width // 2
    draw.line([(middle_x, 0), (middle_x, height)], fill=line_color, width=line_width)

    # Add the percentage text
    font = ImageFont.load_default()  # This can be replaced with a TTF font if desired
    text = f'{percentage} %'
    text_bbox = font.getbbox(text)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    text_position = (10, (height - text_height) // 2)  # Text on the left with some padding
    draw.text(text_position, text, fill='black', font=font)

    return img


img  = create_progress_bar(10, color=(21, 111, 27), bg_color=(229, 250, 213), line_width=10, border_radius= 70)

img.show()
img.save('test.jpg')