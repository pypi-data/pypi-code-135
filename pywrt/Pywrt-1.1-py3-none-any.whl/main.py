from Pywrt import Pywrt

a = Pywrt()
path_doc = "/home/samsung/Desktop/arquivo.pdf"


a.translate_document(path_doc, 'espanhol')

#print(a.translate_text('Você constrói o seu próprio futuro todos os dias.', 'francês'))