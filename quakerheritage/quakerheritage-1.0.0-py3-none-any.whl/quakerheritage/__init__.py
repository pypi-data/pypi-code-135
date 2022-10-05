# quakerheritage/__init__.py
"""Collects text data from online pdfs held by the Quaker Meeting House Heritage Project.

Modules exported by this package:

`build`: Unifies the functional modules and runs the main code to create a formatted Pandas DataFrame from pdfs held by Britain Yearly Meeting\n

`getWebData`: Main web function that collects url data and extracts text from each pdf examined\n

`cleanseData`: Runs Pandas functionality to merge text data into workable DataFrame and creates consistent data quality\n

"""
__version__ = "1.0.0"