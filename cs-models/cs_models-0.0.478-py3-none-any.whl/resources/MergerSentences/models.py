from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    ForeignKey,
    Text,
)

from ...database import Base


class MergerSentenceModel(Base):
    __tablename__ = "merger_sentences"

    id = Column(Integer, primary_key=True)
    merger_id = Column(
        Integer,
        ForeignKey('mergers.id'),
        nullable=False,
    )
    text = Column(Text, nullable=False, index=True)
    updated_at = Column(
        DateTime,
        nullable=False,
        # https://stackoverflow.com/questions/58776476/why-doesnt-freezegun-work-with-sqlalchemy-default-values
        default=lambda: datetime.utcnow(),
        onupdate=lambda: datetime.utcnow(),
    )
