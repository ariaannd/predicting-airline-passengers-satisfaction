# Import Libraries
import prediction 
import streamlit as st
import pandas as pd
import joblib
import eda

# Set Option
st.set_option('deprecation.showPyplotGlobalUse', False)

# Header
st.header('Airline Passenger Satisfaction Prediction')
st.write("""
Created by Aria Ananda

This project is made to predicts wether an airline passenger will be satisfied or not using Machine learning classification method.
""")

@st.cache
def fetch_data():
    df = pd.read_csv('airline_passenger_satisfaction.csv')
    return df

df = fetch_data()
st.write("""Airline Passenger Data Sample""")
st.write(df.head(500))

def main():
    st.title("Airline Passenger Satisfaction Predictor App")


def user_input():
    gender = st.selectbox("Gender", ['Female', 'Male'], key='gender')
    customer_type = st.selectbox("Customer Type", ['Loyal Customer', 'disloyal Customer'], key='customer_type')
    age = st.slider("Age", min_value=8, max_value=80, value=40)
    type_of_travel = st.selectbox("Type of Travel", ['Business travel', 'Personal Travel'], key='type_of_travel')
    customer_class = st.selectbox("Class", ['Business', 'Eco', 'Eco Plus'], key='customer_class')
    flight_distance = st.number_input("Flight Distance", value=2863, key='flight_distance')
    inflight_wifi_service = st.number_input("Enter Inflight Wifi Service Value (0-5)", value=3.0, key='inflight_wifi_service')
    departure_convinient = st.number_input("Enter Departure and Arrival Time Convinience Value (0-5)", value=3.0, key='departure_convinient')
    ease_of_online_booking = st.number_input("Enter Ease of Online Booking Value (0-5)", value=4.0, key = 'ease_of_online_booking')
    gate_location = st.number_input("Enter Gate Location Value (0-5)", value=4.0, key='gate_location')
    food_and_drink = st.number_input("Enter Food and Drink Value (0-5)", value=4.0, key='food_and_drink')
    online_boarding = st.number_input("Enter Online Boarding Value (0-5)", value=3.0, key='online_boarding')
    seat_comfort = st.number_input("Enter Seat Comfort Value (0-5)", value=3.0, key='seat_comfort')
    inflight_entertainment = st.number_input("Enter Inflight Entertainment Value (0-5)", value=3.0, key='inflight_entertainment')
    onboard_service =  st.number_input("Enter On Board Service (0-5)", value=3.0, key='onboard_service')
    leg_room_service = st.number_input("Enter Leg Room Service Value (0-5)", value=3.0, key='leg_room_service')
    baggage_handling = st.number_input("Enter Baggage Handling Value (1-5)", value=3.0, key='baggage_handling')
    checkin_service = st.number_input("Enter Check In Service Value (0-5)", value=3.0, key='checkin_service')
    inflight_service = st.number_input("Enter Inflight Value (0-5)", value=3.0, key='inflight_service')
    cleanliness = st.number_input("Enter Cleanliness Value (0-5)", value=3.0, key='cleanliness')
    departure_delay =  st.number_input("Enter Departure Delay in Minutes", value=30.0, key='departure_delay')
    arrival_delay = st.number_input("Enter Arrival Delay in Minutes", value=30.0, key='arrival_delay')
    
    data={
        'Gender': gender,
        'Customer Type': customer_type,
        'Age': age,
        'Type of Travel': type_of_travel,
        'Class': customer_class,
        'Flight Distance': flight_distance,
        'Inflight wifi service' : inflight_wifi_service,
        'Departure/Arrival time convenient' : departure_convinient,
        'Ease of Online booking' : ease_of_online_booking,
        'Gate location' : gate_location,
        'Food and drink' : food_and_drink,
        'Online boarding' : online_boarding,
        'Seat comfort' : seat_comfort,
        'Inflight entertainment' : inflight_entertainment,
        'On-board service' : onboard_service,
        'Leg room service' : leg_room_service,
        'Baggage handling' : baggage_handling,
        'Checkin service' : checkin_service,
        'Inflight service' : inflight_service,
        'Cleanliness' : cleanliness,
        'Departure Delay in Minutes' : departure_delay,
        'Arrival Delay in Minutes' : arrival_delay
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input()

st.subheader('User Input')
st.write(input_df)

if st.button("Predict Satisfaction"):
    # Make prediction and display the result
    prediction = prediction.predict_default(input_df)
    st.write(f"Prediction: {'Satisfied' if prediction == 'satisfied' else 'Neutral or Dissatisfied'}")
    # if prediction == 'satisfied':
    #     st.write("Satisfied")
    # else:
    #     st.write("Neutral or Dissatisifed.")

st.title('Exploratory Data Analysis')

eda.plot1()
st.write("""
-**Histogram Plot of Passenger Ages - Insights**  
- Majority of passengers age are between 20 - 60
- Most of `frequent passengers age are of age 39-40`
- Young (below age 20) and Elderly (age 60+) passengers rarely use Japan's Airlines service.  indicating potential areas for targeted marketing and service improvements to attract a wider demographic range. 

Understanding the preferences and needs of these age groups can aid in tailoring services to better meet passenger expectations and enhance overall customer satisfaction within Japan's Airlines.
""")

eda.plot2()
st.write("""
**Violin Plot of flight Distance - Insights**  

The visualization of flight distance variation across different flights on Japan's Airlines reveals distinct patterns. The majority of flights fall within the range of approximately 300 to 1200 miles, `indicating common short to medium-haul routes within a specific region`. Occasionally, there are longer flights extending up to around 1500 and 2500 miles, likely representing longer-haul routes connecting major cities or spanning across regions. Rarely, there are extreme outliers with distances exceeding 4000 miles, indicative of infrequent long-haul international flights. These insights could provide valuable information for route planning and scheduling. Understanding these patterns can help optimize operations and enhance the airline's service offerings to meet passenger needs effectively.""")

eda.plot3()
st.write("""
**Bar Plot and Pie Chart of inflight wifi service**  

From the descriptive summary, it's evident that inflight service received the lowest satisfaction score among all satisfaction metrics. Analyzing the visualization further, we observe that nearly half (49.7%) of passengers rated inflight Wi-Fi service between 2 and 3, `indicating a mediocre satisfaction level`. In contrast, only a small proportion of passengers rated it highly, with 11.1% giving a rating of 5, and 19.1% giving a rating of 4. Interestingly, a notable portion of passengers rated the service poorly, with 17.2% giving a rating of 0, and only 3% giving a rating of 1. This `suggests that while a significant portion of passengers have a neutral or positive perception of the inflight Wi-Fi service, there is also a considerable dissatisfaction among passengers`, highlighting areas for potential improvement to enhance overall passenger experience.""")

eda.plot4()
st.write("""
**Histogram and Pie Chart of Satisfaction - Insights**  

From the overall satisfaction visualization, it's evident that only 43.4% or approximately 58,000 passengers are satisfied, while the majority, comprising 56.6% or over 70,000 passengers, `express a neutral or dissatisfied sentiment among passengers`. This indicates a significant portion of passengers are not fully content with their experience, highlighting potential areas for improvement in the airline's services or customer experience initiatives. Addressing the concerns of neutral or dissatisfied passengers could be crucial in enhancing overall passenger satisfaction and loyalty, ultimately contributing to the airline's success and reputation in the industry. From this target distribution we also could know that the data is not imbalance.

""")

eda.plot5()
st.write("""
**Countplots of rating distributions of other service satisfaction-related Columns**  

Below are some insights we can take from the countplots of services satisfaction related columns:

- The distribution of ratings reveals some stark contrasts in passenger satisfaction across various services. While some passengers gave low ratings (0) to services like Baggage handling, Departure/Arrival Time Convenient, Ease of online booking, online boarding, and leg room service, others provided relatively higher ratings (3-5). This suggests a notable disparity in the perceived quality of different aspects of the airline experience.
- Interestingly, services receiving ratings of 1-2 show a more scattered distribution across all categories, with notable concentrations in ease of online booking, food and drink, and gate location. `This indicates areas where passengers are particularly dissatisfied and where targeted improvements could yield significant enhancements in overall satisfaction`.
- Moreover, despite the majority of customers opting for a moderate rating of 3 across most services, some services, such as check-in service, inflight service, and baggage handling, receive notably higher ratings of 4 and even occasional 5s. This implies that certain aspects of the passenger experience are consistently meeting or exceeding expectations, warranting further investigation into their underlying factors for potential replication or improvement in other areas.
""")

eda.plot6()
st.write("""
**Violin Plot of Satisfaction and Age - Insights**   

From the visualization, it's apparent that there exists a slight positive correlation between passenger satisfaction and age. This comes from distinction of age and their satisfaction level. `Notably, younger passengers tend to exhibit lower satisfaction levels compared to their older counterparts`. This observation is supported by the wider spread of satisfaction levels among younger age groups, indicating a greater variability in satisfaction experiences. Conversely, older passengers demonstrate a narrower spread of satisfaction levels, with the median satisfaction level notably higher than that of younger passengers. The violin plot illustrates this trend by depicting a positive relationship between passenger age and satisfaction levels. In summary, the visualization suggests that `younger passengers are more inclined to report neutral or dissatisfied levels of satisfaction, while older passengers are more likely to express higher levels of satisfaction with their flight experiences`. This assumptions is in line with the wi-fi inflight satisfaction, where we could assume younger generation would more likely tend to using the wi-fi than older generation.
""")

eda.plot7()
st.write("""
**Countplot of satisfaction Grouped by Type of Travel - Insights**  

The countplot visualization based on the type of travel reveals a stark contrast in satisfaction levels between passengers traveling for business purposes and those traveling for personal reasons. A notable observation is that over 50,000 passengers on business trips reported being satisfied, whereas the number of satisfied passengers on personal trips was significantly lower, totaling just below 10,000. Conversely, the count of passengers expressing neutral or dissatisfied sentiments was more balanced between the two travel types, with approximately 37,000 passengers on business trips and 36,000 passengers on personal trips falling into this category. This suggests that, `overall, passengers on business trips tend to have higher satisfaction levels compared to those on personal trips`, possibly indicating differences in service expectations or experiences tailored to the respective travel purposes. 

""")

eda.plot8()
st.write("""
**Countplot of Satisfaction levels of loyal and non loyal customers - Insights**  

The countplot analysis reveals notable disparities in satisfaction levels between loyal and non-loyal customers of Japan's Airline. Specifically, approximately 50,000 loyal customers reported feeling satisfied, whereas over 55,000 loyal customers expressed neutral or dissatisfied sentiments regarding the airline's performance. In contrast, only around 5,000 non-loyal customers reported feeling satisfied, while approximately 18,000 non-loyal customers conveyed neutral or dissatisfied feelings. `This stark contrast suggests that loyal customers tend to have higher satisfaction levels compared to non-loyal customers`, highlighting the importance of customer loyalty in shaping overall satisfaction with Japan's Airline.
""")


