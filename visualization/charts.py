
import plotly.graph_objects as go
import streamlit as st


def show_comparison_chart(results):

    algorithms = list(results.keys())

    hits = [results[name][1] for name in algorithms]
    faults = [results[name][2] for name in algorithms]

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            name="Page Hits",
            x=algorithms,
            y=hits
        )
    )

    fig.add_trace(
        go.Bar(
            name="Page Faults",
            x=algorithms,
            y=faults
        )
    )

    fig.update_layout(
        title="Page Hits vs Page Faults",
        xaxis_title="Page Replacement Algorithm",
        yaxis_title="Number of Pages",
        barmode="group"
    )

    st.plotly_chart(fig, use_container_width=True)
