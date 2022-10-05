import os
import googletrans
from google.cloud import translate_v3beta1 as translate
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "pacote/credencial/GoogleAccountKey.json"

class Pywrt:
    def __init__(self):
        self.project_id = "academic-aloe-363213"
        self.languages = googletrans.LANGUAGES

    def translate_document(self, file_path: str, lang = 'en'):
        
        if lang != 'en':
            input_lang = lang.lower()
            input_lang = self.translate_text(input_lang, lang = 'en')
            flag = False

            for x,y in self.languages.items():
                if input_lang == y:
                    flag = True
                    lang = x

            if flag == False:
                print("Document can not be translated to {}".format(lang))
                exit()

        self.client = translate.TranslationServiceClient()

        self.location = "us-central1"

        self.parent = f"projects/{self.project_id}/locations/{self.location}"

        # Supported file types: https://cloud.google.com/translate/docs/supported-formats
        with open(file_path, "rb") as document:
            document_content = document.read()

        self.document_input_config = {
            "content": document_content,
            "mime_type": "application/pdf",
        }

        self.response = self.client.translate_document(
            request={
                "parent": self.parent,
                "target_language_code": "{}".format(lang),
                "document_input_config": self.document_input_config,
            }
        )

        try:
            os.mkdir('saida')
        except:
            pass

        root_path = os.getcwd() + '/saida'
        string = '/output{}.pdf'.format(' - ' + input_lang)
        final_path = root_path + string
        f = open(final_path, 'wb')
        f.write(self.response.document_translation.byte_stream_outputs[0])
        f.close()
        
        if flag == True:
            print('Done!')


    def translate_text(self, text, lang = 'en'):
        """Translating Text."""
        if lang != 'en':
            input_lang = lang.lower()
            input_lang = self.translate_text(input_lang, lang = 'en')
            flag = False

            for x,y in self.languages.items():
                if input_lang == y:
                    flag = True
                    lang = x

            if flag == False:
                print("Text can not be translated to {}".format(input_lang))
                exit()

        self.client = translate.TranslationServiceClient()

        self.location = "global"

        self.parent = f"projects/{self.project_id}/locations/{self.location}"

        self.response = self.client.translate_text(
            request={
                "parent": self.parent,
                "contents": [text],
                "mime_type": "text/plain",  # mime types: text/plain, text/html
                "source_language_code": "",
                "target_language_code": "{}".format(lang),
            }
        )
        
        return self.response.translations[0].translated_text.lower()