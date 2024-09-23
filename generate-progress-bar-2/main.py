from PIL import Image, ImageDraw, ImageFont


def create_leadership_progress_bar(value, color, bg_color, under, up, type, width_cm=100, height_cm=4, dpi=100, line_width=10, border_radius=70, num_lines=1, texts=None, font_size=40):
    # Convert dimensions from cm to pixels
    width = int(width_cm * dpi / 2.54)  # 1 inch = 2.54 cm
    height = int(height_cm * dpi / 2.54)
    total_height = height + 250  # Extra height for labels and arrow

    # Create a blank image with a white background
    img = Image.new('RGB', (width, total_height), color='white')
    draw = ImageDraw.Draw(img)

    # Define the bar colors
    bar_color = color
    background_color = bg_color
    line_color = (255, 255, 255)  # White color

    # Scale from under to up
    scale_min = under
    scale_max = up
    
    # Calculate the length of the progress bar based on the given value
    bar_length = max(0, int(width * ((value - scale_min) / (scale_max - scale_min))))

    if type == "ascending":
        if value <= 5:
            border_radius = 40
            bar_length = 80
        elif value > scale_max:
            bar_length = max(0, int(width))
    elif type == "decending":
        if value >= under - 5:
            border_radius = 40
            bar_length = 80
        elif value < scale_max:
            bar_length = max(0, int(width))

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

    # Draw the separating white lines
    spacing = width // (num_lines + 1)

    for i in range(1, num_lines + 1):
        line_x = spacing * i
        draw.line([(line_x, 0), (line_x, height)], fill=line_color, width=line_width)

    # Load the font
    font = ImageFont.truetype("arial.ttf", font_size)

    # Draw the text in each section
    if texts:
        section_width = width // (num_lines + 1)
        for i, text in enumerate(texts):
            text_bbox = draw.textbbox((0, 0), text, font=font)
            text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
            text_position = (i * section_width + (section_width - text_width) // 2, (height - text_height) // 2)
            draw.text(text_position, text, fill='black', font=font)

    # Draw "Low" and "High" labels
    low_text = "Low"
    high_text = "High"
    low_text_position = (0, height + 150)
    high_text_bbox = draw.textbbox((0, 0), high_text, font=font)
    high_text_width = high_text_bbox[2] - high_text_bbox[0]
    high_text_position = (width - high_text_width, height + 150)
    draw.text(low_text_position, low_text, fill=(0, 123, 167), font=font)
    draw.text(high_text_position, high_text, fill=(0, 123, 167), font=font)


    # Determine additional or substraction for arrow location
    arrow_extra_location = -10
    if type == 'ascending':
        if value >= scale_max - 3:
            arrow_extra_location = 80
    elif type == 'decending':
        if(value <= up + 3):
            arrow_extra_location = 80
        
    # Draw the larger Red Arrow and the value below it
    arrow_position = (bar_length - arrow_extra_location, height + 20)
    arrow_points = [
        (arrow_position[0] - 15, arrow_position[1] + 40),  # Bottom-left point
        (arrow_position[0] + 35, arrow_position[1] + 40),  # Bottom-right point
        (arrow_position[0] + 10, arrow_position[1])        # Top point
    ]
    draw.polygon(arrow_points, fill=(165, 42, 42))

    value_text = f"{value}"
    value_text_bbox = draw.textbbox((0, 0), value_text, font=font)
    value_text_width = value_text_bbox[2] - value_text_bbox[0]
    value_text_position = (arrow_position[0] + 10 - value_text_width // 2, arrow_position[1] + 45)
    draw.text(value_text_position, value_text, fill=(165, 42, 42), font=font)

    return img

bg_color = (253, 242, 218, 1)
color = (234, 143, 72, 1)
accendingValue = ['25', '50', '75', '100', '125', '150'] 
decendingValue = ['60', '50', '40', '30', '20', '10']
insert_value = input("Masukkan angka proggres bar: ")
img = create_leadership_progress_bar(int(insert_value), color=color, bg_color=bg_color, under=70, up=10, type="decending",line_width=10, border_radius=70, num_lines=5, texts=decendingValue, font_size=80)
# img = create_leadership_progress_bar(int(insert_value), color=color, bg_color=bg_color, under=0, up=150, type="ascending",line_width=10, border_radius=70, num_lines=5, texts=accendingValue, font_size=80)
img.show()