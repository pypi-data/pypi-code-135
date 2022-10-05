class PyNutrition:
    def imc(peso, altura):
        return peso/(altura * altura)

    def litrosAgua(peso):
        return peso * 35

    def qtdCalorias(peso, altura, idade, sexo):

        if sexo == 'm':
            return (66 + (6.2 * peso) + (12.7 * altura)) - (6.76 * idade)

        if sexo == 'f':
            return (655.1 + (4.35 * peso) + (4.7* altura)) - (4.7 * idade)

    def qtdProteina(qtdCalorias):
        return (qtdCalorias * 0.4)/4

    def qtdCarboidratos(qtdCalorias):
        return (qtdCalorias * 0.4)/4

    def qtdGorduras(qtdCalorias):
        return (qtdCalorias * 0.2)/9