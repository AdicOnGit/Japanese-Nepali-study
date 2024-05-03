<img src="https://github.com/AdicOnGit/Japanese-Nepali-study/assets/137413419/987b89f2-c71b-49b5-b1c0-8d0c9c615f1c" width="500" height="500">
# Japanese-Nepali Anki Deck Generator

This application consists of two main scripts that aid in generating Anki flashcard decks to help learners study Japanese vocabulary with Nepali translations.

## Scripts

### `anki_deck_maker.py`

This script creates an Anki deck from a CSV file containing Japanese vocabulary, their Nepali meanings, and additional details about usage and proficiency levels. The deck is styled and formatted to enhance learning.

#### Features

- Generates a custom-styled Anki deck.
- Reads data from a CSV file and processes it into flashcards.
- Outputs a `.apkg` file that can be imported directly into Anki.

### `conversion1.py`

This script converts raw JSON data containing vocabulary and their translations into a CSV format that can be processed by `anki_deck_maker.py`.

#### Features

- Parses JSON data to extract vocabulary and their Nepali meanings.
- Matches vocabulary with an existing CSV file of core Japanese words to add translations.
- Outputs a new CSV file ready for deck creation.

## Installation

To run these scripts, you need Python installed on your machine along with the following packages:

- `genanki`
- `csv`
- `json`

You can install the necessary package using pip:

```bash
pip install genanki
```

## Usage

### Preparing the Data

Before generating the Anki deck, ensure you have the correct JSON and CSV files in place as described in the scripts.

1. Place your core vocabulary CSV file and the translation JSON file in the appropriate `versions` directory.
2. Adjust `file_version` in each script to match your data files' naming convention.

### Running the Scripts

Execute `conversion1.py` first to prepare the CSV file:

```bash
python conversion1.py
```

After the CSV file is ready, run `anki_deck_maker.py` to create the Anki deck:

```bash
python anki_deck_maker.py
```

The generated `.apkg` file will be located in the `versions/{file_version}` directory, ready to be imported into Anki.
