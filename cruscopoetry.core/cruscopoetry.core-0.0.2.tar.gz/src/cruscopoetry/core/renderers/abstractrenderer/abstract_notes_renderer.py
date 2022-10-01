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
import abc
from ...jsonparser import JsonNotes, JsonNote
from typing import Tuple


class AbstractNoteRenderer(metaclass=abc.ABCMeta):
	"""Abstract class for the rendering of a single note of a CruscoPoetry JSON file.
	
	Args:
		jnote (JsonNote): the object representing the note of the json parsing of the poem
		lines_map (dict): a dict where every label that has been set for a line is associated to the correpsonding line number.
	
	Attrs:
		jnote (JsonNote): the object representing the note of the json parsing of the poem
		lines_map (dict): a dict where every label that has been set for a line is associated to the correpsonding line number.
	"""

	def __init__(self, reference: str, text: str):
		self._reference = reference
		self._text = text

	@property
	def reference(self):
		return self._reference
	
	@property
	def text(self):
		return self._text
	
	@abc.abstractmethod
	def render(self) -> str:
		return "%s: %s"%(self.reference, self.text)
	

class AbstractNotesRenderer(metaclass=abc.ABCMeta):
	"""Abstract class for the rendering of the notes of a CruscoPoetry JSON file.
	
	Args:
		jnotes (JsonNotes): the object representing the notes section of the json parsing of the poem
		lines_map (dict): a dict where every label that has been set for a line is associated to the correpsonding line number.
	
	Attrs:
		notes (Tuple[AbstractNoteRenderer]): the renderers of notes of the poem.
		
	This class has two abstract methods:
	 - build_note_renderer
	 - render
	
	Concrete implementations of this class can be easily built by setting the class argument NOTE_RENDERER_CLASS with the concrete implementation of AbstractNoteRenderer that one wants to use.
	If the initialization method of the concrete note renderer takes the same parametres of AbstractNoteRenderer, then the overriding of build_note_renderer can consist in just calling the super() 
	method.
	
	While implemented the render method, calling it form super() will return a list of instances of NOTE_RENDERER_CLASS representing the notes to render.
	"""
	
	NOTE_RENDERER_CLASS = AbstractNoteRenderer

	def __init__(self, jnotes, lines_map):
		self._jnotes = jnotes
		self._lines_map = lines_map
	
	@property
	def lines_map(self):
		return self._lines_map
	
	@property
	def jnotes(self):
		return self._jnotes

	def _get_note_reference(self, note: JsonNote):
		"""If the parameter 'note' is referenced by verse number or by 'all', it returns the its reference. If otherwise the note is referenced by a line label, it will return the line's number."""
		
		if ((note.reference.isdigit()) or (note.reference == "all")):
			return note.reference
		else:
			index = self.lines_map[note.reference]
			return str(index+1)


	@abc.abstractmethod		
	def build_note_renderer(self, note, translation_id: str):
		reference = self._get_note_reference(note)

		text = note.text if translation_id == None else note.get_translation_by_id(translation_id)
		return self.__class__.NOTE_RENDERER_CLASS(reference, text)
	
	@abc.abstractmethod
	def render(self, translation_id: str = None) -> str:
		"""Provides the renderings of the notes.
		Args:
			translation_id (str): the id of the translation that should be included in the rendering, or None if the source text needs to be included.
		"""
		note_renderers = tuple(self.build_note_renderer(note, translation_id) for note in self.jnotes.iter_notes())
		return note_renderers
