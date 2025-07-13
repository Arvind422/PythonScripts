import os
import argparse
import subprocess
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_files, output_path):
    merger = PdfMerger()
    for pdf in pdf_files:
        print(f"Adding: {pdf}")
        merger.append(pdf)
    merger.write(output_path)
    merger.close()
    print(f"✅ Merged PDF saved to: {output_path}")

def compress_pdf_ghostscript(input_pdf, output_pdf, quality="ebook"):
    # Ghostscript compression quality: screen, ebook, printer, prepress
    cmd = [
        "gswin64c",
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        f"-dPDFSETTINGS=/{quality}",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={output_pdf}",
        input_pdf
    ]
    print(f"🔄 Compressing using Ghostscript ({quality})...")
    subprocess.run(cmd, check=True)
    print(f"✅ Compressed PDF saved to: {output_pdf}")

def get_pdf_files_from_folder(folder):
    return sorted([
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.lower().endswith(".pdf")
    ])

def main():
    parser = argparse.ArgumentParser(description="Merge and optionally compress PDFs via CLI.")
    parser.add_argument("--folder", required=True, help="Folder containing PDFs to merge")
    parser.add_argument("--output", default="merged.pdf", help="Filename for merged PDF")
    parser.add_argument("--compress", action="store_true", help="Compress the merged PDF")
    parser.add_argument("--quality", choices=["screen", "ebook", "printer", "prepress"], default="ebook", help="Compression quality (default: ebook)")

    args = parser.parse_args()
    temp_file = "temp_merge.pdf"

    # Ensure old file isn't lingering
    if os.path.exists(temp_file):
        try:
            os.remove(temp_file)
        except PermissionError:
            print("❌ Cannot remove temp_merge.pdf — please close it if open in any viewer.")
            return

    pdf_files = get_pdf_files_from_folder(args.folder)
    if not pdf_files:
        print("❌ No PDF files found in the folder.")
        return

    merge_pdfs(pdf_files, temp_file)

    if args.compress:
        compress_pdf_ghostscript(temp_file, args.output, args.quality)
        os.remove(temp_file)
    else:
        os.rename(temp_file, args.output)

if __name__ == "__main__":
    main()
