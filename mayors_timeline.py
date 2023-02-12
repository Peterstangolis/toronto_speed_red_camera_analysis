

def mayors_plot():
    from variables import city_colors

    import matplotlib.pyplot as plt
    from matplotlib.offsetbox import AnnotationBbox, OffsetImage
    import matplotlib.image as image

    from datetime import datetime
    import pandas as pd

    today = datetime.today().strftime("%Y-%m-%d")
    dates = [
        '2003-12-01',
        '2010-12-01',
        '2014-12-01',
        today
    ]
    mayors = [
        'David Miller',
        'Rob Ford',
        'John Tory',
        'John Tory'
    ]
    levels = [
        2, 2, 2, 2
    ]
    mayors_df = pd.DataFrame(data={'Date': dates, 'Mayors': mayors, 'Levels': levels})
    mayors_df["Date"] = pd.to_datetime(mayors_df['Date'])

    ## Images DF
    images = [
        'images/miller.png',
        'images/ford.png',
        'images/tory.png'
    ]

    image_loc = [
        '2007-05-05',
        '2012-12-01',
        '2019-06-01',
    ]

    image_zoom = [0.35, 0.15, 0.15]

    images_df = pd.DataFrame(data={"image_name":images, "image_location":image_loc, 'image_zoom': image_zoom})
    images_df["image_location"] = pd.to_datetime(images_df["image_location"])


    fig, ax = plt.subplots(figsize=(10, 3))
    fig.patch.set_facecolor('#0E1117')
    plt.yticks(fontsize=15, color='#ABA595')
    plt.xticks(fontsize=14, rotation=45, color='#ABA595')

    ax.plot(mayors_df.Date, [.1, ] * len(mayors_df), "-o", color=city_colors[0], markerfacecolor='white', linewidth=1.2, markersize=10)

    ax.set_xticks(pd.date_range("2003-12-01", today, freq="ys"), range(2003, 2023));

    ax.set_ylim(0, 3);

    mayor_count = {}
    for idx in range(len(mayors_df)):
        dt, mayor, level = mayors_df["Date"][idx], mayors_df["Mayors"][idx], mayors_df["Levels"][idx]
        mayor_count[mayor] = mayor_count.get(mayor, 0) + 1
        dt_str = dt.strftime("%b-%Y")
        if mayor_count[mayor] < 2:
            ax.annotate(mayor + "\n" + dt_str, xy=(dt, 0.1), xytext=(dt, level),
                        arrowprops=dict(arrowstyle='-', color="grey", linewidth=0.6),
                        ha='center',
                        color='white',
                        fontsize=15
                        );

    for idx in range(len(images_df)):
        image_on_chart, file, zoom = images_df["image_location"][idx], images_df["image_name"][idx], images_df["image_zoom"][idx]
        logo = image.imread(file)
        imagebox = OffsetImage(logo, zoom=zoom)

        ab = AnnotationBbox(imagebox, (image_on_chart, 0.9), frameon=False)
        ax.add_artist(ab)

    ax.spines[["left", "top", "right","bottom"]].set_visible(False);
    ax.yaxis.set_visible(False)
    ax.set_facecolor("#0E1117")

    return fig