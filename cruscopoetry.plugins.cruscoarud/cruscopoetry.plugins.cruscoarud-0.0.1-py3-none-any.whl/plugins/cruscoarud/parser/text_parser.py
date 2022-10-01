# This file is part of Cruscoarud, a plugin of Cruscopoetry.
# 
# Cruscoarud is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Cruscoarud is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Cruscoarud. If not, see <http://www.gnu.org/licenses/>.
from ..common.metric_elements import MetricElements
from .line_parser import LineParser
from cruscopoetry.core.jsonparser import JsonParser
from collections import OrderedDict
from typing import Tuple
from .exceptions import FailedParsingException, NotMatchingColaNumberError
from functools import wraps


class TextParser(JsonParser):

	LINE_PARSER_CLASS = LineParser

	def __init__(self, filepath: str, elements_instance: MetricElements = None):
		super().__init__(filepath)
		self._elements = elements_instance if elements_instance != None else MetricElements()

		self.metre, self.form = None, None
		self.line_parser = None
		
	@property
	def meta_key(self):
		return self._elements.configuration.json_fields["META_FIELD_NAME"]
		
	@property
	def cola_key(self):
		return self._elements.configuration.json_fields["COLA_FIELD_NAME"]
	
	def _store_metre_and_form(self, metre_obj: LineParser):
		metre, form = int(metre_obj.metre), int(metre_obj.form)
		int_to_store = metre * self._elements.metre_info_base_16_order + form
		self.metadata[self.meta_key] = int_to_store
		self.save()
		
		#we update as well the instance's attributes:
		self._get_metre_and_form()
		
	@property
	def line_parser_class(self):
		return self.__class__.LINE_PARSER_CLASS

	def _get_metre_and_form(self):
		metre_info = self.metadata[self.meta_key]
		if type(metre_info) == str:
			if metre_info[:2] == "0x":
				metre_info = int(metre_info, base = 16)
			else:
				metre_info = int(metre_info, base = 10)
		
		metre = metre_info // self._elements.metre_info_base_16_order
		form = metre_info % self._elements.metre_info_base_16_order
		self.metre = metre
		self.form = form
		self.line_parser = self.line_parser_class(self.metre, self.form, self._elements)

	def _get_all_line_parsers(self) -> Tuple[LineParser]:
		line_parsers = []
		for metre in self._elements.metres_pool:
			for form in metre.forms:
				line_parsers.append(self.line_parser_class(metre, form, self._elements))
		return tuple(line_parsers)

	def find_metre(self):
		"""Tries to find the right metre and metre form for parsing a text. If more than one metre is found, the one presenting the minor quantity of variations (ʿilal, ziḥāfāt) is returned."""
		parsers = [[line_parser, 0] for line_parser in self._get_all_line_parsers()]
		for line in self.text.iter_lines():
			for i in range(len(parsers)-1,-1,-1):
				try:
					line_parsing = parsers[i][0].parse(line)
					parsers[i][1] += line_parsing.variation_level
				except FailedParsingException:
					parsers.pop(i)
				except NotMatchingColaNumberError:
					parsers.pop(i)
			if len(parsers) == 0:
				break
		
		if len(parsers) == 0:
			print("\u001b[1;31mNo possible parsing found.\u001b[0m")
			return None
			
		#now we sort all the parsers by their variation level and return the one with the lowest:
		parsers = sorted(parsers, key = lambda item: item[1])
		
		if len(parsers) > 1:
			print("\u001b[1;33mMore than one possible parsing found:")
		else:
			print("\u001b[1;32mOne possible parsing found!")
			
			for parser in parsers:
				print("%s %s (variation level: %d)"%(parser[0].metre.name, parser[0].form.name, parser[1]))
			print("\u001b[0m")
		
		#now we store the remained parser in the JSON file:
		self._store_metre_and_form(parsers[0][0])
		return parsers[0][0]

	def metre_info_required(method):
		"""Used as a decorator on other methods, ensures that the Json file already contains the necessary prosodic information in its metadata.
		In order to be able to be used with this decorators, the first positional arguments of the methods (after self) must be a boolean `verbose` variable.
		"""
		@wraps(method)
		def ensure_metre_info(*args, **kwargs):
			_self = args[0]
			_args = args[1:]
			_verbose = _args[0]

			#first we check that the metre information is already stored; if not, we ask the use to call find_metre and return None:
			if _self.meta_key not in _self.metadata.keys():
				print("\u001b[1;31mNo metric information found. Please use the method find_metres() before parsing.\u001b[0m")
				return None
				
			if _verbose:
				print("\u001b[1;32mMetric information found:\u001b[0m")
			_self._get_metre_and_form()
			
			return method(_self, *_args, **kwargs)
		
		return ensure_metre_info
		
	def find_metres_for_each_line(self, verbose: bool = False) -> tuple:
		"""Tries to parse each line of the poem with any metre and metre form possible combination, and returns a tuple where each item at index i is a tuple of (LineParser, LineParsing) pairs of 
		all the successful parsings of the line whose index is i."""
		results = []
		line_parsers = self._get_all_line_parsers()
		for line in self.text.iter_lines():
			line_parsings = []
			if verbose:
				print("\u001b[1;33mFinding metre for line %d, %s:"%(line.number, line.transcription), end=" ")
				for colon in line.iter_cola():
					print(line_parsers[0]._to_harfs(colon), end= " ")
				print("\u001b[0m", end=" ")
			for line_parser in line_parsers:
				try:
					line_parsing = line_parser.parse(line)
					line_parsings.append((line_parser, line_parsing))
				except FailedParsingException as e:
					pass
				except NotMatchingColaNumberError:
					pass
			line_parsings = sorted(line_parsings, key = lambda it: it[1].variation_level)
			if verbose:
				if len(line_parsings) > 1:
					print("\u001b[1;33m%d matches\u001b[0m"%len(line_parsings))
				elif len(line_parsings) == 1:
					print("\u001b[1;32m%d match\u001b[0m"%len(line_parsings))
				else:
					print("\u001b[1;31mNo match\u001b[0m")
			results.append(tuple(line_parsings))
		return tuple(results)

	@metre_info_required
	def parse(self, verbose: bool = False):
		for line in self.text.iter_lines():
			try:
				line_parsing = self.line_parser.parse(line)
				line_parsing.store_on(line)
			except FailedParsingException as e:
				e.line_number = line.number
				e.metre = self._elements.metres_pool[self.metre].name
				e.form = self._elements.metre_forms_pool[self.form].name
				e.color = FailedParsingException.WARNING
				print(e)
		self.save()

		#we return True as success flag
		return True
	
	def reset(self):
		"""Deletes all the information previously stored by the CruscoArud plugin on the file `json_file"""
		
		if self.meta_key in self.metadata.keys():
			del self.metadata[self.meta_key]
		
		for colon in self.text.iter_cola_dict():
			if self.cola_key in colon.keys():
				del colon[self.cola_key]
		
		self.save()
