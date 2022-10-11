# 2022.9.26
import streamlit.components.v1 as components
import streamlit as st
st.set_page_config (layout="wide")
from penly import * 

def getdate(ap): 
	''' ap:CC1BE0E29824:date-20220925:page-0.100.0:pen-xls  '''
	res =  list(set ([mid(k, 'date-') for k in redis.kvr.keys(f"ap:{ap}:*") if k.endswith(":pen-xls") ]))
	res.sort(reverse=True)
	return res

def svgdemo():
	svg= ''' <svg viewBox="0 0 5600 7920">
  <polyline points="26,90 23,89 25,89 24,88 24,90 24,92 20,98 17,121 23,144 35,159 48,162 73,142 87,108 89,76 80,56 58,51 31,66 15,99 13,117" style="fill:none;stroke:blue;stroke-width:15" />
  <polyline points="97,54 94,52 97,47 109,44 110,41 111,42 112,43 112,41 116,42 114,44 117,53 124,113 134,167 140,174 153,143 164,109 167,83 170,64 172,62 166,61 155,59" style="fill:none;stroke:black;stroke-width:15" />
  <polyline points="175,108 178,114 188,118 199,121 215,120 242,112 247,102 248,92 247,84 237,75 219,72 211,77 205,95 199,125 200,153 210,171 220,173 247,155 273,116 290,89 297,78 298,71 296,64 294,61 294,63 295,64 296,66 297,68 299,76 302,107 309,145 310,156 310,145 312,118 319,91 325,86 327,89 332,99 340,105" style="fill:none;stroke:black;stroke-width:15" />
  <polyline points="410,81 423,50 399,62 381,85 377,135 384,166 392,173 405,174 424,150 444,134 448,126 449,125 447,125 448,125 447,125 448,128 448,131 450,141 456,157 467,166 482,169 489,149 492,133 490,117 478,102 450,91 445,94 444,99 459,110 481,102" style="fill:none;stroke:black;stroke-width:15" />
  <polyline points="527,89 532,82 532,79 534,81 535,84 534,102 526,134 524,140 526,139 531,132 535,113 546,90 558,75 568,64 569,64 571,67 570,71 577,97 578,114 578,117 579,117 582,114 586,108 594,91 604,74 613,60 614,58 615,59 616,63 618,82 615,111 616,133 614,162 614,156 625,124" style="fill:none;stroke:black;stroke-width:15" />
  <polyline points="655,84 655,87 659,93 668,96 681,95 696,90 710,82 718,70 718,57 715,52 709,48 698,47 670,57 655,96 652,145 681,175 710,174 724,168 728,160 733,128" style="fill:none;stroke:black;stroke-width:15" />
</svg> '''
	st.components.v1.html(svg, width=None, height=1200, scrolling=False)

def polyline( stroke:str="7112,13084,19,1664174211 7105,13117,37,1664174211", width:int=15):
	''' '''
	arr = stroke.strip().split(' ') 
	points =  ' '.join( [",".join(tup.split(',')[0:2]) for tup in arr])
	return f'''<polyline points="{points}" style="fill:none;stroke:black;stroke-width:{width}" />'''

def svg( strokes , width:int=15):
	return '<svg viewBox="0 0 11548 16404">' + "\n".join([ polyline(s, width) for s in strokes])  + '</svg>'