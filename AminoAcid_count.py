import csv
import os

# Function to process a text document and create a CSV file with protein IDs, sequences, and amino acid counts
def process_text_document(input_file, output_folder, delimiter='>'):
    data = []

    with open(input_file, 'r') as text_file:
        current_id = None
        current_sequence = ''

        for line in text_file:
            line = line.strip()
            if line.startswith(delimiter):
                # Process the previous sequence if any
                if current_id is not None:
                    amino_acid_count = len(current_sequence)
                    data.append([current_id, current_sequence, amino_acid_count])

                # Extract the protein ID
                current_id = line[len(delimiter):]
                current_sequence = ''
            else:
                current_sequence += line

        # Process the last sequence
        if current_id is not None:
            amino_acid_count = len(current_sequence)
            data.append([current_id, current_sequence, amino_acid_count])

    # Get the base name of the input file (excluding extension)
    base_name = os.path.splitext(os.path.basename(input_file))[0]

    # Create the output CSV file path
    output_file = os.path.join(output_folder, f'{base_name}.csv')

    # Write data to the CSV file in the specified output folder
    with open(output_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Protein ID', 'Sequence', 'Amino Acid Count'])
        csv_writer.writerows(data)

def process_all_text_files(input_folder, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # List all text files in the input folder
    text_files = [f for f in os.listdir(input_folder) if f.endswith('.txt')]

    for text_file in text_files:
        input_file = os.path.join(input_folder, text_file)
        process_text_document(input_file, output_folder)

if __name__ == "__main__":
    input_folder = 'input_folder'  # Replace with the path to your input folder
    output_folder = 'output_folder'  # Replace with the path to your output folder
    process_all_text_files(input_folder, output_folder)
