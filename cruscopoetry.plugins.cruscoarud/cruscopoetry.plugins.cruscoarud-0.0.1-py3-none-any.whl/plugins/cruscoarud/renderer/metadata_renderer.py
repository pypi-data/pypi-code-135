#    This file is part of CruscoPoetry.
#
#    CruscoPoetry is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    CruscoPoetry is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with CruscoPoetry.  If not, see <http://www.gnu.org/licenses/>.
from cruscopoetry.core.renderers.htmlrenderer.metadata_renderer import HtmlMetadataRenderer
from cruscopoetry.core.jsonparser import JsonMetadata, JsonTranslations
from ..common.metric_elements import MetricElements
from typing import Tuple


class CruscoArudMetadataRenderer(HtmlMetadataRenderer):
	
	def __init__(self, metadata: JsonMetadata, translations: JsonTranslations, elements: MetricElements):
		super().__init__(metadata, translations)
		self._elements = elements if elements != None else MetricElements()
		self.metre, self.form = self._get_metre_and_form()

	def _get_metre_and_form(self) -> Tuple[int, int]:
		#we get metre information from the metadata:
		try:
			metre_info = self.metadata[self._elements.configuration.json_fields["META_FIELD_NAME"]]
		except KeyError:
			print("\u001b[1;31mTODO: handle this error:\u001b[0m")
			raise

		if type(metre_info) == str:
			if metre_info[:2] == "0x":
				metre_info = int(metre_info, base = 16)
			else:
				metre_info = int(metre_info, base = 10)
		
		metre = metre_info // self._elements.metre_info_base_16_order
		metre = self._elements.metres_pool[metre]

		form = metre_info % self._elements.metre_info_base_16_order
		form = self._elements.metre_forms_pool[form]
		return metre, form

	def _render_field(self, key: str, value, is_mandatory: bool):
		if key == self._elements.configuration.json_fields["META_FIELD_NAME"]:
			value = "%s %s"%(self.metre.name, self.form.name)
		return super()._render_field(key, value, is_mandatory)

	def render(self, translation_id: str) -> str:
		"""Organizes the metadata in a string as tabular format.
		
		Returns
			view (str): the view of the text as string.
		"""
		return super().render(translation_id)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
