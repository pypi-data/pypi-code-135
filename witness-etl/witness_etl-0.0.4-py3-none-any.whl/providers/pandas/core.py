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

import pandas as pd
import logging
import pickle
from witness.core.abstract import AbstractBatch, AbstractLoader, AbstractExtractor

log = logging.getLogger(__name__)


class PandasBatch(AbstractBatch):

    __slots__ = ('data', 'meta')

    def __init__(self, data=None, meta=None):
        self.data: pd.DataFrame or None = data
        self.meta: dict or None = meta
        self.is_restored = False

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

    def info(self):
        pass


class PandasLoader(AbstractLoader):

    def __init__(self, uri):
        super().__init__(uri)

    def prepare(self, batch):
        super().prepare(batch)
        df = pd.DataFrame(batch.data, dtype='str')
        self.output = df
        return self

    def attach_meta(self, meta_elements: [list[str]] or None = None):
        try:
            meta = self.batch.meta
            for element in meta:
                meta[element] = str(meta[element])
        except AttributeError:
            log.exception('No batch object was passed to loader.'
                          'Pass a batch object to "prepare" method first.')
            raise AttributeError('No batch object was passed to loader')
        if meta_elements is None:
            for element in meta:
                self.output[element] = meta[element]
        else:
            for element in meta_elements:
                self.output[element] = meta[element]

        return self

    def load(self):
        raise NotImplementedError
