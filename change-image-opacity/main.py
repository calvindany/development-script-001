from PIL import Image

def change_opacity(image_path, output_path, opacity):
    # Open the image
    img = Image.open(image_path).convert("RGBA")  # Ensure it's RGBA for transparency support
    
    # Extract the alpha channel and adjust it
    r, g, b, a = img.split()
    
    # Apply the opacity factor (opacity is a value between 0 and 1)
    a = a.point(lambda p: int(p * opacity))
    
    # Merge the new alpha channel back with the image
    img = Image.merge('RGBA', (r, g, b, a))
    
    # Save the modified image
    img.save(output_path, format="PNG")

# Example usage
change_opacity("image.jpg", "output_image.png", 0.6)  # Set 50% opacity
