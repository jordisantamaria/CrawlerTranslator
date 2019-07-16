import logging
import translator
import datetime
logging.basicConfig(level=logging.INFO)
import pandas as pd

def _read_vocabulary():
    with open('vocabulary.txt', 'r') as file:
        data = file.read()
    logging.info(data)
    data_array = data.split('\n')
    data_array.remove('')
    logging.info(data_array)
    return data_array

def _get_translate_to_english_links(vocab_array):
    vocabTranslateLinks = ['https://www.wordreference.com/es/en/translation.asp?spen=' + vocab for
                           vocab in vocab_array]
    logging.info(vocabTranslateLinks)
    return vocabTranslateLinks

def _get_translate_to_japanese_links(vocab_array):
    vocabTranslateLinks = ['https://jisho.org/search/' + vocab for
                           vocab in vocab_array]
    logging.info(vocabTranslateLinks)
    return vocabTranslateLinks

if __name__ == '__main__':

    #read vocabulary list
    vocab_array = _read_vocabulary()

    #translate to english
    translate_to_english_links = _get_translate_to_english_links(vocab_array)
    english_words_array = translator.get_english_translations(translate_to_english_links)

    #translate to japanese
    transate_to_japanese_links = _get_translate_to_japanese_links(english_words_array)
    japanese_words_with_furigana_array = translator.get_japanese_translations_and_furigana(transate_to_japanese_links)

    #include spanish meaning
    data = pd.DataFrame(japanese_words_with_furigana_array, columns=['Japones', 'Hiragana'])
    try:
        data['Significado'] = vocab_array
    except:
        print("An error ocurred adding the significate on the array")

    logging.info(data)

    # Save data to csv
    now = datetime.datetime.now().strftime('%Y_%m_%d')
    out_file_name = 'translations_{datetime}.csv'.format(
        datetime=now)
    data.to_csv(out_file_name)
