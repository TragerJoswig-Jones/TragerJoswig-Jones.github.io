import pandas as pd
import plotly.express as px
import plotly.io as pio
#pio.templates
template="seaborn"

color_list = {
                "SEL ": "#0C3F6A",
                "UW BSEE ": "#4b2e83",
                "Micron ": "#0077C8", # 0093d6
                "GM ": "#194390", # #23559e
                "NREL SULI ": "#0079C2",
                "UW PhD ": "#b7a57a",
                }

df = pd.DataFrame([
    dict(Experience="Internship", Start='2016-06-15', Finish='2016-09-20', Organization="SEL "),
    dict(Experience="Internship", Start='2017-06-15', Finish='2017-09-20', Organization="SEL "),
    dict(Experience="Internship", Start='2018-06-15', Finish='2018-09-20', Organization="SEL "),
    dict(Experience="Education", Start='2017-09-27', Finish='2021-06-11', Organization="UW BSEE "),
    dict(Experience="Internship", Start='2019-06-24', Finish='2019-09-06', Organization="Micron "),
    dict(Experience="Internship", Start='2020-06-15', Finish='2020-09-04', Organization="GM "),
    dict(Experience="Internship", Start='2021-06-14', Finish='2021-08-13', Organization="NREL SULI "),
    dict(Experience="Education", Start='2021-09-29', Finish='2026-06-11', Organization="UW PhD ")
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Experience", color="Organization",
                    facet_row_spacing=0.001, facet_col_spacing=0.001, color_discrete_map=color_list,
                    text=["SEL","SEL","SEL","UW","Micron","GM","NREL","UW"])

fig.show()