from fpdf import FPDF
from tqdm import tqdm
import argparse

def generate_pdf(prime_number, output_file):
    # Initialize the PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.set_font("Arial", size=12)

    # Define the number of lines and characters per line
    lines_per_page = 69  # Adjust based on your font size and page layout
    characters_per_line = 80  # Adjust based on your font size and page layout
    line_height = 4  # Adjust based on your font size and page layout

    # Calculate the total number of pages needed
    total_characters = len(prime_number)
    characters_per_page = lines_per_page * characters_per_line
    total_pages = (total_characters + characters_per_page - 1) // characters_per_page

    # Split the prime number into chunks and add to the PDF
    start = 0
    with tqdm(total=total_pages * lines_per_page, desc="Generating PDF") as pbar:
        for page in range(total_pages):
            pdf.add_page()
            for line in range(lines_per_page):
                end = start + characters_per_line
                chunk = prime_number[start:end]
                if not chunk:
                    break
                pdf.cell(0, line_height, txt=chunk, ln=True)
                start = end
                pbar.update(1)

    # Save the PDF
    pdf.output(output_file)
    print(f"PDF saved as {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a PDF of a large prime number.")
    parser.add_argument('--testPDF', action='store_true', help="Generate a PDF using a smaller number for testing.")
    args = parser.parse_args()

    if args.testPDF:
        # Use a smaller number for testing
        prime_number = str(2**136279 - 1)
        output_file = "test_prime.pdf"
    else:
        # Use the large prime number
        prime_number = str(2**136279841 - 1)
        output_file = "biggest_prime.pdf"

    generate_pdf(prime_number, output_file)