import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Class 17")

st.header("Data")
st.write("This section is for showing data structure")

df = pd.read_excel("./sample_-_superstore (2).xls")

st.write(df.head(3))


st.set_page_config(layout="wide")
st.header("Visualizations")


#figure 1#
col1, col2 = st.columns([7,3])

with col1:
    df2 = df[df["Country/Region"]=="United States"]
    
    profit_sums_state = df2.groupby("State/Province")["Profit"].sum()
    sale_sums_state = df2.groupby("State/Province")["Sales"].sum()
    profit_margin_state = profit_sums_state/sale_sums_state
    profit_margin_state = profit_margin_state.reset_index(name="Profit Margin")
    
    fig1 = px.choropleth(
    locations=profit_margin_state["State/Province"],
    locationmode="USA-states",
    color=profit_margin_state["Profit Margin"],
    scope="usa",
    color_continuous_scale="Viridis"
    )
    
    st.plotly_chart(fig1, width="stretch") 

#fig 2#
with col2:
    profit_category = df2.groupby("Category")["Profit"].sum()
    sales_category = df2.groupby("Category")["Sales"].sum()
    profit_margin_category = profit_category/sales_category
    profit_margin_category.reset_index(name="Profit Margin")
    profit_margin_category = profit_margin_category.reset_index(name="Profit Margin")
    
    fig2 = px.bar(profit_margin_category, x="Category", y="Profit Margin", color="Category")
    
    st.plotly_chart(fig2, width="stretch")

col3, col4 = st.columns([5,5])

#fig 3#
with col3:
    df2["YM"] = pd.to_datetime(df2["Order Date"]).dt.strftime("%Y/%m")
    
    a = df2.groupby(["Category", "YM"])["Profit"].sum()
    b = df2.groupby(["Category", "YM"])["Sales"].sum()
    
    profit_margin_category_ym = (a / b).reset_index(name="Profit Margin")
    profit_margin_category_ym


    fig4 = px.treemap(df2, path=["Category", "Sub-Category"], values="Sales", color="Category")
    
    fig4 = px.treemap(
        df2,
        path=["Category", "Sub-Category"],
        values="Sales",
        color="Category",
        color_discrete_map={
            "Furniture": "#4C72B0",
            "Office Supplies": "#55A868",
            "Technology": "#C44E52"
        }
    )
    
    all_states = df["State/Province"].unique()
    target_states = st.multiselect("Choose states", options=all_states, default=["North Carolina", "South Carolina"])
    
    df = df[df["State/Province"].isin(target_states)]
    



