import streamlit as st
import streamlit.components.v1 as components
import os
from typing import Optional

_RELEASE = True

if not _RELEASE:
    _st_card = components.declare_component(
    'st_card',
    url='http://localhost:3001'
)
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _st_card = components.declare_component("st_card", path=build_dir)



def st_card(
    title: str, section_1: str, section_2: str,section_3: str,footer: str, key: Optional[str] = None
)  -> None:
    return _st_card(title=title, section_1=section_1,section_2=section_2,section_3=section_3,footer=footer,key=key)

st_card(title="Hello World!", section_1="Section 1 Testing",section_2="Section 2 Testing",section_3="Section 3 Testing",footer="My Footer Content",key="Section 1 Testing")