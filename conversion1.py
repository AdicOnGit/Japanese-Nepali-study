import csv
import json

file_version = "second500"
main_core_file = "Core_vocabularies.csv"
new_file = f"versions/{file_version}/Jap-Nep-{file_version}.csv"
raw_json_file = f"versions/{file_version}/Jap-Nep-{file_version}.json"


def process_raw_text(filename):
    with open(filename) as f:
        return json.load(f)


def main():
    nepali_list = process_raw_text(raw_json_file)
    new_list = []

    # Change this to the row number you want to start from (0 for the header row)
    start_row = 501
    # Change this to the row number you want to end at (inclusive)
    end_row = 1001

    with open(main_core_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        header = next(csv_reader)  # Skip the header row

        # Create a dictionary from the Nepali list for faster lookup
        nepali_dict = {item["word"]: {"Nep-meaning": item["Nep-meaning"],
                                      "sent-Nep": item["sent-Nep"]} for item in nepali_list}

        # Process each row within the specified range and check for matches
        row_count = 0
        for row in csv_reader:
            row_count += 1
            if start_row <= row_count < end_row:
                # Assuming the word to match is in the third column (index 2)
                word = row[2]
                if word in nepali_dict:
                    # Insert the Nepali meaning and sentence before the 6th and 10th columns respectively
                    row.insert(5, nepali_dict[word]["Nep-meaning"])
                    row.insert(8, nepali_dict[word]["sent-Nep"])
                    new_list.append(row)

    headers = ["Core-index", "jlpt", "Vocab-expression", "Vocab-kana", "Vocab-meaning-eng",
               "Nep-meaning", "Vocab-pos", "Sentence-expression", "Sentence-meaning-nep", "Sentence-kana", "Sentence-meaning-eng"]

    with open(new_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(headers)
        for line in new_list:
            csv_writer.writerow(line)


if __name__ == "__main__":
    main()
