import re
from typing import List

from flask import Response
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy, Model
from sqlalchemy import JSON, DATETIME, DATE, TIME
from sqlalchemy.cprocessors import str_to_datetime, str_to_date, str_to_time
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, Query

from saika import hard_code, common
from saika.meta_table import MetaTable


class Database(SQLAlchemy):
    session: Session

    def __init__(self, *args, **kwargs):
        engine_options = kwargs.pop('engine_options', {})
        engine_options.setdefault('json_serializer', common.to_json)
        engine_options.setdefault('json_deserializer', common.from_json)
        super().__init__(*args, **kwargs, engine_options=engine_options)

    def init_app(self, app):
        @app.after_request
        def session_commit(resp: Response):
            self.session.commit()
            return resp

        super().init_app(app)

    def dispose_engine(self, **kwargs):
        engine = self.get_engine(**kwargs)  # type: Engine
        engine.dispose()

    def query(self, *entities, commit=True, **kwargs):
        if commit:
            self.session.commit()
        return self.session.query(*entities, **kwargs)

    def compile_sql(self, query: Query, with_data=True):
        compile_kwargs = dict()
        if with_data:
            compile_kwargs.update(literal_binds=True)

        return query.statement.compile(
            compile_kwargs=compile_kwargs
        ).string

    @staticmethod
    def get_primary_key(model, first=True):
        pk_cols = [column.name for column in model.__table__.primary_key]
        if first and len(pk_cols) == 1:
            return pk_cols.pop(0)
        return pk_cols

    @property
    def models(self):
        models = MetaTable.get(hard_code.MI_GLOBAL, hard_code.MK_MODEL_CLASSES, [])  # type: List[Model]
        return models

    @property
    def models_mapping(self):
        return dict((getattr(model, '__tablename__'), model) for model in self.models)

    def get_relationship_objs(self, field):
        primary, secondary = None, None

        if hasattr(field.comparator, 'entity'):
            primary = field.comparator.entity.class_

        if hasattr(field.prop, 'secondary'):
            models_mapping = self.models_mapping
            secondary = field.prop.secondary
            if hasattr(secondary, 'name'):
                secondary = models_mapping.get(secondary.name)

        return primary, secondary

    @staticmethod
    def get_query_models(query):
        models = [i.get('entity') for i in query.column_descriptions]
        models = [model for model in models if model is not None]
        return models

    def add_instance(self, instance, commit=True):
        self.session.add(instance)
        if commit:
            self.session.commit()

    def delete_instance(self, instance, commit=True):
        self.session.delete(instance)
        if commit:
            self.session.commit()

    @staticmethod
    def dump_instance(instance, *columns, hidden_columns: List[str] = None):
        if not hasattr(instance, '__table__'):
            return None

        table_columns = list(instance.__table__.columns)
        table_columns_name = [column.name for column in table_columns]
        model_props = dict(instance.__class__.__dict__)
        if not columns:
            columns = table_columns

        def preprocess_columns(columns):
            if columns is None:
                return []

            result = list(columns)
            for i, column in enumerate(result):
                if isinstance(column, property):
                    for k, v in model_props.items():
                        if column is v:
                            result[i] = k
                            break
                elif column in table_columns:
                    result[i] = column.name
            return result

        columns = preprocess_columns(columns)
        hidden_columns = preprocess_columns(hidden_columns)

        def match_columns(column, target_columns):
            result = []
            if column == '*':
                result += target_columns
            else:
                for match_column in target_columns:
                    if isinstance(match_column, str):
                        if re.match(column.replace('*', '.*'), match_column):
                            result.append(match_column)

            return result

        dump_columns = []
        for column in columns:
            if isinstance(column, str) and '*' in column:
                dump_columns += match_columns(column, table_columns_name)
            else:
                dump_columns.append(column)

        dump_columns = common.list_group_by(dump_columns)

        if hidden_columns is not None:
            for column in hidden_columns:
                if column in dump_columns:
                    dump_columns.remove(column)
                elif isinstance(column, str) and '*' in column:
                    for column_match in match_columns(column, dump_columns):
                        dump_columns.remove(column_match)

        if dump_columns:
            data = {}
            for column in dump_columns:
                if callable(column):
                    patch = column(instance)  # type: dict
                    if patch:
                        data.update(patch)
                elif isinstance(column, str):
                    data[column] = getattr(instance, column)
                else:
                    raise Exception('Invalid Column:', column)

            return data

    @staticmethod
    def load_instance(instance, **kwargs):
        types_conv_func = {
            DATETIME: str_to_datetime,
            DATE: str_to_date,
            TIME: str_to_time,
        }

        columns = instance.__mapper__.columns
        for k, v in kwargs.items():
            col_type = columns[k].type
            if not isinstance(col_type, JSON):
                conv_func = types_conv_func.get(col_type.__class__, col_type.python_type)
                if conv_func and isinstance(v, str):
                    v = conv_func(v)
            setattr(instance, k, v)

        return instance

    @staticmethod
    def copy_instance(instance):
        return Database.load_instance(instance.__class__(), **Database.dump_instance(instance))


db = Database()
migrate = Migrate()
