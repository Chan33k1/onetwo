import json
import os
import re
import requests

def createJSONs(input_file_path, output_folder_path):
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    with open(input_file_path, 'r') as f:
        lines = f.readlines()

    headers = lines[0].strip().split(',')
    data_lines = [l.strip().split(',') for l in lines[1:]]

    for i, row in enumerate(data_lines):
        data = {
            'id': row[0],
            'name': row[1],
            'crawl_date': row[2],
            'host': row[3],
            'actors': row[4].split(','),
            'associations': [x.strip() for x in row[5].split(',')],
            'download_locations': [x.strip() for x in row[6].split(',')],
        }
        data['actors'] = ', '.join(data['actors'])
        data['associations'] = ', '.join(data['associations'])
        data['download_locations'] = [re.sub(r'(\/)+(?=[hH][tT][tT][pP][sS]?:)', '', x.replace('\\', '').strip()) for x in data['download_locations']]

        json_str = json.dumps(data, indent=2)
        folder_name = f"{data['id']}_{data['name'].replace(' ', '_')}"

        folder_path = os.path.join(output_folder_path, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        with open(os.path.join(folder_path, f"row_{i+1}.json"), 'w') as f:
            f.write(json_str)