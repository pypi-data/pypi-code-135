"""Timeseer Client allows querying of data and metadata."""

import json
import time

try:
    import yaml

    HAS_YAML = True
except ImportError:
    HAS_YAML = False


from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Union, Tuple

from kukur import Metadata, SeriesSelector
from kukur.client import Client as KukurClient
import kukur.config

import pyarrow as pa
import pyarrow.flight as fl

from timeseer_client.internal import MissingModuleException


class Client(KukurClient):
    """Client connects to Timeseer using Arrow Flight."""

    def upload_data(
        self,
        metadata_or_data: Union[Metadata, List[Tuple[Metadata, pa.Table]]],
        table: Optional[pa.Table] = None,
        *,
        analyze=True,
        block=True,
    ):
        """Upload time series data to Timeseer.

        This requires a configured 'flight-upload' source in Timeseer.

        There are two ways to call this method.

        One requires two arguments:
            metadata: any known metadata about the time series. This will be merged with the metadata
                already known by Timeseer depending on the source configuration. The source of the series should match
                the source name of a 'flight-upload' source.
            table: a pyarrow.Table of two columns.
                The first column with name 'ts' contains Arrow timestamps.
                The second column with name 'value' contains the values as a number or string.

        The second accepts a list of tuples of the same arguments. This allows uploading multiple time series at the
        same time.

        When `analyze` is `True`, start a flow evaluation.
        When `block` is `True`, block execution until the flow evaluation is done.
        """
        if table is not None:
            assert isinstance(metadata_or_data, Metadata)
            self._upload_data_single(metadata_or_data, table, analyze, block)
        else:
            assert not isinstance(metadata_or_data, Metadata)
            self._upload_data_multiple(metadata_or_data, analyze, block)

    def _upload_data_single(
        self, metadata: Metadata, table: pa.Table, analyze: bool, block: bool
    ):
        self._upload_data_multiple([(metadata, table)], analyze, block)

    def _upload_data_multiple(
        self, many_series: List[Tuple[Metadata, pa.Table]], analyze: bool, block: bool
    ):
        client = self._get_client()
        selectors = []
        for metadata, table in many_series:
            metadata_json = metadata.to_data()
            selector = SeriesSelector.from_tags(
                metadata.series.source, metadata.series.tags, metadata.series.field
            )
            selectors.append(selector)
            descriptor = fl.FlightDescriptor.for_command(
                json.dumps(
                    dict(
                        metadata=metadata_json,
                    )
                )
            )
            writer, reader = client.do_put(descriptor, table.schema)
            writer.write_table(table)
            writer.done_writing()
            buf: pa.Buffer = reader.read()
            response: Dict = json.loads(buf.to_pybytes())
            writer.close()

        if "flowName" in response:
            if analyze:
                _analyze_flow(
                    client, response["flowName"], limitations=selectors, block=block
                )
        elif block and "flow_evaluation_group_id" in response:
            _wait_for_flow_evaluation(client, response)

    def evaluate_flow(self, flow_name: str, *, block=True):
        """Evaluate a flow.

        Args:
            flow_name: the name of the flow to evaluate
            block: block until the evaluation completes (keyword-only, default True)
        """
        client = self._get_client()
        _analyze_flow(client, flow_name, block=block)

    def duplicate_flow(  # pylint:disable=too-many-arguments
        self,
        existing_flow_name: str,
        new_flow_name: str,
        *,
        series_set_names: List[str] = None,
        start_date: datetime = None,
        end_date: datetime = None,
        data_set_name: str = None,
    ):
        """Duplicate an existing flow.

        Args:
            existing_flow_name: the name of the flow to duplicate.
            new_flow_name: the name of the duplicated flow.
            series_set_name: the name of an existing series set to be used in the flow. (Optional).
            start_date: the start date of the flow (Optional).
            end_date: the end date of the flow (Optional).
            data_set_name: the name of the data set to use for the flow (Optional).
        """

        body: Dict = dict(
            existingFlowName=existing_flow_name,
            newFlowName=new_flow_name,
            seriesSetNames=series_set_names,
            dataSetName=data_set_name,
        )
        if start_date is not None:
            body["startDate"] = start_date.isoformat()
        if end_date is not None:
            body["endDate"] = end_date.isoformat()
        self._get_client().do_action(("duplicate_flow", json.dumps(body).encode()))

    def get_event_frames(
        self,
        selector: SeriesSelector,
        start_date: datetime = None,
        end_date: datetime = None,
        frame_type: Union[str, List[str]] = None,
    ) -> pa.Table:
        """Get all event frames matching the given criteria.

        Args:
            selector: the time series source, exposed flow or time series to which the event frames are linked.
            start_date: the start date of the range to find overlapping event frames in. Defaults to one year ago.
            end_date: the end date of the range to find overlapping event frames in. Defaults to now.
            frame_type: the type or types of event frames to search for. Finds all types when empty.

        Returns::
            A pyarrow Table with 6 columns.
            The first column ('start_date') contains the start date.
            The second column ('end_date') contains the end date.
            The third column ('type') contains the type of the returned event frame as a string.
            The fourth column ('explanation') can contain the explanation for an event frame as a string.
            The fifth column ('status') can contain the status of an event frame as a string.
            Columns 6 contains possible multiple references for the event frame.
        """
        if start_date is None or end_date is None:
            now = datetime.utcnow().replace(tzinfo=timezone(timedelta(0)))
            if start_date is None:
                start_date = now.replace(year=now.year - 1)
            if end_date is None:
                end_date = now

        query: Dict[str, Any] = {
            "query": "get_event_frames",
            "selector": selector.to_data(),
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
        }

        if frame_type is not None:
            query["type"] = frame_type

        ticket = fl.Ticket(json.dumps(query))
        return self._get_client().do_get(ticket).read_all()

    def get_data_quality_score_data_sources(
        self, source_names: List[str]
    ) -> Dict[str, int]:
        """Get the data quality score of a data source or exposed flow.

        Args:
            source_names: A list of time series sources or Flight Expose blocks

        Returns::
            A data quality score of every given source as a percentage.
        """
        body = {
            "source_names": source_names,
        }
        results = list(
            self._get_client().do_action(
                ("get_data_quality_score_data_sources", json.dumps(body).encode())
            )
        )
        return json.loads(results[0].body.to_pybytes())

    def get_kpi_scores(
        self,
        source_name: str,
    ) -> Dict[str, Dict[str, int]]:
        """Get the kpi scores of a data source or exposed flow.

        Args:
            source_name: The time series source or the name of the Flight Expose block.

        Returns::
            The score per KPI as a percentage, keyed by the source_name provided.
        """
        body = {
            "source_name": source_name,
        }

        results = list(
            self._get_client().do_action(("get_kpi_scores", json.dumps(body).encode()))
        )
        return json.loads(results[0].body.to_pybytes())

    def get_series_results(
        self, selector: SeriesSelector
    ) -> List[Dict[str, Union[str, float]]]:
        """Return the univariate check results for the given series.

        Args:
            selector: The time series to return results for.

        Returns::
            A list of check results, where each check result is a dictionary with 'name' and 'result'.
            The result is returned as a floating point number between 0.0 (bad) and 1.0 (good)."""
        body = {
            "selector": selector.to_data(),
        }
        results = list(
            self._get_client().do_action(
                ("get_series_results", json.dumps(body).encode())
            )
        )
        return json.loads(results[0].body.to_pybytes())

    def get_series_statistics(self, selector: SeriesSelector) -> List[Dict[str, Any]]:
        """Return the univariate statistics for the given series.

        Args:
            selector: The time series to return statistics for.

        Returns::
            A list of statistics. Each statistic is a dict with three fields:
              - name (str)
              - dataType (str) - one of 'float', 'pct', 'datetime', 'hidden', 'table'
              - result (exact type depending on the dataType)"""
        body = {"selector": selector.to_data()}
        results = list(
            self._get_client().do_action(
                ("get_series_statistics", json.dumps(body).encode())
            )
        )
        return json.loads(results[0].body.to_pybytes())

    def remove_data(self, selector: SeriesSelector):
        """Removes the series indicated by the SeriesSelector and related files.
           The source in the selector should match the source name of a
           'flight-upload' source.

        Args:
            selector: The time series to be removed. If selector contains no series
            name then all the series on the given source are removed.
        """
        body = {"selector": selector.to_data()}

        self._get_client().do_action(("remove_series", json.dumps(body).encode()))

    def list_flows(self) -> List[str]:
        """Return a list containing all the flow names."""
        results = list(
            self._get_client().do_action(("get_flows", json.dumps({}).encode()))
        )
        return list(json.loads(results[0].body.to_pybytes()))

    def list_exposed_blocks(self, flow_name: str) -> Dict[str, List[str]]:
        """Return a dictionary containing all the exposed blocks names per series set.

        Args:
            flow_name: The name of the flow.

        Returns::
            The names of the exposed blocks in a flow per series set.
        """

        body = {"flowName": flow_name}

        results = list(
            self._get_client().do_action(
                ("get_exposed_blocks", json.dumps(body).encode())
            )
        )
        return json.loads(results[0].body.to_pybytes())

    def list_data_services(self) -> List[str]:
        """Return a list containing all the data service names."""
        results = list(
            self._get_client().do_action(
                ("list_data_services", json.dumps({}).encode())
            )
        )
        return list(json.loads(results[0].body.to_pybytes()))

    def get_data_service_kpi_scores(
        self, data_service_name: str, view: str
    ) -> Dict[str, int]:
        """Get the kpi scores of a data service.

        Args:
            data_service_name: The name of the Data Service.
            view: The series set name.

        Returns::
            The score per KPI as a percentage, keyed by the series set name included in the data service.
        """
        body = {
            "data_service_name": data_service_name,
            "view": view,
        }

        results = list(
            self._get_client().do_action(
                ("get_data_service_kpi_scores", json.dumps(body).encode())
            )
        )
        return json.loads(results[0].body.to_pybytes())

    def get_data_service_event_frames(  # pylint:disable=too-many-arguments
        self,
        data_service_name: str,
        view: str,
        selector: SeriesSelector = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        frame_type: Union[str, List[str]] = None,
    ) -> pa.Table:
        """Get all event frames matching the given criteria.

        Args:
            data_service_name: The Data Service name to which the event frames are linked.
            view: The series set name to which the event frames are linked
            selector: the time series to which the event frames are linked.
            start_date: the start date of the range to find overlapping event frames in.
                Defaults to start date of the data service.
            end_date: the end date of the range to find overlapping event frames in.
                Defaults to end date of the data service.
            frame_type: the type or types of event frames to search for. Finds all types when empty.

        Returns::
            A pyarrow Table with 6 columns.
            The first column ('start_date') contains the start date.
            The second column ('end_date') contains the end date.
            The third column ('type') contains the type of the returned event frame as a string.
            The fourth column ('explanation') can contain the explanation for an event frame as a string.
            The fifth column ('status') can contain the status of an event frame as a string.
            Columns 6 contains possible multiple references for the event frame.
            The seventh column contains the uuid of the event frame.
        """

        query: Dict[str, Any] = {
            "query": "get_data_service_event_frames",
            "data_service_name": data_service_name,
            "view": view,
            "selector": selector.to_data() if selector is not None else None,
            "start_date": start_date.isoformat() if start_date is not None else None,
            "end_date": end_date.isoformat() if end_date is not None else None,
        }

        if frame_type is not None:
            query["type"] = frame_type

        ticket = fl.Ticket(json.dumps(query))
        return self._get_client().do_get(ticket).read_all()

    def create_resources(
        self,
        resources: List[Dict] = None,
        *,
        resource: Dict = None,
        path: Optional[Union[Path, str]] = None,
    ):
        """Create resources by supplying one resource, multiple resources or a filename.

        Args:
            resources: a list containing the resource definitions.
            resource: One resource definition.
            path: A path to the file or filename of a resource definition.
                This can be in yaml, toml or json format.
        """
        all_resources = []
        if resources is not None:
            all_resources.extend(resources)
        if resource is not None:
            all_resources.append(resource)
        if path is not None:
            if isinstance(path, str):
                path = Path(path)
            if path.suffix in [".yml", ".yaml"]:
                if not HAS_YAML:
                    raise MissingModuleException("PyYAML")
                all_resources.extend(_read_yaml(path))
            elif path.suffix == ".toml":
                all_resources.extend(_read_toml(path))
            elif path.suffix == ".json":
                all_resources.extend(_read_json(path))
        body = dict(
            resources=all_resources,
        )

        self._get_client().do_action(("create_resources", json.dumps(body).encode()))

    def remove_resources(
        self,
        resources: List[Dict] = None,
        *,
        resource: Dict = None,
    ):
        """Remove resources.

        Args:
            resources: A list containing the resources to remove.
            resource: A dictionary of the resource to remove, type and name has to be present.
        """
        all_resources = []
        if resources is not None:
            all_resources.extend(resources)
        if resource is not None:
            all_resources.append(resource)

        body = dict(
            resources=all_resources,
        )

        self._get_client().do_action(("remove_resources", json.dumps(body).encode()))


def _analyze_flow(
    client: fl.FlightClient,
    flow_name: str,
    *,
    limitations: Optional[List[SeriesSelector]] = None,
    block=True,
):
    flow: Dict = dict(flowName=flow_name)
    if limitations is not None:
        flow["limitations"] = [selector.to_data() for selector in limitations]
    results = list(client.do_action(("evaluate_flow", json.dumps(flow).encode())))
    response = json.loads(results[0].body.to_pybytes())

    if block:
        _wait_for_flow_evaluation(client, response)


def _wait_for_flow_evaluation(client: fl.FlightClient, response: Dict):
    while True:
        results = list(
            client.do_action(
                ("get_flow_evaluation_state", json.dumps(response).encode())
            )
        )
        state = json.loads(results[0].body.to_pybytes())
        if (
            state["completed"] == state["total"]
            and state["blockCompleted"] == state["blockTotal"]
        ):
            break
        time.sleep(1)


def _read_yaml(path: Path) -> List[Dict]:
    with path.open() as file:
        return yaml.safe_load(file)


def _read_toml(path) -> List[Dict]:
    config = kukur.config.from_toml(path)
    return config["resource"]


def _read_json(path: Path) -> List[Dict]:
    with path.open() as file:
        return json.load(file)
