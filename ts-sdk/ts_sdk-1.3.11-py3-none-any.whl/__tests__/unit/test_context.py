import datetime
import os
import sys
from unittest import TestCase
from unittest.mock import MagicMock, patch

import pytest

from ts_sdk.task.__task_script_runner import Context


class LogMock:
    def log(self, data):
        print(data)


class ContextMethodsTest(TestCase):
    def setUp(self):
        os.environ["TASK_SCRIPTS_CONTAINERS_MODE"] = "ecs"
        os.environ["TS_SECRET_password"] = "secretvalue"

        self.datalake_mock = MagicMock()
        self.datalake_mock.get_file_name = MagicMock(return_value="filename")
        self.datalake_mock.get_presigned_url = MagicMock(return_value="presigned_url")

        self.ids_mock = {
            "get_ids": MagicMock(return_value={}),
            "validate_ids": MagicMock(return_value=True),
        }

        self.command_mock = MagicMock()
        self.fileinfo_mock = MagicMock()

        self.input_file = {
            "type": "s3",
            "bucket": "bucket",
            "fileKey": "some/fileKey",
            "fileId": "11111111-eeee-4444-bbbb-222222222222",
        }

        self.pipeline_config = {"ts_secret_name_password": "some/kms/path"}

        self.context_to_test = Context(
            {"inputFile": self.input_file, "pipelineConfig": self.pipeline_config},
            self.datalake_mock,
            self.ids_mock,
            MagicMock(),  # logger
            self.command_mock,
            self.fileinfo_mock,
        )

    def tearDown(self):
        pass

    def test_read_file(self):
        """Make sure read_file with an input file dict calls the correct methods"""
        # Arrange
        self.context_to_test.search_eql = MagicMock(return_value=[])

        # Act
        self.context_to_test.read_file(self.input_file)

        # Assert
        self.datalake_mock.read_file.assert_called_once()
        self.context_to_test.search_eql.assert_not_called()

    def test_read_file_via_file_id_only(self):
        """Make sure that search_eql is called when reading a file using just a fileId"""
        # Arrange
        self.context_to_test.search_eql = MagicMock(return_value=[{}])

        # Act
        self.context_to_test.read_file(
            {"fileId": "11111111-eeee-4444-bbbb-222222222222"}
        )

        # Assert
        self.datalake_mock.read_file.assert_called_once()
        self.context_to_test.search_eql.assert_called_once()

    @patch("ts_sdk.task.__task_script_runner.validate_file_labels")
    def test_write_file(self, validate_file_labels_mock):
        """Make sure write_file calls the correct methods"""
        # Act
        self.context_to_test.write_file("content", "file_name", "RAW")

        # Assert
        self.datalake_mock.write_file.assert_called_once_with(
            content="content",
            context=self.context_to_test._obj,
            file_category="RAW",
            file_meta={"ts_integration_metadata": "", "ts_integration_tags": ""},
            file_name="file_name",
            ids=None,
            labels=(),
            raw_file=self.input_file,
            source_type=None,
        )
        validate_file_labels_mock.assert_called_once_with(tuple())

    @pytest.mark.skip(
        "This test does not test anything and should be fixed.  Skipping to make coverage more accurate"
    )
    def test_get_ids(self):
        r = self.context_to_test.get_ids("namespace", "slug", "version")
        assert r == {}

    @pytest.mark.skip(
        "This test does not test anything and should be fixed.  Skipping to make coverage more accurate"
    )
    def test_validate_ids(self):
        r = self.context_to_test.validate_ids("data", "namespace", "slug", "version")
        assert r == True

    def test_write_ids(self):
        """Test that write_ids calls the correct methods"""
        # Act
        self.context_to_test.write_ids("content", "file_suffix")

        # Assert
        self.datalake_mock.write_ids.assert_called_once()

    def test_get_file_name(self):
        """Test that get_file_name calls the correct methods"""
        # Act
        self.context_to_test.get_file_name(self.input_file)

        # Assert
        self.datalake_mock.get_file_name.assert_called_with(self.input_file)

    def test_get_logger(self):
        """Test that the logger that is returned is the correct one from the context"""
        # Arrange
        log_mock = MagicMock()
        self.context_to_test._log = log_mock

        # Act
        logger = self.context_to_test.get_logger()

        # Assert
        assert logger is log_mock

    def test_get_secret_config_value(self):
        """Test that get_secret_config_value gets the secret from the environment"""
        r = self.context_to_test.get_secret_config_value("password")
        # TODO: Test the method that this method calls, and replace this test with a mock assert
        assert r == "secretvalue"

    def test_get_presigned_url(self):
        """Test that get_presigned_url gets the url from the datalake"""
        r = self.context_to_test.get_presigned_url(self.input_file)
        # TODO: Test the method that this method calls, and replace this test with a mock assert
        assert r == "presigned_url"

    @patch("ts_sdk.task.__task_script_runner.validate_file_tags")
    @patch("ts_sdk.task.__task_script_runner.validate_file_meta")
    def test_update_metadata_tags(
        self, validate_file_meta_mock, validate_file_tags_mock
    ):
        """Test that metadata and tags are correctly updated"""
        # Act
        self.context_to_test.update_metadata_tags(
            self.input_file, {"meta1": "v1"}, ["t1", "t2"]
        )
        self.datalake_mock.update_metadata_tags.assert_called_once_with(
            context=self.context_to_test._obj,
            custom_meta={"meta1": "v1"},
            custom_tags=["t1", "t2"],
            file=self.input_file,
            options={},
        )
        validate_file_meta_mock.assert_called_once_with({"meta1": "v1"})
        validate_file_tags_mock.assert_called_once_with(["t1", "t2"])

    def test_run_command(self):
        """Tests that the run_command method calls the correct methods"""
        # Act
        self.context_to_test.run_command(
            "org_slug", "target_id", "action", {"meta1": "v1"}, "payload"
        )
        # Assert
        self.command_mock.run_command.assert_called_once()

    @patch("ts_sdk.task.__task_script_runner.validate_file_labels")
    def test_add_labels(self, validate_file_labels_mock):
        """Test that add_labels calls the correct function and correctly validates"""
        # Act
        self.context_to_test.add_labels(
            self.input_file, [{"name": "label1", "value": "label-value-1"}]
        )
        # Assert
        self.fileinfo_mock.add_labels.assert_called_once()
        validate_file_labels_mock.assert_called_once_with(
            [{"name": "label1", "value": "label-value-1"}]
        )

    def test_get_labels(self):
        """Test that get_labels calls the correct method"""
        # Act
        self.context_to_test.get_labels(self.input_file)

        # Assert
        self.fileinfo_mock.get_labels.assert_called_once()

    def test_delete_labels(self):
        """Test that delete_labels calls the correct method"""
        # Act
        self.context_to_test.delete_labels(self.input_file, [1, 2, 3])

        # Arrange
        self.fileinfo_mock.delete_labels.assert_called_once_with(
            self.context_to_test._obj, self.input_file["fileId"], [1, 2, 3]
        )

    @patch("ts_sdk.task.__task_script_runner.validate_file_labels")
    def test_add_attributes_labels_only(self, validate_file_labels_mock):
        """Test that add_attributes calls the correct methods when only tags are supplied"""

        # Act
        self.context_to_test.add_attributes(
            self.input_file, labels=[{"name": "label-name", "value": "label-value"}]
        )

        # Assert
        self.fileinfo_mock.add_labels.assert_called_once()
        self.datalake_mock.create_labels_file.assert_not_called()
        self.datalake_mock.update_metadata_tags.assert_not_called()

        validate_file_labels_mock.assert_called_once_with(
            [{"name": "label-name", "value": "label-value"}]
        )

    @patch("ts_sdk.task.__task_script_runner.validate_file_labels")
    @patch("ts_sdk.task.__task_script_runner.validate_file_meta")
    @patch("ts_sdk.task.__task_script_runner.validate_file_tags")
    def test_add_attributes_all_attrs(
        self,
        validate_file_tags_mock,
        validate_file_meta_mock,
        validate_file_labels_mock,
    ):
        """Test that add_attributes calls the correct methods when metadata, tags, and labels are specified"""

        # Act
        self.context_to_test.add_attributes(
            self.input_file,
            custom_meta={"m1": "v1"},
            custom_tags=["t1"],
            labels=[{"name": "label-name", "value": "label-value"}],
        )

        # Assert
        self.fileinfo_mock.add_labels.assert_not_called()
        self.datalake_mock.update_metadata_tags.assert_called_once()
        self.datalake_mock.create_labels_file.assert_called_once()
        create_labels_file_arg = self.datalake_mock.create_labels_file.call_args[1][
            "target_file"
        ]
        update_metadata_tags_options_arg = (
            self.datalake_mock.update_metadata_tags.call_args[1]["options"]
        )
        assert (
            create_labels_file_arg["fileId"]
            == update_metadata_tags_options_arg["new_file_id"]
        )

        validate_file_meta_mock.assert_called_once_with({"m1": "v1"})
        validate_file_tags_mock.assert_called_once_with(["t1"])
        validate_file_labels_mock.assert_called_once_with(
            [{"name": "label-name", "value": "label-value"}]
        )

    @patch("ts_sdk.task.__task_script_runner.validate_file_labels")
    @patch("ts_sdk.task.__task_script_runner.validate_file_tags")
    def test_add_attributes_tags_labels(
        self, validate_file_tags_mock, validate_file_labels_mock
    ):
        """Test that add_attributes calls the correct methods when only tags and labels are specified"""

        # Act
        self.context_to_test.add_attributes(
            self.input_file,
            custom_tags=["t1"],
            labels=[{"name": "label-name", "value": "label-value"}],
        )

        # Assert
        self.fileinfo_mock.add_labels.assert_not_called()
        self.datalake_mock.update_metadata_tags.assert_called_once()
        self.datalake_mock.create_labels_file.assert_called_once()
        create_labels_file_arg = self.datalake_mock.create_labels_file.call_args[1][
            "target_file"
        ]
        update_metadata_tags_options_arg = (
            self.datalake_mock.update_metadata_tags.call_args[1]["options"]
        )
        assert (
            create_labels_file_arg["fileId"]
            == update_metadata_tags_options_arg["new_file_id"]
        )

        validate_file_tags_mock.assert_called_once_with(["t1"])
        validate_file_labels_mock.assert_called_once_with(
            [{"name": "label-name", "value": "label-value"}]
        )

    @patch("ts_sdk.task.__task_script_runner.validate_file_labels")
    @patch("ts_sdk.task.__task_script_runner.validate_file_meta")
    def test_add_attributes_labels_meta_attrs(
        self, validate_file_meta_mock, validate_file_labels_mock
    ):
        """Test that add_attributes calls the correct methods when only metadata and labels are specified"""

        # Act
        self.context_to_test.add_attributes(
            self.input_file,
            custom_meta={"m1": "v1"},
            custom_tags=["t1"],
            labels=[{"name": "label-name", "value": "label-value"}],
        )

        # Assert
        self.fileinfo_mock.add_labels.assert_not_called()
        self.datalake_mock.update_metadata_tags.assert_called_once()
        self.datalake_mock.create_labels_file.assert_called_once()
        create_labels_file_arg = self.datalake_mock.create_labels_file.call_args[1][
            "target_file"
        ]
        update_metadata_tags_options_arg = (
            self.datalake_mock.update_metadata_tags.call_args[1]["options"]
        )
        assert (
            create_labels_file_arg["fileId"]
            == update_metadata_tags_options_arg["new_file_id"]
        )

        validate_file_meta_mock.assert_called_once_with({"m1": "v1"})
        validate_file_labels_mock.assert_called_once_with(
            [{"name": "label-name", "value": "label-value"}]
        )

    @patch("ts_sdk.task.__task_script_runner.validate_file_meta")
    @patch("ts_sdk.task.__task_script_runner.validate_file_tags")
    def test_add_attributes_tags_metadata(
        self, validate_file_tags_mock, validate_file_meta_mock
    ):
        """Test that add_attributes calls the correct methods when only metadata and tags are specified"""

        # Act
        self.context_to_test.add_attributes(
            self.input_file,
            custom_meta={"m1": "v1"},
            custom_tags=["t1"],
        )

        # Assert
        self.fileinfo_mock.add_labels.assert_not_called()
        self.datalake_mock.update_metadata_tags.assert_called_once()
        self.datalake_mock.create_labels_file.assert_not_called()

        update_metadata_tags_options_arg = (
            self.datalake_mock.update_metadata_tags.call_args[1]["options"]
        )

        validate_file_meta_mock.assert_called_once_with({"m1": "v1"})
        validate_file_tags_mock.assert_called_once_with(["t1"])

    def test_add_attributes_no_attrs(self):
        """Test that add_attributes does nothing when no attributes are provided"""

        # Act
        self.context_to_test.add_attributes(self.input_file)

        # Assert
        self.fileinfo_mock.add_labels.assert_not_called()
        self.datalake_mock.update_metadata_tags.assert_not_called()
        self.datalake_mock.create_labels_file.assert_not_called()
