import os
import sys

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from plottable import ColumnDefinition, Table

PLAYERS_DATA_PATH = os.path.join("data", "field_players.csv")


@st.cache_data
def upload_data(data_path: str):
    df = pd.read_csv(data_path)
    return df


# задаем загаловок сайта
st.markdown(
    """<h1 style='text-align: center; color: black;'
            >Players stats</h1>""",
    unsafe_allow_html=True,
)

players_df = upload_data(PLAYERS_DATA_PATH)


bar = px.bar(
    players_df.sort_values("B", ascending=False).head(40),
    x="player_name",
    y="B",
    color="team",
    title="Топ 40 игроков по бонусным очкам",
)
st.plotly_chart(bar)  # , use_container_width=True)

st.subheader("Визуализация данных")

xg_plot = px.scatter(
    players_df.sort_values("GS", ascending=False).head(50),
    x="xG",
    y="GS",
    color="team",
    trendline="ols",
    trendline_scope="overall",
    hover_name="player_name",
    size="xG",
    title="Отношение голов к ожидаемым голам",
    width=1000,
    height=500,
)
st.plotly_chart(xg_plot)


st.subheader("Табличные данные")

cards = players_df.sort_values("YC", ascending=False).loc[
    :, ["player_name", "YC", "team"]
]
cards = cards[cards["YC"] > 2].reset_index().drop(columns="index")
cards["rank"] = [i for i in range(1, len(cards) + 1)]

cards_plot = go.Figure(
    data=[
        go.Table(
            header=dict(
                values=["team", "player name", "Yellow cards"],
                fill_color="paleturquoise",
                align="left",
            ),
            cells=dict(
                values=[cards.team, cards.player_name, cards.YC],
                fill_color="lavender",
                align="left",
            ),
            # text="Игроки, у которых 3 и больше ЖК",
        )
    ]
)

st.plotly_chart(cards_plot)


cols_defs = [
    ColumnDefinition(name="rank", textprops={"ha": "left"}, width=0.5),
    ColumnDefinition(name="team", textprops={"ha": "left"}, width=0.5),
    ColumnDefinition(
        name="player_name", textprops={"ha": "left", "weight": "bold"}, width=0.5
    ),
    ColumnDefinition(name="YC", textprops={"ha": "center"}, width=0.5),
    ColumnDefinition(name="RC", textprops={"ha": "center"}, width=0.5),
]
plt.rcParams["font.family"] = "monospace"
table_fig, ax = plt.subplots(figsize=(5, 8))

table = Table(
    cards.iloc[3:27],
    column_definitions=cols_defs,
    index_col="rank",
    row_dividers=True,
    row_divider_kw={"linewidth": 1, "linestyle": (0, (1, 3))},
    footer_divider=True,
    textprops={"fontsize": 10},
    col_label_divider_kw={"linewidth": 1, "linestyle": "-"},
    column_border_kw={"linewidth": 0.5, "linestyle": "-"},
    ax=ax,
)

table.cells[10, 3].textprops["color"] = "#8ACB88"


st.pyplot(fig=table_fig, use_container_width=True)
