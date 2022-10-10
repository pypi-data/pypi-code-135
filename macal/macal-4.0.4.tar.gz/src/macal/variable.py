#
# Product:   Macal
# Author:    Marco Caspers
# Date:      15-09-2022
#

from __future__ import annotations
import copy
import typing
from . import types
from . import token
from . import value_item
from . import exceptions
from . import ast_function_definition


class Variable:
    def __init__(self, tok: token.LexToken, name: str) -> None:
        self.Token: token.LexToken = tok
        self.Name: str = name
        self.Value: value_item.ValueItem = None
        self.isConst: bool = False


    
    def getValue(self) -> typing.Any:
        if self.Value is None: return None
        if self.Value.Type in [types.VariableTypes.String, types.VariableTypes.Int, types.VariableTypes.Float, types.VariableTypes.Bool, types.VariableTypes.Nil, types.VariableTypes.Variable]:
            return self.Value.Value
        if self.Value.Type == types.VariableTypes.Record:
            return self.__MacalRecordToPythonValue(self.Value)
        if self.Value.Type == types.VariableTypes.Array:
            return self.__MacalArrayToPythonValue(self.Value)
        if self.Value.Type == types.VariableTypes.Function:
            return self.__MacalFunctionToPythonValue(self.Value)
        if self.Value.Type == types.VariableTypes.Type:
            return self.__MacalTypeToPythonValue(self.Value)
        raise exceptions.RuntimeError(f"getValue() for type {self.Value.Type} Not implemented.", self.Token.Location, None)



    def getFunction(self) -> ast_function_definition.FunctionDefinition:
        if self.Value.Type == types.VariableTypes.Function:
            return self.Value.Value
        return None
        #raise exceptions.RuntimeError(f"Invalid getFunction() for non function type. ({self.Type})", self.Token.Location, None) # None may be a valid response, or even a required response. I'm banking on it until i run into problems.



    def __MacalRecordToPythonValue(self, val: value_item.ValueItem) -> typing.Any:
        res = {}
        check = [types.VariableTypes.String, types.VariableTypes.Int, types.VariableTypes.Float, types.VariableTypes.Bool, types.VariableTypes.Nil]
        for (k, v) in val.Value.items():
            if v.Type in check:
                res[k] = v.Value
            elif v.Type == types.VariableTypes.Record:
                res[k] = self.__MacalRecordToPythonValue(v)
            elif v.Type == types.VariableTypes.Array:
                res[k] = self.__MacalArrayToPythonValue(v)
            elif v.Type == types.VariableTypes.Function:
                res[k] = self.__MacalFunctionToPythonValue(v)
            elif v.Type == types.VariableTypes.Type:
                res[k] = self.__MacalTypeToPythonValue(v)
            else:
                raise exceptions.RuntimeError(f"getValue() for type {v.Type} Not implemented.", v.Token.Location, None)
        return res



    def __MacalFunctionToPythonValue(self, val: value_item.ValueItem) -> str:
        func = val.Value
        params = ', '.join([f'{arg.Token.Lexeme}' for arg in func.Arguments])
        return f'<Macal function: {func.Name}({params})>'



    def __MacalArrayToPythonValue(self, val: value_item.ValueItem) -> typing.Any:
        res = []
        for v in val.Value:
            if v.Type in [types.VariableTypes.String, types.VariableTypes.Int, types.VariableTypes.Float, types.VariableTypes.Bool, types.VariableTypes.Nil]:
                res.append(v.Value)
            elif v.Type == types.VariableTypes.Record:
                res.append(self.__MacalRecordToPythonValue(v))
            elif v.Type == types.VariableTypes.Array:
                res.append(self.__MacalArrayToPythonValue(v))
            elif v.Type == types.VariableTypes.Function:
                res.append(self.__MacalFunctionToPythonValue(v))
            elif v.Type == types.VariableTypes.Type:
                res.append(self.__MacalTypeToPythonValue(v))
            else:
                raise exceptions.RuntimeError(f"getValue() for type {v.Type} Not implemented.", v.Token.Location, None)
        return res



    def getType(self) -> types.VariableType:
        if self.Value is None: return None
        return self.Value.Type



    def setValue(self, value: typing.Any, type: types.VariableType) -> None:
        if self.Value is None: return
        self.Value = self.Value.setFromPython(self.Token, type, value)
        return
        if self.Value is None: return
        if type in [types.VariableTypes.String, types.VariableTypes.Int, types.VariableTypes.Float, types.VariableTypes.Bool, types.VariableTypes.Nil]:
            self.Value = value_item.ValueItem().set(self.Token, type, value)
        elif type == types.VariableTypes.Record:
            self.Value = self.__PythonToMacalRecordValue(value)
        elif type == types.VariableTypes.Array:
            self.Value = self.__PythonToMacalArrayValue(value)
        elif type == types.VariableTypes.Type:
            self.Value = self.__PythonMacalTypeStrToMacalTypeValue(value)
        else:
            raise exceptions.RuntimeError(f"setValue() for type {type} Not implemented.", None, None)



    def __PythonToMacalRecordValue(self, val: dict) -> value_item.ValueItem:
        res = {}
        for (k, v) in val.items():
            if v is None:
                res[k] = value_item.ValueItem().set(self.Token, types.VariableTypes.Nil, types.VariableTypes.Nil)
            elif isinstance(v, str):
                res[k] = value_item.ValueItem().set(self.Token, types.VariableTypes.String, v)
            elif isinstance(v, int):
                res[k] = value_item.ValueItem().set(self.Token, types.VariableTypes.Int, v)
            elif isinstance(v, float):
                res[k] = value_item.ValueItem().set(self.Token, types.VariableTypes.Float, v)
            elif isinstance(v, bool):
                res[k] = value_item.ValueItem().set(self.Token, types.VariableTypes.Bool, v)
            elif isinstance(v, dict):
                res[k] = self.__PythonToMacalRecordValue(v)
            elif v.Type == types.VariableTypes.Array:
                res[k] = self.__PythonToMacalArrayValue(v)
            elif v.Type == types.VariableTypes.Type:
                self.Value = self.__PythonToMacalTypeValue(v)
            else:
                raise exceptions.RuntimeError(f"setValue() for type {type(v)} Not implemented.", None, None)
        return value_item.ValueItem().set(self.Token, types.VariableTypes.Record, res)



    def __PythonToMacalFunction(self, val: typing.Any):
        #func = val.Value
        #params = ', '.join([f'{arg.Token.Lexeme}' for arg in func.Arguments])
        #return f'<Macal function: {func.Name}({params})>'
        raise exceptions.RuntimeError("Not implemented.", None, None)



    def __PythonToMacalArrayValue(self, val: list) -> value_item.ValueItem:
        res = []
        for v in val:
            if v is None:
                res.append(value_item.ValueItem().set(self.Token, types.VariableTypes.Nil, types.VariableTypes.Nil))
            elif isinstance(v, str):
                res.append(value_item.ValueItem().set(self.Token, types.VariableTypes.String, v))
            elif isinstance(v, int):
                res.append(value_item.ValueItem().set(self.Token, types.VariableTypes.Int, v))
            elif isinstance(v, float):
                res.append(value_item.ValueItem().set(self.Token, types.VariableTypes.Float, v))
            elif isinstance(v, bool):
                res.append(value_item.ValueItem().set(self.Token, types.VariableTypes.Bool, v))
            elif isinstance(v, dict):
                res.append(self.__PythonToMacalRecordValue(v))
            elif v.Type == types.VariableTypes.Array:
                res.append(self.__PythonToMacalArrayValue(v))
            elif v.Type == types.VariableTypes.Type:
                self.Value = self.__PythonToMacalTypeValue(v)
            else:
                raise exceptions.RuntimeError(f"setValue() for type {type(v)} Not implemented.", None, None)
        return value_item.ValueItem().set(self.Token, types.VariableTypes.Array, res)



    def __PythonMacalTypeStrToMacalTypeValue(self, val: str)  -> value_item.ValueItem:
        if val.startswith('<Macal type: '):
            t = val[13:-1]
        else:
            raise exceptions.RuntimeError("Python string does not contain a Macal type.", None, None)
        return value_item.ValueItem().set(self.Token, types.VariableTypes.Type, t)


    def __MacalTypeToPythonValue(self, val: types.VariableTypes.Type) -> str:
        return f'<Macal type: {val.Value}>'


    def __repr__(self) -> str:
        return self.__str__()



    def __str__(self) -> str:
        return f'{self.Name} = {self.Value}'



    def Clone(self):
        return copy.deepcopy(self)