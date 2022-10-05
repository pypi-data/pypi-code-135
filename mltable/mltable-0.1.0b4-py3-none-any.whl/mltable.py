# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""
Contains functionality to create and interact with MLTable objects
"""
from multiprocessing.sharedctypes import Value
import os
import yaml
from enum import Enum, auto
import random

from azureml.dataprep.api._loggerfactory import track, _LoggerFactory
from azureml.dataprep.api._dataframereader import get_dataframe_reader
from azureml.dataprep.api.mltable._mltable_helper import _read_yaml, _validate, _download_mltable_yaml, \
    _parse_path_format, _PathType
from ._aml_utilities._aml_rest_client_helper import _get_data_asset_by_id, _get_data_asset_by_asset_uri

_PUBLIC_API = 'PublicApi'
_INTERNAL_API = 'InternalCall'
_TRAITS_SECTION_KEY = 'traits'
_INDEX_COLUMNS_KEY = 'index_columns'
_TIMESTAMP_COLUMN_KEY = 'timestamp_column'
_logger = None

# keys for MLTable sections
_EXTRACT_PARTITION_FORMAT_KEY = 'extract_columns_from_partition_format'
_PARTITION_FORMAT_KEY = 'partition_format'
_PATHS_KEY = 'paths'
_METADATA_KEY = 'metadata'
_TRANSFORMATIONS_KEY = 'transformations'
_RUNTIME_NEEDED_PROPS = ['query_source', 'paths', 'transformations', _TRAITS_SECTION_KEY, _METADATA_KEY]


class MLTablePromoteHeadersBehavior(Enum):
    """
    Defines options for how column headers are processed when reading data from files to create a mltable.

    These enumeration values are used in the MLtable class method
    """
    no_header = auto()  #: No column headers are read
    from_first_file = auto()  #: Read headers only from first row of first file, everything else is data.
    all_files_different_headers = auto()  #: Read headers from first row of each file, combining named columns.
    all_files_same_headers = auto()  #: Read headers from first row of first file, drops first row from other files.

    @staticmethod
    def _parse(header):
        try:
            return MLTablePromoteHeadersBehavior[header.lower()]
        except KeyError:
            raise KeyError("Unsupported header provided. The allowed values are : 'no_header', 'from_first_file',"
                           "'all_files_different_headers', 'all_files_same_headers', found {}".format(str(header)))


class MLTableFileEncoding(Enum):
    """
    Defines options for how encoding are processed when reading data from files to create a mltable.

    These enumeration values are used in the MLtable class method
    """
    utf8 = auto()
    iso88591 = auto()
    latin1 = auto()
    ascii = auto()
    utf16 = auto()
    utf32 = auto()
    utf8bom = auto()
    windows1252 = auto()

    @staticmethod
    def _parse(encoding):
        try:
            return MLTableFileEncoding[encoding.lower()]
        except KeyError:
            raise KeyError((
                "Invalid encoding '{}'. The supported encodings are 'utf8', 'iso88591', "
                "'latin1', 'ascii', 'utf16', 'utf32', 'utf8bom' and 'windows1252'.").format(encoding))


def _get_logger():
    global _logger
    if _logger is None:
        _logger = _LoggerFactory.get_logger(__name__)
    return _logger


def _remove_properties_not_runtime_needed(mltable_yaml_dict):
    filtered_mltable_yaml_dict = {k: v for k, v in mltable_yaml_dict.items() if k in _RUNTIME_NEEDED_PROPS and v}
    return filtered_mltable_yaml_dict


# only expecting to get asset id in remote job in prod + local e2e test scenario
def _load_mltable_from_legacy_dataset(asset_id, storage_options=None):
    asset = _get_data_asset_by_id(asset_id, storage_options)
    mltable_string = asset.legacy_dataflow
    if not mltable_string or mltable_string == '':
        raise RuntimeError(f'Data asset service returned invalid MLTable yaml for asset {asset_id}')

    return yaml.safe_load(mltable_string)


# asset uri can be from local or remote
def _load_mltable_from_data_asset_uri(asset_uri_match, storage_options=None):
    data_asset = _get_data_asset_by_asset_uri(asset_uri_match, storage_options)
    is_v2 = data_asset.additional_properties['isV2']
    if is_v2:
        if data_asset.data_version.data_type != 'MLTable':
            raise ValueError('Can only load MLTable type asset')
        local_path = _download_mltable_yaml(data_asset.data_version.data_uri)
        mltable_dict = _read_yaml(local_path)
        mltable_dict = _make_all_paths_absolute(mltable_dict, data_asset.data_version.data_uri)
        _validate(mltable_dict)
        return mltable_dict
    else:
        mltable_string = data_asset.additional_properties['legacyDataflow']
        if not mltable_string:
            raise RuntimeError(f'Data asset service returned invalid MLTable yaml '
                               f'for asset {asset_uri_match[3]}:{asset_uri_match[4]}')

        return yaml.safe_load(mltable_string)


def _make_all_paths_absolute(mltable_yaml_dict, base_path, is_local=False):
    if base_path:
        if 'paths' in mltable_yaml_dict:
            for path_dict in mltable_yaml_dict['paths']:
                for path_prop, path in path_dict.items():
                    path_type, _, _ = _parse_path_format(path)
                    # get absolute path from base_path + relative path
                    if path_type == _PathType.local and not os.path.isabs(path):
                        path_dict[path_prop] = os.path.join(base_path, os.path.normpath(path))
                        # if base_path is local
                        if is_local:
                            path_dict[path_prop] = "file://" + path_dict[path_prop]
    return mltable_yaml_dict


@track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
def load(uri, storage_options: dict=None):
    """
    Loads the MLTable file(YAML) present at the given uri.

    .. remarks::

        There must be a valid MLTable file(YAML) with the name 'MLTable' present at the given uri.

        .. code-block:: python

            # load mltable from local folder
            from mltable import load
            tbl = load('.\\samples\\mltable_sample')

            # load mltable from azureml datastore uri
            from mltable import load
            tbl = load(
                'azureml://subscriptions/<subscription-id>/
                resourcegroups/<resourcegroup-name>/workspaces/<workspace-name>/
                datastores/<datastore-name>/paths/<mltable-path-on-datastore>/')

            # load mltable from azureml data asset uri
            from mltable import load
            tbl = load(
                'azureml://subscriptions/<subscription-id>/
                resourcegroups/<resourcegroup-name>/providers/Microsoft.MachineLearningServices/
                workspaces/<workspace-name>/data/<data-asset-name>/versions/<data-asset-version>/')

    :param uri: uri supports long-form datastore uri, storage uri or local path or data asset uri.
    :type uri: str
    :param storage_options: optional to specify aml workspace information when uri is an aml asset.
        it supports keys of 'subscription', 'resource_group', 'workspace', 'location'.
        All of these are required to locate an azure machine learning workspace.
    :type storage_options: dict[str, str]
    :return: MLTable object representing the MLTable file(YAML) at uri.
    :rtype: mltable.MLTable
    """
    path_type, base_path, match = _parse_path_format(uri)
    is_local = False
    if path_type == _PathType.local:
        base_path = os.path.normpath(base_path)
        local_path = base_path
        is_local = True
        if not os.path.isabs(base_path):
            local_path = os.path.join(os.getcwd(), base_path)
        mltable_dict = _read_yaml(local_path)
        _validate(mltable_dict)
    elif path_type == _PathType.cloud:
        local_path = _download_mltable_yaml(uri)
        mltable_dict = _read_yaml(local_path)
        _validate(mltable_dict)
    elif path_type == _PathType.legacy_dataset:
        # skip mltable yaml validation for v1 legacy dataset because of some legacy schema generated in converter
        mltable_dict = _load_mltable_from_legacy_dataset(uri, storage_options)
        # this is to skip path conversion logic, all paths will be absolute path
        base_path = None
    elif path_type == _PathType.data_asset_uri:
        mltable_dict = _load_mltable_from_data_asset_uri(match, storage_options)
        # path has been mapped to absolute path in _load_mltable_from_data_asset_uri
        base_path = None
    else:
        raise ValueError('The uri should be a valid path to a local or cloud directory which contains an '
                         'MLTable file.')
    mltable_yaml_dict = _remove_properties_not_runtime_needed(mltable_dict)
    # v1 sql dataset doesnt have paths
    orig_rel_paths = mltable_dict[_PATHS_KEY] if _PATHS_KEY in mltable_dict else None
    mltable_yaml_dict = _make_all_paths_absolute(mltable_yaml_dict, base_path, is_local)
    return MLTable._create_from_dict(mltable_dict=mltable_yaml_dict, orig_paths=orig_rel_paths)


@track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
def from_delimited_files(paths, header='all_files_same_headers', delimiter=",", support_multi_line=False,
                         empty_as_string=False, encoding='utf8', include_path_column=False):
    """
    Create the MLTable from the given list of delimited files.

    .. remarks::

        There must be a valid paths string.

        .. code-block:: python

            # load mltable from local delimited file
            from mltable import from_delimited_files
            paths = '[{'file': "./samples/mltable_sample/sample_data.csv"}]'
            mltable = from_delimited_files(paths)

    :param paths: paths supports files or folders type with local or cloud path.
    :type paths: list
    :param header: Controls how column headers are promoted when reading from files. Defaults to all_files_same_header.
        More options can be specified using enum value of :class:`mltable.PromoteHeadersBehavior`.
    :type header: mltable.MLTablePromoteHeadersBehavior
    :param delimiter: The separator used to split columns.
    :type delimiter: str
    :param support_multi_line: By default (support_multi_line=False), all line breaks, including those in quoted
        field values, will be interpreted as a record break. Reading data this way is faster and more optimized
        for parallel execution on multiple CPU cores. However, it may result in silently producing more records
        with misaligned field values. This should be set to True when the delimited files are known to contain
        quoted line breaks.

        .. remarks::

            Given this csv file as example, the data will be read differently based on support_multi_line.

                A,B,C
                A1,B1,C1
                A2,"B
                2",C2

            .. code-block:: python

                 from mltable import from_delimited_files

                # default behavior: support_multi_line=False
                mltable = from_delimited_files(path)
                print(mltable.to_pandas_dataframe())
                #      A   B     C
                #  0  A1  B1    C1
                #  1  A2   B  None
                #  2  2"  C2  None

                # to handle quoted line breaks
                mltable = from_delimited_files(path, support_multi_line=True)
                print(mltable.to_pandas_dataframe())
                #      A       B   C
                #  0  A1      B1  C1
                #  1  A2  B\\r\\n2  C2

    :type support_multi_line: bool
    :param empty_as_string: Specify if empty field values should be loaded as empty strings.
        The default (False) will read empty field values as nulls. Passing this as True will
        read empty field values as empty strings. If the values are converted to numeric or
        datetime then this has no effect, as empty values will be converted to nulls.
    :type empty_as_string: bool
    :param encoding: Specify the file encoding. Supported encodings are 'utf8', 'iso88591', 'latin1', 'ascii',
        'utf16', 'utf32', 'utf8bom' and 'windows1252'.
    :type encoding: str
    :param include_path_column: Boolean to keep path information as column in the mltable. Defaults to False.
        This is useful when reading multiple files, and want to know which file a particular record
        originated from, or to keep useful information in file path.
    :type include_path_column: bool
    :return: MLTable object.
    :rtype: mltable.MLTable
    """
    mltable = from_paths(paths)

    header = MLTablePromoteHeadersBehavior._parse(header)
    encoding = MLTableFileEncoding._parse(encoding)

    new_dataflow = mltable._dataflow.add_transformation('read_delimited',
                                                        {"delimiter": delimiter,
                                                         "header": header.name,
                                                         "support_multi_line": support_multi_line,
                                                         "empty_as_string": empty_as_string,
                                                         "encoding": encoding.name,
                                                         "include_path_column": include_path_column})

    return mltable._create_from_dataflow(new_dataflow, mltable.paths)


@track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
def from_parquet_files(paths, include_path_column=False):
    """
    Create the MLTable from the given list of parquet files.

    .. remarks::

        There must be a valid paths dictionary

        .. code-block:: python

            # load mltable from local parquet paths
            from mltable import from_parquet_files
            paths = '[{'file': "./samples/mltable_sample/sample_data.parquet"}]'
            mltable = from_parquet_files(paths)

    :param paths: paths supports files or folders type with local or cloud path.
    :type paths: list
    :param include_path_column: Boolean to keep path information as column in the mltable. Defaults to False.
        This is useful when reading multiple files, and want to know which file a particular record
        originated from, or to keep useful information in file path.
    :type include_path_column: bool
    :return: MLTable object.
    :rtype: mltable.MLTable
    """
    mltable = from_paths(paths)
    new_dataflow = mltable._dataflow.add_transformation('read_parquet', {"include_path_column": include_path_column})
    return mltable._create_from_dataflow(new_dataflow, mltable.paths)


@track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
def from_json_lines_files(paths, drop_invalid_lines=False, encoding="utf8", include_path_column=False):
    """
    Create the MLTable from the given list of json lines files.

    .. remarks::

        There must be a valid paths dictionary

        .. code-block:: python

            # load mltable from local parquet paths
            from mltable import from_json_lines_files
            paths = '[{'file': "./samples/mltable_sample/sample_data.jsonl"}]'
            mltable = from_json_lines_files(paths)

    :param paths: paths supports files or folder type with local or cloud path.
    :type paths: list
    :param drop_invalid_lines: How to handle lines that are invalid JSON. If its true, it just drop invalid lines,
        otherwise it will fail. Default to False.
    :type drop_invalid_lines: str
    :param encoding: Specify the file encoding. Supported encodings are 'utf8', 'iso88591', 'latin1', 'ascii',
        'utf16', 'utf32', 'utf8bom' and 'windows1252'
    :type encoding: str
    :param include_path_column: Boolean to keep path information as column in the mltable. Defaults to False.
        This is useful when reading multiple files, and want to know which file a particular record
        originated from, or to keep useful information in file path.
    :type include_path_column: bool
    :return: MLTable object.
    :rtype: mltable.MLTable
    """
    mltable = from_paths(paths)

    encoding = MLTableFileEncoding._parse(encoding)
    new_dataflow = mltable._dataflow.add_transformation('read_json_lines',
                                                        {"drop_invalid_lines": drop_invalid_lines,
                                                         "encoding": encoding.name,
                                                         "include_path_column": include_path_column})
    return mltable._create_from_dataflow(new_dataflow, mltable.paths)


@track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
def from_paths(paths):
    """
    Create the MLTable from the given paths.

    .. remarks::

        There must be a valid paths dictionary

        .. code-block:: python

            # load mltable from local paths
            from mltable import from_paths
            tbl = from_paths([{'file': "./samples/mltable_sample"}])

            # load mltable from cloud paths
            from mltable import load
            tbl = from_paths([{'file': "https://<blob-storage-name>.blob.core.windows.net/<path>/sample_file"}])

    :param paths: paths supports file or folder type with local or cloud path.
    :type paths: list
    :return: MLTable object.
    :rtype: mltable.MLTable
    """
    mltable_dict = {_PATHS_KEY: paths}
    mltable_yaml_dict = mltable_dict
    if 'paths' in mltable_yaml_dict:
        for path_dict in mltable_yaml_dict['paths']:
            for path_prop, path in path_dict.items():
                path_type, local_path, _ = _parse_path_format(path)
                local_path = os.path.normpath(local_path)
                if path_type == _PathType.local:
                    if not os.path.isabs(local_path):
                        local_path = os.path.normpath(os.path.join(os.getcwd(), local_path))
                    path_dict[path_prop] = "file://" + local_path
    _validate(mltable_yaml_dict)
    return MLTable._create_from_dict(mltable_dict=mltable_yaml_dict, orig_paths=paths)


@track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
def from_delta_lake(path, timestamp=None, version=None):
    """Creates an MLTable object to read in Parquet files from delta lake table.

    .. remarks::

        **from_delta_lake** creates an MLTable object which defines the operations to
        load data from delta lake folder into tabular representation.

        For the data to be accessible by Azure Machine Learning, `path` must point to the delta table directory
        and the delta lake files that are referenced must be accessible by AzureML services or behind public web urls.

        **from_delta_lake** supports reading delta lake data from a url pointing to: Blob, ADLS Gen1 and ADLS Gen2

        Users are able to read in and materialize the data by calling `to_pandas_dataframe()` on the returned MLTable

        .. code-block:: python

            # create an MLTable object from a delta lake using timestamp versioning and materialize the data
            from mltable import from_delta_lake
            mltable_timestamp = from_delta_lake(path="./data/delta-01", timestamp="2021-05-24T00:00:00Z")
            pd = mltable_timestamp.to_pandas_dataframe()

            # create  an MLTable object from a delta lake using integer versioning and materialize the data
            from mltable import from_delta_lake
            mltable_version = from_delta_lake(path="./data/delta-02", version=1)
            pd = mltable_version.to_pandas_dataframe()

    :param path: Path pointing to the delta table directory containing the delta lake parquet files to read
    :type path: str
    :param timestamp: datetime string in ISO-8601 format to use to read in matching parquet files
    :type timestamp: string
    :param version: integer version to use to read in matching parquet files
    :type version: int
    :return: MLTable object
    :rtype: mltable.MLTable
    """
    if timestamp and version:
        raise KeyError("Both timestamp and version parameters were provided, but only one of version "
                       "or timestamp can be specified.")

    mltable = from_paths([{"folder": path}])
    return mltable._add_transformation_step('read_delta_lake', {'version': version, 'timestamp': timestamp})


class MLTable:
    """
    Represent MLTable.

    A MLTable defines a series of lazily-evaluated, immutable operations to load data from the
    data source. Data is not loaded from the source until MLTable is asked to deliver data.
    """

    def __init__(self):
        """
        Initialize a new MLTable

        This constructor is not supposed to be invoked directly. MLTable is intended to be created using
        :func:`mltable.load`
        """
        self._loaded = False

    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def _ensure_random_seed(self, seed):
        """
        If the given seed is not an integer or None, raises a ValueError. Otherwise if None creates a
        random seed based on the current date & time in seconds rounded to nearest second.

        :param seed: possible value for random seed
        :type seed: object
        :return: valid random seed
        :rtype: int
        """
        if seed is None:
            return random.randint(1, 1000)
        elif not isinstance(seed, int):
            raise ValueError('A random seed must be an integer')
        return seed

    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def _check_loaded(self):
        if not self._loaded:
            raise ValueError('MLTable does not appear to be loaded correctly. '
                             'Please use MLTable.load() to load a mltable file into memory.')

    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def _add_transformation_step(self, step, args, index=None):
        """
        Adds the given transformation step and its associated arguments to this MLTable's PyRsDataflow at
        given index in list of all added transformation steps. Returns a new MLTable whose dataflow is the
        PyRsDataflow resulting from the prior addition

        :param step: transformation step
        :type step: str
        :param args: arguments for given transformation step
        :type: object
        :param index: optional argument to indicate which index to add the step
        :type: int
        :return: MLTable with resulting PyRsDataflow
        :rtype: mltable.MLTable
        """
        new_dataflow = self._dataflow.add_transformation(step, args, index)
        return MLTable._create_from_dataflow(new_dataflow, self.paths)

    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def _normalize_column_inputs(self, columns):
        if isinstance(columns, str):
            return [columns]
        elif isinstance(columns, list) and len(columns) > 0 and all(isinstance(col, str) for col in columns):
            return columns
        raise ValueError('Columns should be a string or list of strings with at least one element')

    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def _get_columns_in_traits(self):
        """
        Gets all the columns that are set in this MLTable's Traits

        :return: set of all Traits
        :rtype: set[str]
        """
        columns_in_traits = set()
        if self.traits:
            timestamp_col = self.traits._check_and_get_trait_col(_TIMESTAMP_COLUMN_KEY)
            if timestamp_col is not None:
                columns_in_traits.add(timestamp_col)

            index_cols = self.traits._check_and_get_trait_col(_INDEX_COLUMNS_KEY)
            if index_cols is not None:
                columns_in_traits.update(index_cols)

        return columns_in_traits

    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def to_pandas_dataframe(self):
        """
        Load all records from the paths specified in the MLTable file into a pandas DataFrame.

        .. remarks::

            The following code snippet shows how to use the to_pandas_dataframe api to obtain a pandas dataframe
            corresponding to the provided MLTable.

            .. code-block:: python

                from mltable import load
                tbl = load('.\\samples\\mltable_sample')
                pdf = tbl.to_pandas_dataframe()
                print(pdf.shape)

        :return: pandas.DataFrame object containing the records from the paths in the MLTable.
        :rtype: pandas.DataFrame
        """
        self._check_loaded()
        try:
            dataframe_reader = get_dataframe_reader()
            mltable_yaml_str = self._dataflow.to_yaml_string()
            df = dataframe_reader._rslex_to_pandas_with_fallback(mltable_yaml_str)
        except Exception as e:
            message = e.args[0]
            if "InvalidPythonExpression" in message:
                raise ValueError("Not a valid python expression in filter") from e
            else:
                raise e
        return df

    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def extract_columns_from_partition_format(self, partition_format):
        """
        Adds a transformation step to use the partition information of each path and extract them into columns
        based on the specified partition format.

        Format part '{column_name}' creates string column, and '{column_name:yyyy/MM/dd/HH/mm/ss}' creates
        datetime column, where 'yyyy', 'MM', 'dd', 'HH', 'mm' and 'ss' are used to extract year, month, day,
        hour, minute and second for the datetime type.

        The format should start from the position of first partition key until the end of file path.
        For example, given the path '/Accounts/2019/01/01/data.csv' where the partition is by department name
        and time, partition_format='/{Department}/{PartitionDate:yyyy/MM/dd}/data.csv'
        creates a string column 'Department' with the value 'Accounts' and a datetime column 'PartitionDate'
        with the value '2019-01-01'.

        :param partition_format: Partition format to use to extract data into columns
        :type partition_format: str
        :return: MLTable whose partition format is set to given format
        :rtype: mltable.MLTable
        """
        self._check_loaded()
        return self._add_transformation_step('extract_columns_from_partition_format',
                                             {_PARTITION_FORMAT_KEY: partition_format},
                                             0)

    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def _get_partition_key_values(self, partition_keys=None):
        """Return unique key values of partition_keys.

        validate if partition_keys is a valid subset of full set of partition keys, return unique key values of
        partition_keys, default to return the unique key combinations by taking the full set of partition keys of this
        dataset if partition_keys is None

        .. code-block:: python

            # get all partition key value pairs
            partitions = mltable.get_partition_key_values()
            # Return [{'country': 'US', 'state': 'WA', 'partition_date': datetime('2020-1-1')}]

            partitions = mltable.get_partition_key_values(['country'])
            # Return [{'country': 'US'}]

        :param partition_keys: partition keys
        :type partition_keys: builtin.list[str]
        """
        if not partition_keys:
            partition_keys = self.partition_keys
        if not self.partition_keys:
            raise Exception("cannot retrieve partition key values for a mltable that has no "
                            "partition keys")

        invalid_keys = [x for x in partition_keys if x not in self.partition_keys]
        if len(invalid_keys) != 0:
            raise ValueError(f"{invalid_keys} are invalid partition keys")

        # currently use summarize to find the distinct result
        mltable = self.take(count=1)
        pd = mltable.to_pandas_dataframe()
        no_partition_key_columns = [x for x in pd.columns if x not in partition_keys]
        mltable = self
        if len(no_partition_key_columns) > 0:
            mltable = mltable._add_transformation_step('summarize',
                                                       {"aggregates":
                                                        [{"source_column": no_partition_key_columns[0],
                                                          "aggregate": "count",
                                                          "new_column": "new_count"}],
                                                        "group_by": partition_keys})
        mltable = mltable.keep_columns(partition_keys)
        # need to implement distinct from rlex https://msdata.visualstudio.com/Vienna/_workitems/edit/1749317
        # mltable = self.distinct_rows()
        pd = mltable.to_pandas_dataframe()
        pd = pd.drop_duplicates()
        partition_key_values = pd.to_dict(orient='records') if pd.shape[0] != 0 else []
        return partition_key_values

    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def filter(self, expression):
        """
        Filter the data, leaving only the records that match the specified expression.

        .. remarks::

            Expressions are started by indexing the mltable with the name of a column. They support a variety of
                functions and operators and can be combined using logical operators. The resulting expression will be
                lazily evaluated for each record when a data pull occurs and not where it is defined.

            .. code-block:: python

                filtered_mltable = mltable.filter('feature_1 == \"5\" and target > \"0.5)\"')
                filtered_mltable = mltable.filter('col("FBI Code") == \"11\"')

        :param expression: The expression to evaluate.
        :type expression: string
        :return: MLTable after filter
        :rtype: mltable.MLTable
        """
        self._check_loaded()
        return self._add_transformation_step('filter', expression)

    @property
    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def paths(self):
        """
        Returns a list of dicts containing paths specified in the MLTable.

        :return: list of dicts containing paths specified in the MLTable
        :rtype: list[dict]
        """
        self._check_loaded()
        return self._orig_paths

    @property
    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def partition_keys(self):
        """Return the partition keys.

        :return: the partition keys
        :rtype: builtin.list[str]
        """

        def parse_partition_format(partition_format):
            date_parts = ['yyyy', 'MM', 'dd', 'HH', 'mm', 'ss']
            date_part_map = {d: '_sys_{}'.format(d) for d in date_parts}
            defined_date_parts = []
            date_column = None
            columns = []
            i = 0
            pattern = ''
            while i < len(partition_format):
                c = partition_format[i]
                if c == '/':
                    pattern += '\\/'
                elif partition_format[i:i + 2] in ['{{', '}}']:
                    pattern += c
                    i += 1
                elif c == '{':
                    close = i + 1
                    while close < len(partition_format) and partition_format[close] != '}':
                        close += 1
                    key = partition_format[i + 1:close]
                    if ':' in key:
                        date_column, date_format = key.split(':')
                        for date_part in date_parts:
                            date_format = date_format.replace(date_part, '{' + date_part_map[date_part] + '}')
                        partition_format = partition_format[:i] + date_format + partition_format[close + 1:]
                        continue
                    else:
                        found_date = False
                        for k, v in date_part_map.items():
                            if partition_format.startswith(v, i + 1):
                                pattern_to_add = '(?<{}>\\d{{{}}})'.format(v, len(k))
                                if pattern_to_add in pattern:
                                    pattern += '(\\d{{{}}})'.format(len(k))
                                else:
                                    pattern += pattern_to_add
                                    defined_date_parts.append(k)
                                found_date = True
                                break

                        if not found_date:
                            pattern_to_add = '(?<{}>[^\\.\\/\\\\]+)'.format(key)
                            if pattern_to_add in pattern:
                                pattern += '([^\\.\\/\\\\]+)'
                            else:
                                columns.append(key)
                                pattern += pattern_to_add
                        i = close
                elif c == '*':
                    pattern += '(.*?)'
                elif c == '.':
                    pattern += '\\.'
                else:
                    pattern += c
                i += 1
            if date_column is not None:
                columns.append(date_column)

            if defined_date_parts and 'yyyy' not in defined_date_parts:
                raise ValueError(f'Invalid partition_format "{partition_format}". {validation_error["NO_YEAR"]}')
            return pattern, defined_date_parts, columns

        if len(self._partition_keys) > 0:
            return self._partition_keys
        mltable_yaml_str = self._dataflow.to_yaml_string()
        mltable_dict = yaml.safe_load(mltable_yaml_str)
        if _TRANSFORMATIONS_KEY in mltable_dict:
            for mltable_transformation in mltable_dict[_TRANSFORMATIONS_KEY]:
                if _EXTRACT_PARTITION_FORMAT_KEY in mltable_transformation:
                    parsed_result = parse_partition_format(
                        mltable_transformation[_EXTRACT_PARTITION_FORMAT_KEY][_PARTITION_FORMAT_KEY])
                    if len(parsed_result) == 3 and parsed_result[2]:
                        self._partition_keys = parsed_result[2]
                        return parsed_result[2]
        return []

    @staticmethod
    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def _create_from_dict(mltable_dict, orig_paths):
        """
        Creates a new MLTable from a dictionary containing information from
        a MLTable file

        :param mltable_dict: MLTable dict to read from
        :type mltable_dict: dict
        :param orig_paths: paths (relative or absolute) contained in the given MLTable
        :type orig_paths: list[str]
        :return: MLTable from given dict
        :rtype: mltable.MLTable
        """
        # TODO move this to imports on dataflow release
        try:
            from azureml.dataprep.rslex import PyRsDataflow
            mltable_yaml_string = yaml.dump(mltable_dict)
            dataflow = PyRsDataflow(mltable_yaml_string)
        except ImportError:
            _get_logger().warn('Not able to import PyRsDataflow')
        except Exception as ex:
            raise ex

        return MLTable._create_from_dataflow(dataflow, orig_paths)

    @staticmethod
    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def _create_from_dataflow(dataflow, orig_paths):
        """
        Creates a new MLTable from a PyRsDataflow

        :param new_dataflow: PyRsDataflow to read from
        :type new_dataflow: PyRsDataflow
        :param orig_paths: paths (relative or absolute) contained in the MLTable given Dataflow is based on
        :type orig_paths: list[str]
        :return: MLTable from given PyRsDataflow
        :rtype: mltable.MLTable
        """
        new_mltable = MLTable()
        new_mltable._dataflow = dataflow
        new_mltable._loaded = True
        new_mltable._orig_paths = orig_paths
        new_mltable._partition_keys = []
        new_mltable.traits = Traits._create(new_mltable)
        return new_mltable

    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def take(self, count=20):
        """
        Adds a transformation step to select the first `count` rows of this MLTable

        :param count: number of rows from top of table to select
        :type count: int
        :return: MLTable with added "take" transformation step
        :rtype: mltable.MLTable
        """
        if not (isinstance(count, int) and count > 0):
            raise ValueError('Number of rows must be a positive integer')
        return self._add_transformation_step('take', count)

    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def show(self, count=20):
        """
        Retrieves the first `count` rows of this MLTable as a Pandas Dataframe

        :param count: number of rows from top of table to select
        :type count: int
        :return: first `count` rows of the MLTable
        :rtype: Pandas Dataframe
        """
        return self.take(count).to_pandas_dataframe()

    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def take_random_sample(self, probability, seed=None):
        """
        Adds a transformation step to randomly select each row of this MLTable with `probability` chance.
        Probability must be in range [0, 1]. May optionally set a random seed.

        :param probability: chance that each row is selected
        :type: probability: float
        :param seed: optional random seed
        :type seed: Optional[int]
        :return: MLTable with added transformation step
        :rtype: mltable.MLTable
        """
        if not (isinstance(probability, (float, int)) and 0 < probability < 1):
            raise ValueError('Probability should an integer or float greater than 0 and less than 1')
        seed = self._ensure_random_seed(seed)
        return self._add_transformation_step('take_random_sample',
                                             {"probability": probability, "seed": seed})

    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def drop_columns(self, columns):
        """
        Adds a transformation step to drop desired columns from the dataset

        If a timeseries column is dropped, the corresponding capabilities will be dropped for the
        returned MLTable

        :param columns: The name or a list of names for the columns to drop
        :type columns: Union[str, builtin.list[str]]
        :return: MLTable with added transformation step
        :rtype: mltable.MLTable
        """
        self._check_loaded()
        columns = self._normalize_column_inputs(columns)
        columns_in_traits = self._get_columns_in_traits()
        if not columns_in_traits.isdisjoint(columns):
            raise ValueError('Columns in traits must be kept and cannot be dropped')
        return self._add_transformation_step('drop_columns', columns)

    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def keep_columns(self, columns):
        """
        Adds a transformation step to Keep the specified columns and drop all others from the dataset

        If a timeseries column is dropped, the corresponding capabilities will be dropped for the
        returned MLTable

        :param columns: The name or a list of names for the columns to keep
        :type columns: Union[str, builtin.list[str]]
        :return: MLTable with added transformation step
        :rtype: mltable.MLTable
        """
        self._check_loaded()
        columns = self._normalize_column_inputs(columns)
        columns_in_traits = self._get_columns_in_traits()
        if not columns_in_traits.issubset(columns):
            raise ValueError('Columns in traits must be kept and cannot be dropped')
        return self._add_transformation_step('keep_columns', columns)

    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def random_split(self, percent=.5, seed=None):
        """
        Randomly splits this MLTable into two MLTables, one having approximately "percent"% of the original
        MLTable's data and the other having the remainder (1-"percent"%).

        :param percent: percent of the MLTable to split between
        :type percent: Union[int, float]
        :param seed: optional random seed
        :type seed: Optional[int]
        :return: two MLTables with this MLTable's data split between them by "percent"
        :rtype: Tuple[mltable.MLTable, mltable.MLTable]
        """
        if not (isinstance(percent, float) and 0 < percent < 1):
            raise ValueError('Percent should be a float greater than 0 and less than 1')
        seed = self._ensure_random_seed(seed)
        split_a = self._add_transformation_step('sample', {"sampler": "random_percent",
                                                           "sampler_arguments": {
                                                               "probability" : percent,
                                                               "probability_lower_bound": 0.0,
                                                               "seed" : seed}})
        split_b = self._add_transformation_step('sample', {"sampler": "random_percent",
                                                           "sampler_arguments": {
                                                               "probability" : 1.0,
                                                               "probability_lower_bound": percent,
                                                               "seed" : seed}})
        return split_a, split_b


class Traits:
    """
    Class that map to the traits section of the MLTable.

    Currently supported traits are: timestamp_column and index_columns
    """

    @staticmethod
    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def _create(mltable):
        traits = Traits()
        traits._mltable = mltable
        return traits

    @property
    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def _mltable_dict(self):
        mltable_yaml_str = self._mltable._dataflow.to_yaml_string()
        return yaml.safe_load(mltable_yaml_str)

    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def _has_trait_column(self, col_name):
        mltable_dict = self._mltable_dict
        return _METADATA_KEY in mltable_dict and \
            _TRAITS_SECTION_KEY in mltable_dict[_METADATA_KEY] and \
            col_name in mltable_dict[_METADATA_KEY][_TRAITS_SECTION_KEY]

    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def _get_trait_col(self, col_name):
        return self._mltable_dict[_METADATA_KEY][_TRAITS_SECTION_KEY][col_name]

    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def _check_and_get_trait_col(self, col_name):
        return self._get_trait_col(col_name) if self._has_trait_column(col_name) else None

    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def _set_trait_col(self, col_name, col_value):
        mltable_dict = self._mltable_dict
        if _TRAITS_SECTION_KEY not in mltable_dict[_METADATA_KEY]:
            mltable_dict[_METADATA_KEY][_TRAITS_SECTION_KEY] = \
                {col_name: col_value}
        else:
            mltable_dict[_METADATA_KEY][_TRAITS_SECTION_KEY][col_name] = col_value

        # TODO move this to imports on dataflow release
        try:
            from azureml.dataprep.rslex import PyRsDataflow
            mltable_yaml_string = yaml.dump(mltable_dict)
            self._mltable._dataflow = PyRsDataflow(mltable_yaml_string)
        except ImportError:
            _get_logger().warn('Not able to import PyRsDataflow')
        except Exception as ex:
            raise ex

    @property
    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def timestamp_column(self):
        """
        If set returns the name of the timestamp column, else rasies a KeyError

        :return: If set, returns the name of the timestamp column.
        :rtype: str
        """
        col = self._check_and_get_trait_col(_TIMESTAMP_COLUMN_KEY)
        if col is None:
            raise KeyError('Timestamp column does not appear to be set. Please make sure you have set it.')
        return col

    @timestamp_column.setter
    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def timestamp_column(self, column_name):
        """
        Setter for timestamp_column trait.

        :param column_name: Name of the timestamp column.
        :type column_name: str
        """
        if not isinstance(column_name, str):
            raise TypeError(f'An object of type string is expected, but encountered type: {type(column_name)}')
        self._set_trait_col(_TIMESTAMP_COLUMN_KEY, column_name)

    @property
    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def index_columns(self):
        """
        If set returns a list of index columns' names, else raises a KeyError

        :return: If set, returns the list containing the names of index columns.
        :rtype: list[str]
        """
        col = self._check_and_get_trait_col(_INDEX_COLUMNS_KEY)
        if col is None:
            raise KeyError('Index columns do not appear to be set. Please make sure you have set them.')
        return col

    @index_columns.setter
    @track(_get_logger, custom_dimensions={'app_name': 'MLTable'})
    def index_columns(self, index_columns_list):
        """
        Setter for index_columns trait.

        :param index_columns_list: List containing names of index columns.
        :type index_columns_list: list[str]
        """
        if index_columns_list and not isinstance(index_columns_list, list):
            raise TypeError(f'An object of type list is expected, but encountered type: {type(index_columns_list)}')
        self._set_trait_col(_INDEX_COLUMNS_KEY, index_columns_list)
