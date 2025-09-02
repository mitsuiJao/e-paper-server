import re
from PIL import Image
import numpy as np

def xbm2img(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    width = int(re.search(r'#define\s+\w+_width\s+(\d+)', content).group(1))
    height = int(re.search(r'#define\s+\w+_height\s+(\d+)', content).group(1))
    bits_str = re.search(r'\{\s*(.*?)\s*\}', content, re.DOTALL).group(1)
    hex_values = [int(v.strip(), 16) for v in bits_str.split(',') if v.strip()]

    bitmap = np.zeros((height, width), dtype=np.uint8)
    byte_index = 0
    for y in range(height):
        for x in range(width):
            byte = hex_values[byte_index + x // 8]
            bit_position = x % 8
            if (byte >> bit_position) & 1:
                bitmap[y][x] = 255
        byte_index += (width // 8)
    
    return Image.fromarray(bitmap, mode='L')

if __name__ == '__main__':
    img = read_xbm_as_image("img/16/sun.xbm")
    img.save("converted_image.png")