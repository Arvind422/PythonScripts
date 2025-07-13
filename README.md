# PythonScripts
This Repo comprises of various python code snippet's which can help in easing our small day-to-day activities 

### imageURL_to_PDF.py

This code downloades images from given URL and saves them in Image Folder and then at the end creates a PDF file. 

CMD command sample : python .\image_to_PDF.py --url "https://imagefiles/{ID}.jpg?2025123" --start 1 --end 5 --output sampleOutput.pdf

### images_to_PDF.py

This code converts the images in the Image Folder and creates a PDF file. 

CMD command sample : python .\images_to_PDF.py

### MergePDFwithCompression

Step 1: Requirements
    Install the required libraries:
          pip install PyPDF2

    Install Ghostscript (for PDF compression):
        Windows: https://ghostscript.com/download/gsdnld.html
        Linux/macOS: Use your package manager (sudo apt install ghostscript or brew install ghostscript)

NOTE : Make sure gs (Ghostscript) is available in your system path.

Step 3: Run from Command Line
    python pdf_merge_compress.py --folder pdfs --output final.pdf --compress --quality ebook

Options:

--folder: Directory with PDFs to merge.
--output: Final merged file name.
--compress: Enable compression using Ghostscript.
--quality: Compression level:
          screen – lowest quality (smallest size)
          ebook – medium (good for reading)
          printer – high quality
          prepress – very high quality

