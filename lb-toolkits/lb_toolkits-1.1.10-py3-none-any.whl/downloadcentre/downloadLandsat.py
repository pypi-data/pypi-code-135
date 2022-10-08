# -*- coding:utf-8 -*-
'''
@Project  : lb_toolkits

@File     : downloadLandsat.py

@Modify Time : 2022/8/11 15:34

@Author : Lee

@Version : 1.0

@Description :

'''
import datetime

from lb_toolkits.utils.api import API
from lb_toolkits.utils.earthexplorer import EarthExplorer


class downloadLandsat():

    def __init__(self, username, password):
        self.username = username
        self.password = password


    def searchlandsat(self, product,
                      startdate, enddate=None,
                      longitude=None, latitude=None,
                      bbox=None, cloud_cover_max=None,
                      months=None, max_results=100):
        '''
        Search for scenes.

        Parameters
        ----------
        product: str
                Case-insensitive dataset alias (e.g. landsat_tm_c1).
                LANDSAT_TM_C1、LANDSAT_ETM_C1和LANDSAT_8_C1
        longitude : float, optional
                Longitude of the point of interest.
        latitude : float, optional
                Latitude of the point of interest.
        bbox : tuple, optional
                (xmin, ymin, xmax, ymax) of the bounding box.
        cloud_cover_max: int, optional
                Max. cloud cover in percent (1-100).
        startdate: datetime
                YYYY-MM-DD
        enddate : datetime, optional
                YYYY-MM-DD. Equal to startdate if not provided.
        months: list of int, optional
                Limit results to specific months (1-12).
        max_results: int, optional
                Max. number of results. Defaults to 100.

        Returns
        -------
            list of dict
                Matching scenes as a list of dict containing metadata.
        '''
        if enddate is None :
            enddate = startdate

        start_date = startdate.strftime('%Y-%m-%d')
        end_date   = enddate.strftime('%Y-%m-%d')
        api = API(self.username, self.password)

        scenes = api.search(dataset=product,
            latitude=latitude,     longitude=longitude,
            start_date=start_date, end_date=end_date,
            bbox = bbox,           max_cloud_cover=cloud_cover_max,
            months=months,         max_results=max_results)

        print('{} scenes found.'.format(len(scenes)))
        api.logout()

        return scenes

    def downloadlandsat(self, Landsat_name, output_dir,
                        scene_id=None, retry=3, timeout=5*60):
        '''
        Download a Landsat scene.

        Parameters
        ----------
        Landsat_name
        output_dir: str;
            Output directory. Automatically created if it does not exist.
        scene_id: str, optional
        retry: int, optional
            尝试失败次数
        timeout : int, optional
        Connection timeout in seconds.:

        Returns
        -------
            str
            Path to downloaded file.
        '''

        if scene_id is not None:
            Earth_Down = EarthExplorer(self.username, self.password)
            Earth_Down.download(identifier=scene_id, output_dir=output_dir, timeout=timeout)
            Earth_Down.logout()

            return None

        for scene in Landsat_name:
            for i in range(retry) :
                try:
                    Earth_Down = EarthExplorer(self.username, self.password)
                    ID = scene['entity_id']
                    # IDpro = ID[3:9]
                    Earth_Down.download(identifier=ID, output_dir=output_dir, timeout=timeout)
                    Earth_Down.logout()
                    break
                except BaseException as e :
                    continue

