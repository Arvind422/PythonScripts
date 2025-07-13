import os
from PIL import Image

def images_to_pdf(folder_path, output_pdf):
    # Get all image file paths sorted alphabetically
    image_files = sorted([
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.webp'))
    ])

    if not image_files:
        print("No valid image files found in the folder.")
        return

    # Open and convert all images to RGB
    images = [Image.open(img).convert("RGB") for img in image_files]

    # Save as PDF
    images[0].save(output_pdf, save_all=True, append_images=images[1:])
    print(f"✅ PDF saved successfully as: {output_pdf}")

# --- Example usage ---
folder = "coursePPTimages"               # your folder with images
output = "compiled_output.pdf"  # desired output PDF file

images_to_pdf(folder, output)