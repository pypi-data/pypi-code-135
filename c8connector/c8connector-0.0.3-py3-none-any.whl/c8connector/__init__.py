#  Copyright (c) 2022 Macrometa Corp All rights reserved.


class C8ConnectorMeta(type):
    """C8Connector metaclass"""

    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (
                hasattr(subclass, 'name') and callable(subclass.name) and
                hasattr(subclass, 'type') and callable(subclass.type) and
                hasattr(subclass, 'version') and callable(subclass.version) and
                hasattr(subclass, 'description') and callable(subclass.description) and
                hasattr(subclass, 'validate') and callable(subclass.validate) and
                hasattr(subclass, 'samples') and callable(subclass.fetchsample) and
                hasattr(subclass, 'config') and callable(subclass.getparameters)
        )


class ConfigProperty:
    """C8Connector config property"""

    def __init__(self, name: str, type: str, is_mandatory: bool):
        self.name = name
        self.type = type
        self.is_mandatory = is_mandatory


class C8Connector(metaclass=C8ConnectorMeta):
    """C8Connector superclass"""

    def name(self) -> str:
        """Returns the name of the connector."""
        pass

    def type(self) -> str:
        """Returns the type of the connector."""
        pass

    def version(self) -> str:
        """Returns the version of the connector."""
        pass

    def description(self) -> str:
        """Returns the description of the connector."""
        pass

    def validate(self, integration: dict) -> bool:
        """Validate given configurations against the connector."""
        pass

    def samples(self, integration: dict) -> list:
        """Fetch sample data using the given configurations."""
        pass

    def config(self) -> list[ConfigProperty]:
        """Get configuration parameters for the connector."""
        pass
