import streamlit as st
from core.llm_utils import LLMUtils
from core.database import get_score_history
import altair as alt

def render_score_history():
    
    st.title("📊 Score History")
    df = get_score_history()
    if not df.empty:
        df["Index"] = range(1, len(df) + 1)

        # Base line chart of actual scores
        base = alt.Chart(df).mark_line(point=True).encode(
            x=alt.X("Index", title="Attempt Number"),
            y=alt.Y("Score", title="Score"),
            tooltip=["Index", "Score"]
        ).properties(
            title="Score Progression with Trend Line",
            width=700,
            height=400
        )

        # Trend line using regression
        trend = base.transform_regression("Index", "Score").mark_line(color="orange", strokeDash=[5,5]).encode()

        chart = base + trend
        st.altair_chart(chart, use_container_width=True)

    else:
        st.info("No score data yet.")

    pass

