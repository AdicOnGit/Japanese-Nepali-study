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

    prompt_text = f'''I will give you a list containing Japanese words along with their English meanings and example Japanese sentences using those words in context. You need to review each one and return the information in the following JSON format:

{{
  "word": "Japanese word",
  "Nep-meaning": "Nepali meaning of the word equivalent to the provided English meaning",
  "sent-Nep": "Translated sentence of the provided Japanese sentence in Nepali",
  "mnemonic": "A short and funny mnemonic in Nepali that helps me remember reading of the Japanese word like in this example: ぎじゅつ: "गिद्द जुत्ता"

कल्पना गर्नुहोस् कि एउटा गिद्दले प्रविधिसँग जोडिएको विशेष कौशलको जुत्ता लगाइरहेको छ। यो दृश्य हास्यास्पद छ र सजिलै सम्झन सकिन्छ।

यसरी, "ぎ" लाई "गिद्द" र "じゅつ" लाई "जुत्ता" सँग जोडेर तपाईं ぎじゅつ (कौशल, प्रविधि) शब्दलाई सजिलै सम्झन सक्नुहुन्छ।",
  "explanation":"Explanation of the word in  JSON format like in this example":
  {{
      "word": "技術",
      "pronunciation": "ぎじゅつ",
      "meanings": [
        {{
          "nepali": "कौशल",
          "english": "skill, technique",
          "details": [
            "कुनै काम वा प्रक्रियामा दक्षता र दक्षताको स्तर।",
            "जस्तै - चित्रकलामा कलाकारको कौशल, नृत्यमा नर्तकको कौशल, लेखनमा लेखकको कौशल आदि।"
          ]
        }},
        {{
          "nepali": "प्रविधि",
          "english": "technology, method",
          "details": [
            "वैज्ञानिक र प्राविधिक ज्ञानको उपयोग गरेर विकास गरिएको विधि वा उपकरण।",
            "जस्तै - कम्प्युटर प्रविधि, सूचना प्रविधि, निर्माण प्रविधि आदि।"
          ]
        }}
      ]
    }}
}}

This is the list:

{list_}'''

    print(prompt_text)


if __name__ == "__main__":
    prompt_text_maker()
