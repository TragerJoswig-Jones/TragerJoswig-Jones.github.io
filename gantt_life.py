import pandas as pd
import plotly.express as px
import plotly.io as pio
from datetime import date
#pio.templates
template="simple_white" #"plotly_dark"
today = '2021-07-14'

color_list = {
                "SEL ": "#0C3F6A",
                "UW BSEE ": "#4b2e83",
                "Micron ": "#0077C8", # 0093d6
                "GM ": "#194390", # #23559e
                "NREL SULI ": "#0079C2",
                "UW PhD ": "#b7a57a",
                "UW SEAL ": "#C1C1C1",
                "UW REAL ": "#e8e3d3",
                "UW WPEL ": "#85754d"
                }

text = ["<b>SEL</b>","<b>SEL</b>","<b>SEL</b>","<b>UW BSEE</b>"+" "*38,
        "<b>Micron</b>","<b>SEAL</b>","<b>REAL</b>"+" "*8,"<b>GM</b>","<b>NREL</b>",
        "<b>UW PhD</b>"+" "*50,"<b>WPEL</b>"+" "*52]

category_orders = {
                    "Education": 0,
                    "Research": 1,
                    "Internships": 2
                    }
experiece_order = ["Internship", "Research", "Education"] # Bottom up

df = pd.DataFrame([
    dict(Experience="Internship", Start='2016-06-15', Finish='2016-09-20', Organization="SEL "),
    dict(Experience="Internship", Start='2017-06-15', Finish='2017-09-20', Organization="SEL "),
    dict(Experience="Internship", Start='2018-06-15', Finish='2018-09-20', Organization="SEL "),
    dict(Experience="Education", Start='2017-09-27', Finish='2021-06-11', Organization="UW BSEE "),
    dict(Experience="Internship", Start='2019-06-24', Finish='2019-09-06', Organization="Micron "),
    dict(Experience="Research", Start='2019-09-25', Finish='2019-12-15', Organization="UW SEAL "),
    dict(Experience="Research", Start='2020-04-20', Finish='2021-06-11', Organization="UW REAL "),
    dict(Experience="Internship", Start='2020-06-15', Finish='2020-09-04', Organization="GM "),
    dict(Experience="Internship", Start='2021-06-14', Finish='2021-08-20', Organization="NREL SULI "),
    dict(Experience="Education", Start='2021-09-29', Finish='2026-06-11', Organization="UW PhD "),
    dict(Experience="Research", Start='2021-09-20', Finish='2026-06-11', Organization="UW WPEL "),
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Experience", color="Organization",
                    facet_row_spacing=0.001, facet_col_spacing=0.001, color_discrete_map=color_list,
                    text=text, category_orders=category_orders, template=template, width=1250, height=800)
fig.add_vrect(x0=today,x1='2026-09-20',fillcolor='lightslategray',opacity=0.25, line_width=0,
                annotation_text="The Future", annotation_position="top left") 
fig.update_layout(yaxis=dict(categoryorder='array')) # reverse the order of the y-axis tick labels
fig.update_layout(yaxis=dict(categoryarray=experiece_order)) # reverse the order of the y-axis tick labels
fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    showlegend=False,
                    font_color="#808080",
                    font_size=12)
fig.update_xaxes(range=['2016-01-01', '2026-06-30'])

fig.write_image("images/gantt_"+str(date.today())+"_unedited.svg")
fig.show()