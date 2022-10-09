from danklabs.ui.core import WebPage, lw_charts_js_urs, table, vega_js_urls
from dominate import document
from dominate import tags as d

html = document(title="TI Web")
with html.body:
    with d.div(_class="y-axis-centered"):
        t = table(id="data-table")
        d.button("Load", onclick=t.load_table("data"))

ui_page = WebPage(
    html=html,
    js_urls=vega_js_urls + lw_charts_js_urs,
    global_js_vars={"data": [["c1", "c2"], [1, 2]]},
)
