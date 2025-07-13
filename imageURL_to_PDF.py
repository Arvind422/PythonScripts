# This code downloades images from given URL and saves them in Image Folder and then at the end creates a PDF file. 
# python .\image_to_PDF.py --url "https://objectstorage.us-phoenix-1.oraclecloud.com/p/2EKlM64udC0NhxdrIwk9taz6JhgxfXi3Agp2klnFmckU1JF0tuPBfOAkMqBrU86R/n/axy7nrjok4zr/b/BCKMLPHXPROD_AVATAR/o/ekit/private/19fd207f-b7e4-437e-b296-3c8675de09fd/flipbooks/b726983c-c20f-43c0-bc65-4fc11189d08d/D1111080GC10_ag/files/mobile/{ID}.jpg?250306140300" --start 1 --end 76 --output CourseBook.pdf

import os
import argparse
import requests
from PIL import Image
from io import BytesIO

def fetch_and_save_images(url_template, start, end, outdir):
    os.makedirs(outdir, exist_ok=True)
    images = []

    for i in range(start, end + 1):
        url = url_template.replace("{ID}", str(i))
        print(f"Fetching: {url}")
        try:
            response = requests.get(url)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content)).convert("RGB")
            filename = os.path.join(outdir, f"image_{i}.jpg")
            img.save(filename)
            images.append(filename)
        except Exception as e:
            print(f"Failed to fetch {url}: {e}")

    return images

def images_to_pdf(image_files, output_pdf):
    if not image_files:
        print("No images found to compile into PDF.")
        return

    images = [Image.open(img).convert("RGB") for img in image_files]
    images[0].save(output_pdf, save_all=True, append_images=images[1:])
    print(f"PDF saved as: {output_pdf}")

def main():
    parser = argparse.ArgumentParser(description="Fetch images from URL with range substitution and convert to PDF.")
    parser.add_argument("--url", required=True, help="URL with {ID} placeholder (e.g., https://site.com/img?id={ID})")
    parser.add_argument("--start", type=int, required=True, help="Start of range")
    parser.add_argument("--end", type=int, required=True, help="End of range (inclusive)")
    parser.add_argument("--outdir", default="images", help="Directory to save images")
    parser.add_argument("--output", default="output.pdf", help="Filename for output PDF")

    args = parser.parse_args()

    image_files = fetch_and_save_images(args.url, args.start, args.end, args.outdir)
    images_to_pdf(image_files, args.output)

if __name__ == "__main__":
    main()