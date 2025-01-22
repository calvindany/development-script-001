import csv
import re

def clean_csv(input_file, output_file):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile, delimiter=',')  # Use ',' as separator
        cleaned_data = []

        for row in reader:
            cleaned_row = [re.sub(r'[\t\x00-\x1F]', ' ', cell.replace('；', ';').strip()) for cell in row]  # Remove control characters and replace special semicolons
            cleaned_row = [f'"{cell}"' if cell.isdigit() and cell.startswith('0') else cell for cell in cleaned_row]  # Wrap leading zeros in quotes

            cleaned_data.append(cleaned_row)

    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile, delimiter=',')  # Write using ',' as separator
        writer.writerows(cleaned_data)

    print(f"Cleaned CSV saved to: {output_file}")

# Example usage
input_csv = "assets/A_Code.csv"  # Replace with your input file
output_csv = "assets/a_cleaned_output.csv"  # Replace with desired output file name
clean_csv(input_csv, output_csv)
