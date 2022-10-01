from pydantic import BaseModel, Field, root_validator


class File(BaseModel):
    filename: str
    size: int = None
    content: bytes = Field(None, repr=False)

    @root_validator
    def update_fields(cls, fields):
        if fields["content"]:
            fields["size"] = len(fields["content"])
        return fields
