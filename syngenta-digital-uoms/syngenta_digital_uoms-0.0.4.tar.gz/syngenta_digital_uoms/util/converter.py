from syngenta_digital_uoms.common.vocabulary import Vocabulary


class Converter:
    def __init__(self, **kwargs):
        self.__input_vocab = Vocabulary(vocab_type=kwargs.get('input_vocab', 'adapt'))
        self.__output_vocab = Vocabulary(vocab_type=kwargs.get('output_vocab', 'adapt'))
        self.__same_vocab = (self.__input_vocab.vocab_type == self.__output_vocab.vocab_type)

    # Converts the given unit of measure to the respective dimension's canonical
    # unit of measure in the output vocabulary
    def convert_uom(self, input_uom_code):
        dimension = self.__input_vocab.get_dimension(uom_code=input_uom_code)

        return self.__output_vocab.get_canonical_uom(dimension=dimension)

    # If output_uom_code is not provided, we default to the
    # canonical UoM code in the output_vocab
    def convert_value(self, input_uom_code, input_value, output_uom_code, order_of_operation='ADD_FIRST'):
        input_dimension_canonical = self.__input_vocab.get_canonical_uom(self.__input_vocab.get_dimension(input_uom_code))
        is_canonical = (input_uom_code == input_dimension_canonical)

        if not is_canonical:
            input_value = self.__convert_to_canonical(input_uom_code, input_value, order_of_operation)

        output_value = self.__convert_to_destination(output_uom_code, input_value, order_of_operation)
        return output_value

    def __convert_to_canonical(self, input_uom_code, input_value, order_of_operation):
        factor, offset = self.__input_vocab.get_factor_and_offset(uom_code=input_uom_code)

        if order_of_operation == 'ADD_FIRST':
            return (input_value + offset) * factor
        else:
            return (input_value * factor) + offset

    def __convert_to_destination(self, output_uom_code, input_value, order_of_operation):
        factor, offset = self.__output_vocab.get_factor_and_offset(uom_code=output_uom_code)
        if order_of_operation == 'ADD_FIRST':
            return (input_value / factor) - offset
        else:
            return (input_value - offset) / factor
