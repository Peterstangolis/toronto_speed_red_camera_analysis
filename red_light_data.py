

import pandas as pd



def input_data(url):
    df = pd.read_excel(url,
                       skiprows=4,
                       )
    df.set_index('Charges Laid by Location & Year', inplace=True)
    df = df.iloc[:-4, :]
    return df

def replace_asterix(n):
    try:
        n = n.replace("*", "").replace("***", "").replace('**', '')
        return n
    except:
        return n


def cleanup_df(df):
    new_col_names = []
    year_data = {}
    cols = df.columns
    for col in cols:

        ## Create the new column name
        col_name = f'{col}_clean'
        ## Add the new column name to the list
        new_col_names.append(col_name)
        ## Add the column year to the dictionary
        year_data[str(col)] = []

        df[col] = df[col].apply(replace_asterix)
        df[col_name] = pd.to_numeric(df[col])

    return df.loc[:, new_col_names[0]:new_col_names[-1] ], new_col_names, year_data

def red_light_stats(new_column_names, stats_dict, df):
    from variables import red_light_camera_fine_amt, red_light_court_costs

    df_columns = df.columns
    for e, col in enumerate(new_column_names):
        added_stats = dict()
        total_fines = df[col].sum() * (red_light_camera_fine_amt + red_light_court_costs)
        total_tickets = df[col].sum()
        df_filtered = df[df[col] > 0][col]
        active_red_light_cameras = len(df)
        added_stats["Total_Tickets"] = total_tickets
        added_stats["Total_Fines"] = total_fines
        added_stats["Active Cameras"] = active_red_light_cameras

        stats_dict[str(df_columns[e])] = added_stats

    return stats_dict


def max_year_overall(df):

    overall_max = 0
    intersection_max = None
    year_max = None
    max_year_intersection = dict()
    cols = df.columns
    for col in cols:
        value = df[col].max(skipna=True)
        intersection = (df[col].idxmax())
        if value > overall_max:
            overall_max = value
            intersection_max = intersection
            year_max = col[0:4]
        v_i = [intersection, value]
        max_year_intersection[col[0:4]] = v_i

    return max_year_intersection, overall_max, intersection_max, year_max



def years_in_service(df, new_col_names):
    import numpy as np

    df2 = df.loc[:, new_col_names]

    total_cameras_year = dict()
    years_series = []
    years_service_length = []
    for i in range(len(df2)):
        years = []
        for e,c in enumerate((df2.columns)):
            v = df.iloc[i, e]
            try:
                if (int(v) > 0) and (v is not np.nan):
                    years.append(c[0:4])
                    if c[0:4] not in total_cameras_year.keys():
                        total_cameras_year[c[0:4]] = 1
                    else:
                        total_cameras_year[c[0:4]] += 1
            except:
                pass
        years_length = len(years)
        years_service_length.append(years_length)
        years_series.append(years)

    return years_series, years_service_length, total_cameras_year














