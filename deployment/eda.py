# Import Libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define data
df = pd.read_csv('airline_passenger_satisfaction.csv')

# Grouping Columns

# Numerical Columns
num_cont_cols = ['Age', 'Flight Distance', 'Departure Delay in Minutes', 'Arrival Delay in Minutes']

num_disc_cols = ['Inflight wifi service', 'Departure/Arrival time convenient', 'Ease of Online booking' ,  'Gate location',
                 'Food and drink', 'Online boarding' ,  'Seat comfort',  'Inflight entertainment',  'On-board service',
                 'Leg room service', 'Baggage handling', 'Checkin service', 'Inflight service', 'Cleanliness']

# Categorical Columns
cat_disc_cols = ['Gender', 'Customer Type',  'Type of Travel', 'Class']

# Create Plot Functions
def plot1():
    # Histogram Plot of Passenger Ages
    plt.figure(figsize=(8, 6))
    plt.hist(df['Age'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribution of Passenger Ages')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.grid(True)
    st.pyplot()

def plot2():
    # Bar Plot and Pie Chart of inflight wifi service

    # Inflight wifi service value counts into variable
    satisfaction_counts = df['Inflight wifi service'].value_counts().sort_index()

    # Satisfaction labels
    satisfaction_labels = ['0', '1', '2', '3', '4', '5'] 

    # Figure and axis 
    fig, axs = plt.subplots(1, 2, figsize=(15, 6))

    # Bar Plot
    axs[0].bar(satisfaction_labels, satisfaction_counts, color='skyblue')
    axs[0].set_title('Bar Plot of Passenger Satisfaction with Inflight Wi-Fi Service')
    axs[0].set_xlabel('Satisfaction Rating')
    axs[0].set_ylabel('Number of Passengers')
    axs[0].grid(axis='y', linestyle='--', alpha=1)  

    # Pie Chart
    axs[1].pie(satisfaction_counts, labels=satisfaction_labels, autopct='%1.1f%%', startangle=140, colors=['lightblue', 'lightgreen', 'gold', 'lightcoral', 'lightskyblue'])
    axs[1].set_title('Pie Chart of Passenger Satisfaction with Inflight Wi-Fi Service')
    axs[1].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

    # Showing the plot
    plt.tight_layout()
    st.pyplot()

def plot3():
    # Histogram and Pie Chart of satisfaction

    # Satisfaction counts
    satisfaction_counts = df['satisfaction'].value_counts()

    # Figure and axis
    fig, axs = plt.subplots(1, 2, figsize=(15, 6))

    # Histogram
    axs[0].hist(df['satisfaction'], bins=5, color='skyblue', edgecolor='black')
    axs[0].set_title('Histogram of Passenger Satisfaction Levels')
    axs[0].set_xlabel('Satisfaction Level')
    axs[0].set_ylabel('Number of Passengers')
    axs[0].set_xticks([0.1, 0.9])
    axs[0].set_xticklabels(['satisfied', 'neutral or dissatisfied'])
    axs[0].grid(axis='y', linestyle='--', alpha=0.7)

    # Pie Chart
    axs[1].pie(satisfaction_counts, labels=satisfaction_counts.index, autopct='%1.1f%%', startangle=140, colors=['orange', 'lightgreen'])
    axs[1].set_title('Pie Chart of Passenger Satisfaction Levels')
    axs[1].axis('equal')

    # Showing the Plot
    plt.tight_layout()
    st.pyplot()

def plot4():
    # Histogram and Pie Chart of satisfaction
    
    # Satisfaction counts
    satisfaction_counts = df['satisfaction'].value_counts()
    
    # Figure and axis
    fig, axs = plt.subplots(1, 2, figsize=(15, 6))
    
    # Histogram
    axs[0].hist(df['satisfaction'], bins=5, color='skyblue', edgecolor='black')
    axs[0].set_title('Histogram of Passenger Satisfaction Levels')
    axs[0].set_xlabel('Satisfaction Level')
    axs[0].set_ylabel('Number of Passengers')
    axs[0].set_xticks([0.1, 0.9])
    axs[0].set_xticklabels(['satisfied', 'neutral or dissatisfied'])
    axs[0].grid(axis='y', linestyle='--', alpha=0.7)
    
    # Pie Chart
    axs[1].pie(satisfaction_counts, labels=satisfaction_counts.index, autopct='%1.1f%%', startangle=140, colors=['orange', 'lightgreen'])
    axs[1].set_title('Pie Chart of Passenger Satisfaction Levels')
    axs[1].axis('equal')
    
    # Showing the Plot
    plt.tight_layout()
    st.pyplot()

def plot5():
        # Countplots of rating distributions of other service satisfaction-related Columns
    fig = plt.figure(figsize=(20, 15))
    n_columns = 3
    n_rows = 4

    # Define custom colors for countplot
    custom_colors = ["#FF5733", "#33FF7A", "#338CFF", "#FF33B2", "#B233FF", "#FF8C33", "#33FFB2", "#B2FF33", "#336DFF", "#FF33B2", "#33FF7A", "#FF5733"]

    for position in range(1, ((n_columns * n_rows) + 1)):
        if position > len(num_disc_cols):
            break
        else:
            fig.add_subplot(n_rows, n_columns, position)
            sns.countplot(data=df, x=num_disc_cols[position], palette=custom_colors).set(title=f'\n{num_disc_cols[position]}', xlabel='')
            fig.subplots_adjust(hspace=0.25, wspace=0.3)
    st.pyplot()

def plot6():
        # Violin Plot of Satisfaction and Age
    plt.figure(figsize=(8, 6))
    sns.violinplot(x='satisfaction', y='Age', data=df, palette='pastel', inner='quartile')
    plt.title('Correlation between Passenger Satisfaction Levels and Age')
    plt.xlabel('Satisfaction Level')
    plt.ylabel('Age')
    plt.grid(True)
    st.pyplot()

def plot7():
        # Countplot of satisfaction Grouped by Type of Travel
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x='satisfaction', hue='Type of Travel', palette='pastel')
    plt.title('Satisfaction Levels by Type of Travel')
    plt.xlabel('Satisfaction Level')
    plt.ylabel('Number of Passengers')
    plt.legend(title='Type of Travel')
    plt.grid(axis='y', linestyle='--', alpha=1)
    st.pyplot()

def plot8():
        # Countplot of Satisfaction levels of loyal and non loyal customers
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x='Customer Type', hue='satisfaction', palette='pastel')
    plt.title('Satisfaction Levels by Customer Type')
    plt.xlabel('Customer Type')
    plt.ylabel('Count')
    plt.legend(title='Satisfaction Level')
    plt.grid(axis='y', linestyle='--', alpha=1)
    st.pyplot()
