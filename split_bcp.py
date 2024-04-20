import os
import argparse

DEFAULT_CHUNK_SIZE = 400 * 1024  # 400 KB

def split_text_content(text, chunk_size=DEFAULT_CHUNK_SIZE):
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks

def process_bcp_file(input_file, output_folder):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    chunks = split_text_content(content)
    
    base_filename = os.path.splitext(os.path.basename(input_file))[0]
    for i, chunk in enumerate(chunks):
        output_filename = os.path.join(output_folder, f'{base_filename}_part{i+1}.bcp')
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(chunk)

def main():
    parser = argparse.ArgumentParser(description='Utility for parsing and splitting .bcp files.')
    parser.add_argument('input_folder', type=str, help='Path to the folder containing .bcp input files')
    
    args = parser.parse_args()
    
    output_folder = os.path.join(args.input_folder, 'output')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(args.input_folder):
        if filename.endswith('.bcp'):
            input_file = os.path.join(args.input_folder, filename)
            process_bcp_file(input_file, output_folder)
            print(f'Processed {filename}')

if __name__ == '__main__':
    main()
