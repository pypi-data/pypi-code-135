#  Copyright (c) 2022.  Eugene Popov.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

from witness.core.abstract import AbstractBatch
import pickle


class Batch(AbstractBatch):
    """
    Central class of entire lib.
    Able to store standardized data structure
    containing data in form of records and metadata dictionary.
    """

    __slots__ = ('data', 'meta')

    def __init__(self, data=None, meta=None):

        self.data: list or None = data
        self.meta: dict or None = meta
        self.is_restored = False

    def info(self):

        if self.meta is None and self.data is None:
            return 'Batch object is not containing any data.'

        number_of_records = len(self.data) if self.data is not None else None

        message = f"""
        Number of records: {number_of_records}
        Was {'restored from dump ' + f"{self.meta['dump_uri']}" if self.is_restored else 'originally extracted'}
        Source: {self.meta['record_source']}
        Extraction datetime: {self.meta['extraction_timestamp']}
        """

        try:
            message = message + f"Tags: {self.meta['tags']}\n"
        except KeyError:
            pass

        return message

    def fill(self, extractor):
        """
        Fills batch internal datastructures using
        the extractor passed in.
        """
        output = extractor.extract().unify().output
        setattr(self, 'data', output['data'])
        setattr(self, 'meta', output['meta'])
        return self

    def push(self, loader, meta_elements: [list[str]] or None = None):
        """
        Pushes data, with the appropriate meta attached,
        to the store defined by the loader passed in.
        """
        loader.prepare(self).attach_meta(meta_elements).load()
        return self

    def _register_dump(self, uri):
        self.meta['dump_uri'] = uri

    def dump(self, uri):
        """
        Dumps batch data to pickle file with defined uri.
        """
        with open(uri, 'wb') as file:
            pickle.dump(self.data, file)
        self._register_dump(uri)

    def restore(self, uri=None):
        """
        Fills batch with data from dump.
        If no dump uri provided it'll try search in batch meta.
        """
        uri = self.meta['dump_uri'] if uri is None else uri
        with open(uri, 'rb') as file:
            output = pickle.load(file)
        setattr(self, 'data', output)
        self.is_restored = True
        return self

