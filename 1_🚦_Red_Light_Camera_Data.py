
#import local variables / functions
from variables import red_light_camera_charges_link, city_colors, red_light_camera_fine_amt,\
    red_light_court_costs, light_colors, red_light_victim_surcharge
from red_light_data import input_data, replace_asterix, cleanup_df, red_light_stats, max_year_overall,years_in_service
from mayors_timeline import mayors_plot

## Import main libraries
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


## Streamlit Page Setup
st.set_page_config(
    page_title="Toronto Red-Speed Camera Stats",
    page_icon='🚦',
    layout="centered"
)

## Load dataset
df_red = input_data(url=red_light_camera_charges_link)

df_red2, new_columns, stats_dict = cleanup_df(df=df_red)

dict_stats = red_light_stats(new_column_names=new_columns, stats_dict=stats_dict, df=df_red2 )

maxes_years_intersections, overall_max_tickers, overall_intersection, max_year = max_year_overall(df_red2)

years_series, years_service_length, camera_by_year = years_in_service(df=df_red, new_col_names=new_columns)

total_tickets_street = df_red2.sum(axis=1).sort_values(ascending=False)
total_tickets_issued = total_tickets_street.sum()

df_red['Years in service'] = years_series
df_red["Total years in service"] = years_service_length

df_years_service = df_red.loc[:, "Total years in service"]

df_tickets_years = total_tickets_street.to_frame().join(df_years_service)



#### ---- MAIN PAGE ---- ####
st.markdown(
    f"<H5 style='border-radius:25px; padding:20px; text-align:center; color:#f2f2f2; font-size:39px;background-image: linear-gradient(to right, {light_colors[0]}, #F7831Ecc, #239E70cc);'> RED LIGHT <mark style = 'font-family:liberation serif; font-size:37px; color:#F2F2F2; background-color:transparent;'>CAMERAS IN TORONTO </mark></H5>",
    unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

#### ---- TABS ---- ####
tab1, tab2, tab3 = st.tabs(["Historical Overview", "Yearly Overview", "Intersection Overview"])

with tab1:
    projected_charges = round(total_tickets_issued * (red_light_camera_fine_amt + red_light_court_costs)/1000000,1)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns((2, 1))
    with col1:
        st.markdown(f"<p style = 'font-size:40px;color:#EBE2CC;border-left: 3px solid {light_colors[0]}; padding:10px; '> TOTAL PROGRAM YEARS</p>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<p style = 'font-size:38px;color:{light_colors[0]};padding:10px;  '> {len(new_columns)}</p>", unsafe_allow_html=True)

    col3, col4 = st.columns((2, 1))
    with col3:
        st.markdown(f"<p style = 'font-size:40px;color:#EBE2CC;border-left: 3px solid {light_colors[1]}; padding:10px; '> TOTAL TICKETS ISSUED </p>", unsafe_allow_html=True)
    with col4:
        st.markdown(f"<p style = 'font-size:38px;color:{light_colors[1]};padding:10px; '> {round(total_tickets_issued):,}</p>", unsafe_allow_html=True)

    col5, col6 = st.columns((2, 1))
    with col5:
        st.markdown(f"<p style = 'font-size:40px;color:#EBE2CC;border-left: 3px solid {light_colors[2]}; padding:10px; '> PROJECTED CHARGES</p>", unsafe_allow_html=True)
    with col6:
        st.markdown(f"<p style = 'font-size:38px;color:{light_colors[2]};padding:10px; '> ${projected_charges}M</p>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<p style = 'font-size:32px;color:#ABA595;text-align:center;font-weight:bold; '> TICKET COST BREAKDOWN </p>", unsafe_allow_html=True)
    st.markdown(
        f"<p style = 'font-size:14px;color:#ABA595;text-align:center;border-left: 1px solid #ABA595;border-right: 1px solid #ABA595;margin-left:130px;margin-right:130px;"
        f" '>The City of TORONTO collects the FINE AMOUNT & COURT COSTS<br> The VICTIM SURCHARGE goes to the Province. </p>",
        unsafe_allow_html=True)



    col7, col8, col9, col10 = st.columns((1,1,1, 1))
    with col7:
        st.markdown(f"<p style = 'font-size:18px;color:{light_colors[2]};padding:1px;text-align:center; '> FINE AMOUNT </p>",
                    unsafe_allow_html=True)
        st.markdown(f"<p style = 'font-size:38px;color:{light_colors[2]};padding:10px;text-align:center; '> ${int(red_light_camera_fine_amt):}</p>", unsafe_allow_html=True)

    with col8:
        st.markdown(f"<p style = 'font-size:18px;color:{light_colors[2]};padding:1px;text-align:center; '> COURT COSTS </p>",
                    unsafe_allow_html=True)
        st.markdown(f"<p style = 'font-size:38px;color:{light_colors[2]};padding:10px;text-align:center; '> ${int(red_light_court_costs):}</p>", unsafe_allow_html=True)
    with col9:
        st.markdown(f"<p style = 'font-size:18px;color:{light_colors[0]};padding:1px;text-align:center; '> VICTIM SURCHARGE </p>",
                    unsafe_allow_html=True)
        st.markdown(f"<p style = 'font-size:38px;color:{light_colors[0]};padding:10px;text-align:center; '> ${int(red_light_victim_surcharge):}</p>", unsafe_allow_html=True)
    with col10:
        st.markdown(f"<p style = 'font-size:18px;color:{light_colors[0]};padding:1px;text-align:center; '> DEMERIT POINTS </p>",
                    unsafe_allow_html=True)
        st.markdown(f"<p style = 'font-size:38px;color:{light_colors[0]};padding:10px;text-align:center; '> {0:}</p>", unsafe_allow_html=True)


with tab2:

    #st.markdown(f"<hr style = 'border-bottom: 2px solid {light_colors[0]}; width: 20%;'> ", unsafe_allow_html=True)
    #st.markdown(f"<p style = 'font-size:40px;color:{light_colors[0]};padding-left:15px; '> ACTIVE CAMERAS BY YEAR </p>", unsafe_allow_html=True)
    st.markdown(f"<p style = 'font-size:40px;color:{light_colors[0]};border-left: 3px solid {light_colors[0]}; padding-left:25px;margin-left:80px; '> *ACTIVE CAMERAS BY YEAR </p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    ## PLOT 1
    years = list(camera_by_year.keys())
    camera_totals = list(camera_by_year.values())
    colors = ['#ABA595' if (s < max(camera_totals)) else light_colors[0]  for s in camera_totals]
    fig, ax = plt.subplots(figsize=(10,5))
    fig.patch.set_facecolor('#0E1117')
    sns.set_style('dark')
    width = 0.8
    ax = sns.barplot(x=years, y = camera_totals, palette=colors, width=width)
    plt.xlabel(None)
    plt.xticks(fontsize=14, rotation=45, color='#ABA595' )
    plt.ylabel("Camera Totals", fontsize=20, color='#ABA595')
    plt.yticks(fontsize=15, color='#ABA595')
    ax.text(x = 14.6, y = camera_totals[-1]+5, s = camera_totals[-1], color = light_colors[0], size = 16, weight = 'bold')
    sns.despine(bottom=True)
    ax.grid(False)
    ax.tick_params(bottom=False, left=True)
    ax.set_facecolor("#0E1117")
    st.pyplot(fig=fig)
    st.markdown("<p style='font-size:13px;color:#ABA595;margin-left:60px;'> *ACTIVE: When a red light camera has registered >0 tickets.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)


    st.markdown(f"<p style = 'font-size:40px;color:{light_colors[1]};border-left: 3px solid {light_colors[1]}; padding-left:25px;margin-left:80px; '> TICKETS ISSUED </p>", unsafe_allow_html=True)
    tickets_list = []
    total_fines_list = []
    years_list = []

    for e,col in enumerate(new_columns):
        tickets = dict_stats[col]['Total_Tickets']
        tickets_list.append(int(tickets))
        total_fines = dict_stats[col]["Total_Fines"]
        total_fines_list.append(int(total_fines))
        year = col[0:4]
        years_list.append(year)

    top_charges_year = round(max(total_fines_list) / 1000000, 1)

    ## PLOT 2
    st.markdown("<br>", unsafe_allow_html=True)

    colors = ['#ABA595' if (s < max(tickets_list)) else light_colors[1]  for s in tickets_list]
    fig2, ax2 = plt.subplots(figsize=(10,5))
    fig2.patch.set_facecolor('#0E1117')
    sns.set_style('dark')
    width = 0.8
    ax2 = sns.barplot(x=years_list, y = tickets_list, palette=colors, width=width)
    plt.xlabel(None)
    plt.xticks(fontsize=14, rotation=45, color='#ABA595' )
    plt.ylabel("Tickets Issued Per Year", fontsize=20, color='#ABA595')
    plt.yticks(fontsize=15, color='#ABA595')
    ax2.text(x = 13.4, y = max(tickets_list)+1500, s = f"{max(tickets_list):,}", color = light_colors[1], size = 15, weight = 'bold')
    sns.despine(bottom=True)
    ax2.grid(False)
    ax2.tick_params(bottom=False, left=True)
    ax2.set_facecolor("#0E1117")
    ylabels = ['{:,.1f}'.format(y) + 'K' for y in ax2.get_yticks()/1000]
    ax2.set_yticklabels(ylabels)
    st.pyplot(fig=fig2)
    st.markdown("<br>", unsafe_allow_html=True)


    ## PLOT 3
    st.markdown(f"<p style = 'font-size:40px;color:{light_colors[2]};border-left: 3px solid {light_colors[2]}; padding-left:25px;margin-left:80px; '> TOTAL FINES </p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    colors = ['#ABA595' if (s < max(total_fines_list)) else light_colors[2]  for s in total_fines_list]
    fig3, ax3 = plt.subplots(figsize=(10,5))
    fig3.patch.set_facecolor('#0E1117')
    sns.set_style('dark')
    width = 0.8
    ax3 = sns.barplot(x=years_list, y = total_fines_list, palette=colors, width=width)
    plt.xlabel(None)
    plt.xticks(fontsize=14, rotation=45, color='#ABA595' )
    plt.ylabel("Total Yearly Charges (approx.)", fontsize=20, color='#ABA595')
    plt.yticks(fontsize=15, color='#ABA595')
    ax3.text(x = 13.2, y = max(total_fines_list)+430000, s = f"${top_charges_year}M", color = light_colors[2], size = 14, weight = 'bold')
    sns.despine(bottom=True)
    ax3.grid(False)
    ax3.tick_params(bottom=False, left=True)
    ax3.set_facecolor("#0E1117")
    ylabels = ['{:,.1f}'.format(y) + 'M' for y in ax3.get_yticks()/1000000]
    ax3.set_yticklabels(ylabels)
    st.pyplot(fig=fig3)

    ## Timeline plot
    st.markdown(
        f"<p style = 'font-size:40px;color:{city_colors[0]};border-left: 3px solid {city_colors[0]}; padding-left:25px;margin-left:80px; '> TORONTO MAYORS </p>",
        unsafe_allow_html=True)

    mayor_fig = mayors_plot()
    st.pyplot(fig=mayor_fig)



with tab3:
    # SECTION 1
    #st.markdown(f"<hr style=' border-top: 3px dashed {light_colors[2]};margin-left:5px;margin-right:5px; '> ", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<p style = 'font-size:35px;color:#f2f2f2;border-left: 3px solid {light_colors[0]};text-align:center;margin-left:5px;margin-right:5px '>TOP TICKET PRODUCING INTERSECTION</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:14px;color:#f2f2f2;margin-left:60px;text-align:center;'>TOTAL CHARGES FOR THE YEAR </p>", unsafe_allow_html=True)

    st.markdown(f"<h5 style='border-radius:5px; margin-left:100px; margin-right:100px; padding:10px; text-align:center; color:#f2f2f2; font-size:31px;border-style:solid;"
                f"background-image: linear-gradient(to right, {city_colors[1]}cc, {city_colors[1]}cc,{city_colors[0]}cc);'>  {overall_intersection} </h5>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col11, col12, col13, col14 = st.columns((1,1,1,1))
    with col11:
        st.markdown(f"<p style = 'font-size:18px;color:{light_colors[0]};padding:1px;text-align:center; '> YEAR </p>",
                    unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"<p style = 'font-size:38px;color:{light_colors[0]};padding:10px;text-align:center; '> {max_year}</p>", unsafe_allow_html=True)

    with col12:
        st.markdown(f"<p style = 'font-size:18px;color:{light_colors[1]};padding:1px;text-align:center; '> TICKETS<br> ISSUED </p>",
                    unsafe_allow_html=True)
        st.markdown(f"<p style = 'font-size:38px;color:{light_colors[1]};padding:10px;text-align:center; '> {int(overall_max_tickers):,}</p>", unsafe_allow_html=True)
    with col13:
        st.markdown(f"<p style = 'font-size:18px;color:{light_colors[1]};padding:1px;text-align:center; '> TICKET AVG <br>(PER DAY) </p>",
                    unsafe_allow_html=True)
        st.markdown(f"<p style = 'font-size:38px;color:{light_colors[1]};padding:10px;text-align:center; '> {int(round(overall_max_tickers / 365, 0)):}</p>", unsafe_allow_html=True)
    with col14:
        st.markdown(f"<p style = 'font-size:18px;color:{light_colors[2]};padding:1px;text-align:center; '> TOTAL FINES<br>(APPROX.) </p>",
                    unsafe_allow_html=True)
        st.markdown(f"<p style = 'font-size:38px;color:{light_colors[2]};padding:10px;text-align:center; '> {round((overall_max_tickers * (red_light_camera_fine_amt + red_light_court_costs))/1000000,2)}M</p>", unsafe_allow_html=True)

    #st.markdown(f"<hr style=' border-top: 3px dashed {light_colors[0]}; '> ", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    #st.markdown("<br>", unsafe_allow_html=True)

    ## SECTION 2
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<p style = 'font-size:35px;color:#f2f2f2;border-left: 3px solid {light_colors[1]};text-align:center;margin-left:5px;margin-right:20px '>TOP INTERSECTION FOR EACH YEAR</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<p style=' font-size:20px;color:#f2f2f2;text-align:center;'> SELECT A YEAR BELOW </p>",unsafe_allow_html=True)
    selected_year = st.select_slider(
        "YEAR",
        options=list(maxes_years_intersections.keys()),
        value=list(maxes_years_intersections.keys())[-1]
    )
    st.markdown("<br>", unsafe_allow_html=True)
    col15, col16, col17 = st.columns((2, 0.5, 0.5))
    with col15:
        st.markdown(" ")
    with col16:
        st.markdown(f"<p style = 'font-size:18px;color:{light_colors[0]};padding:1px;text-align:center; '>YEAR </p>", unsafe_allow_html=True)
    with col17:
        st.markdown(
            f"<p style = 'font-size:18px;color:{light_colors[1]};padding:1px;text-align:center; '> TICKETS</p>",
            unsafe_allow_html=True)
    #for e,k in enumerate(maxes_years_intersections.keys()):
    #col_one, col_two, col_three = "col_1a", "col_1b", "col_1c"
    col_1a, col_1b, col_1c = st.columns((2, 0.5, 0.5))
    with col_1a:
        st.markdown(
            f"<h5 style='border-radius:5px; margin-left:0px; margin-right:20px; padding:16px; text-align:center; color:#f2f2f2; font-size:20px;border-style:solid;"
            f"font-style:bold;background-image: linear-gradient(to right, {city_colors[1]}cc, {city_colors[1]}cc,{city_colors[0]}cc);'>  {maxes_years_intersections[selected_year][0]} </h5>",
            unsafe_allow_html=True)
    with col_1b:
        st.markdown(f"<p style = 'font-size:25px;color:{light_colors[0]};padding:1px;text-align:center; '>{selected_year} </p>", unsafe_allow_html=True)
    with col_1c:
        st.markdown(
            f"<p style = 'font-size:25px;color:{light_colors[1]};padding:1px;text-align:center; '> {int(maxes_years_intersections[selected_year][1]):,} </p>",
            unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    #st.markdown(f"<hr style=' border-top: 2.5px dashed {light_colors[1]}; '> ", unsafe_allow_html=True)

    ## SECTION 3
    st.markdown("<br>", unsafe_allow_html=True)
    df_tickets_years =  df_tickets_years.sort_values(by=0, ascending=False)
    #st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        f"<p style = 'font-size:35px;color:#f2f2f2;border-left: 3px solid {light_colors[2]};text-align:center;"
        f"margin-left:5px;margin-right:5px;padding-left:50px; '>LOCATIONS WITH THE HIGHEST NUMBERS OF TICKETS</p>",
        unsafe_allow_html=True)
    st.markdown("<p style='font-size:14px;color:#f2f2f2;margin-left:60px;text-align:center;'>TOTAL CHARGES AT EACH LOCATION SINCE THE PROGRAM BEGAN </p>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col18, col19, col20 = st.columns((2, 0.5, 0.5))
    with col18:
        st.markdown(" ")
    with col19:
        st.markdown(f"<p style = 'font-size:18px;color:{light_colors[0]};padding:1px;text-align:center; '>ACTIVE YEARS</p>",
                    unsafe_allow_html=True)
    with col20:
        st.markdown(
            f"<p style = 'font-size:18px;color:{light_colors[1]};padding:1px;text-align:center; '> TICKETS</p>",
            unsafe_allow_html=True)


    for i in range(11):
        index_list = df_tickets_years.index

        col_one, col_two, col_three = f"col_{i}d", f"col_{i}e", f"col_{i}f"
        col_one, col_two, col_three = st.columns((2, .5, .5))
        with col_one:
            st.markdown(
                f"<h5 style='border-radius:5px; margin-left:0px; margin-right:17px;margin-bottom:3px; padding:16px; text-align:center; color:#f2f2f2; font-size:20px;border-style: solid; "
                f"font-style:bold;background-image: linear-gradient(to right, {city_colors[1]}, {city_colors[1]}cc,{city_colors[1]}cc);'>  {index_list[i]} </h5>",
                unsafe_allow_html=True)
        with col_two:
            st.markdown(
                f"<p style = 'font-size:25px;color:{light_colors[0]};padding:1px;text-align:center; '>{int(df_tickets_years.iloc[i, :]['Total years in service'])}</p>",
                unsafe_allow_html=True)
        with col_three:
            st.markdown(
                f"<p style = 'font-size:25px;color:{light_colors[1]};padding:1px;text-align:center; '>{int((df_tickets_years.iloc[i, :][0])):,} </p>",
                unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)






## SIDEBAR

with st.sidebar:
    st.image('images/torontolog_noBG.png', width=200)
    st.markdown(f"<p style='font-size:20px;color:#f2f2f2;text-align:center;'>PROGRAM START </p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:30px;color:{city_colors[0]};text-align:center;'>2007 </p>",
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
    st.markdown(
        f"<p style='font-size:14px;color:{city_colors[0]};text-align:center;font-weight:italics;'>Prepared by: Peter Stangolis </p>",
        unsafe_allow_html=True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Program running")


