from django import template

register = template.Library()

@register.simple_tag
def contrast_text_color(background_color):
    # Implement logic to determine whether to use white or black text
    # based on the background color for better contrast
    # Example logic: If the background color is light, use black; otherwise, use white.
    return 'black' if is_light_color(background_color) else 'grey'

def is_light_color(hex_color):
    # Example logic: Check if the hex color represents a light color
    # You may need to adjust this logic based on your specific requirements
    if not hex_color or not isinstance(hex_color, str):
        # Handle the case where hex_color is empty or not a string
        return False

    try:
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        brightness = (r * 299 + g * 587 + b * 114) / 1000
        return brightness > 128
    except ValueError:
        # Handle the case where hex_color is not a valid hex color
        return False

