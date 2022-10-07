from sympy.keras.nn.modules.module import Module
from sympy.core.symbol import Symbol
from sympy.concrete.expr_with_limits import Lamda
from sympy.tensor.tensor import TensorUnequal
    
class Embedding(Module):

    def __init__(self, input_dim, output_dim):
        super().__init__()
        self.W = Symbol(real=True, shape=(input_dim, output_dim))
        
    def forward(self, inputs):
        indices, limits = inputs.variables_with_limits()
        return Lamda(self.W[inputs[tuple(indices)]], *limits)
    
        
class MaskedEmbedding(Module):

    def __init__(self, input_dim, output_dim):
        super().__init__()
        self.embedding = Embedding(input_dim, output_dim)
        
    def forward(self, inputs, mask=None):
        output = self.embedding(inputs)
        mask = TensorUnequal(inputs, 0) if mask else None
        return output, mask
        
