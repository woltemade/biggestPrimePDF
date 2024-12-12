# Prime Number PDF Generator

This project generates a PDF containing a large prime number. The prime number is calculated as `2**136279841 - 1` and is split into multiple pages in the PDF.

## Requirements

- Python 3.x
- `fpdf` library
- `tqdm` library

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/woltemade/biggestPrimePDF.git
   cd biggestPrimePDF
   ```

2. Install the required libraries:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the script to generate the PDF:

```sh
python main.py
```

To generate a PDF using a smaller number for testing purposes, use the --testPDF parameter:

```sh
python main.py --testPDF
```

Explanation
main.py: The main script that generates the PDF.

Without any parameters, it generates a PDF containing the large prime number 2\*\*136279841 - 1 and saves it as biggest_prime.pdf. Take +- 6 hours to generate the PDF.

With the --testPDF parameter, it generates a PDF using a smaller number 2\*\*136279 - 1 and saves it as test_prime.pdf.
requirements.txt: Lists the dependencies required for the project (fpdf and tqdm).

Adjust the hardcoded font size and lines heights etc. in the main.py file to fit your needs. Generate at least 20 pages of a smaller number to test the layout.

The chunk sizes does not always fit perfectly on the pages, so you need to adjust the chunk size to fit the page perfectly. If not, blank spaces will appear between number chunks.

The following variables can be adjusted:

```python
pdf.set_auto_page_break(auto=True, margin=10)
pdf.set_font("Arial", size=12)

# Define the number of lines and characters per line
lines_per_page = 69  # Adjust based on your font size and page layout
characters_per_line = 80  # Adjust based on your font size and page layout
line_height = 4  # Adjust based on your font size and page layout
```

To search for a number sequence within this huge number:

# Define the sequence to search for in search.py

    sequence = "123456789101112"  # Replace with the sequence you want to search for

then use the following command to execute the search:

```sh
python search.py
```

License
This project is licensed under the MIT License. ```
