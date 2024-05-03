import csv
import json

file_version = "first500"
main_core_file = "Core_vocabularies.csv"
new_file = f"versions/{file_version}/Jap-Nep-{file_version}.csv"
raw_text_file = f"versions/{file_version}/Jap-Nep-{file_version}.json"


def process_raw_text(filename):
    with open(filename) as f:
        return json.load(f)


def main():
    nepali_list = process_raw_text(raw_text_file)
    new_list = []

    # Change this to the row number you want to start from (0 for the header row)
    start_row = 1
    # Change this to the row number you want to end at (inclusive)
    end_row = 501

    with open(main_core_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        header = next(csv_reader)  # Skip the header row

        # Create a dictionary from the Nepali list for faster lookup
        nepali_dict = {item["word"]: item["Nep-meaning"]
                       for item in nepali_list}

        # Process each row within the specified range and check for matches
        row_count = 0
        for row in csv_reader:
            row_count += 1
            if start_row <= row_count < end_row:
                # Assuming the word to match is in the third column (index 2)
                word = row[2]
                if word in nepali_dict:
                    # Insert the Nepali meaning before the 6th column (at index 5)
                    row.insert(5, nepali_dict[word])
                    new_list.append(row)

    headers = ["Core-index", "jlpt", "Vocab-expression", "Vocab-kana", "Vocab-meaning",
               "Nep-meaning", "Vocab-pos", "Sentence-expression", "Sentence-kana", "Sentence-meaning"]

    with open(new_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(headers)
        for line in new_list:
            csv_writer.writerow(line)


if __name__ == "__main__":
    main()
