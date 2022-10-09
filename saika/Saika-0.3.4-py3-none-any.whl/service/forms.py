from typing import List

from flask_sqlalchemy import BaseQuery
from sqlalchemy import or_
from wtforms import StringField, IntegerField, FieldList, FormField, BooleanField
from wtforms.validators import DataRequired

from saika.database import db
from saika.enums import *
from saika.exception import AppException
from saika.form import Form, JSONForm
from saika.form.fields import DataField
from .operators import Operators


class FieldOperateForm(Form):
    field = StringField(validators=[DataRequired()])
    operate = StringField(validators=[DataRequired()])
    args = DataField()

    def operator(self, model):
        models_rel = []

        models_mapping = db.models_mapping
        parts = self.field.data.split('.')  # type: List[str]
        if len(parts) > 1:
            for part in parts[:-1]:
                models_rel.append(part)
            model_name = parts[-2].lstrip('^')
            model = models_mapping.get(model_name)
            if model is None:
                raise AppException(*MODEL_INVALID, data=model_name)

        field = getattr(model, parts[-1], None)
        if field is None:
            raise AppException(*FIELD_INVALID, data=parts[-1])

        operator = Operators.get(self.operate.data, None)

        if operator is None:
            raise AppException(*OPERATOR_INVALID, data=self.operate.data)

        args = self.args.data
        if not isinstance(args, list):
            args = [args]

        return operator(field, args), models_rel


class PaginateForm(JSONForm):
    page = IntegerField(default=1)
    per_page = IntegerField(default=10)


class AdvancedPaginateForm(PaginateForm):
    filters = FieldList(FormField(FieldOperateForm))
    filters_or = BooleanField()
    orders = FieldList(FormField(FieldOperateForm))

    @property
    def data(self):
        data = super().data.copy()
        data.pop('filters')
        data.pop('filters_or')
        data.pop('orders')
        return data

    @property
    def data_raw(self):
        return super().data

    def query_process(self, query, model=None):
        query: BaseQuery
        if model is None:
            model = db.get_query_models(query)[0]

        models_rel = []

        filters = []
        orders = []

        def handle_operate_fields(fields, dest):
            nonlocal models_rel
            for form in fields:
                result = form.operator(model)
                if result is not None:
                    [operator, objs_rel] = result
                    models_rel += objs_rel
                    dest.append(operator)

        handle_operate_fields(self.filters, filters)
        handle_operate_fields(self.orders, orders)

        models_joined = set(map(lambda join: join[0], query._legacy_setup_joins))
        for model_rel in models_rel:
            model_rel: str
            model_name = model_rel.lstrip('^')
            model_cls = db.models_mapping.get(model_name)

            if model_cls and model_cls not in models_joined and model_cls.__table__ not in models_joined:
                if model_rel.startswith('^'):
                    query = query.outerjoin(model_cls)
                else:
                    query = query.join(model_cls)
                models_joined.add(model_cls)

        if filters:
            if self.filters_or.data:
                filters = [or_(*filters)]
            query = query.filter(*filters)
        if orders:
            query = query.order_by(*orders)

        return query
