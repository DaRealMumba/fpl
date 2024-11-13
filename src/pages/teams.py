import os
import sys

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from plottable import ColumnDefinition, Table
from plottable.cmap import normed_cmap
from plottable.plots import image

TABLE_PATH = os.path.join("data", "pl_table.csv")


@st.cache_data
def upload_data(data_path: str):
    df = pd.read_csv(data_path)
    return df


df = pd.read_csv(TABLE_PATH)

bg_color = "#FFFFFF"  # I usually just like to do a white background
text_color = "#000000"  # With black text

row_colors = {
    "top4": "#E1FABC",
    "top6": "#FFFC97",
    "relegation": "#E79A9A",
    "even": "#E2E2E1",
    "odd": "#B3B0B0",
}

plt.rcParams["text.color"] = text_color
plt.rcParams["font.family"] = "monospace"

# задаем загаловок сайта
st.markdown(
    """<h1 style='text-align: center; color: black;'
            >Team stats</h1>""",
    unsafe_allow_html=True,
)

st.subheader("Current PL table")

df["badges"] = df["Squad"].apply(
    lambda x: f"/Users/mumin/Desktop/DS/personal/fpl/logos/{x.lower()}_logo.png"
)
table_df = df.copy().loc[
    :,
    [
        "Rk",
        "badges",
        "Squad",
        "MP",
        "W",
        "D",
        "L",
        "GF",
        "GA",
        "GD",
        "Pts",
        "Pts/MP",
        "xG",
        "xGA",
        "xGD",
        "xGD/90",
        "Last 5",
    ],
]

st.table(table_df.head())

cols_defs = [
    ColumnDefinition(name="Rk", textprops={"ha": "left", "va": "center"}, width=0.5),
    ColumnDefinition(
        name="badges",
        textprops={"ha": "left", "va": "center", "color": bg_color},
        width=0.5,
        plot_fn=image,
    ),
    ColumnDefinition(
        name="Squad", textprops={"ha": "right", "weight": "bold"}, width=1.75
    ),
    ColumnDefinition(
        name="MP", group="Matches played", textprops={"ha": "right"}, width=0.5
    ),
    ColumnDefinition(
        name="W", group="Matches played", textprops={"ha": "right"}, width=0.5
    ),
    ColumnDefinition(
        name="D", group="Matches played", textprops={"ha": "right"}, width=0.5
    ),
    ColumnDefinition(
        name="L", group="Matches played", textprops={"ha": "right"}, width=0.5
    ),
    ColumnDefinition(name="GF", group="Goals", textprops={"ha": "right"}, width=0.5),
    ColumnDefinition(name="GA", group="Goals", textprops={"ha": "center"}, width=0.5),
    ColumnDefinition(name="GD", group="Goals", textprops={"ha": "center"}, width=0.5),
    ColumnDefinition(name="Pts", group="Points", textprops={"ha": "center"}, width=0.5),
    ColumnDefinition(
        name="Pts/MP", group="Points", textprops={"ha": "center"}, width=0.5
    ),
    ColumnDefinition(
        name="xG",
        group="Expected Goals",
        textprops={
            "ha": "center",
            "color": "#000000",
            "weight": "bold",
            "bbox": {"boxstyle": "circle", "pad": 0.35},
        },
        cmap=normed_cmap(table_df["xG"], cmap=matplotlib.cm.PiYG, num_stds=2),
    ),
    ColumnDefinition(
        name="xGA",
        group="Expected Goals",
        textprops={
            "ha": "center",
            "color": "#000000",
            "weight": "bold",
            "bbox": {"boxstyle": "circle", "pad": 0.35},
        },
        cmap=normed_cmap(table_df["xGA"], cmap=matplotlib.cm.PiYG_r, num_stds=2),
    ),
    ColumnDefinition(
        name="xGD",
        group="Expected Goals",
        textprops={
            "ha": "center",
            "color": "#000000",
            "weight": "bold",
            "bbox": {"boxstyle": "circle", "pad": 0.35},
        },
        cmap=normed_cmap(table_df["xGD"], cmap=matplotlib.cm.PiYG, num_stds=2),
    ),
    ColumnDefinition(
        name="xGD/90",
        group="Expected Goals",
        textprops={
            "ha": "center",
            "color": "#000000",
            "weight": "bold",
            "bbox": {"boxstyle": "circle", "pad": 0.35},
        },
        cmap=normed_cmap(table_df["xGD/90"], cmap=matplotlib.cm.PiYG, num_stds=2),
    ),
    ColumnDefinition(name="Last 5", group="Form", textprops={"ha": "center"}),
]

team_fig, ax = plt.subplots(figsize=(20, 22))
team_fig.set_facecolor(bg_color)
ax.set_facecolor(bg_color)

table = Table(
    table_df,
    column_definitions=cols_defs,
    index_col="Rk",
    row_dividers=True,
    row_divider_kw={"linewidth": 1, "linestyle": (0, (1, 5))},
    footer_divider=True,
    textprops={"fontsize": 14},
    col_label_divider_kw={"linewidth": 1, "linestyle": "-"},
    column_border_kw={"linewidth": 0.5, "linestyle": "-"},
    ax=ax,
).autoset_fontcolors(colnames=["xG", "xGA", "xGD", "xGD/90"])

table.cells[10, 3].textprops["color"] = "#8ACB88"

for idx in [0, 1, 2, 3]:
    table.rows[idx].set_facecolor(row_colors["top4"])

table.rows[4].set_facecolor(row_colors["top6"])

for idx in [17, 18, 19]:
    table.rows[idx].set_facecolor(row_colors["relegation"])

st.pyplot(fig=team_fig, use_container_width=True)
