import abc
from dataclasses import dataclass
from decimal import Decimal
from enum import Enum
import json
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from pure_protobuf.dataclasses_ import field, message, one_of, part
from pure_protobuf.oneof import OneOf_
import toloka.client as toloka

from .. import base, objects
from ..utils import DecimalEncoder

# We use Protobuf to serialize objects on lzy whiteboards.
# Standard pickle serialization does not fit our needs, because in general case refactorings in library code may lead
# to incorrect objects deserialization for old, already persisted whiteboards.
#
# For each class which will be stored in whiteboards, we define its serialization wrapper. A possible alternative is
# to provide additional metadata (@message class decorator, attributes data, etc.) to source classes, but we fully
# separate serialization logic from pure business-logic classes, because:
# 1) Currently we have issues with `pure-protobuf` dependency in Arcadia contrib.
# 2) Some attributes types, i.e. dicts, are not Protobuf serializable, and we don't want to modify source classes only
#    because of serialization needs.
#
# To serialize classes from inheritance schemes, we use Protobuf one_of.
#
# We also have another case, when client defines his own classes. Such sets of classes are limited (i.e. subclasses of
# Class) and we typically know data of these classes (.value for Class inheritor). But we don't know to which class
# we need to deserialize this data. So we introduce classes registry, and the client have to associate a permanent
# name with each of his self-defined class, so we can later instantiate this concrete class by its name.

TolokaObj = toloka.primitives.base.BaseTolokaObject

T = TypeVar('T', bound=Type[Any], covariant=True)
ClassT = TypeVar('ClassT', bound=Type[base.Class], covariant=True)
TolokaObjT = TypeVar('TolokaObjT', bound=Type[TolokaObj], covariant=True)

# DO NOT CHANGE THIS NAMES!
# They are persisted in lzy whiteboards and must remain the same for correct deserialization.
object_types_registry: Dict[Type[base.Object], str] = {
    base.SbSChoice: 'SbSChoice',
    base.BinaryEvaluation: 'BinaryEvaluation',
    objects.Audio: 'Audio',
    objects.Image: 'Image',
    objects.Text: 'Text',
    objects.Video: 'Video',
}
object_types_registry_reversed = {name: type for type, name in object_types_registry.items()}


def register_object_type(type: Type[base.Object], name: str):
    global object_types_registry, object_types_registry_reversed
    object_types_registry[type] = name
    object_types_registry_reversed[name] = type


class ProtobufSerializer(Generic[T]):
    @staticmethod
    @abc.abstractmethod
    def serialize(obj: T) -> 'ProtobufSerializer':
        ...

    @abc.abstractmethod
    def deserialize(self) -> T:
        ...


@message
@dataclass
class LocalizedStringEntry:
    lang: str = field(1)
    text: str = field(2)


@message
@dataclass
class LocalizedString(ProtobufSerializer[base.LocalizedString]):
    entries: List[LocalizedStringEntry] = field(1)

    @staticmethod
    def serialize(obj: base.LocalizedString) -> 'LocalizedString':
        return LocalizedString(entries=[LocalizedStringEntry(lang, text) for lang, text in obj.lang_to_text.items()])

    def deserialize(self) -> base.LocalizedString:
        return base.LocalizedString(lang_to_text={entry.lang: entry.text for entry in self.entries})


@message
@dataclass
class StrEnumSerializer(ProtobufSerializer[Enum], Generic[ClassT]):
    value: str = field(1)

    @staticmethod
    @abc.abstractmethod
    def enum_cls() -> Type[Enum]:
        ...

    @classmethod
    def serialize(cls, obj: Enum) -> 'StrEnumSerializer':
        return cls(value=obj.value)

    def deserialize(self) -> Enum:
        return self.enum_cls()(self.value)


class TextFormat(StrEnumSerializer[base.TextFormat]):
    @staticmethod
    def enum_cls() -> Type[base.TextFormat]:
        return base.TextFormat


@message
@dataclass
class Title(ProtobufSerializer[base.Title]):
    text: LocalizedString = field(1)
    format: TextFormat = field(2)

    @staticmethod
    def serialize(obj: base.Title) -> 'Title':
        return Title(text=LocalizedString.serialize(obj.text), format=TextFormat.serialize(obj.format))

    def deserialize(self) -> base.Title:
        return base.Title(text=self.text.deserialize(), format=self.format.deserialize())


class SbSChoice(StrEnumSerializer[base.SbSChoice]):
    @staticmethod
    def enum_cls() -> Type[base.SbSChoice]:
        return base.SbSChoice


@message
@dataclass
class BinaryEvaluation(ProtobufSerializer[base.BinaryEvaluation]):
    ok: bool = field(1)

    @staticmethod
    def serialize(obj: base.BinaryEvaluation) -> 'BinaryEvaluation':
        return BinaryEvaluation(obj.ok)

    def deserialize(self) -> base.BinaryEvaluation:
        return base.BinaryEvaluation(self.ok)


@message
@dataclass
class ObjectMeta(ProtobufSerializer[base.ObjectMeta]):
    type: str = field(1)
    name: Optional[str] = field(2)
    title: Optional[Title] = field(3)
    required: bool = field(4)

    @staticmethod
    def serialize(obj: base.ObjectMeta) -> 'ObjectMeta':
        return ObjectMeta(
            type=object_types_registry[obj.type],
            name=obj.name,
            title=Title.serialize(obj.title) if obj.title else None,
            required=obj.required,
        )

    def deserialize(self) -> base.ObjectMeta:
        return base.ObjectMeta(
            type=object_types_registry_reversed[self.type],
            name=self.name,
            title=self.title.deserialize(),
            required=self.required,
        )


# TODO: ClassMeta


@message
@dataclass
class FunctionArgument(ProtobufSerializer[Union[Type[base.Object], base.ObjectMeta]]):
    arg: OneOf_ = one_of(
        type=part(str, 1),
        meta=part(ObjectMeta, 2),
    )

    @staticmethod
    def serialize(obj: Union[Type[base.Object], base.ObjectMeta]) -> 'FunctionArgument':
        arg = FunctionArgument()
        if isinstance(obj, base.ObjectMeta):
            arg.arg.meta = ObjectMeta.serialize(obj)
        else:
            arg.arg.type = object_types_registry[obj]
        return arg

    def deserialize(self) -> Union[Type[base.Object], base.ObjectMeta]:
        which_one = self.arg.which_one_of
        if which_one == 'type':
            return object_types_registry_reversed[self.arg.type]
        else:
            return self.arg.meta.deserialize()


@message
@dataclass
class ClassificationFunction(ProtobufSerializer[base.ClassificationFunction]):
    inputs: List[FunctionArgument] = field(1)
    cls: FunctionArgument = field(2)

    @staticmethod
    def serialize(obj: base.ClassificationFunction) -> 'ClassificationFunction':
        return ClassificationFunction(
            inputs=[FunctionArgument.serialize(input) for input in obj.inputs],
            cls=FunctionArgument.serialize(obj.cls),
        )

    def deserialize(self) -> base.ClassificationFunction:
        return base.ClassificationFunction(
            inputs=tuple(FunctionArgument.deserialize(input) for input in self.inputs),
            cls=FunctionArgument.deserialize(self.cls),
        )


@message
@dataclass
class SbSFunction(ProtobufSerializer[base.SbSFunction]):
    inputs: List[FunctionArgument] = field(1)
    hints: List[FunctionArgument] = field(2)
    choice: FunctionArgument = field(3)

    @staticmethod
    def serialize(obj: base.SbSFunction) -> 'SbSFunction':
        return SbSFunction(
            inputs=[FunctionArgument.serialize(input) for input in obj.inputs],
            hints=[FunctionArgument.serialize(hint) for hint in obj.hints] if obj.hints else [],
            choice=FunctionArgument.serialize(obj.choice),
        )

    def deserialize(self) -> base.SbSFunction:
        return base.SbSFunction(
            inputs=tuple(FunctionArgument.deserialize(input) for input in self.inputs),
            hints=tuple(FunctionArgument.deserialize(hint) for hint in self.hints) if self.hints else None,
            choice=FunctionArgument.deserialize(self.choice),
        )


@message
@dataclass
class AnnotationFunction(ProtobufSerializer[base.AnnotationFunction]):
    inputs: List[FunctionArgument] = field(1)
    outputs: List[FunctionArgument] = field(2)
    evaluation: FunctionArgument = field(3)

    @staticmethod
    def serialize(obj: base.AnnotationFunction) -> 'AnnotationFunction':
        return AnnotationFunction(
            inputs=[FunctionArgument.serialize(input) for input in obj.inputs],
            outputs=[FunctionArgument.serialize(output) for output in obj.outputs],
            evaluation=FunctionArgument.serialize(obj.evaluation),
        )

    def deserialize(self) -> base.AnnotationFunction:
        return base.AnnotationFunction(
            inputs=tuple(FunctionArgument.deserialize(input) for input in self.inputs),
            outputs=tuple(FunctionArgument.deserialize(output) for output in self.outputs),
            evaluation=FunctionArgument.deserialize(self.evaluation),
        )


@message
@dataclass
class TaskFunction(ProtobufSerializer[base.TaskFunction]):
    function: OneOf_ = one_of(
        classification=part(ClassificationFunction, 1),
        sbs=part(SbSFunction, 2),
        annotation=part(AnnotationFunction, 3),
    )

    @staticmethod
    def serialize(obj: base.TaskFunction) -> 'TaskFunction':
        function = TaskFunction()
        if isinstance(obj, base.ClassificationFunction):
            function.function.classification = ClassificationFunction.serialize(obj)
        elif isinstance(obj, base.SbSFunction):
            function.function.sbs = SbSFunction.serialize(obj)
        elif isinstance(obj, base.AnnotationFunction):
            function.function.annotation = AnnotationFunction.serialize(obj)
        else:
            raise ValueError(f'unexpected function {obj}')
        return function

    def deserialize(self) -> base.TaskFunction:
        which_one = self.function.which_one_of
        if which_one == 'classification':
            return self.function.classification.deserialize()
        elif which_one == 'sbs':
            return self.function.sbs.deserialize()
        elif which_one == 'annotation':
            return self.function.annotation.deserialize()
        else:
            raise ValueError(f'unexpected task function one_of {which_one}')


@message
@dataclass
class TaskSpec(ProtobufSerializer[base.TaskSpec]):
    id: str = field(1)
    function: TaskFunction = field(2)
    name: LocalizedString = field(3)
    description: LocalizedString = field(4)
    instruction: LocalizedString = field(5)

    @staticmethod
    def serialize(obj: base.TaskSpec) -> 'TaskSpec':
        return TaskSpec(
            id=obj.id,
            function=TaskFunction.serialize(obj.function),
            name=LocalizedString.serialize(obj.name),
            description=LocalizedString.serialize(obj.description),
            instruction=LocalizedString.serialize(obj.instruction),
        )

    def deserialize(self) -> base.TaskSpec:
        return base.TaskSpec(
            id=self.id,
            function=self.function.deserialize(),
            name=self.name.deserialize(),
            description=self.description.deserialize(),
            instruction=self.instruction.deserialize(),
        )


# TODO: client.Params


@message
@dataclass
class TolokaObject(ProtobufSerializer[TolokaObj], Generic[TolokaObjT]):
    json: str = field(1)

    @classmethod
    def serialize(cls, obj: TolokaObj):
        return cls(json=json.dumps(obj.unstructure(), cls=DecimalEncoder))

    def deserialize(self) -> TolokaObj:
        return self.toloka_cls().structure(json.loads(self.json, parse_float=Decimal))

    @staticmethod
    @abc.abstractmethod
    def toloka_cls() -> Type[TolokaObj]:
        ...


class TolokaPool(TolokaObject[toloka.Pool]):
    @staticmethod
    def toloka_cls() -> Type[TolokaObj]:
        return toloka.Pool
