# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['dated_translator']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.4.1,<2.0.0']

setup_kwargs = {
    'name': 'dated-translator',
    'version': '0.1.1',
    'description': 'A Python package that helps translate from one term to another, depending on a passed date, from a CSV that contains some verified information.',
    'long_description': '# dated-translator\n\nA Python package that helps translate from one term to another, depending on a passed date, from a CSV that contains some verified information.\n\n## Getting started\n\n### Installation\n\nYou can install this package using `pip`:\n\n```sh\n$ pip install dated_translator\n```\n\n### First lookup\n\nSet up the lookup object first. In this case, we have a `data_file.csv` which contains (at least) four required columns: `Term 1`, `Term 2`, `Start Date`, and `End Date`. For a more advanced setup, see below.\n\n```py\nlookup = Lookup(dataset="data_file.csv")\n\nlookup.left_translate("Term 1", "1800-01-01") # Will return a list with the values of term 2 that exist in any given span of start and end date\n\nlookup.right_translate("Term 2", "1800-01-01") # Will return a list with the values of term 1 that exist in any given span of start and end date\n```\n\n## Advanced setup\n\n_This example is a real-world example from the Living with Machines project, and if you want to test it yourself (after installing the package), you can clone this repository and check out the example/`Example.ipynb` notebook._\n\nSay that we have a list of newspaper titles with different abbreviations, and we need to check which identification number, `NLP` that each abbreviation is associated with, within a certain date range.\n\nThe file that we\'d pass to the setup of the `Lookup` object, in this example called `JISC-papers.csv`, would look something like this:\n\n\n| Newspaper Title                                                          | NLP | Normalised Title | Abbr | StartD | StartM | StartY | EndD | EndM | EndY |\n| ------------------------------------------------------------------------ | --- | ---------------- | ---- | ------ | ------ | ------ | ---- | ---- | ---- |\n| Aberdeen Journal and general advertiser for the north of Scotland, The   | 31  | Aberdeen Journal | ANJO | 1      | Jan    | 1800   | 23   | Aug  | 1876 |\n| Aberdeen Weekly Journal and general advertiser for the north of Scotland | 32  | Aberdeen Journal | ANJO | 30     | Aug    | 1876   | 31   | Dec  | 1900 |\n\nIn this example, we want to get the resulting `NLP` **31** for any ANJO abbreviations (`Abbr`) between 1881-01-01 and 1876-08-23, and **32** for any of the same abbreviation between 1876-08-30 and 1900-12-31.\n\nTo set this up, we need to pass the dataset\'s name, and specify the names of the lookup\'s term 1 (`Abbr`) and term 2 (`NLP`). _Note: It doesn\'t matter in which order you pass them, but which one is considered term 1 and 2 will affect our `left_translate` and `right_translate` methods further down the line._\n\nWe also need to specify the particular date column format in our file. Since we\'re not using the standard setup here (a `Start Date` and `End Date` column respectively), we can pass a dictionary which requires three items, specifying the name of the year, month, and day columns, and their date formatting. We do so for both the start date and end date columns:\n\n```py\nlookup = Lookup(\n    dataset="JISC-papers.csv",\n    term_1_column = "Abbr",\n    term_2_column = "NLP",\n    start_date_column = {\n        "StartY": "%Y",\n        "StartM": "%b",\n        "StartD": "%d"\n    },\n    end_date_column = {\n        "EndY": "%Y",\n        "EndM": "%b",\n        "EndD": "%d"\n    }\n)\n```\n\nAfter this setup, we can run the `left_translate` method to check what the `NLP` is for the abbreviation "ANJO" on the date 1800-01-01:\n\n```py\nlookup.left_translate("ANJO", "1800-01-01")\n```\n\nThis should return the value: `[31]`, that is, a list of the possible NLPs for this abbreviation on this particular date.\n\nSimilarly, we can run the `right_translate` method to check what the `Abbr` is for a given `NLP` (31) on the date 1800-01-01:\n\n```py\nlookup.right_translate(31, "1800-01-01")\n```\n\nThe result should, in a reverse of the result above, be `[\'ANJO\']`, that is, a list of the possible abbreviations for this NLP in on this particular date.',
    'author': 'Kalle Westerling',
    'author_email': 'kalle.westerling@bl.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Living-with-machines/dated-translator',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
