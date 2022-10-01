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
import re
import json
import os
from .metadataparser.metadata_parser import Metadata
from .textparser.text_parser import Text
from .notesparser.notes_parser import Notes
from ..base_parser import *	

class Poem(BaseParser):
	"""Represents a poem. This class performs the operation of parsing the poem and building an json document representing it. The input file must be in cruscopoetry format.
	This class parses the poem up to the word level.
	
	Args:
		poem_path: the path of the poem file, in cruscopoetry format.
	
	Attrs:
		metadata (Metadata): the poem's metadata.
		text (Text): the poem's parsed text.
		notes (Notes): the poem's notes.
		
	Raises:
		InvalidPathError: raised if the file doesn't exist or is a directory.
	"""
	
	def __init__(self, poem_path: str):
		super().__init__(poem_path)
		with open(self.path, 'r') as myfile:
			poem_text = myfile.read()

		parsed = SectionsParser(poem_text)
		metadata, text, notes = parsed.sections
		self.metadata: Metadata = Metadata(metadata)
		self.text: Text = Text(text)
		self.notes: Notes = Notes(notes)

	def json_dict(self) -> dict:
		ret_dict = {
			"metadata": self.metadata.json_dict(),
			"text": self.text.json_dict(),
			"notes": self.notes.json_dict(),
			"translations": {}#here general information relative to translations will be stored.
		}
		return ret_dict
		
	def deploy(self, output: str):
		print("Deploying on %s..."%output)
		with open(output, 'w') as outfile:
			json.dump(self.json_dict(), outfile)
		
	def __repr__(self):
		return self.metadata.__repr__() + "\n" + self.text.__repr__()


class SectionsParser:

	REGEX_PATTERN = "^.*?METADATA\n(?P<metadata>.*?)(\nTEXT(\n(?P<text>.*?))?)?(\nNOTES\n(\n(?P<notes>.*?))?)?$"


	def __init__(self, poem_text: str):
		
		regex_pattern = self.__class__.REGEX_PATTERN.replace("\n", os.linesep)
			
		regex = re.compile(regex_pattern, re.DOTALL)
		matches = regex.match(poem_text)
###		print("\u001b[1;33mSectionParser.__init__:")
###		for group in matches.groups():
###			print("'%s'"%group)
###		print("\u001b[0m")
		metadata = matches.group("metadata")

		#if there is no text section, we store at its place an empty string:
		text = matches.group("text")
		#if there is no text section, we store at its place an empty string:
		text = text if text != None else ''

		notes = matches.group("notes")
		#if there is no notes section, we store at its place an empty string:
		notes = notes if notes != None else ''
		
		#if there is no text and the key-words TEXT and NOTES are one next the other, separated by an only line separator character, then the regex will take the NOTES section for the text one.
		#we can patch this now:
		if text[:5] == "NOTES" and notes == '':
			text, notes = notes, text
			notes = notes.split("NOTES" + os.linesep)[1]
		
###		print("\u001b[1;32mSectionsParser.__init__: '%s'"%metadata, "'%s'"%text, "'%s'\u001b[0m"%notes)
		self.sections: tuple = (metadata, text, notes)
