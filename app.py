
import streamlit as st
import pandas as pd

from algorithms.fifo import fifo
from algorithms.lru import lru
from algorithms.optimal import optimal
from visualization.charts import show_comparison_chart


st.set_page_config(
    page_title="Page Replacement Simulator",
    page_icon="💻",
    layout="wide"
)

st.title("💻 Page Replacement Algorithm Simulator")

st.write(
    "Explore and compare FIFO, LRU and Optimal "
    "page replacement algorithms."
)

st.divider()

st.subheader("Simulation Settings")

reference_input = st.text_input(
    "Enter page reference string",
    "1 2 3 1 4 2 5"
)

frame_capacity = st.number_input(
    "Number of frames",
    min_value=1,
    max_value=10,
    value=3,
    step=1
)

algorithm = st.selectbox(
    "Choose Page Replacement Algorithm",
    ["FIFO", "LRU", "Optimal", "Compare All"]
)


def show_result(name, result):
    history, hits, faults = result
    total = hits + faults

    st.subheader(name)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Page Hits", hits)
    col2.metric("Page Faults", faults)
    col3.metric("Hit Ratio", f"{hits / total:.2%}")
    col4.metric("Fault Ratio", f"{faults / total:.2%}")

    rows = []

    for step, item in enumerate(history, start=1):
        row = {
            "Step": step,
            "Page": item["page"]
        }

        for i in range(int(frame_capacity)):
            if i < len(item["frames"]):
                row[f"Frame {i + 1}"] = str(item["frames"][i])
            else:
                row[f"Frame {i + 1}"] = "-"

        row["Status"] = item["status"]
        rows.append(row)

    st.write("Frame-by-frame simulation")
    st.dataframe(pd.DataFrame(rows), use_container_width=True)



if st.button("Run Simulation"):

    try:
        pages = [int(x) for x in reference_input.split()]

        if not pages:
            st.error("Please enter a page reference string.")

        else:
            algorithms = {
                "FIFO": fifo,
                "LRU": lru,
                "Optimal": optimal
            }

            if algorithm == "Compare All":

                comparison_results = {}

                for name, function in algorithms.items():
                    result = function(pages, int(frame_capacity))
                    comparison_results[name] = result
                    show_result(name, result)

                show_comparison_chart(comparison_results)

            else:
                result = algorithms[algorithm](
                    pages,
                    int(frame_capacity)
                )

                show_result(algorithm, result)

                show_comparison_chart({algorithm: result})

    except ValueError:
        st.error("Please enter valid numbers separated by spaces.")


