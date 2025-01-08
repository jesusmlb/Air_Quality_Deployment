import streamlit as st
import pandas as pd
from datetime import datetime, time

def information_page():
    # Page title and description
    st.title("Information")
    
    # Create two columns for best/worst time cards
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("🌟 Best time to be outside\n\n"
                "**8:00 AM - 11:00 AM**\n\n"
                "Air quality: Good")
    
    with col2:
        st.info("⚠️ Worst time to be outside\n\n"
                  "**2:00 PM - 5:00 PM**\n\n"
                  "Air quality: Bad")
    
    # Create two columns for user selection of time and group
    col1, col2 = st.columns(2)
    
    with col1:
        option_time = st.selectbox("Select time period",
    ("6:00 AM - 9:00 AM", "9:00 AM - 12:00 AM", "12:00 PM - 3:00 PM", "3:00 PM - 6:00 PM", "6:00 PM - 9:00 PM", "9:00 PM - 12:00 AM", "12:00 AM - 3:00 AM", "3:00 AM - 6:00 AM"),
    )
        st.write("You selected:", option_time)
    
    with col2:
        option_group = st.selectbox("Select group",
    ("General population", "Children under 12 years old and pregnant people", "People with cardiovascular or respiratory diseases and those over 60 years of age"),
    )
        st.write("You selected:", option_group)
    
    # Create the main recommendations table
    data = {
        'Time': ['6:00 AM - 7:00 AM', '7:00 AM - 8:00 AM', '8:00 AM - 9:00 AM'],
        'Air Quality': ['Good', 'Bad', 'Bad'],
        'Risk Level': ['Low', 'High', 'High'],
        'Description of risk': ['The health risk is minimal or non-existent.', 'It is unlikely that health will be affected.', 'It is unlikely that health will be affected.'],
        'Messages': [
            'Enjoy outdoor activities',
            'Outdoor activities are possible. If you have symptoms such as coughing or shortness of breath, take more breaks and do less vigorous activities. Stay informed about the evolution of air quality.',
            'Outdoor activities are possible. If you have symptoms such as coughing or shortness of breath, take more breaks and do less vigorous activities. Stay informed about the evolution of air quality.'
        ]
    }
    
    df = pd.DataFrame(data)

    # Style the dataframe
    def color_risk(val):
        if val == 'Low' or val == 'Goo':
            return 'color: #00E400'
        elif val == 'Moderate':
            return 'color: #FFFF00'
        elif val == 'High':
            return 'color: #FF7E00'
        elif val == 'Very High':
            return 'color: #FF0000'
        else:
            return 'color: #8F3F97'

    # Style the dataframe
    def color_air_quality(val):
        if val == 'Good':
            return 'color: #00E400'
        elif val == 'Acceptable':
            return 'color: #FFFF00'
        elif val == 'Bad':
            return 'color: #FF7E00'
        elif val == 'Very bad':
            return 'color: #FF0000'
        else:
            return 'color: #8F3F97'

    # Apply styling
    styled_df = df.style.applymap(color_risk, subset=['Risk Level']).applymap(color_air_quality, subset=['Air Quality'])
    
    # Display the table with custom CSS
    st.markdown("""
        <style>
        .stDataFrame {
            font-size: 16px;
        }
        .stDataFrame td {
            padding: 15px !important;
        }
        .stDataFrame th {
            background-color: #f0f2f6;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.table(styled_df)
    
    # Add explanatory notes
    st.markdown("""
    ### Notes
    - Information is based on a 24-hour forecast for the Air and Health Index
    - The Air and Health Index and associated messages are only for information purposes to warn the population in a city or locality at a given time.
    - Please consider personal health conditions and stay updated with local authorities and health providers.
    """)

if __name__ == "__main__":
    st.set_page_config(
        page_title="Information",
        page_icon="🏥",
        layout="wide"
    )
    information_page()