import logging
from abc import ABC, abstractproperty
from typing import List, Union
from uuid import UUID

import orjson
from beartype import beartype

from picsellia.decorators import exception_handler
from picsellia.sdk.connexion import Connexion
from picsellia.sdk.tag import Tag, TagTarget

logger = logging.getLogger("picsellia")


class Taggable(ABC):
    def __init__(self, target_type: TagTarget) -> None:
        self._target_type = target_type

    @property
    def target_type(self) -> TagTarget:
        return self._target_type

    @abstractproperty
    def ids(self) -> List[UUID]:
        pass

    @abstractproperty
    def connexion(self) -> Connexion:
        pass

    @exception_handler
    @beartype
    def add_tags(self, tags: Union[Tag, List[Tag]]) -> None:
        """Add some tags to an object (can be used on Data/MultiData/Asset/MultiAsset/DatasetVersion/Dataset/Model/ModelVersion)

        You can give a tag or a list of tag.

        Examples:
            ```python
                tag_bicyle = client.create_tag("bicycle", Target.DATA)
                tag_car = client.create_tag("car", Target.DATA)
                tag_truck = client.create_tag("truck", Target.DATA)

                data.add_tags(tag_bicyle)
                data.add_tags([tag_car, tag_truck])
            ```
        """
        if isinstance(tags, Tag):
            tags = [tags]

        assert tags != [], "Given tags are empty. They can't be empty"

        for tag in tags:
            assert (
                tag.target_type == self.target_type
            ), "Given tag ({}) is targetted on {}. It can't be added because on a {} ".format(
                tag.name, tag.target_type, self.target_type
            )

        for tag in tags:
            payload = self.ids
            self.connexion.post(
                "/sdk/tag/{}/attach".format(tag.id),
                data=orjson.dumps(payload),
            )
        logger.info("{} tags added to {}).".format(len(tags), self))

    @exception_handler
    @beartype
    def remove_tags(self, tags: Union[Tag, List[Tag]]) -> None:
        """Remove some tags from an object (can be used on Data/Asset/DatasetVersion/Dataset/Model/ModelVersion)

        You can give a Tag or a list of Tag.

        Examples:
            ```python
                data.remove_tags(tag_bicyle)
                data.remove_tags([tag_car, tag_truck])
            ```
        """
        if isinstance(tags, Tag):
            tags = [tags]

        assert tags != [], "Given tags are empty. They can't be empty"

        for tag in tags:
            assert (
                tag.target_type == self._target_type
            ), "Given tag ({}) can't be removed because it is not targetted on data".format(
                tag.name
            )

        for tag in tags:
            payload = self.ids
            self.connexion.post(
                "/sdk/tag/{}/detach".format(tag.id),
                data=orjson.dumps(payload),
            )
        logger.info("{} tags removed from {}.".format(len(tags), self))
