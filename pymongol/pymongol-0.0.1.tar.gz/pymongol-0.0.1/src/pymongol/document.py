import inflect
import re

import pymongo.collection
from bson import ObjectId
from pymongo.database import Database
from pymongo.errors import OperationFailure

p = inflect.engine()


class Cursor(pymongo.cursor.Cursor):

    def next(self):
        item = super().next()
        model = getattr(self.collection, 'model', dict)
        return model(item)

    __next__ = next


class Collection(pymongo.collection.Collection):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.model = None

    def set_model(self, model):
        self.model = model

    def __bool__(self):
        return True

    def find(self, *args, **kwargs):
        return Cursor(self, *args, **kwargs)


class BaseDocument(type):
    DEFAULT_DATABASE: Database = None

    def __new__(mcs, name, parent, *args, **kwargs):
        new_class = super().__new__(mcs, name, parent, *args, **kwargs)
        if parent[0] == Doc:
            return new_class

        meta = getattr(new_class, "Meta", None)

        schema = {}

        for field_name in dir(new_class):
            field = getattr(new_class, field_name)
            if isinstance(field, Field):
                if field.virtual and False:
                    delattr(new_class, field_name)
                if field.get_name():
                    if hasattr(new_class, field_name) and False:
                        delattr(new_class, field_name)
                else:
                    field.set_name(field_name)
                schema[field.get_name()] = field

        projection = {
            k: v.projection()
            for k, v in schema.items()
        }

        collection_name = getattr(meta, 'collection', p.plural(re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()))
        database: Database = getattr(meta, 'database', mcs.DEFAULT_DATABASE)
        if not isinstance(database, Database):
            raise Exception('Invalid pymongo database!')
        collection = database.get_collection(collection_name)
        collection.__class__ = Collection
        collection.set_model(new_class)

        setattr(new_class, "collection", collection)
        setattr(new_class, "schema", schema)
        setattr(new_class, 'projection', projection)

        indexes = getattr(meta, 'indexes', [])
        if len(indexes):
            for index in indexes:
                try:
                    collection.create_indexes([index])
                except OperationFailure as e:
                    if e.code == 86:
                        collection.drop_index(index.document['name'])
                        collection.create_indexes([index])
                    else:
                        raise e

        return new_class

    @classmethod
    def set_default_database(mcs, database: Database):
        mcs.DEFAULT_DATABASE = database


class Field:

    def __init__(self, project: bool = True, children: [dict | list] = None, default=None, name=None, virtual=False) -> None:
        self.project = project
        self._default = default
        self._children = []
        self._path = ''
        self._name = None
        self.virtual = virtual
        self.set_name(name)
        self._set_children(children)
        for c in self._children:
            setattr(self, c.get_name(), c)

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value
        if value:
            _path = self._path.rsplit('.', 1)[0] if self._path else ''
            self.set_path(f'{_path}.{value}' if _path else value)

    def get_path(self, dollar: bool = False, parts: int = 0):
        path = self._path
        if parts > 0:
            path = '.'.join(path.split('.')[:parts])
        elif parts < 0:
            path = '.'.join(path.split('.')[parts:])
        return ('$' if dollar else '') + path

    def set_path(self, value):
        self._path = value
        for c in self._children:
            c.set_path(f'{value}.{c.get_name()}')

    def _set_children(self, value):
        value = value or []
        if isinstance(value, dict):
            for child_name, child in value.items():
                if not isinstance(child, Field):
                    raise Exception('All children must be instance of Field')
                child.set_name(child_name)
            value = list(value.values())

        if isinstance(value, list):
            if not all(isinstance(c, Field) for c in value):
                raise Exception('All children must be instance of Field')

            nonamed_children = [c for c in value if not c.get_name()]
            if len(nonamed_children):
                raise Exception('Some fields have no name')
            children_names = [c.get_name() for c in value]
            if len(children_names) != len(set(children_names)):
                raise Exception('Multiple filed with the same name')
        else:
            raise Exception('Invalid value for property "children"')

        for c in value:
            c.set_path(self._path + c.get_name())
        self._children = value

    def default(self):
        if callable(self._default):
            result = self._default()
        elif self._children:
            result = {
                c.get_name(): c.default()
                for c in self._children
            }
        else:
            result = self._default

        if isinstance(result, dict) and not isinstance(result, Document):
            result = Doc(result)
        return result

    def projection(self):
        if not self.project:
            return False
        if len(self._children) == 0:
            return True
        return {
            c.get_name(): c.projection()
            for c in self._children
        }


class ListField(Field):

    def __init__(self, project: bool = True, children: [dict | list] = None, name=None,
                 virtual=False) -> None:
        super().__init__(project=project, children=children, default=list, name=name, virtual=virtual)


class Doc(object):
    def __init__(self, attributes) -> None:
        for k, v in attributes.items():
            self.__setattr__(k, v)

    def __setattr__(self, key, value):
        # TODO: support list of list of Doc
        if key != '_raw':
            if isinstance(value, dict):
                value = Doc(value)
            elif isinstance(value, list):
                value = [
                    Doc(x) if isinstance(x, dict) else x
                    for x in value
                ]
        super().__setattr__(key, value)

    def to_dict(self, projection: dict | bool = None):
        # TODO: support list of list of Doc
        if projection is None:
            projection = True
        result = {}
        for k, v in self.__dict__.items():
            if k != '_raw' and not isinstance(v, Field):
                proj = projection.get(k) if isinstance(projection, dict) else bool(projection)
                if proj:
                    if isinstance(v, Doc) and not isinstance(v, Document):
                        v = v.to_dict(proj)
                    elif isinstance(v, list):
                        v = [
                            x.to_dict(proj) if isinstance(x, Doc) and not isinstance(x, Document) else x
                            for x in v
                        ]
                    result[k] = v
        return result


class Document(Doc, metaclass=BaseDocument):

    collection: Collection

    def __init__(self, *arg, **kwargs) -> None:
        attributes = arg[0] if len(arg) > 0 and isinstance(arg[0], dict) else dict(kwargs)
        self.clear()
        self._raw = attributes
        super().__init__(attributes)

    def clear(self):
        self.__dict__.clear()
        for k, v in self.schema.items():
            if not v.virtual:
                setattr(self, k, v.default())

    _virtual_id = Field(virtual=True, name='id')
    _id = Field(project=False)

    @property
    def id(self):
        _id = getattr(self, '_id', None)
        if isinstance(_id, Field):
            return None
        return _id

    def save(self, update: dict = None):
        _id = getattr(self, '_id')
        if isinstance(_id, ObjectId):
            update = update or {'$set': self.to_dict()}
            self.collection.update_one(dict(_id=_id), update)
        else:
            doc = self.to_dict()
            doc.pop('_id', None)
            _id = self.collection.insert_one(doc).inserted_id
        new = self.collection.find_one(dict(_id=_id))
        self.__init__(new.to_dict())
        return self

    def project(self, projection: dict = None, *arg, **kwargs):
        if projection is None:
            projection = self.projection

        if isinstance(projection, bool):
            return self.to_dict() if projection else None
        elif isinstance(projection, dict):
            result = {}
            for k, proj in projection.items():
                if proj and hasattr(self, k):
                    v = getattr(self, k)
                    if not isinstance(v, Field):
                        if isinstance(v, Doc) and not isinstance(v, Document):
                            v = v.to_dict(projection=proj)
                        elif isinstance(v, list):
                            v = [
                                x.to_dict(projection=proj) if isinstance(x, Doc) and not isinstance(x, Document) else x
                                for x in v
                            ]
                        result[k] = v

            return result
        else:
            raise Exception('Invalid projection')
