import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_appointments_by_time(df):
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(
        data=df,
        x='TIME_BETWEEN_BOOK_AND_APPT',
        y='COUNT_OF_APPOINTMENTS',
        color='skyblue'
    )

    for container in ax.containers:
        ax.bar_label(container, fmt='%d', label_type='edge', padding=3)

    plt.xlabel('Time Between Booking and Appointment')
    plt.ylabel('Count of Appointments')
    plt.title('Rate of Appointments by Time Between Booking and Appointment')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_population_distribution(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Population'], bins=30, kde=True, color='purple')
    plt.xlabel('Population')
    plt.ylabel('Frequency')
    plt.title('Distribution of Population')
    plt.tight_layout()
    plt.show()