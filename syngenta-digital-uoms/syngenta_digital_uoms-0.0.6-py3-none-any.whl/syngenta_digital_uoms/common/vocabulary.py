import pandas as pd


class UnsupportedVocabularyException(Exception):
    pass


class Vocabulary:
    def __init__(self, **kwargs):
        self.__reader = pd
        self.__vocabularies = {
            'adapt',
            # 'ddi',
            # 'unrec20',
            # 'ebiz'
        }
        self.__vocab_type = kwargs.get('vocab_type', 'adapt').lower()
        self.__db = self.__read_vocabulary(self.__vocab_type)

    def __read_vocabulary(self, vocab_type):
        if vocab_type not in self.__vocabularies:
            raise(UnsupportedVocabularyException("Provided vocabulary type is currently unsupported. \n"
                                                 f"Please select from the following: {self.__vocabularies}"))

        return self.__reader.read_excel(f'syngenta_digital_uoms/common/{vocab_type}_uoms.xlsx')

    def get_dimension(self, uom_code):
        return self.__db[self.__db.symbol == uom_code]['dimension'].item()

    def list_dimensions(self):
        return list(self.__db.dimension.unique())

    def list_dimension_uoms(self, dimension):
        return list(self.__db[self.__db.dimension == dimension.upper()].symbol.unique())

    def get_canonical_uom(self, dimension):
        return self.__db[self.__db.dimension == dimension][self.__db.isCanonical]['symbol'].item()

    def get_factor_and_offset(self, uom_code):
        row = self.__db[self.__db.symbol == uom_code]
        return row['factor'].item(), row['offset'].item()

    @property
    def vocab_type(self):
        return self.__vocab_type


if __name__ == '__main__':
    v = Vocabulary()
    print(v.list_dimension_uoms('DISTANCE'))