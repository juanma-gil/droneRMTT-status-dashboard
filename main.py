import time
import pandas as pd
import matplotlib.pyplot as plt
import random_input as r_in
import client_status_tello as client_status
import streamlit as st
import json

# Main Streamlit app
st.title('Drone Telemetry Dashboard')

# Create a JSON container
json_container = st.empty()
chart_placeholder = st.empty()

# Create a list to store the history of drone data
history = []

flight_time = [0]

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
fig4a, ax4a = plt.subplots(figsize=(5, 5))
fig4b, ax4b = plt.subplots(figsize=(5, 5))
fig4c, ax4c = plt.subplots(figsize=(5, 5))

line4a, = ax4a.plot([], [], linewidth=2,label='agx')
line4b, = ax4b.plot([], [], linewidth=2, label='agy')
line4c, = ax4c.plot([], [], linewidth=2, label='agz')
ax4a.set_title('Aceleration X')
ax4a.grid()
ax4a.legend()
ax4a.set_xlabel('Time')
ax4a.set_ylabel('Aceleration X')

ax4b.set_title('Aceleration Y')
ax4b.grid()
ax4b.legend()
ax4b.set_xlabel('Time')
ax4b.set_ylabel('Aceleration')

ax4c.set_title('Aceleration Z')
ax4c.grid()
ax4c.legend()
ax4c.set_xlabel('Time')
ax4c.set_ylabel('Aceleration Z')

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
fig6a, ax6a = plt.subplots(figsize=(5, 5))
fig6b, ax6b = plt.subplots(figsize=(5, 5))
fig6c, ax6c = plt.subplots(figsize=(5, 5))

line6a, = ax6a.plot([], [], linewidth=2,label='pitch')
line6b, = ax6b.plot([], [], linewidth=2, label='roll')
line6c, = ax6c.plot([], [], linewidth=2, label='yaw')

ax6a.set_title('Pitch')
ax6a.grid()
ax6a.legend()
ax6a.set_xlabel('Time')
ax6a.set_ylabel('Pitch')

ax6b.set_title('Roll')
ax6b.grid()
ax6b.legend()
ax6b.set_xlabel('Time')
ax6b.set_ylabel('Roll')

ax6c.set_title('Yaw')
ax6c.grid()
ax6c.legend()
ax6c.set_xlabel('Time')
ax6c.set_ylabel('Yaw')

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
    drone_data = client_status.get_json_data()
    #drone_data = r_in.generate_random_drone_data()
    
    json_data = json.loads(drone_data)
 
    # Create a Pandas DataFrame from the drone data
    df = pd.DataFrame.from_dict(json_data, orient="index")
   # print(df)
    # Add the new data points to the history list
    history.append(df)

  #  flight_time = [float(df.loc['time'][0]) for df in history]

    # Update the line chart with the new battery data
    time_data = flight_time
    bat_data = [float(df.loc['bat'][0]) for df in history]
    line2.set_data(time_data, bat_data)
    ax2.relim()
    ax2.autoscale_view()

    # Update the line chart with the new pressure data
    baro_data = [float(df.loc['baro'][0]) for df in history]
    line3.set_data(time_data, baro_data)
    ax3.relim()
    ax3.autoscale_view()

    # Update the line chart with the new aceleration data
    agx_data = [float(df.loc['agx'][0]) for df in history]
    agy_data = [float(df.loc['agy'][0]) for df in history]
    agz_data = [float(df.loc['agz'][0]) for df in history]
    
    line4a.set_data(time_data, agx_data)
    line4b.set_data(time_data, agy_data)
    line4c.set_data(time_data, agz_data)
    
    ax4a.relim()
    ax4a.autoscale_view()
    ax4b.relim()
    ax4b.autoscale_view()
    ax4c.relim()
    ax4c.autoscale_view()

    # Update the line chart with the new velocity data
    vgx_data = [float(df.loc['vgx'][0]) for df in history]
    vgy_data = [float(df.loc['vgy'][0]) for df in history]
    vgc_data = [float(df.loc['vgz'][0]) for df in history]
    line5a.set_data(time_data, vgx_data)
    line5b.set_data(time_data, vgy_data)
    line5c.set_data(time_data, vgc_data)
    ax5.relim()
    ax5.autoscale_view()
    
    # Update the line chart with the new velocity data
    pitch_data = [float(df.loc['pitch']) for df in history]
    roll_data = [float(df.loc['roll']) for df in history]
    yaw_data = [float(df.loc['yaw']) for df in history]
    line6a.set_data(time_data, pitch_data)
    line6b.set_data(time_data, roll_data)
    line6c.set_data(time_data, yaw_data)
    ax6a.relim()
    ax6a.autoscale_view()
    ax6b.relim()
    ax6b.autoscale_view()
    ax6c.relim()
    ax6c.autoscale_view()

    # Update the line chart with the new altitude data
    alt_data = [float(df.loc['h'][0]) for df in history]
    line7.set_data(time_data, alt_data)
    ax7.relim()
    ax7.autoscale_view()

    # TODO: if you don't want to use the random data comment this line and uncomment flight_time var above
    flight_time.append(flight_time[-1] + 1e-3)

    #Update the JSON container with the new data
    json_container.json(drone_data)


    with chart_placeholder:
        # creating three columns
        col1, col2 = st.columns(2)
        with col1:
            st.pyplot(fig2)
            st.pyplot(fig6a)
            st.pyplot(fig6c)
            st.pyplot(fig4a)
            st.pyplot(fig3)
        with col2:
            st.pyplot(fig5)
            st.pyplot(fig6b)
            st.pyplot(fig4b)
            st.pyplot(fig4c)
            st.pyplot(fig7)
            
   # Sleep for a specified interval (e.g., 1 second) to simulate real-time updates
    time.sleep(1e-3)
    