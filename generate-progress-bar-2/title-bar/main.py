from PIL import Image, ImageDraw, ImageFont

# Convert cm to pixels
dpi = 72
width_cm = 18.5
height_cm = 1.4  # Set desired height in cm

width_px = int((width_cm / 2.54) * dpi)
height_px = int((height_cm / 2.54) * dpi)

# Create a new image with a white background
img = Image.new("RGB", (width_px, height_px), color="white")

# Draw object
draw = ImageDraw.Draw(img)

# Define colors
green = (0, 102, 102)
gray = (224, 224, 224)

# Define the proportions
left_width_px = int(width_px * 0.4)  # 40% of the width for the green part
right_width_px = width_px - left_width_px  # Remaining width for the gray part

# Draw the green rectangle on the left
draw.rectangle([0, 0, left_width_px, height_px], fill=green)

# Draw the gray rectangle on the right
draw.rectangle([left_width_px, 0, width_px, height_px], fill=gray)

# Load a font (adjust the path to your font if needed)
try:
    font = ImageFont.truetype("arial.ttf", 12)
except IOError:
    font = ImageFont.load_default()

# Define text and positions
left_text = "DIAGNOSTIC SKILL"
right_text = "117"
left_text_position = (10, int(height_px / 4))  # position of the left text
right_text_position = (left_width_px + 10, int(height_px / 4))  # position of the right text

# Add the text
draw.text(left_text_position, left_text, fill="white", font=font)
draw.text(right_text_position, right_text, fill="black", font=font)

# Save or show the image
img.show()  # To display the image
img.save("diagnostic_skill_image_18_5cm.png")  # To save the image
