import streamlit as st
import plotly.express as px
import pandas as pd

# import dataset
st.title("INTERACTIVE DATA VISUALIZATION")
df=px.data.gapminder()
st.write(df)
# st.write(df.columns)

#Summary Statistics
# st.write(df.describe())

# #data management 
year_option = df["year"].unique().tolist()
# year = st.selectbox("which year should we plot?",year_option,0)
# df=df[df['year']== year]

# #plotting

fig = px.scatter(df,x='gdpPercap',y='lifeExp',size='pop',color='continent',hover_name='continent',
                 log_x=True,size_max=55,range_x=[100,1000],range_y=[20,90],
                 animation_frame='year',animation_group='country')

# Update the layout to change background color to white
fig.update_layout(
    width=2000,
    height=400,
    paper_bgcolor='grey',  # Background outside the plot
    plot_bgcolor='black',    # Background inside the plot
    xaxis_title='<b>GDP PER CAPITA</b>',  # Bold and black text for x-axis
    yaxis_title='<b>LIFE EXPECTANCY</b>',  # Bold and black text for y-axis
    font=dict(color="black")  # Set default font color to black
)

#Plot Command
st.write(fig)