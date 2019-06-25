import csv

from wiktionaryparser import WiktionaryParser
from .models import Word, Translation, WordDefinition

list_of_words = []
file_name = 'wordslearnt.csv'

def read_csv():
    with open('wordslearnt.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        line_count = 0
        current_index = 0
        for row in csv_reader:
            if line_count != 0:
                if (current_index > 278) and (row[0] not in list_of_words):
                    print(current_index, row[0])
                    fetch_word(row[0])
                list_of_words.append(row[0])
            line_count+=1
            current_index +=1


def fetch_word(word):
    parser = WiktionaryParser()
    each_word = word.lower()
    word_details = parser.fetch(each_word)
    if len(word_details) and len(word_details[0].get('definitions', [])):
        word_details = word_details[0]
        word_definitions = word_details.pop('definitions')
        priority = 0
        pronounciation_details = word_details.pop('pronunciations')

        audio_links = pronounciation_details.get('audio',[])
        pronounciations = pronounciation_details.get('text', [])
        new_word = Word.objects.create(
            word_english = each_word,
            pronounciations = pronounciations,
            audio_links = audio_links
        )
        translations = word_details.pop('translations')
        for each_translation in translations:
            meaning = each_translation.get('meaning')
            for language_code in each_translation.get('available_translations'):
                for each_local_word in each_translation.get('available_translations').get(language_code):
                    Translation.objects.create(
                        english_word = new_word,
                        meaning = meaning,
                        local_word = each_local_word,
                        utf_encoded = each_local_word.encode('utf-8'),
                        language = language_code
                    )

        for each_definition in word_definitions:
            definition_text = each_definition.get('text',[])
            part_of_speech = each_definition.get('partOfSpeech')
            examples = each_definition.get('examples')
            synonyms = []
            for each_related in each_definition.get('relatedWords'):
                if each_related.get('relationshipType','') == 'synonyms':
                    synonyms = each_related.get('words',[])
            new_word_definition = WordDefinition.objects.create(
                english_word = new_word,
                definitions = definition_text,
                priority = priority,
                part_of_speech = part_of_speech,
                examples = examples,
                synonyms = synonyms
            )
            priority += 1
        
        


