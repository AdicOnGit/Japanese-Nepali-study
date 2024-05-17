import csv


def prompt_text_maker():
    csv_file_name = "Core_vocabularies.csv"

    list_ = []

    with open(csv_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        row_count = 0
        starting_row = 501
        ending_row = 1001
        # skip the header
        next(csv_reader)
        for row in csv_reader:
            row_count += 1
            if starting_row <= row_count < ending_row:
                dic = {
                    "Japanese-word": row[2],
                    "English-meaning": row[4],
                    "Japanese-sentence": row[6]
                }
                list_.append(dic)

    print(f"""I will give you a list containing Japanese words along with their English meanings and example Japanese sentences using those words in context. You need to review each one and return the information in the following JSON format:

{{
  "word": "Japanese word",
  "Nep-meaning": "Nepali meaning of the word equivalent to the provided English meaning",
  "sent-Nep": "Translated sentence of the provided Japanese sentence in Nepali"
}}

This is the list:

{list_}""")


if __name__ == "__main__":
    prompt_text_maker()
