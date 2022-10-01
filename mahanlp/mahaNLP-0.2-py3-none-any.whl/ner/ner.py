from mahaNLP.modelRepo.mahaNER import NERModel

Models = {
    'marathi-ner': 'l3cube-pune/marathi-ner'
}


def listModels():
    modelElements = Models
    print("NER Models: ")
    for i in modelElements:
        print(i, ": ", modelElements[i], "\n")


listModels()
