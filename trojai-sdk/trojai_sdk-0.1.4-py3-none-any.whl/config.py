"""Base config class for task-specific config classes"""

import re
import ast, logging
from pathlib import Path
from dataclasses import dataclass
from typing import Any, Union, Optional
from core import TrojConfigError
from trojsdk.core.data_utils import load_json_from_disk
from dataclasses_json.undefined import UndefinedParameterError
from dataclasses_json import dataclass_json, DataClassJsonMixin, Undefined


@dataclass_json(undefined=Undefined.RAISE)
@dataclass
class BaseTrojConfig(DataClassJsonMixin):

    """
    Base class  for loading user's top-level JSON config.
    Intended to be extended to task-specific config classes in the sub-modules
    """

    name: str
    task_type: str
    attacks: Any
    dataset: Any
    model: Any

    @classmethod
    def config_from_json(
        cls, json_path: Union[str, Path], sub_jsons: bool = True
    ) -> "BaseTrojConfig":

        """
        This method is needed to read a config dictionary from a JSON file on disk
        and assign the values from the JSON to the fields of the class by corresponding
        keys. Note that the keys in the JSON file must be exactly the same as the names
        of the class fields.

        This method through inheritance will be used to construct task-specific configs

        :param json_path: path to JSON config file (str or pathlib.Path)
        :param sub_jsons: if True, check every value in config JSON to be a path to a lower level JSON config (bool)
        :return: class with values from JSON config assigned to the class fields
        """

        if type(json_path) == str:
            json_path = Path(json_path)

        try:
            config_dict = load_json_from_disk(json_path, sub_jsons=sub_jsons)
            return cls.from_dict(config_dict)

        except KeyError as err:
            raise TrojConfigError(
                f'\n\nKey "{err.args[0]}" missing from json.'
                "Make sure all required key-value pairs are "
                "present in the json"
            )

        except AttributeError:
            raise TrojConfigError(
                "\n\nCould not unpack one of sub-jsons. Make sure "
                "that paths to sub-jsons are specified correctly."
            )

        except UndefinedParameterError as err:
            message = str(err)
            dict_substring = (
                "{" + re.findall("{(.+?)}", re.sub("\(.+?\)", "", message))[0] + "}"
            )
            unknown_dict = ast.literal_eval(dict_substring)
            raise TrojConfigError(
                f'\n\nGot unexpected key(s) in json: "{list(unknown_dict.keys())}"\n'
            )
        except Exception as err:
            if hasattr(err, "message"):
                raise TrojConfigError(err.message)
            else:
                raise TrojConfigError(repr(err))

    @classmethod
    def config_from_dict(cls, config_dict: dict) -> "BaseTrojConfig":
        """Given a dictionary, initializes fields with values from corresponding keys"""
        import os
        from trojsdk.core.data_utils import test_paths

        invalid_paths = test_paths(config_dict)

        if len(invalid_paths) > 0:
            from trojsdk.core.TrojError import TrojConfigError

            err = TrojConfigError(
                "\n\nSome paths provided were invalid!"
                + "\n"
                + "Please ensure the following paths are correct:"
                + "\n"
                + str(invalid_paths)
                + "\n\n"
                + "The current working directory is:"
                + "\n"
                + str(os.getcwd())
                + "\n\n"
                + "The following files are in the working directory:"
                + "\n"
                + str(os.listdir())
            )
            raise (err)

        try:

            return cls.from_dict(config_dict)

        except KeyError as err:
            raise TrojConfigError(
                f'\n\nKey "{err.args[0]}" missing from json.'
                "Make sure all required key-value pairs are "
                "present in the json"
            )

        except AttributeError as e:
            raise TrojConfigError(
                "\n\nCould not unpack one of sub-jsons. Make sure "
                "that paths to sub-jsons are specified correctly."
            )

        except UndefinedParameterError as err:
            message = str(err)
            dict_substring = (
                "{" + re.findall("{(.+?)}", re.sub("\(.+?\)", "", message))[0] + "}"
            )
            unknown_dict = ast.literal_eval(dict_substring)
            raise TrojConfigError(
                f'\n\nGot unexpected key(s) in json: "{list(unknown_dict.keys())}"\n'
            )
        except Exception as err:
            if hasattr(err, "message"):
                raise TrojConfigError(err.message)
            else:
                raise TrojConfigError(repr(err))
