import logging
import bs4
import requests
logging.basicConfig(level=logging.INFO)

def get_english_translations(translate_to_english_links):
    englishWordsArray = []
    for link in translate_to_english_links:
        #request page
        response = requests.get(link)
        #filter the translate world on the page
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        translation = soup.select('td.ToWrd')[1]
        translation.em.extract()
        firstWordTranslation = translation.text.split(',')[0]

        englishWordsArray.append(firstWordTranslation)

    logging.info(englishWordsArray)
    return englishWordsArray

def get_japanese_translations_and_furigana(translate_to_japanese_links):
    japaneseWordsArray = []
    for link in translate_to_japanese_links:
        # request page
        response = requests.get(link)
        # filter the translate world on the page
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        wordJapanese = soup.select('div.concept_light-wrapper span.text')[0].text.replace('\n', '').replace(' ', '')
        furigana = soup.select('div.concept_light-wrapper span.furigana span')[0].text
        japaneseWordsArray.append([wordJapanese, furigana])

    logging.info(japaneseWordsArray)
    return japaneseWordsArray
