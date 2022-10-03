import os
import pytest
from unittest import mock


@mock.patch.dict(os.environ, {"CINNAROLL_API_KEY": ""})
def test_module_import_without_api_key() -> None:
    with mock.patch('builtins.open', mock.mock_open(read_data='')):
        with pytest.raises(Exception):
            import cinnaroll


@mock.patch.dict(os.environ, {"CINNAROLL_API_KEY": "abc123"})
def test_module_import_with_api_key_in_env() -> None:
    with mock.patch('builtins.open', mock.mock_open(read_data='')):
        import cinnaroll


get_api_key_from_file_cases = [
    ['[default]\n'
     '"API Key" = "123abc"',
     "123abc"],
    ["", ""],
    ['[123]\n'
     '"API Key" = "123abc"',
     ""],
]


@mock.patch.dict(os.environ, {"CINNAROLL_API_KEY": "abc123"})
@pytest.mark.parametrize("input_file_content, expected_output", get_api_key_from_file_cases)
def test_get_api_key_from_toml_file_content(input_file_content: str, expected_output: str) -> None:
    with mock.patch('builtins.open', mock.mock_open(read_data=input_file_content)):
        import cinnaroll
        actual_output = cinnaroll.get_api_key_from_toml_file_content(input_file_content)
        assert expected_output == actual_output
