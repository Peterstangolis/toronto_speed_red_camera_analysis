import datetime

# import local libraries - variables
from variables import ase_charges_link, city_colors, light_colors, active_speed_cameras, speed_cameras_site_lastUpdated
from speed_camera_data import input_data, speed_fines_year, speed_fines_year_total, total_service_days
from speed_cameras_map import speed_cameras_map


## Import main libraries
import streamlit as st
import numpy as np


## Streamlit Page Setup
st.set_page_config(
    page_title="Toronto Red-Speed Camera Stats",
    page_icon='🚦',
    layout="centered"
)


### --- LOAD DATASET --- ###
df_speed = input_data(url=ase_charges_link, col="Enforcement End Date")

df_speed_dates, speed_years = speed_fines_year(df_speed)

## Max tickets per month
max_tickets_perMonth = df_speed_dates.max()

df_2020, df_2021, df_2022 = speed_fines_year_total(df=df_speed_dates, years_count=speed_years)

df_service = total_service_days(df=df_speed)

speed_camera_start = df_speed_dates.columns[0].strftime("%B %#d, %Y")
speed_camera_present = datetime.datetime.today().strftime("%B %#d, %Y")


# Main page
st.markdown(
    f"<H5 style='border-radius:40px; padding:20px; text-align:center; color:#64721f; font-size:45px;background-image: linear-gradient(to right, {city_colors[1]}, {city_colors[0]}cc, {city_colors[2]}cc);'>"
    f" SPEED <mark style = 'font-family:liberation serif; font-size:37px; color:#F2F2F2; background-color:transparent;'>CAMERAS IN TORONTO </mark></H5>",
    unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)


df_speed_dates_total = df_speed_dates.sum(axis=1).to_frame()

df_speed_total_days_total = df_speed_dates_total.join(df_service)
df_speed_total_days_total["Tickets per day"]= df_speed_total_days_total[0] / df_speed_total_days_total["days"]
df_speed_total_days_total["Tickets per day"]= np.round(df_speed_total_days_total["Tickets per day"],decimals=2)

df_speed_total_days_perday = df_speed_total_days_total.join(df_speed.iloc[:, 0])
df_speed_total_days_perday = df_speed_total_days_perday.sort_values(by="Tickets per day", ascending=False)

#### ---- TABS ---- ####
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Historical Overview", "Yearly Overview", "Monthly Overview", "Location Overview", "Speed Cameras Mapped"])

with tab1:
    col1, col2 = st.columns((2, 1))
    with col1:
        st.markdown(f"<p style = 'font-size:35px;color:#EBE2CC;border-left: 3px solid {city_colors[0]}; padding:10px; '> TOTAL TICKETS ISSUED</p>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<p style = 'font-size:42px;color:{city_colors[0]};padding:10px;  '> {int(df_speed_dates_total.sum()[0]):,}</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col3, col4 = st.columns((2, 1))
    with col3:
        st.markdown(f"<p style = 'font-size:35px;color:#EBE2CC;border-left: 3px solid {city_colors[3]}; padding:10px; '> *REVENUE COLLECTED</p>", unsafe_allow_html=True)
    with col4:
        st.markdown(f"<p style = 'font-size:42px;color:{city_colors[3]};padding:10px; '> 34M</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)


    col5, col6 = st.columns((2, 1))
    with col5:
        st.markdown(f"<p style = 'font-size:35px;color:#EBE2CC;border-left: 3px solid { city_colors[3]}; padding:10px; '> AVG FINE AMOUNT </p>", unsafe_allow_html=True)
    with col6:
        st.markdown(f"<p style = 'font-size:42px;color:{city_colors[3]};padding:10px; '> ${round(34000000/int(df_speed_dates_total.sum()[0]),2)} </p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)


    st.markdown("<p style='font-size:13px;color:#EBE2CC;margin-left:20px;'> *SOURCE: City of Toronto</p>", unsafe_allow_html=True)



with tab2:

    col7, col8, col9, col10 = st.columns((1.5,1,1,1))
    with col7:
        st.write("")
    with col8:
        st.markdown(f"<p style='font-size:30px;color:#f2f2f2;text-align:center;font-weight:bold;"
                    f"background-color:{city_colors[1]};border-radius:10px;margin-left:10px;margin-right:20px; '> 2020 </p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    with col9:
        st.markdown(f"<p style='font-size:30px;color:#f2f2f2;text-align:center;font-weight:bold;"
                    f"background-color:{city_colors[2]};border-radius:10px;margin-left:10px;margin-right:20px; '> 2021 </p>", unsafe_allow_html=True)
    with col10:
        st.markdown(f"<p style='font-size:30px;color:#f2f2f2;text-align:center;font-weight:bold;"
                    f"background-color:{city_colors[3]};border-radius:10px;margin-left:10px;margin-right:20px; '> 2022 </p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col15, col16, col17, col18 = st.columns((1.5, 1, 1, 1))
    with col15:
        st.markdown(f"<p style='font-size:28px;color:{city_colors[3]};text-align:left;border-left: 3px solid {city_colors[3]};padding-left:15px; '> TICKETS ISSUED </p>", unsafe_allow_html=True)
    with col16:
        st.markdown(f"<p style='font-size:35px;color:#f2f2f2;text-align:center; '> {int(df_2020.sum(skipna=True).sum()):,} </p>", unsafe_allow_html=True)
    with col17:
        st.markdown(f"<p style='font-size:35px;color:#f2f2f2;text-align:center; '> {int(df_2021.sum(skipna=True).sum()):,} </p>", unsafe_allow_html=True)
    with col18:
        st.markdown(f"<p style='font-size:35px;color:#f2f2f2;text-align:center; '> {int(df_2022.sum(skipna=True).sum()):,} </p>", unsafe_allow_html=True)

    col11, col12, col13, col14 = st.columns((1.5, 1, 1, 1))
    with col11:
        st.markdown(f"<p style='font-size:28px;color:{city_colors[0]};text-align:left;border-left: 3px solid {city_colors[0]};padding-left:15px; '> DAYS ACTIVE </p>", unsafe_allow_html=True)
    with col12:
        st.markdown(f"<p style='font-size:35px;color:#f2f2f2;text-align:center; '> {str((df_2020.columns[-1]+  datetime.timedelta(days=30)) - df_2020.columns[0]).split(' ')[0]} </p>", unsafe_allow_html=True)
    with col13:
        st.markdown(f"<p style='font-size:35px;color:#f2f2f2;text-align:center; '> {str((df_2021.columns[-1]+datetime.timedelta(days=30)) - df_2021.columns[0]).split(' ')[0]} </p>", unsafe_allow_html=True)
    with col14:
        st.markdown(f"<p style='font-size:35px;color:#f2f2f2;text-align:center; '> {str(df_2022.columns[-1] - df_2022.columns[0]).split(' ')[0]}  </p>", unsafe_allow_html=True)


    col19, col20, col21, col22 = st.columns((1.5, 1, 1, 1))
    with col19:
        st.markdown(f"<p style='font-size:28px;color:{city_colors[-1]};text-align:left;border-left: 3px solid {city_colors[-1]};padding-left:15px; '> AVG. TICKETS<br>PER DAY </p>",
                    unsafe_allow_html=True)
    with col20:
        st.markdown(
            f"<p style='font-size:35px;color:#f2f2f2;text-align:center; '>"
            f" {int(df_2020.sum(skipna=True).sum() / int((str((df_2020.columns[-1]+  datetime.timedelta(days=30)) - df_2020.columns[0]).split(' ')[0])))} </p>",
            unsafe_allow_html=True)
    with col21:
        st.markdown(
            f"<p style='font-size:35px;color:#f2f2f2;text-align:center; '>"
            f" {int(df_2021.sum(skipna=True).sum() / int((str((df_2021.columns[-1]+  datetime.timedelta(days=30)) - df_2021.columns[0]).split(' ')[0])))} </p>",
            unsafe_allow_html=True)
    with col22:
        st.markdown(
            f"<p style='font-size:35px;color:#f2f2f2;text-align:center; '>"
            f" {int(df_2022.sum(skipna=True).sum() / int((str((df_2022.columns[-1]) - df_2022.columns[0]).split(' ')[0])))} </p>",
            unsafe_allow_html=True)

with tab3:
    st.markdown(f"<h4 style='font-size:45px;color:{city_colors[0]};text-align:center; '> MONTHLY TICKET OVERVIEW </h4>", unsafe_allow_html=True)
    st.markdown(
        f"<p style='font-size:24px;color:{city_colors[3]};text-align:center;border-left: 1px solid {city_colors[0]};border-right: 1px solid {city_colors[0]};margin-left:150px;margin-right:150px;"
        f" '>HIGHEST TOTAL TICKETS FOR THE MONTH </p>",
        unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    colee, colff, colgg = st.columns((2,1,1))
    with colee:
        st.markdown(f"<h4 style='font-size:24px;color:{city_colors[3]};text-align:center; '></h4>",
                    unsafe_allow_html=True)
    with colgg:
        st.markdown(f"<h4 style='font-size:24px;color:{city_colors[3]};text-align:center; '> DATES </h4>",
                    unsafe_allow_html=True)
    with colff:
        st.markdown(f"<h4 style='font-size:24px;color:{city_colors[3]};text-align:center; '> TICKETS </h4>",
                    unsafe_allow_html=True)
    max_monthly_tickets = int(max_tickets_perMonth.max())
    print(max_monthly_tickets)
    for idx in range(len(max_tickets_perMonth)):
        col_zzz, col_yyy, col_xxx = f'col_zzz{idx}', f'col_yyy{idx}', f'col_xxx{idx}'
        col_zzz, col_yyy, col_xxx = st.columns((2,1,1))

        i, v = max_tickets_perMonth.index[idx], max_tickets_perMonth.iloc[idx]
        if v == max_monthly_tickets:
            max_color = '#F2CC39'
        else:
            max_color = '#EBE2CC'
        i_str = i.strftime("%b %Y").upper()

        with col_zzz:
            st.markdown(
                f"<h5 style='border-radius:5px; margin-left:0px; margin-right:15px;margin-bottom:2px; padding:14px; text-align:center; color:{max_color}; font-size:18px;border-style: solid; "
                f"font-style:bold;background-image: linear-gradient(to right, {city_colors[1]}, {city_colors[1]}cc,{city_colors[1]}cc);'>  {df_speed.loc[df_speed[i] == v]['Location*'].values[0]} </h5>",
                unsafe_allow_html=True)
        with col_yyy:
            st.markdown(
                f"<p style='font-size:28px;color:{max_color};text-align:center; '> {int(v)}",
                unsafe_allow_html=True)
        with col_xxx:
            st.markdown(
                f"<p style='font-size:28px;color:{max_color};text-align:center; '> {i_str}",
                unsafe_allow_html=True)

with tab4:
    st.markdown(f"<h4 style='font-size:45px;color:{city_colors[3]};text-align:center; '>TOP 10 LOCATIONS</h4>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:24px;color:{city_colors[3]};text-align:center;border-left: 1px solid {city_colors[0]};border-right: 1px solid {city_colors[0]};margin-left:150px;margin-right:150px;padding:10px;"
                f" '>HIGHEST DAILY TICKET CHARGES SINCE THE PROGRAM BEGAN </p>",
                unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    colaa, colbb, colcc, coldd = st.columns((2,1,1,1))
    with colaa:
        st.markdown(f"<p style = 'font-size:23px;color:{city_colors[3]};text-align:center;font-weight:normal;'>", unsafe_allow_html=True)
    with colbb:
        st.markdown(f"<p style = 'font-size:23px;color:{city_colors[3]};text-align:center;font-weight:normal;'>TOTAL TICKETS", unsafe_allow_html=True)
    with colcc:
        st.markdown(f"<p style = 'font-size:23px;color:{city_colors[3]};text-align:center;font-weight:normal;'>DAYS<br> ACTIVE", unsafe_allow_html=True)
    with coldd:
        st.markdown(f"<p style = 'font-size:23px;color:{city_colors[3]};text-align:center;font-weight:normal;'>TICKETS <br>PER DAY",
                    unsafe_allow_html=True)

    for i in range(11):
        row = df_speed_total_days_perday.iloc[i]
        colw, colx, coly, colz = f"col_{i}w", f"col_{i}x", f"col_{i}y", f"col_{i}z"
        colw, colx, coly, colz = st.columns((2,1,1,1))
        with colw:
            #st.markdown(row["Location*"])
            st.markdown(
                f"<h5 style='border-radius:5px; margin-left:0px; margin-right:15px;margin-bottom:2px; padding:14px; text-align:center; color:#EBE2CC; font-size:18px;border-style: solid; "
                f"font-style:bold;background-image: linear-gradient(to right, {city_colors[1]}, {city_colors[1]}cc,{city_colors[1]}cc);'>  {row['Location*']} </h5>",
                unsafe_allow_html=True)
        with colx:
            st.markdown(f"<p style='font-size:28px;color:#EBE2CC;text-align:center; '> {round(row[0]/1000,1)}K", unsafe_allow_html=True)
        with coly:
            st.markdown(
                f"<p style='font-size:28px;color:#EBE2CC;text-align:center; '> {row['days']}",
                unsafe_allow_html=True)
        with colz:
            #st.markdown(f"{int(round(row['Tickets per day'],0))}")
            st.markdown(
                f"<p style='font-size:28px;color:#EBE2CC;text-align:center; '> {int(round(row['Tickets per day'],0))}",
                unsafe_allow_html=True)

with tab5:
    if 'current_cam_state' not in st.session_state:
        st.session_state["current_cam_state"] = "Active"

    if st.session_state.current_cam_state == 'Active':
        highlight_color = '#64721f'
    else:
        highlight_color = 'gray'

    st.markdown(f"<h4 style='font-size:40px;color:$f2f2f2; '> <mark style='text-align:center;text-style:bold;color:{highlight_color};background-color:transparent;border-radius:40%;padding:10px;'> {st.session_state.current_cam_state.upper() } </mark>SPEED CAMERA LOCATIONS </h4>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:20px;color:{highlight_color};text-transform:uppercase; '> _ Speed Cameras Are Currently {st.session_state.current_cam_state} </p>", unsafe_allow_html=True)

    state_of_cameras = st.radio(label='Select the cameras you wish to see on the map', options=["Active", "Planned"],
                                index=0,
                                key='current_cam_state',
                                horizontal=True
                                 )

    speed_cameras_map(camera_state=st.session_state.current_cam_state)
    st.caption("SOURCE: https://open.toronto.ca/dataset/automated-speed-enforcement-locations/")
    st.caption(f"DATA LAST UPDATED: {speed_cameras_site_lastUpdated:%B %Y}")


#### ---- SIDEBAR ---- ####

with st.sidebar:
    st.image('images/torontolog_noBG.png', width = 200)

    st.markdown(f"<p style='font-size:20px;color:#f2f2f2;text-align:center;'>PROGRAM START </p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:30px;color:{city_colors[0]};text-align:center;'>{speed_camera_start} </p>",
                unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:14px;color:{city_colors[0]};text-align:center;font-weight:italics;'>Prepared by: Peter Stangolis </p>", unsafe_allow_html=True)



