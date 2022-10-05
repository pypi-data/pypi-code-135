
import json
import geojson
import zipfile
import io

from pathlib import Path
from typing import Dict, List, Union
from intelinair_utils import AgmriApi

ANNOTATION_URL_TEMPLATE = 'https://api.{}.intelinair.dev/admin/graphql/index'


class AnnotationsApi:

    def __init__(self, agmri_env: str):
        self.api = AgmriApi(agmri_env)

    def list_annotation_types(self, api_limit_size: int = 100):
        offset = 0
        while True:
            query = """
            query { 
              listTagOptions( 
                max: %s
                offset: %s 
                queryCommand: {
                  domain: "Annotation"
                }
              ) { 
                results { 
                  id 
                  name 
                  description 
                  type {
                    id
                    name
                    keyName
                    domainName
                    __typename
                  }
                  color   
                  __typename 
                } 
                totalCount 
                __typename 
              } 
            } 
            """ % (api_limit_size, offset)

            response = self.api.graphql_request('admin', query=query)

            for tag_option in response['data']['listTagOptions']['results']:
                yield tag_option

            if api_limit_size + offset < response['data']['listTagOptions']['totalCount']:
                offset += api_limit_size
            else:
                break

    def create_annotation_project(self, name: str, description: str = "", label_ids: List[int] = None):
        """Create annotation project.

        Args:
            name: name of created project
            description: description for the project
            label_ids: labels used in the project

        Returns: integer project id

        """
        api_key = 'projectCreate'
        payload = """mutation {
          %s(project: {
                        name: \"%s\",
                        description : \"%s\",
                        labelIds: %s
                                }
                        )
                        {
                            id
                            name
                            description
                            labelIds
                            status
                            errors {
                                message
                            }
                        }
                    }""" % (api_key, name,
                            description,
                            str([] if label_ids is None else label_ids))

        response = self._make_request(payload=payload, api_key=api_key)
        return response['data'][api_key]['id']

    def list_annotation_projects(self, api_limit_size=100):
        offset = 0
        while True:
            query = """
            query { 
              listProjects( 
                max: %s 
                offset: %s 
                queryCommand: {}
              ) { 
                results { 
                  id 
                  name 
                  description 
                  labels { 
                    id 
                    name 
                    color 
                    type { 
                      id 
                      domainName 
                      __typename 
                    } 
                    __typename 
                  } 
                  members { 
                    id 
                    user { 
                      id 
                      token 
                      firstname 
                      lastname 
                      __typename 
                    } 
                    __typename 
                  } 
                  status 
                  configs 
                  __typename 
                } 
                totalCount 
                __typename 
              } 
            } 
            """ % (api_limit_size, offset)

            response = self.api.graphql_request('admin', query=query)

            for project in response['data']['listProjects']['results']:
                yield project

            if api_limit_size + offset < response['data']['listProjects']['totalCount']:
                offset += api_limit_size
            else:
                break

    def delete_annotation_project(self, project_id: int):
        query = """
        mutation  {
          projectDelete(id: %s) {
            success
            error
            __typename
          }
        }
        """ % (project_id,)

        response = self.api.graphql_request('admin', query=query)
        assert response['data']['projectDelete']['success'], 'Failed to delete project'

    def create_annotatable_flight(self, project_id: int, flight_id: int):
        """Create annotatable flight out of ordinary flight.

        Args:
            project_id: project in which to create annotatable flight
            flight_id: ordinary flight id

        Returns:
            id of created annotatable flight

        """
        api_key = 'annotatableFlightCreate'
        payload = """mutation {
                  %s(annotatableFlight: {
                                project : {
                                      id : %d
                                    }
                                flight : {
                                     id : %d
                                    }
                                }
                  )
                  {
                    id
                    errors {
                        message
                    }
                  }
                }""" % (api_key, project_id, flight_id)
        response = self._make_request(payload=payload, api_key=api_key)
        return response['data'][api_key]['id']

    def list_annotatable_flights(self, project_id: int, api_limit_size: int = 100):
        offset = 0
        while True:
            query = """
            query { 
              listAnnotatableFlights( 
                max: %s
                offset: %s 
                queryCommand: {
                  projectId: %s
                }
              ) { 
                results { 
                  id 
                  assignee {
                    id
                    user {
                      id
                      username
                      __typename
                    }
                    __typename
                  }
                  status
                  project {
                    id
                    __typename
                  }
                  flight {
                    id
                    code
                    __typename
                  }
                  notes
                  groupNumber   
                  __typename 
                } 
                totalCount 
                __typename 
              } 
            } 
            """ % (api_limit_size, offset, project_id)

            response = self.api.graphql_request('admin', query=query)

            for annotatable_flight in response['data']['listAnnotatableFlights']['results']:
                yield annotatable_flight

            if api_limit_size + offset < response['data']['listAnnotatableFlights']['totalCount']:
                offset += api_limit_size
            else:
                break

    def add_annotations(self, annotatable_flight_id: int, polygons: Dict, labels: List[str]):
        """Add annotation to annotatable flight.

        Args:
            annotatable_flight_id: id of flight to add annotation
            polygons: polygons to add as annotation
            labels: string annotation labels

        Returns:
            response from api call

        """
        api_key = 'annotationCreate'
        payload = """
                mutation {
                  %s(annotation: {
                      flight: {
                          id  : %d
                          },
                      color: \"#FF9A34\"
                      labels: %s
                      geometry: \"%s\"
                  }) {
                id
                labels
                errors {
                    message
                }                
            }
        }""" % (api_key,
                annotatable_flight_id,
                json.dumps(labels) if labels else '[]',
                geojson.dumps(polygons).replace('"', '\\"'))
        response = self._make_request(payload=payload, api_key=api_key)
        return response

    def download_annotations(self, project_id: int, output_path: Union[str, Path]):
        response = self.api.post('/annotations/export', ignore_json=True, params={
            "projectId": project_id,
            "flightCode": None,
            "labelIds": None
        })

        annotations_zipfile = zipfile.ZipFile(io.BytesIO(response.content))
        assert len(annotations_zipfile.filelist) == 1
        annotations = annotations_zipfile.read(annotations_zipfile.filelist[0])
        with open(output_path, 'wb') as fp:
            fp.write(annotations)

    def _make_request(self, payload: str, api_key: str):
        """Make actual call to graphql with provided payload.

        Args:
            payload: request payload
            api_key: name of api in use

        Returns:

        """
        response = self.api.graphql_request(service='admin', query=payload)
        errors = response["errors"] if 'errors' in response else response["data"][api_key].get("errors")
        if errors:
            raise Exception(f'Errors while making api request to {api_key}: {errors}')
        return response
