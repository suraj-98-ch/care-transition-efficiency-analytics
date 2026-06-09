import streamlit as st


def show_kpis(kpis):

    cols = st.columns(len(kpis))

    for col, (title, value) in zip(cols, kpis):
        with col:
            st.markdown(
                f"""
                <div style="
                    background:#1e293b;
                    padding:20px;
                    border-radius:15px;
                    text-align:center;
                    border:1px solid #334155;
                    margin-bottom:10px;
                ">
                    <h4 style="margin:0;color:#94a3b8;">
                        {title}
                    </h4>
                    <h2 style="margin-top:10px;color:white;">
                        {value}
                    </h2>
                </div>
                """,
                unsafe_allow_html=True
            )