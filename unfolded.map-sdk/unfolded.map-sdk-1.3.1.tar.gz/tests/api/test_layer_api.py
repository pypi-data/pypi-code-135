from tests._utils import check_expected_comm_message
from tests.conftest import MockComm
from unfolded.map_sdk.map.widget import SyncWidgetMap


class TestGetLayers:
    def test_widget_message(self, mock_comm: MockComm):
        m = SyncWidgetMap()
        m.get_layers()

        expected = {
            "type": "v1/map-sdk-get-layers",
            "args": [],
        }

        assert check_expected_comm_message(expected, mock_comm.log_send)


class TestGetLayerById:
    def test_widget_message(self, mock_comm: MockComm):
        m = SyncWidgetMap()
        m.get_layer_by_id("layer-id")

        expected = {
            "type": "v1/map-sdk-get-layer-by-id",
            "args": ["layer-id"],
        }

        assert check_expected_comm_message(expected, mock_comm.log_send)


class TestAddLayer:
    @property
    def expected(self):
        return {
            "type": "v1/map-sdk-add-layer",
            "args": [
                {"id": "layer-id", "dataId": "data-1", "fields": {"field-1": "value-1"}}
            ],
        }

    def test_widget_message(self, mock_comm: MockComm):
        m = SyncWidgetMap()
        layer = {
            "id": "layer-id",
            "data_id": "data-1",
            "fields": {"field-1": "value-1"},
        }

        m.add_layer(layer)

        assert check_expected_comm_message(self.expected, mock_comm.log_send)

    def test_widget_message_kwargs(self, mock_comm: MockComm):
        m = SyncWidgetMap()
        layer = {
            "id": "layer-id",
            "data_id": "data-1",
            "fields": {"field-1": "value-1"},
        }

        m.add_layer(**layer)

        assert check_expected_comm_message(self.expected, mock_comm.log_send)

    def test_add_layer_with_config(self, mock_comm: MockComm):
        m = SyncWidgetMap()
        layer_id = "earthquake_points"
        dataset_id = "dataset-id"
        layer = {
            "id": layer_id,
            "type": "point",
            "data_id": dataset_id,
            "label": "Earthquakes",
            "is_visible": True,
            "fields": {"lat": "Latitude", "lng": "Longitude"},
            "config": {
                "visual_channels": {
                    "colorField": {"name": "Depth", "type": "real"},
                }
            },
        }
        m.add_layer(layer)

        expected = {
            "type": "v1/map-sdk-add-layer",
            "args": [
                {
                    "id": layer_id,
                    "type": "point",
                    "dataId": dataset_id,
                    "label": "Earthquakes",
                    "isVisible": True,
                    "fields": {"lat": "Latitude", "lng": "Longitude"},
                    "config": {
                        "visualChannels": {
                            "colorField": {"name": "Depth", "type": "real"},
                        }
                    },
                }
            ],
        }
        assert check_expected_comm_message(expected, mock_comm.log_send)


class TestUpdateLayer:
    @property
    def expected(self):
        return {
            "type": "v1/map-sdk-update-layer",
            "args": [
                "layer-id",
                {"fields": {"field-1": "value-1"}},
            ],
        }

    def test_widget_message(self, mock_comm: MockComm):
        m = SyncWidgetMap()
        values = {"fields": {"field-1": "value-1"}}
        m.update_layer("layer-id", values)

        assert check_expected_comm_message(self.expected, mock_comm.log_send)

    def test_widget_message_kwargs(self, mock_comm: MockComm):
        m = SyncWidgetMap()
        values = {"fields": {"field-1": "value-1"}}
        m.update_layer("layer-id", **values)

        assert check_expected_comm_message(self.expected, mock_comm.log_send)


class TestRemoveLayer:
    def test_widget_message(self, mock_comm: MockComm):
        m = SyncWidgetMap()

        m.remove_layer("layer-id")

        expected = {
            "type": "v1/map-sdk-remove-layer",
            "args": ["layer-id"],
        }

        assert check_expected_comm_message(expected, mock_comm.log_send)


class TestGetLayerGroups:
    def test_widget_message(self, mock_comm: MockComm):
        m = SyncWidgetMap()
        m.get_layer_groups()

        expected = {
            "type": "v1/map-sdk-get-layer-groups",
            "args": [],
        }

        assert check_expected_comm_message(expected, mock_comm.log_send)


class TestGetLayerGroupById:
    def test_widget_message(self, mock_comm: MockComm):
        m = SyncWidgetMap()
        m.get_layer_group_by_id("layer-group-id")

        expected = {
            "type": "v1/map-sdk-get-layer-group-by-id",
            "args": ["layer-group-id"],
        }

        assert check_expected_comm_message(expected, mock_comm.log_send)


class TestAddLayerGroupAction:
    @property
    def expected(self):
        return {
            "type": "v1/map-sdk-add-layer-group",
            "args": [
                {"id": "layer-group-id", "label": "layer-group-1", "isVisible": False}
            ],
        }

    def test_widget_message(self, mock_comm: MockComm):
        m = SyncWidgetMap()

        layer_group = {
            "id": "layer-group-id",
            "label": "layer-group-1",
            "is_visible": False,
        }
        m.add_layer_group(layer_group)

        assert check_expected_comm_message(self.expected, mock_comm.log_send)

    def test_widget_message_kwargs(self, mock_comm: MockComm):
        m = SyncWidgetMap()

        layer_group = {
            "id": "layer-group-id",
            "label": "layer-group-1",
            "is_visible": False,
        }
        m.add_layer_group(**layer_group)

        assert check_expected_comm_message(self.expected, mock_comm.log_send)


class TestUpdateLayerGroupAction:
    @property
    def expected(self):
        return {
            "type": "v1/map-sdk-update-layer-group",
            "args": [
                "layer-group-id",
                {"label": "layer-group-2"},
            ],
        }

    def test_widget_message(self, mock_comm: MockComm):
        m = SyncWidgetMap()
        values = {"label": "layer-group-2"}
        m.update_layer_group("layer-group-id", values)

        assert check_expected_comm_message(self.expected, mock_comm.log_send)

    def test_widget_message_kwargs(self, mock_comm: MockComm):
        m = SyncWidgetMap()
        values = {"label": "layer-group-2"}
        m.update_layer_group("layer-group-id", **values)

        assert check_expected_comm_message(self.expected, mock_comm.log_send)


class TestRemoveLayerGroup:
    def test_widget_message(self, mock_comm: MockComm):
        m = SyncWidgetMap()

        m.remove_layer_group("layer-group-id")

        expected = {
            "type": "v1/map-sdk-remove-layer-group",
            "args": ["layer-group-id"],
        }

        assert check_expected_comm_message(expected, mock_comm.log_send)


class TestGetLayerTimeline:
    def test_widget_message(self, mock_comm: MockComm):
        m = SyncWidgetMap()
        m.get_layer_timeline()

        expected = {
            "type": "v1/map-sdk-get-layer-timeline",
            "args": [],
        }

        assert check_expected_comm_message(expected, mock_comm.log_send)


class TestUpdateLayerTimeline:
    @property
    def expected(self):
        return {
            "type": "v1/map-sdk-update-layer-timeline",
            "args": [{"currentTime": 0}],
        }

    def test_widget_message(self, mock_comm: MockComm):
        m = SyncWidgetMap()
        m.update_layer_timeline({"current_time": 0})

        assert check_expected_comm_message(self.expected, mock_comm.log_send)

    def test_widget_message_kwargs(self, mock_comm: MockComm):
        m = SyncWidgetMap()
        m.update_layer_timeline(**{"current_time": 0})

        assert check_expected_comm_message(self.expected, mock_comm.log_send)
