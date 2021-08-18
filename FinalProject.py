"""
Name:       Aidan Jacowleff
CS230:      Section 2
Data:       Used cars for sale on craigslist
URL:        Link to your web application online (see extra credit)
Description:

This program seeks to answer 2 questions:

The first question I seek to answer is how many miles do cars of certain years have.  If a new car has a lot of miles,
you would want to stay away from it.  If an old car doesn't have a lot of miles that also could be a bad sign.

The second question I seek to answer also revolves around quality.
I would like to compare the year of the car to the price.  if the price of the car is still high even though its older,
that means it is likely a very good car.  if a new car has a low price it probably has something wrong with it.
"""

import streamlit as st
import numpy as np
from statistics import median
from statistics import mean
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

# collect data for the years and miles
data_file = pd.read_csv('vehicles.csv')
year = (data_file.loc[30:150, 'year'])
price = (data_file.loc[30:150, 'price'])
miles = (data_file.loc[30:150, 'odometer'])

def scatter():

    price = [data_file.loc[30:150, 'price']]
    year = data_file.loc[30:150, 'year']
    plt.title(f"Price of Vehicle compared to year", color="blue")
    plt.xlabel(f"Year")
    plt.ylabel(f"Price")
    plt.xticks(rotation=45)
    plt.scatter(year, price)


# shows the cars miles with the year for the top 150 values in the list, the range can be adjusted
def bar_chart():
    year = data_file.loc[30:150, 'year']
    miles = data_file.loc[30:150, 'odometer']
    plt.xlabel(f"Year")
    plt.ylabel(f"Miles")
    plt.xticks(rotation=45)
    plt.title(f"Year compared to Miles", color="red")
    plt.bar(year, miles)

options = ['select an option','Year versus Miles','Year versus Price']


st.title("*Welcome to the Craigslist Used Car sorter*")
st.write("<-- Select What data you would like to see")
video_file = open('drifting.mp4', 'rb')
video_byte = video_file.read()
st.video(video_byte)
st.write("*Note: All data is based on a subset of data for faster loading times - Specific sets can be revised upon request*")

def user_inputs():
    st.sidebar.header("Select Chart ")
    value = st.sidebar.selectbox("Select Dataset", options)
    button = st.sidebar.button("Get Chart")
    return value, button
def get_data(value):
    if value == 'Year versus Miles':
        return bar_chart()
    else:
        return scatter()

def main():
    value, button = user_inputs()
    if button:
        data = get_data(value)
        st.title(f"Chart for {value}")
        st.pyplot(data)


if __name__ == "__main__":
    main()










st.set_option('deprecation.showPyplotGlobalUse', False)



