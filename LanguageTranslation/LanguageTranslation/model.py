'''
Created on 19-Dec-2018

@author: Vishnu
'''

from textblob import TextBlob

langs = {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 
         'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 
         'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 
         'ceb': 'cebuano', 'zh-CN': 'cantonese', 'zh-TW': 'mandarin', 'co': 'corsican', 
         'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 
         'eo': 'esperanto', 'et': 'estonian', 'fi': 'finnish', 'fr': 'french', 'fy': 'Frisian', 
         'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 
         'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'hi': 'hindi', 'hmn': 'hmong', 
         'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 
         'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 
         'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'lao', 
         'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 
         'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 
         'my': 'burmese', 'ne': 'nepali', 'no': 'norwegian', 'ny': 'nyanja', 'ps': 'pashto', 'fa': 'persian', 
         'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'Samoan', 
         'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 
         'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 
         'sv': 'swedish', 'tl': 'filipino', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 
         'uk': 'ukrainian', 'ur': 'urdu', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 
         'yo': 'yoruba', 'zu': 'zulu'}

def Translation(text, language):
    language = language.lower()
    try:
        language = dict((v,k) for k, v in langs.items())[str(language)]
    except:
        translation = "Please check the spelling of language entered."
    text = text.lower()
    txt = TextBlob(text)
    lan = txt.detect_language()
    if str(lan) != str(language):
        try:
            translation = str(txt.translate(to=str(language)))
        except:
            translation = "The input can't be translated."
    else:
        translation = "Please input another language."
    result = {}
    result['result'] = translation
    result['success'] = True
    return result
