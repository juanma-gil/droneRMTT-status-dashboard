import time
import pandas as pd
import matplotlib.pyplot as plt
import random_input as r_in
import client_status_tello as client_status
import streamlit as st

# Main Streamlit app
st.title('Drone Telemetry Dashboard')

# Create a JSON container
json_container = st.empty()
chart_placeholder = st.empty()

# Create a list to store the history of drone data
history = []

flight_time = [0]

# Create a 3D scatter plot of the x, y, and z coordinates
fig = plt.figure(figsize=(5, 5))
ax = plt.axes(projection='3d')
ax.set_title('Drone Position')
scatter = ax.scatter3D([], [], [])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
# Set a transparent background for the chart
fig.set_facecolor('none')

# Create a line chart of the battery data
fig2, ax2 = plt.subplots(figsize=(5, 5))
line2, = ax2.plot([], [], color='#FF7F50', linewidth=2, label='battery')
ax2.set_title('Battery')
ax2.grid()
ax2.legend()
ax2.set_xlabel('Time')
ax2.set_ylabel('Battery')

# Create a line chart of the pressure data
fig3, ax3 = plt.subplots(figsize=(5, 5))
line3, = ax3.plot([], [], color='#FF7F50', linewidth=2, label='pressure')
ax3.set_title('Pressure')
ax3.grid()
ax3.legend()
ax3.set_xlabel('Time')
ax3.set_ylabel('Pressure')

# Create a line chart of the aceleration data
fig4, ax4 = plt.subplots(figsize=(5, 5))
line4a, = ax4.plot([], [], linewidth=2,label='agx')
line4b, = ax4.plot([], [], linewidth=2, label='agy')
line4c, = ax4.plot([], [], linewidth=2, label='agz')
ax4.set_title('Aceleration')
ax4.grid()
ax4.legend()
ax4.set_xlabel('Time')
ax4.set_ylabel('Aceleration')

# Create a line chart of the velocity data
fig5, ax5 = plt.subplots(figsize=(5, 5))
line5a, = ax5.plot([], [], linewidth=2,label='vgx')
line5b, = ax5.plot([], [], linewidth=2, label='vgy')
line5c, = ax5.plot([], [], linewidth=2, label='vgz')
ax5.set_title('Velocity')
ax5.grid()
ax5.legend()
ax5.set_xlabel('Time')
ax5.set_ylabel('Velocity')

# Create a line chart of the mpry data
fig6, ax6 = plt.subplots(figsize=(5, 5))
line6a, = ax6.plot([], [], linewidth=2,label='pitch')
line6b, = ax6.plot([], [], linewidth=2, label='roll')
line6c, = ax6.plot([], [], linewidth=2, label='yaw')
ax6.set_title('Mpry')
ax6.grid()
ax6.legend()
ax6.set_xlabel('Time')
ax6.set_ylabel('mpry')

# Create a line chart of the altitude data
fig7, ax7 = plt.subplots(figsize=(5, 5))
line7, = ax7.plot([], [], linewidth=2,label='altitude')
ax7.set_title('Altitude')
ax7.grid()
ax7.legend()
ax7.set_xlabel('Time')
ax7.set_ylabel('Altitude')

while True:
    # Generate random drone data
    # drone_data = client_status.get_json_data()
    drone_data = r_in.generate_random_drone_data()
    
    # Create a Pandas DataFrame from the drone data
    df = pd.DataFrame(drone_data)

    # Add the new data points to the history list
    history.append(df)

    # flight_time = [df['time'].values[0] for df in history]

    # Update the scatter plot with the new data points
    for df in history:
        ax.scatter3D(df['x'], df['y'], df['z'], c='#FF7F50')

    # Update the line chart with the new battery data
    time_data = flight_time
    bat_data = [df['bat'].values[0] for df in history]
    line2.set_data(time_data, bat_data)
    ax2.relim()
    ax2.autoscale_view()

    # Update the line chart with the new pressure data
    baro_data = [df['baro'].values[0] for df in history]
    line3.set_data(time_data, baro_data)
    ax3.relim()
    ax3.autoscale_view()

    # Update the line chart with the new aceleration data
    agx_data = [df['agx'].values[0] for df in history]
    agy_data = [df['agy'].values[0] for df in history]
    agc_data = [df['agz'].values[0] for df in history]
    line4a.set_data(time_data, agx_data)
    line4b.set_data(time_data, agy_data)
    line4c.set_data(time_data, agc_data)
    ax4.relim()
    ax4.autoscale_view()

    # Update the line chart with the new velocity data
    vgx_data = [df['vgx'].values[0] for df in history]
    vgy_data = [df['vgy'].values[0] for df in history]
    vgc_data = [df['vgz'].values[0] for df in history]
    line5a.set_data(time_data, vgx_data)
    line5b.set_data(time_data, vgy_data)
    line5c.set_data(time_data, vgc_data)
    ax5.relim()
    ax5.autoscale_view()
    
    # Update the line chart with the new velocity data
    pitch_data = [df['mpry'].values[0] for df in history]
    roll_data = [df['mpry'].values[1] for df in history]
    yaw_data = [df['mpry'].values[2] for df in history]
    line6a.set_data(time_data, pitch_data)
    line6b.set_data(time_data, roll_data)
    line6c.set_data(time_data, yaw_data)
    ax6.relim()
    ax6.autoscale_view()

    # Update the line chart with the new altitude data
    alt_data = [df['h'].values[0] for df in history]
    line7.set_data(time_data, alt_data)
    ax7.relim()
    ax7.autoscale_view()

    # TODO: if you don't want to use the random data comment this line and uncomment flight_time var above
    flight_time.append(flight_time[-1] + 1)

    #Update the JSON container with the new data
    json_container.json(drone_data)

    with chart_placeholder:
        # creating three columns
        col1, col2 = st.columns(2)
        with col1:
            st.pyplot(fig)
            st.pyplot(fig3)
            st.pyplot(fig5)
            st.pyplot(fig7)
        with col2:
            st.pyplot(fig2)
            st.pyplot(fig4)
            st.pyplot(fig6)
    # Sleep for a specified interval (e.g., 1 second) to simulate real-time updates
    time.sleep(1)
    