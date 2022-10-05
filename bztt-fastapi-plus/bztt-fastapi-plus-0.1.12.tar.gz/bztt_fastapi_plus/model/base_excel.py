from sqlalchemy import Column, String, Text,TIMESTAMP, text,Index, DECIMAL,Float, Date ,BigInteger ,Integer,DateTime,TEXT
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, LONGTEXT, TINYINT,VARCHAR


from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()


class BaseExcel(DeclarativeBase):
    """
    基础Model模型对象
    """
    __abstract__ = True

    id = Column(BIGINT(20), primary_key=True, comment='序号')

    parent_id = Column(BIGINT(20), nullable=False, server_default=text("0"), comment='父序号')
    is_deleted = Column(TINYINT(1), nullable=False, server_default=text("0"), comment='软删')
    uuid = Column(String(36), server_default=text("''"), comment='uuid')
    
    created_by = Column(BIGINT(20), nullable=False, server_default=text("0"), comment='创建人')
    created_time = Column(TIMESTAMP, nullable=False, server_default=text("current_timestamp()"), comment='创建时间')
    updated_by = Column(BIGINT(20), nullable=False, server_default=text("0"), comment='更新人')
    updated_time = Column(TIMESTAMP, nullable=False, server_default=text("current_timestamp() ON UPDATE current_timestamp()"), comment='更新时间')

