from translate import Translator


def traduzir(text, de, para):
    

    try:
        translator= Translator(to_lang=para, from_lang=de)
        
        translation = translator.translate(text)
        return translation
    except:
        return False