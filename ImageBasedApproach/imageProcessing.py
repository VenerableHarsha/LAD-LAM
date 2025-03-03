import os
import cv2
import numpy as np

# Directory where images are saved
image_dir = "downloaded_images"
output_collage = "collage.jpg"

# Resize settings
resize_width, resize_height = 300, 300  # Adjust as needed
grid_size = (3, 3)  # Change for different layouts

# Load and resize images
image_files = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith((".jpg", ".png"))]

resized_images = []
for img_path in image_files:
    img = cv2.imread(img_path)  # Read the image
    if img is None:
        print(f"Skipping empty or unreadable file: {img_path}")
        continue  # Skip empty images

    img = cv2.resize(img, (resize_width, resize_height))  # Resize
    resized_images.append(img)

# Check if we have enough images for the collage
num_images_needed = grid_size[0] * grid_size[1]
if len(resized_images) < num_images_needed:
    print(f"Not enough valid images! Only {len(resized_images)} found, but {num_images_needed} needed.")
    num_images_needed = len(resized_images)  # Adjust grid size dynamically

# Create a blank canvas for the collage
collage_width = grid_size[1] * resize_width
collage_height = grid_size[0] * resize_height
collage = np.zeros((collage_height, collage_width, 3), dtype=np.uint8)

# Place images on the canvas
for idx, img in enumerate(resized_images[:num_images_needed]):
    row = idx // grid_size[1]
    col = idx % grid_size[1]
    y_offset = row * resize_height
    x_offset = col * resize_width
    collage[y_offset:y_offset + resize_height, x_offset:x_offset + resize_width] = img

# Save the collage
cv2.imwrite(output_collage, collage)
print(f"Collage saved as {output_collage}")