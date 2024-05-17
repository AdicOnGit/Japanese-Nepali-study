import genanki
import csv

file_version = "second500"
# Define the CSS styles for the front and back of the card
front_style = """
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  
  #card {
   height: 100vh;
  width: calc(100vw - 2px);  /* Adjusted width to account for potential border */
  background-color: pink;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  }
  
  .sub-div1 {
    height: 40%;
    width: 100%;
    border: 1px solid black;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 10px;
  }
  
  .header {
    height: 50%;
    width: 25%;
    border: 1px solid black;
    background-color: orange;
    font-size: 50px;
    padding: 5px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    box-shadow: 2px 2px black;
  }
  
  .sub-div2 {
    height: 60%;
    width: 100%;
    border: 1px solid black;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: space-evenly;
    padding: 10px;
  }
  
  .common-lvl,
  .jlpt-lvl,
  .vocab-pos {
    height: 25%;
    background-color: slateblue;
    width: 25%;
    padding: 5px;
    display: flex;
    align-items: center;
    font-size: 25px;
    color: beige;
    border: 1px solid black;
    box-shadow: 2px 2px black;
  }
"""

back_style = """
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#card {
  height: 100vh;
  width: 100vw;
  background-color: pink;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.header {
  height: 50%;
  width: 25%;
  background-color: orange;
  font-size: 50px;
  padding: 5px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  box-shadow: 2px 2px black;
}

.main-div1,
.main-div2,
.main-div3 {
  height: 30%;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 10px;
}

.main-div2,
.main-div3 {
  justify-content: space-between;
}

.main-div2-sub-div1,
.main-div2-sub-div2,
.main-div3-sub-div1{
  height: 100%;
  width: 45%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: space-evenly;
  padding: 10px;
}

.kanji,
.vocab-meaning-eng,
.vocab-kana,
.sentence-expression,
.sentence-kana,
.sentence-meaning-eng,
.sentence-meaning-nep{
  height: 25%;
  background-color: black;
  width: 80%;
  padding: 5px;
  display: flex;
  align-items: center;
  font-size: 25px;
  color: beige;
  box-shadow: 2px 2px purple;
}

.common-lvl,
.jlpt-lvl,
.vocab-pos {
  height: 25%;
  background-color: slateblue;
  width: 50%;
  padding: 5px;
  display: flex;
  align-items: center;
  font-size: 25px;
  color: beige;
  box-shadow: 2px 2px black;
}

.main-div3-sub-div1 {
  width: 100%;
}


.sentence-expression,
.sentence-kana,
.sentence-meaning-eng,
.sentence-meaning-nep {
  background-color: #FFF5E0;
  color: #141E46;
  box-shadow: none;
  width: 91%;
}

.vocab-kana{
  height: 35%;
  justify-content: center;
  background: linear-gradient(to right, 
    #FFB3BA, /* Light red */
    #FFDFBA, /* Light orange */
    #FFFFBA, /* Light yellow */
    #BAFFC9, /* Light green */
    #BAE1FF  /* Light blue */
  );   
  color: black;            
  text-shadow: 2px 2px 4px rgba(186, 255, 201, 0.5); 
  font-size: 40px;
  font-weight: bold;
}
.header, .sub-div1, .sub-div2, .main-div1, .main-div2, .main-div3 {
  box-sizing: border-box;  /* Re-emphasizing box-sizing for all components */
}

@media (max-width: 430px) and (max-height: 930px) {
  #card {
    height: 930px;
    width: 100%;
  }

  .header {
    height: 100px;
    width: 100%;
    font-size: 30px;
  }

  .main-div1,
  .main-div2,
  .main-div3 {
    height: 200px;
    border: 1px solid black;
  }

  .main-div3-sub-div1 {
    width: 100%;
  }
  
  .main-div2-sub-div1{
    width: 80%;
    padding: 0%;
  }
  .main-div2-sub-div2{
    padding: 0%;
    width: 19%;
  }

  .kanji,
  .vocab-meaning-eng,
  .vocab-kana,
  .sentence-expression,
  .sentence-kana,
  .sentence-meaning-eng,
  .sentence-meaning-nep {
    font-size: 16px;
    width: 100%;
  }

  .common-lvl,
  .jlpt-lvl,
  .vocab-pos {
    font-size: 16px;
    width: 100%;
  }
}
"""

# Define the template for the front of the card
front_template = """
<div id="card">
<div class="sub-div1">
 <div class="header">{{Nepali-meaning}}</div>
 </div>
 <div class="sub-div2">
 <div class="common-lvl">Common Level: {{Common Level}}</div>
 <div class="jlpt-lvl">JLPT Level: {{JLPT Level}}</div>
 <div class="vocab-pos">{{Vocab-pos}}</div>
 </div>
</div>
"""

# Define the template for the back of the card
back_template = """
<div id="card">
      <div class="main-div1">
        <div class="header">{{Nepali-meaning}}</div>
      </div>
      <div class="main-div2">
        <div class="main-div2-sub-div1">
          <div class="vocab-kana">{{Vocab-kana}}</div>
          <div class="kanji">Kanji: {{Kanji}}</div>
          <div class="vocab-meaning-eng">English: {{Vocab-meaning-eng}}</div>
        </div>
        <div class="main-div2-sub-div2">
          <div class="common-lvl">Common: {{Common Level}}</div>
          <div class="jlpt-lvl">JLPT: {{JLPT Level}}</div>
          <div class="vocab-pos">{{Vocab-pos}}</div>
        </div>
      </div>
      <div class="main-div3">
        <div class="main-div3-sub-div1">
          <div class="sentence-expression">{{Sentence-expression}}</div>
          <div class="sentence-kana">{{Sentence-kana}}</div>
          <div class="sentence-meaning-nep">{{Sentence-meaning-nep}}</div>
        </div>
          <div class="sentence-meaning-eng">{{Sentence-meaning-eng}}</div>
        </div>
      </div>
    </div>
"""

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

# Load the CSV file and create Anki notes
with open(f'versions/{file_version}/Jap-Nep-{file_version}.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
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
                row['Sentence-meaning-nep'],
                row['Sentence-kana'],
                row['Sentence-meaning-eng'],
            ]
        )
        my_deck.add_note(my_note)

# Save the deck to a file
output_path = f'versions/{file_version}/Jap-Nep-{file_version}.apkg'
genanki.Package(my_deck).write_to_file(output_path)
