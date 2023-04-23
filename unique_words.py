import regex as re
import csv
from translate import Translator
# Read the Quranic text file
with open('quran-simple-plain.txt', 'r', encoding='utf-8') as file:
    quranic_text = file.read()

# Extract unique Arabic words using regular expression
#arabic_words = re.findall(r'\p{Arabic}+', quranic_text, re.UNICODE)

# Remove duplicates and convert to set for uniqueness
#unique_arabic_words = set(quranic_text)
unique_arabic_words = quranic_text.split(' ')
# Create a list to store the CSV rows
unique_arabic_words = set(unique_arabic_words)
csv_rows = []

def fetch_english_meaning(arabic_word):
    try:
        # Translate Arabic word to English
        translator = Translator(to_lang='en', from_lang='ar')
        english_meaning = translator.translate(arabic_word)
        return english_meaning
    except Exception as e:
        print(f"Error fetching English meaning for '{arabic_word}': {str(e)}")
        return None
    
# Loop through the unique Arabic words and add to the CSV rows
for arabic_word in unique_arabic_words:
    # Fetch English meaning of Arabic word from source or API
    english_meaning = "sample"#fetch_english_meaning(arabic_word)  # Replace with actual implementation

    # Append the Arabic word and its English meaning to the CSV rows
    csv_rows.append([arabic_word, english_meaning])

# Write the CSV rows to a CSV file
with open('quranic_words.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['arabic_text', 'english_text']
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)
    writer.writerows(csv_rows)

