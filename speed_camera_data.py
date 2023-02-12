
import pandas as pd


def replace_present(t):
    import datetime
    try:
        if t == 'Present':
            t = datetime.datetime.now()
        return t
    except:
        return t


def input_data(url, col):
    df = pd.read_excel(url,
                       skiprows=0,
                       na_filter=True,
                       na_values=['-'])
    #df.set_index('Location*', inplace=True)
    df_copy = df.iloc[:-2, 1:].copy(deep=True)

    df_copy[col] = df_copy[col].apply(replace_present)

    return df_copy


def speed_fines_year(df):

    df_speed_dates = df.iloc[:, 3:].copy(deep=True)

    years = dict()
    cols = df_speed_dates.columns.tolist()
    for col in cols:
        if str(col.year) not in years.keys():
            years[str(col.year)] = 1
        else:
            years[str(col.year)] += 1

    return df_speed_dates, years


def speed_fines_year_total(df, years_count):

    k = years_count.keys()
    v = list(years_count.values())
    df1 = df.iloc[:, :v[0]].copy(deep=True)
    df1.fillna(0, axis=1, inplace=True)
    df2 = df.iloc[:, (v[0]):(v[0]+v[1])]
    df2.fillna(0, axis=1, inplace=True)
    df3 = df.iloc[:, (v[0]+v[1]):(v[0]+v[1]+v[2])]
    df3.fillna(0, axis=1, inplace=True)

    return df1, df2, df3

def total_service_days(df):

    df_copy = df.copy(deep=True)
    series_a = df_copy["Enforcement End Date"] - df_copy["Enforcement Start Date"]

    series_a = series_a.to_frame()

    list_a = series_a[0].tolist()
    days = []
    for d in list_a:
        days.append(int(str(d).split(" ")[0]))

    series_a['days'] =days

    return series_a.iloc[:, 1:]







