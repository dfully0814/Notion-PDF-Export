import os
import markdown
from weasyprint import HTML

def convert_md_to_pdf(md_file_path, output_pdf_path):
    # Read the Markdown file
    with open(md_file_path, 'r', encoding='utf-8') as file:
        md_content = file.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content)

    # Convert HTML to PDF
    HTML(string=html_content).write_pdf(output_pdf_path)

# Directory containing markdown files
INPUT_DIRECTORY = ''
OUTPUT_DIRECTORY = ''

# Loop through all files in the directory
for filename in os.listdir(INPUT_DIRECTORY):
    if filename.endswith('.md'):
        file_path = os.path.join(INPUT_DIRECTORY, filename)
        pdf_path = os.path.join(OUTPUT_DIRECTORY, os.path.splitext(filename)[0] + '.pdf')
        convert_md_to_pdf(file_path, pdf_path)
        print(f"Converted {filename} to PDF.")