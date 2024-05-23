import genanki
import csv
import json
import re

file_version = "second500"

# Read the contents of the files
with open('templates_styles/front_style.css', 'r') as file:
    front_style = file.read()

with open('templates_styles/back_style.css', 'r') as file:
    back_style = file.read()

with open('templates_styles/front_template.html', 'r') as file:
    front_template = file.read()

with open('templates_styles/back_template.html', 'r') as file:
    back_template = file.read()

# Create a new Anki deck model with the specified front and back templates and styles
my_model = genanki.Model(
    1607392319,
    'Japanese Vocabulary Model',
    fields=[
        {'name': 'Common Level'},
        {'name': 'JLPT Level'},
        {'name': 'Kanji'},
        {'name': 'Vocab-pos'},
        {'name': 'Vocab-kana'},
        {'name': 'Vocab-meaning-eng'},
        {'name': 'Nepali-meaning'},
        {'name': 'Sentence-expression'},
        {'name': 'Sentence-kana'},
        {'name': 'Sentence-meaning-eng'},
        {'name': 'Sentence-meaning-nep'},
        {'name': 'Mnemonic'},
        {'name': 'Explanation'}
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': front_template,
            'afmt': back_template,
        },
    ],
    css=front_style + back_style,
)

# Create a new Anki deck
my_deck = genanki.Deck(
    2059400110,
    f'Jap-Nep-{file_version}')


def clean_and_format_json(json_str):
    # Replace single quotes with double quotes
    json_str = json_str.replace("'", '"')
    # Remove trailing commas if any
    json_str = re.sub(r',\s*}', '}', json_str)
    json_str = re.sub(r',\s*]', ']', json_str)
    return json_str


# Load the CSV file and create Anki notes
with open(f'versions/{file_version}/Jap-Nep-{file_version}.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Fix and clean the JSON format for explanation
        explanation_str = clean_and_format_json(row['Explanation'])
        print(f"Cleaned Explanation: {explanation_str}")  # Debugging output
        try:
            # Parse the explanation JSON
            explanation = json.loads(explanation_str)
            explanation_formatted = f"<ul>"
            for meaning in explanation['meanings']:
                explanation_formatted += f"<li><strong>{meaning['nepali']} ({meaning['english']}):</strong><ul>"
                for detail in meaning['details']:
                    explanation_formatted += f"<li>{detail}</li>"
                explanation_formatted += "</ul></li>"
            explanation_formatted += "</ul>"

            # Debugging output to check the formatted explanation
            print(f"Formatted Explanation: {explanation_formatted}")

            my_note = genanki.Note(
                model=my_model,
                fields=[
                    row['Core-index'],
                    row['jlpt'],
                    row['Vocab-expression'],
                    row['Vocab-pos'],
                    row['Vocab-kana'],
                    row['Vocab-meaning-eng'],
                    row['Nep-meaning'],
                    row['Sentence-expression'],
                    row['Sentence-kana'],
                    row['Sentence-meaning-eng'],
                    row['Sentence-meaning-nep'],
                    row['Mnemonic'],
                    explanation_formatted
                ]
            )
            my_deck.add_note(my_note)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON for row {row['Core-index']}: {e}")
        except KeyError as e:
            print(f"Missing key in row {row['Core-index']}: {e}")

# Save the deck to a file
output_path = f'versions/{file_version}/Jap-Nep-{file_version}.apkg'
genanki.Package(my_deck).write_to_file(output_path)
