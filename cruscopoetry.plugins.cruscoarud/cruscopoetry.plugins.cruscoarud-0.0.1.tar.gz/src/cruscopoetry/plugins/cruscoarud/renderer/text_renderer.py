# This file is part of CruscoPoetry.
# 
# CruscoPoetry is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# CruscoPoetry is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with CruscoPoetry. If not, see <http://www.gnu.org/licenses/>.
from ..common.metric_elements import MetricElements
from .text_body_renderer import CruscoArudTextBodyRenderer
from .metadata_renderer import CruscoArudMetadataRenderer
from cruscopoetry.core.renderers import HtmlRenderer
from cruscopoetry.core.jsonparser import JsonParser
from cruscopoetry.core.renderers import TranslationArrangement


class CruscoArudHtmlRenderer(HtmlRenderer):

	METADATA_RENDERER = CruscoArudMetadataRenderer
	TEXT_BODY_RENDERER = CruscoArudTextBodyRenderer


	def __init__(self, path, elements: MetricElements):
		self.json = JsonParser(path)

		self._elements = elements if elements != None else MetricElements()
		self._metadata_renderer = self.build_metadata_renderer(self.json)
		
		self.metre: int = int(self._metadata_renderer.metre)
		self.form: int = int(self._metadata_renderer.form)
		
		#we get the feet sequence from self.metre and self.form:
		metre = self._elements.metres_pool[self.metre]
		form = self._elements.metre_forms_pool[self.form]
		
		self.feet_sequence = form.apply(metre)

		self._text_body_renderer = self.build_text_body_renderer(self.json)
		self._notes_renderer = self.build_notes_renderer(self.json)


	def build_metadata_renderer(self, json: JsonParser):
		metadata = json.metadata
		translations = json.translations
		return self.__class__.METADATA_RENDERER(metadata, translations, self._elements)

	def build_text_body_renderer(self, json: JsonParser):
		json_text = json.text
		return self.__class__.TEXT_BODY_RENDERER(json_text, self.feet_sequence, self._elements)

	def build_notes_renderer(self, json: JsonParser):
		return super().build_notes_renderer(json)
		

	def render(self, translation_id: str, translation_arrangement: TranslationArrangement, number_after: int, pretty_print: bool) -> str:
		return super().render(translation_id, translation_arrangement, number_after, pretty_print)
