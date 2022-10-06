#!/usr/bin/env python3

from SimConnect.RequestList import RequestHelper


class NewRequestFeatures:
    def add_features(self, sim_integration):
        CameraList = Camera(sim_integration.sm)
        sim_integration.get_aircraft_requests().list.append(CameraList)


class Camera(RequestHelper):
    list = {
        "CAMERA_STATE": ["Camera state", b'CAMERA STATE',  b'Enum', 'Y'],
        "CAMERA_VIEW_TYPE_AND_INDEX:index": ["Camera view and type", b'CAMERA VIEW TYPE AND INDEX:index',  b'Enum', 'Y'],
        "COCKPIT_CAMERA_HEIGHT": ["Camera state", b'COCKPIT CAMERA HEIGHT',  b'Percent', 'Y'],
        "COCKPIT_CAMERA_UPPER_POSITION": ["Camera state", b'COCKPIT CAMERA UPPER POSITION',  b'Bool', 'Y'],
        "CAMERA_REQUEST_ACTION": ["Camera reset", b'CAMERA REQUEST ACTION',  b'Enum', 'Y'],
        "PLANE_TOUCHDOWN_NORMAL_VELOCITY": ["Touchdown velocity", b'PLANE TOUCHDOWN NORMAL VELOCITY',  b'Feet per second', 'N'],
        "FLY_ASSISTANT_RIBBONS_ACTIVE": ["Returns true when both ribbon assistances are active (taxi and landing), and can also be used to set them.", b'FLY ASSISTANT RIBBONS ACTIVE', b'Bool', 'Y'],
        "FLY_ASSISTANT_LANDING_SPEED": ["Returns the POH range or an estimated value for this speed.", b'FLY ASSISTANT LANDING SPEED', b'String', 'N'],
        "GENERAL_ENG_REVERSE_THRUST_ENGAGED": ["This will return 1 (TRUE) if the reverse thruster is engaged, or 0 (FALSE) otherwise.", b'GENERAL ENG REVERSE THRUST ENGAGED', b'Bool', 'N'],
    }
