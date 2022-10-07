import os
from typing import Union, Any

import regex
from a_pandas_ex_plode_tool import pd_add_explode_tools
from urllib.parse import urlparse

pd_add_explode_tools()
import ujson
import pandas as pd
import requests

pd.set_option("colheader_justify", "center")


def uri_validator(x: str) -> bool:
    "https://stackoverflow.com/questions/7160737/how-to-validate-a-url-in-python-malformed-or-not"
    try:
        result = urlparse(x)
        return all([result.scheme, result.netloc])
    except:
        return False


def create_html_table_from_iterable(
    data: Any,
    filename: Union[None, str] = None,
    title: str = "Pandas DataFrame",
    sparsify: bool = False,
) -> tuple[str, str]:
    r"""
    Convert any nested iterable to an HTML table. Design is separated from data. You can use the preset, but if you want,
    you can easily create your own CSS style.



        Parameters:
            data: Any
                You can pass any iterable (list, dict, tuple …), json file path (str) or json URL (str)
            filename: Union[None,str]
                File path for output, will be saved in your current working directory
                If None, no files will be written.
            title: str
                Title  for HTML
                (default =  'Pandas DataFrame')
            sparsify: bool
                Repeat keys in every line
                (default = False)

        Returns:
            tuple[str,str]

    """
    if isinstance(data, str):
        if os.path.exists(data):
            with open(data, mode="r", encoding="utf-8") as f:
                data = f.read()

        elif uri_validator(data) is True:
            data = requests.get(data).content
        else:
            pass
        data = ujson.loads(data)
    df = pd.Q_AnyNestedIterable_2df(data, unstack=False)
    html_string = f"""
    <html>
      <head><title>{title}</title></head>
      <link rel="stylesheet" type="text/css" href="df_style.css"/>
      <body>
        {{table}}
      </body>
    </html>.
    """
    styledatei = r"""
    body {
        color: #333;
        font: 140%/80px 'Helvetica Neue', helvetica, arial, sans-serif;
        text-shadow: 0 1px 0 #fff;
    }
    
    strong {
        font-weight: bold; 
    }
    
    em {
        font-style: italic; 
    }
    
    table {
        background: #f0f0f5;
        border-collapse: separate;
        box-shadow: inset 3 4px 3 #fff;
        font-size: 16px;
        line-height: 24px;
        margin: 30px auto;
        text-align: left;
        table-layout: fixed;
    }	
    
    
    
    th {
        background: linear-gradient(#777, #444);
        border-left: 0px solid #555;
        border-right: 0px solid #777;
        border-top: 0px solid #555;
        border-bottom: 0px solid #333;
        box-shadow: inset 0 1px 0 #999;
        color: #fff;
      font-weight: bold;
        padding: 10px 15px;
        position: relative;
        text-shadow: 0 1px 0 #000;	
    }
    
    th:after {
        background: linear-gradient(rgba(255,255,255,0), rgba(255,255,255,.08));
        content: '';
        display: block;
        height: 75%;
        left:10;
        margin: 0px 0 0 0;
        position: absolute;
        top: 55%;
        width: 100%;
    }
    
    th:nth-child(even) {
        border-left: 1px solid #111;	
        box-shadow: inset 2px 2px 0 #999;
            background: linear-gradient(rgba(0,0,20,.7), rgba(0,140,140,.99));
    
    }
    
    th:nth-child(odd) {
        border-left: 1px solid #111;	
        box-shadow: inset 2px 2px 0 #999;
            background: linear-gradient(rgba(0,0,70,.7), rgba(0,100,100,.99));
    
    }
    
    td {
        border-right: 1px solid #fff;
        border-left: 1px solid #e8e8e8;
        border-top: 1px solid #fff;
        border-bottom: 1px solid #e8e8e8;
        padding: 10px 15px;
        position: relative;
    }
    
    th:last-child {
        box-shadow: inset -1px 1px 0 #500;
        background: linear-gradient(rgba(0,0,120,.7), rgba(0,0,255,.99));
    
    }
    
    tr {
        background: linear-gradient(rgba(0,100,100,.7), rgba(0,255,255,.99));
    }
    
    tr:nth-child(odd) td {
        background: #f1f1f1;	
            font-size: 18px;
    }
    tr:nth-child(even) td {
        background: #a1f1f1;	
            font-size: 18px;
    
    }
    td:empty {background: green;}
    
    th:empty {
        background: #a1f1f1;	
            border-left: 0px solid #555;
        border-right: 0px solid #777;
        border-top: 0px solid #555;
        border-bottom: 0px solid #333;
        box-shadow: inset 0 0px 0 #999;
    
        }    
    tr:empty {background: green;}
    """
    styfile = os.path.join(os.getcwd(), "df_style.css")
    if filename is not None:
        with open(styfile, "w", encoding="utf-8") as f:
            f.write(styledatei)

    htm = html_string.format(
        table=df.d_unstack()
        .fillna("")
        .d_stack()
        .drop(columns="aa_all_keys")
        .rename(columns={"aa_value": "values"})
        .to_html(classes="mystyle", sparsify=sparsify, justify="match-parent")
    )
    htm = regex.sub(r"(<th[^>]*>\d+)\.0+(</th>)", r"\g<1>\g<2>", htm)
    if filename is not None:
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(htm)
        print(f"Files saved:\n{filepath}\n{styfile}")
    return htm, styfile


if __name__ == "__main__":
    data = {
        "glossary": {
            "title": "example glossary",
            "GlossDiv": {
                "title": "S",
                "GlossList": {
                    "GlossEntry": {
                        "ID": "SGML",
                        "SortAs": "SGML",
                        "GlossTerm": "Standard Generalized Markup Language",
                        "Acronym": "SGML",
                        "Abbrev": "ISO 8879:1986",
                        "GlossDef": {
                            "para": "A meta-markup language, used to create markup languages such as DocBook.",
                            "GlossSeeAlso": ["GML", "XML"],
                        },
                        "GlossSee": "markup",
                    }
                },
            },
        }
    }

    """https://json.org/example.html"""
    jsonstring = """{"web-app": {
      "servlet": [   
        {
          "servlet-name": "cofaxCDS",
          "servlet-class": "org.cofax.cds.CDSServlet",
          "init-param": {
            "configGlossary:installationAt": "Philadelphia, PA",
            "configGlossary:adminEmail": "ksm@pobox.com",
            "configGlossary:poweredBy": "Cofax",
            "configGlossary:poweredByIcon": "/images/cofax.gif",
            "configGlossary:staticPath": "/content/static",
            "templateProcessorClass": "org.cofax.WysiwygTemplate",
            "templateLoaderClass": "org.cofax.FilesTemplateLoader",
            "templatePath": "templates",
            "templateOverridePath": "",
            "defaultListTemplate": "listTemplate.htm",
            "defaultFileTemplate": "articleTemplate.htm",
            "useJSP": false,
            "jspListTemplate": "listTemplate.jsp",
            "jspFileTemplate": "articleTemplate.jsp",
            "cachePackageTagsTrack": 200,
            "cachePackageTagsStore": 200,
            "cachePackageTagsRefresh": 60,
            "cacheTemplatesTrack": 100,
            "cacheTemplatesStore": 50,
            "cacheTemplatesRefresh": 15,
            "cachePagesTrack": 200,
            "cachePagesStore": 100,
            "cachePagesRefresh": 10,
            "cachePagesDirtyRead": 10,
            "searchEngineListTemplate": "forSearchEnginesList.htm",
            "searchEngineFileTemplate": "forSearchEngines.htm",
            "searchEngineRobotsDb": "WEB-INF/robots.db",
            "useDataStore": true,
            "dataStoreClass": "org.cofax.SqlDataStore",
            "redirectionClass": "org.cofax.SqlRedirection",
            "dataStoreName": "cofax",
            "dataStoreDriver": "com.microsoft.jdbc.sqlserver.SQLServerDriver",
            "dataStoreUrl": "jdbc:microsoft:sqlserver://LOCALHOST:1433;DatabaseName=goon",
            "dataStoreUser": "sa",
            "dataStorePassword": "dataStoreTestQuery",
            "dataStoreTestQuery": "SET NOCOUNT ON;select test='test';",
            "dataStoreLogFile": "/usr/local/tomcat/logs/datastore.log",
            "dataStoreInitConns": 10,
            "dataStoreMaxConns": 100,
            "dataStoreConnUsageLimit": 100,
            "dataStoreLogLevel": "debug",
            "maxUrlLength": 500}},
        {
          "servlet-name": "cofaxEmail",
          "servlet-class": "org.cofax.cds.EmailServlet",
          "init-param": {
          "mailHost": "mail1",
          "mailHostOverride": "mail2"}},
        {
          "servlet-name": "cofaxAdmin",
          "servlet-class": "org.cofax.cds.AdminServlet"},
     
        {
          "servlet-name": "fileServlet",
          "servlet-class": "org.cofax.cds.FileServlet"},
        {
          "servlet-name": "cofaxTools",
          "servlet-class": "org.cofax.cms.CofaxToolsServlet",
          "init-param": {
            "templatePath": "toolstemplates/",
            "log": 1,
            "logLocation": "/usr/local/tomcat/logs/CofaxTools.log",
            "logMaxSize": "",
            "dataLog": 1,
            "dataLogLocation": "/usr/local/tomcat/logs/dataLog.log",
            "dataLogMaxSize": "",
            "removePageCache": "/content/admin/remove?cache=pages&id=",
            "removeTemplateCache": "/content/admin/remove?cache=templates&id=",
            "fileTransferFolder": "/usr/local/tomcat/webapps/content/fileTransferFolder",
            "lookInContext": 1,
            "adminGroupID": 4,
            "betaServer": true}}],
      "servlet-mapping": {
        "cofaxCDS": "/",
        "cofaxEmail": "/cofaxutil/aemail/*",
        "cofaxAdmin": "/admin/*",
        "fileServlet": "/static/*",
        "cofaxTools": "/tools/*"},
     
      "taglib": {
        "taglib-uri": "cofax.tld",
        "taglib-location": "/WEB-INF/tlds/cofax.tld"}}}"""

    jsonurl = "https://mysafeinfo.com/api/data?list=englishmonarchs&format=json"

    jsonfile = r"F:\jsonstackoverflow.json"
    #'https://api.stackexchange.com/2.2/answers?order=desc&sort=activity&site=stackoverflow'

    #'https://stackoverflow.com/questions/64359762/constructing-a-pandas-dataframe-with-columns-and-sub-columns-from-nested-diction
    nesteddict = {
        "level1": {
            "t1": {
                "s1": {"col1": 5, "col2": 4, "col3": 4, "col4": 9},
                "s2": {"col1": 1, "col2": 5, "col3": 4, "col4": 8},
                "s3": {"col1": 11, "col2": 8, "col3": 2, "col4": 9},
                "s4": {"col1": 5, "col2": 4, "col3": 4, "col4": 9},
            },
            "t2": {
                "s1": {"col1": 5, "col2": 4, "col3": 4, "col4": 9},
                "s2": {"col1": 1, "col2": 5, "col3": 4, "col4": 8},
                "s3": {"col1": 11, "col2": 8, "col3": 2, "col4": 9},
                "s4": {"col1": 5, "col2": 4, "col3": 4, "col4": 9},
            },
            "t3": {
                "s1": {"col1": 1, "col2": 2, "col3": 3, "col4": 4},
                "s2": {"col1": 5, "col2": 6, "col3": 7, "col4": 8},
                "s3": {"col1": 9, "col2": 10, "col3": 11, "col4": 12},
                "s4": {"col1": 13, "col2": 14, "col3": 15, "col4": 16},
            },
        },
        "level2": {
            "t1": {
                "s1": {"col1": 5, "col2": 4, "col3": 9, "col4": 9},
                "s2": {"col1": 1, "col2": 5, "col3": 4, "col4": 5},
                "s3": {"col1": 11, "col2": 8, "col3": 2, "col4": 13},
                "s4": {"col1": 5, "col2": 4, "col3": 4, "col4": 20},
            },
            "t2": {
                "s1": {"col1": 5, "col2": 4, "col3": 4, "col4": 9},
                "s2": {"col1": 1, "col2": 5, "col3": 4, "col4": 8},
                "s3": {"col1": 11, "col2": 8, "col3": 2, "col4": 9},
                "s4": {"col1": 5, "col2": 4, "col3": 4, "col4": 9},
            },
            "t3": {
                "s1": {"col1": 1, "col2": 2, "col3": 3, "col4": 4},
                "s2": {"col1": 5, "col2": 6, "col3": 7, "col4": 8},
                "s3": {"col1": 9, "col2": 10, "col3": 11, "col4": 12},
                "s4": {"col1": 13, "col2": 14, "col3": 15, "col4": 16},
            },
        },
    }

    fromjsonorg_result = create_html_table_from_iterable(
        data, filename="fromjsonorg.html", title="Pandas - DataFrame", sparsify=True
    )

    jsonstring_result = create_html_table_from_iterable(
        jsonstring,
        filename="jsonstring.html",
        title="Pandas - DataFrame",
        sparsify=True,
    )

    json_url_result = create_html_table_from_iterable(
        jsonurl, filename="json_url.html", title="Pandas - DataFrame", sparsify=True
    )

    json_from_file = create_html_table_from_iterable(
        jsonfile,
        filename="json_from_file.html",
        title="Pandas - DataFrame",
        sparsify=False,
    )

    nested_dict = create_html_table_from_iterable(
        nesteddict,
        filename="from_nested_dict.html",
        title="Pandas - DataFrame",
        sparsify=False,
    )
