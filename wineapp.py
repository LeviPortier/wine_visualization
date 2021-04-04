import streamlit as st
from compute2d import compute_2d_histogram
import numpy as np
import pandas as pd
import altair as at
from copy import copy
from paracoords import create_paracoords

#set configurations and title
st.set_page_config(page_title="Wine Explorer",
    page_icon=":wine_glass:",
    layout='wide')

st.title('Vinho Verde Quality Explorer')
st.write("This interactive webapp allows you to explore the quality and contents of portuguese vinho verde wine. Vinho verde is a unique product from the Minho region of Portugal. It is characterized by its medium alcohol percentage and people mostly appreciate its freshness in the summer. This data is retrieved from https://archive.ics.uci.edu/ml/datasets/wine%20quality. Lets start by choosing between white and red wine")

#load data
white = pd.read_csv('winequality-white.csv', sep=';')
red = pd.read_csv('winequality-red.csv', sep=';')


#create 2d correlation
value_columns_white = copy(white)
white2d_bins = pd.concat([compute_2d_histogram(var1, var2, white) for var1 in value_columns_white for var2 in value_columns_white])

value_columns_red = copy(red)
red2d_bins = pd.concat([compute_2d_histogram(var1, var2, white) for var1 in value_columns_red for var2 in value_columns_red])

#create selector
st.markdown("### **Choose your wine type:**")
select_color = ['Red','White']
option = st.radio('',select_color)

if option == 'Red':
    data = red
    data2d_bins = red2d_bins
if option == 'White':
    data = white
    data2d_bins = red2d_bins

#function to create first plot
fig = create_paracoords(data)
"The dataset contains physicochemical attributes of each wine and a rating (scale 1-10) by an expert. The plot below shows all these attributes together"
"Play around with the slider in the first column to see how quality is affected by different combinations of psychochemical substances"
st.plotly_chart(fig, use_container_width=True)


###SECOND PLOT USING ALTAIR####
#create correlation table
corr_data = data.corr().stack().reset_index().rename(columns={0: 'correlation', 'level_0': 'variable', 'level_1': 'variable2'})
#round values
corr_data['correlation_label']=np.round(corr_data['correlation'],2)

### Create correlation plot ###
# Define selector
var_sel_cor = at.selection_single(fields=['variable', 'variable2'], clear=False, 
                                  init={'variable': 'quality', 'variable2': 'alcohol'})

# Define correlation heatmap
base = at.Chart(corr_data).encode(
    x='variable2:O',
    y='variable:O'    
)
text = base.mark_text().encode(
    text='correlation_label',
    color=at.condition(
        at.datum.correlation > 0.5, 
        at.value('white'),
        at.value('black')
    )
)

cor_plot = base.mark_rect().encode(
    color=at.condition(var_sel_cor, at.value('pink'), 'correlation:Q')
).add_selection(var_sel_cor)

# Define 2d binned histogram plot
scat_plot = at.Chart(data2d_bins).transform_filter(
    var_sel_cor
).mark_rect().encode(
    at.X('value2:N', sort=at.EncodingSortField(field='raw_left_value2')), 
    at.Y('value:N', sort=at.EncodingSortField(field='raw_left_value', order='descending')),
    at.Color('correlation:Q', scale=at.Scale(scheme='blues'))
)


"Explore the correlation between the chemical properties of wine. By clicking on a correlation in the left plot, the right plot will show the correlation between the two variables. For instance clicking on the correlation between alcohol and quality in the left plot, will show you the correlation in the right plot and for which values it is strongest."

# Combine all plots
@st.cache
st.altair_chart(at.hconcat((cor_plot + text).properties(width=350, height=350, title = 'Correlation of Chemical Properties'),
 scat_plot.properties(width=350, height=350)).resolve_scale(color='independent'))


