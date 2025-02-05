import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from numpy.exceptions import AxisError
import pandas as pd
from scipy import stats

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, Integer, String, insert, select

engine = create_engine("sqlite+pysqlite:///GPSdata1.db", echo=False)

metadata_obj = MetaData()

players_table = Table("players", metadata_obj, autoload_with=engine)
sessions_data_table = Table("sessions_data", metadata_obj, autoload_with=engine)

# Sort a list of x and corresponding y corrdinates by the x coordinate, ascending
def bubblesort_by_x(x_coords, y_coords) -> tuple[np.ndarray, np.ndarray]:
    for n in range(len(x_coords) - 1, 0, - 1 ):

        swapped = False

        for i in range(n):
            if x_coords[i] > x_coords[i + 1]:
                
                x_coords[i], x_coords[i + 1] = x_coords[i + 1], x_coords[i]
                y_coords[i], y_coords[i + 1] = y_coords[i + 1], y_coords[i]

                swapped = True

        if not swapped:
            break

    return (x_coords, y_coords)


def interpolate_2D_array(arr, x_val: float|int) -> float:
    if not isinstance(arr, np.ndarray):
        raise TypeError("Input must be an ndarray")
    try:
        if not arr.shape[1] == 2:
            raise AxisError("Array shape must be (n,2)")
    except IndexError:
        raise AxisError("Array shape must be (n,2)")
    
    intercept = 0

    for i in range(0, len(arr) - 1):
        x, y = arr[i]
        next_x, next_y = arr[i+1]

        if x < x_val and next_y >= x_val:
            intercept = (x + next_x) / 2
            return intercept


def generate_RPs_team_row(df: pd.DataFrame, measure: str, pallette: str, show_stdv: bool, bw_adjust: int|float, height: int|float):
    g = sns.FacetGrid(df, row="team", hue="team", row_order=["1st", "U23", "U18", "U17"], height=height, aspect=5, palette=sns.color_palette(pallette))
    g.map(sns.kdeplot, measure, bw_adjust=bw_adjust, fill=True, alpha=.2, lw=2)


    for i, ax in enumerate(g.axes.flat):
        ax.text(-0.05, 0.8, g.row_names[i],
                fontsize=12, transform = ax.transAxes)
        ax.set_xlim(min(df[measure]), max(df[measure]))

    # add mean lines   
    if(show_stdv):     
        for i, ax in enumerate(g.axes.flat):
            for j, collection in enumerate(ax.collections):

                # Mean required to calulate x position of mean line
                df_p = df[(df["team"] == g.row_names[i])]
                mean = df_p[measure].mean()
                stdv = np.std(df_p[measure])
                
                # vertices need to have y=0 coords filtered out for interp to work
                vertices = collection.get_paths()[0].vertices
                vertices = vertices[vertices.T[1] > 0]

                # As row order has been changed, face color needs to be indexced from collection and not theme
                face_color = collection.get_facecolor()[j]
                face_color[3] *= 1.5
                R,G,B,A = face_color
                # bubble sort to reduce risk of stack overflow?
                x_coords, y_coords = bubblesort_by_x(vertices.T[0], vertices.T[1])
                mean_height = np.interp(mean, x_coords, y_coords)
                stdm_height = np.interp(mean - stdv, x_coords, y_coords)
                stdp_height = np.interp(mean + stdv, x_coords, y_coords)

                ax.fill_between(x_coords, 0, y_coords, where=(mean - stdv <= x_coords) & (x_coords <= mean + stdv), interpolate=False, facecolor=face_color)
                
                ax.vlines(mean,0,mean_height, ls=":", colors=[R,G,B, 1])

                # ax.vlines(mean - stdv,0,stdm_height, ls=":", colors=sns.color_palette("bright")[j])
                # ax.vlines(mean + stdv,0,stdp_height, ls=":", colors=sns.color_palette("bright")[j])
            
            
        
    # Set the subplots to overlap
    g.figure.subplots_adjust(hspace=-.5)
    plt.xlabel(measure, fontsize=12)
    g.set_titles("")
    # Remove axes details that don't play well with overlap
    
    g.set(yticks=[], ylabel="")
    g.despine(bottom=False, left=True)
    # g.add_legend(title="Position", loc="upper right", fontsize=12)
    g.refline(y=0, linewidth=0.5, linestyle="-", color=None, clip_on=False)


def generate_RPs_position_row(df: pd.DataFrame, measure: str, pallette: str, show_stdv: bool, bw_adjust: int|float, height: int|float):
    g = sns.FacetGrid(df, row="position", hue="position", height=height, aspect=5, palette=sns.color_palette(pallette))
    g.map(sns.kdeplot, measure, bw_adjust=bw_adjust, fill=True, alpha=.2, lw=2)


    for i, ax in enumerate(g.axes.flat):
        ax.text(-0.05, 0.8, g.row_names[i],
                fontsize=12, transform = ax.transAxes)
        ax.set_xlim(min(df[measure]), max(df[measure]))

    # add mean lines
    if(show_stdv):        
        for i, ax in enumerate(g.axes.flat):
            for j, collection in enumerate(ax.collections):

                # Mean required to calulate x position of mean line
                df_p = df[ (df["position"] == g.row_names[i])]
                mean = df_p[measure].mean()
                stdv = np.std(df_p[measure])
                
                # vertices need to have y=0 coords filtered out for interp to work
                vertices = collection.get_paths()[0].vertices
                vertices = vertices[vertices.T[1] > 0]

                # As row order has been changed, face color needs to be indexced from collection and not theme
                face_color = collection.get_facecolor()[j]
                face_color[3] *= 1.5
                R,G,B,A = face_color
                # bubble sort to reduce risk of stack overflow?
                x_coords, y_coords = bubblesort_by_x(vertices.T[0], vertices.T[1])
                mean_height = np.interp(mean, x_coords, y_coords)
                stdm_height = np.interp(mean - stdv, x_coords, y_coords)
                stdp_height = np.interp(mean + stdv, x_coords, y_coords)

                ax.fill_between(x_coords, 0, y_coords, where=(mean - stdv <= x_coords) & (x_coords <= mean + stdv), interpolate=False, facecolor=face_color)
                
                ax.vlines(mean,0,mean_height, ls=":", colors=[R,G,B, 1])

                # ax.vlines(mean - stdv,0,stdm_height, ls=":", colors=sns.color_palette("bright")[j])
                # ax.vlines(mean + stdv,0,stdp_height, ls=":", colors=sns.color_palette("bright")[j])
            
            
        
    # Set the subplots to overlap
    g.figure.subplots_adjust(hspace=-.5)
    # Remove axes details that don't play well with overlap
    plt.xlabel(measure, fontsize=12)
    g.set_titles("")
    g.set(yticks=[], ylabel="")
    g.despine(bottom=False, left=True)
    # g.add_legend(title="Position", loc="upper right", fontsize=12)
    g.refline(y=0, linewidth=0.5, linestyle="-", color=None, clip_on=False)

    
def generate_RPs_team_position_row(df: pd.DataFrame, measure: str, pallette: str, bw_adjust: int|float, height: int|float, ):
    g = sns.FacetGrid(df, row="team", hue="position", row_order=["1st", "U23", "U18", "U17"], height=height, aspect=5, palette=sns.color_palette(pallette))
    g.map(sns.kdeplot, measure, bw_adjust=bw_adjust, fill=True, alpha=.05, lw=2)


    for i, ax in enumerate(g.axes.flat):
        ax.text(-0.05, 0.8, g.row_names[i],
                fontsize=12, transform = ax.transAxes)
        ax.set_xlim(min(df[measure]), max(df[measure]))
        
    
    # add mean lines        
    for i, ax in enumerate(g.axes.flat):
        for j, collection in enumerate(ax.collections):

            # Mean required to calulate x position of mean line
            df_p = df[(df["position"] == g.hue_names[j]) & (df["team"] == g.row_names[i])]
            mean = df_p[measure].mean()
            stdv = np.std(df_p[measure])

            # vertices need to have y=0 coords filtered out for interp to work
            vertices = collection.get_paths()[0].vertices
            vertices = vertices[vertices.T[1] > 0]

            # bubble sort to reduce risk of stack overflow?
            x_coords, y_coords = bubblesort_by_x(vertices.T[0], vertices.T[1])
            mean_height = np.interp(mean, x_coords, y_coords)
            stdm_height = np.interp(mean - stdv, x_coords, y_coords)
            stdp_height = np.interp(mean + stdv, x_coords, y_coords)

            ax.vlines(mean,0,mean_height, ls=":", colors=sns.color_palette(pallette)[j])
            # ax.fill_between(x_coords, 0, y_coords, where=(mean - stdv <= x_coords) & (x_coords <= mean + stdv), interpolate=False, facecolor=sns.color_palette("bright")[j], alpha=0.2)

            # ax.vlines(mean - stdv,0,stdm_height, ls=":", colors=sns.color_palette("bright")[j])
            # ax.vlines(mean + stdv,0,stdp_height, ls=":", colors=sns.color_palette("bright")[j])
            
            
        
    # Set the subplots to overlap
    g.figure.subplots_adjust(hspace=-.5)

    # Remove axes details that don't play well with overlap
    g.set_titles("")
    plt.xlabel(measure, fontsize=12)
    g.set(yticks=[], ylabel="")
    g.despine(bottom=False, left=True)
    g.add_legend(title="", loc="upper right", fontsize=12)
    g.refline(y=0, linewidth=0.5, linestyle="-", color=None, clip_on=False)