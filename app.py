from io import BytesIO

import altair as alt
import pandas as pd
import plotly.express as px
import requests
import streamlit as st


# Function to fetch CPS data from FTP server
@st.cache_data
def load_cps_data():
    url = 'https://www2.census.gov/programs-surveys/cps/datasets/2024/basic/jul24pub.csv'
    response = requests.get(url)
    try:
        data = pd.read_csv(BytesIO(response.content), encoding='latin1')
    except pd.errors.ParserError as e:
        st.error(f"Error parsing CSV file: {e}")
        st.stop()
    return data

# Preprocess CPS data
def preprocess_cps_data(data):
    # Verify that the columns exist in the dataframe
    expected_columns = ['prtage', 'pesex', 'peeduca', 'pemlr']
    if not all(col in data.columns for col in expected_columns):
        st.error(f"One or more required columns are missing: {expected_columns}")
        st.stop()

    # Select relevant columns for visualization
    data = data[['prtage', 'pesex', 'peeduca', 'pemlr']]
    data = data.rename(columns={'prtage': 'Age', 'pesex': 'Sex', 'peeduca': 'Education', 'pemlr': 'Employment Status'})

    # Convert categorical columns to readable format
    sex_map = {1: 'Male', 2: 'Female'}
    education_map = {
        31: 'Less than 1st grade', 32: '1st, 2nd, 3rd or 4th grade', 33: '5th or 6th grade', 34: '7th or 8th grade',
        35: '9th grade', 36: '10th grade', 37: '11th grade', 38: '12th grade no diploma', 39: 'High school grad (GED)',
        40: 'Some college but no degree', 41: 'Associate degree - occupational/vocational',
        42: 'Associate degree - academic program', 43: 'Bachelor’s degree', 44: 'Master’s degree',
        45: 'Professional school degree', 46: 'Doctorate degree'
    }
    employment_status_map = {
        1: 'Employed - at work', 2: 'Employed - absent', 3: 'Unemployed - on layoff',
        4: 'Unemployed - looking', 5: 'Not in labor force - retired', 6: 'Not in labor force - disabled',
        7: 'Not in labor force - other'
    }

    data['Sex'] = data['Sex'].map(sex_map)
    data['Education'] = data['Education'].map(education_map)
    data['Employment Status'] = data['Employment Status'].map(employment_status_map)

    return data

cps_data = load_cps_data()
cps_data = preprocess_cps_data(cps_data)

# Streamlit UI
st.title('US Census CPS Data Visualization')
st.write('Visualizations based on the July 2024 Current Population Survey.')

# Visualization 1: Age Distribution by Employment Status
st.subheader('Age Distribution by Employment Status')
st.write('This Plotly box plot shows the distribution of ages for different employment statuses. Hover over the boxes to see detailed statistics.')
fig1 = px.box(cps_data, x='Employment Status', y='Age', title='Age Distribution by Employment Status')
st.plotly_chart(fig1)

# Visualization 2: Education Level by Sex
st.subheader('Education Level by Sex')
st.write('This Altair chart shows the education level distribution by sex. Hover over the bars to see details.')
alt_chart = alt.Chart(cps_data).mark_bar().encode(
    x='count()',
    y='Education',
    color='Sex',
    tooltip=['count()', 'Education', 'Sex']
).interactive().properties(
    width=700,
    height=400
)
st.altair_chart(alt_chart)

# Visualization 3: Employment Status by Age and Sex (Heatmap)
st.subheader('Employment Status by Age and Sex')
st.write('This heatmap shows the density of different age groups within each employment status, split by sex.')

# Prepare data for heatmap
heatmap_data = cps_data.groupby(['Employment Status', 'Sex', 'Age']).size().reset_index(name='Count')

# Create heatmap
fig2 = px.density_heatmap(
    heatmap_data,
    x='Age',
    y='Employment Status',
    z='Count',
    facet_col='Sex',
    color_continuous_scale='Viridis',
    title='Employment Status by Age and Sex'
)

st.plotly_chart(fig2)
