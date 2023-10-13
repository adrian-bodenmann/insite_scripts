import sys
import typing
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, "D:/software/git_bash/biocam_scripts/ship_or_shore_side")
from plot_image_score import (
    plot_with_plotly,
    plot_real_time_and_post_processed_scores_series,
    load_scores_and_altitudes,
    plot_data
)

def plot_scores_from_both_cameras(
    program_log_path: typing.Union[str, Path],
    post_computed_scores_directory: typing.Union[str, Path],
    nav_log_directory: typing.Union[str, Path],
    figures_output_dir: typing.Union[str, Path],
    limit_y_axis_laser: float = 2000,
):
    timestamp_str = Path(post_computed_scores_directory).parts[-1][0:15]

    plot_real_time_and_post_processed_scores_series(
        program_log_path = program_log_path,
        post_computed_scores_path = Path(post_computed_scores_directory) / "cam61008269_strobe_image_scores_post_computed.csv",
        nav_log_path = Path(nav_log_directory) / "auv_dr_cam61008269.csv",
        timestamp_str = timestamp_str,
        score_type = "colour",
        figures_output_dir = figures_output_dir
    )
    
    plot_real_time_and_post_processed_scores_series(
        program_log_path = program_log_path,
        post_computed_scores_path = Path(post_computed_scores_directory) / "laser_image_scores_post_computed.csv",
        nav_log_path = Path(nav_log_directory) / "auv_dr_cam61008031.csv",
        timestamp_str = timestamp_str,
        score_type = "laser",
        figures_output_dir = figures_output_dir,
        limit_y_axis_laser = limit_y_axis_laser
    )

def plot_all_real_and_post_proc_datasets_with_range_of_timeshifts(
    figures_output_dir: typing.Union[str, Path]
):
    plot_scores_from_both_cameras(
        "B:/Data/raw/2022/insite/alr/log/20220923/20220923_125148_program.log",
        "D:/processed/2022/insite/alr/20220923_130737_alr_bc4k15c_mapping/",
        "J:/processed/2022/insite/alr/20220923_130737_alr_bc4k15c_mapping/json_renav_20220712_090846_20220712_145800/csv/dead_reckoning/",
        figures_output_dir
    )


## Determine time shift between program log and nav log

def plot_colour_score_real_time_and_post_proc(time_shift_s: float = 0):
    plt.figure("Timeshift: " + str(time_shift_s) + "s")
    nav_log_path = "D:/processed/2022/dy152/alr/20220720_094049_alr_bc4k15c_mapping/json_renav_20220720_094049_20220720_195846/csv/dead_reckoning/auv_dr_cam61008031.csv"
    output_path = f"D:/temp/image_score/20220720_094049/20220720_094049_comparison_timeshift_{time_shift_s:+03.0f}s.png"
    output_path = output_path.replace("+", "plus_")
    output_path = output_path.replace("-", "minus_")
    plot_data(
        "D:/processed/2022/dy152/alr/20220720_094049_alr_bc4k15c_mapping/cam61008269_strobe_image_scores_post_computed.csv",
        nav_log_path,
        marker_s0=".",
        label="20220720_094049 post computed, auv_nav alt",
        indicate_camera_in_label=False,
        alpha=.2,
        compensate_for_16bit=True,
        show_plot=False
    )
    program_log_path = Path("D:/raw/2022/dy152/alr/log/20220720/20220720_093555_program.log")
    plot_data(
        program_log_path,
        nav_log_path,
        marker_s0="gx",
        marker_s1="m.",
        plot_s0=False,
        label="from log",   # "20220720_094049 real time, auv_nav alt",
        indicate_camera_in_label=False,
        alpha=.3,
        show_plot=False,
        time_shift_s=time_shift_s,
        path=output_path
    )


## Plotting with plotly (for tooltips)

def load_insite_logged_scores():
    time_shift_s = 0  # ToDo: find out what this should be
    nwh_l = load_scores_and_altitudes("D:/raw/2022/insite/alr/log/20220923/20220923_125148_program.log", "W:/media/hdd22/adrian/processed/2022/insite/alr/20220923_130737_alr_bc4k15c_mapping/json_renav_20220923_043050_20220925_013054/csv/ekf/auv_ekf_cam61008269.csv", time_shift_s=time_shift_s)
    nwh_l.drop(columns=['score_1'], inplace=True)
    nwh_l.rename(columns={"score_0": "score"}, inplace=True)

    miller_l = load_scores_and_altitudes("D:/raw/2022/insite/alr/log/20221004/20221004_150503_program.log", "W:/media/hdd22/adrian/processed/2022/insite/alr/20221004_153010_alr_bc4k15c_mapping/json_renav_20221004_140025_20221005_170027/csv/ekf/auv_ekf_cam61008269.csv", time_shift_s=time_shift_s)
    miller_l.drop(columns=['score_1'], inplace=True)
    miller_l.rename(columns={"score_0": "score"}, inplace=True)

    bp_l = load_scores_and_altitudes("D:/raw/2022/insite/alr/log/20221006/20221006_092722_program.log", "W:/media/hdd22/adrian/processed/2022/insite/alr/20221006_095110_alr_bc4k15c_mapping/json_renav_20221006_090029_20221006_170029/csv/ekf/auv_ekf_cam61008269.csv", time_shift_s=time_shift_s)
    bp_l.drop(columns=['score_1'], inplace=True)
    bp_l.rename(columns={"score_0": "score"}, inplace=True)

    return nwh_l, miller_l, bp_l


def plot_insite_laser_scores_with_plotly_with_tooltips( ):
    nwh_l, miller_l, bp_l = load_insite_logged_scores()
    output_dir = Path("D:/cruises/2022/dy152_insite/plots/by_code")
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Plot scores with plotlib (for tooltips) to {output_dir}...")
    alpha = 1
    f = plot_with_plotly(nwh_l, "Nort West Hutton laser", color="green", alpha=alpha)
    f.write_html(output_dir / "North_West_Hutton_laser_score.html")

    f = plot_with_plotly(miller_l, "Miller laser", color="olive", alpha=alpha)
    f.write_html(output_dir / "Miller_laser_score.html")

    f = plot_with_plotly(bp_l, "Braemar Pockmarks", color="red", alpha=alpha)
    f.write_html(output_dir / "Braemar_Pockmarks_score.html")

    f = plot_with_plotly(nwh_l, label="Nort West Hutton laser", color="green", alpha=alpha)
    f = plot_with_plotly(miller_l, label="Miller laser", color="olive", alpha=alpha, plotly_fig=f)
    f = plot_with_plotly(bp_l, label="Braemar Pockmarks", color="red", alpha=alpha, plotly_fig=f)
    f.write_html(output_dir / "insite_laser_score.html")

    print("... done plotting scores with plotlib (for tooltips).")


if __name__ == "__main__" :
    # plot_all_real_and_post_proc_datasets_with_range_of_timeshifts("D:/temp/image_score_plots")
    plot_insite_laser_scores_with_plotly_with_tooltips()
