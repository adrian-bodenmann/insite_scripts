import sys
import typing
from pathlib import Path
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, "D:/software/git_bash/biocam_scripts/ship_or_shore_side")
from plot_image_score import plot_data, plot_real_time_and_post_processed_scores_series

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


if __name__ == "__main__" :
    plot_all_real_and_post_proc_datasets_with_range_of_timeshifts("D:/temp/image_score_plots")