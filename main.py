import logging
import translator
logging.basicConfig(level=logging.INFO)


def _get_vocabulary():
    with open('vocabulary.txt', 'r') as file:
        data = file.read()
    data_array = data.replace('\n', '').split(', ')
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
    vocab_array = _get_vocabulary()

    #translate to english
    translate_to_english_links = _get_translate_to_english_links(vocab_array)
    english_words_array = translator.get_english_translations(translate_to_english_links)

    #translate to japanese
    transate_to_japanese_links = _get_translate_to_japanese_links(english_words_array)
    japanese_words_with_furigana_array = translator.get_japanese_translations_and_furigana(transate_to_japanese_links)

    #write the list with translations


