import os
import numpy as np
from PIL import Image
from imagenet_c import corrupt


SEVERITY=3
CORRUPTION_NAME="gaussian_noise"

# Directories
input_dir = "./data/oxford_pets/images"
output_dir = "./data/oxford_pets_gn/images"
os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist

# Iterate over all images in input_dir
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(input_dir, filename)
        
        # Load image
        image = np.array(Image.open(image_path).convert('RGB'), dtype=np.uint8)
        # Apply corruption
        corrupted_image = corrupt(image, severity=SEVERITY, corruption_name=CORRUPTION_NAME)
        
        # Save corrupted image
        corrupted_image = Image.fromarray(corrupted_image.astype(np.uint8))
        corrupted_image.save(os.path.join(output_dir, filename))
        break

print("Corruption process completed!")
