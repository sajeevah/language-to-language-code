import csv
import json

code_data = []
error_data = []
with open('language.csv') as languages:
    csv_languages = csv.reader(languages, delimiter=',')
    for language in csv_languages:
        with open('language-codes_csv.csv') as codes: 
            csv_codes = csv.reader(codes, delimiter=',')
            found = 0
            for code in csv_codes:
                if code[1].strip().lower() == language[0].strip().lower():
                    print('found ', language[0])
                    code_data.append(code[0])
                    found = 1
                    break
            if found == 0:
                error_data.append(language[0])
                print('not found ', language[0])

with open('result.json', 'w') as f:
    json.dump(code_data, f)

with open('error.json', 'w') as f:
    json.dump(error_data, f)