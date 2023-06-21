import argparse
import pandas as pd
import matplotlib.pyplot as plt


def main(biocam_log_path, alr_log_path, shift_auv_time_by, biocam_roll_offset_deg, biocam_pitch_offset_deg):
    biocam_log = pd.read_csv(biocam_log_path)
    biocam_log["timestamp"] = pd.to_datetime(biocam_log["time_utc"], format="%Y%m%d_%H%M%S_%f")
    biocam_log["pitch_deg"] *= -1  # BioCam pitch is opposite to AUV pitch. ALR pitch is the correct orientation.
    biocam_log["yaw_deg"] *= -1    # BioCam yaw is opposite to AUV heading and also off by several degrees - trust ALR heading more.
    alr_log = pd.read_csv(alr_log_path, usecols=["corrected_timestamp", "AUV_roll", "AUV_pitch", "AUV_heading"])
    alr_log["corrected_timestamp"] += shift_auv_time_by
    alr_log["timestamp"] = pd.to_datetime(alr_log["corrected_timestamp"], unit='s')
    alr_log["AUV_roll"] *= 180 / 3.14159
    alr_log["roll_at_biocam"] = alr_log["AUV_roll"] + biocam_roll_offset_deg
    alr_log["AUV_pitch"] *= 180 / 3.14159
    alr_log["pitch_at_biocam"] = alr_log["AUV_pitch"] + biocam_pitch_offset_deg
    alr_log["AUV_heading"] *= 180 / 3.14159

    plt.figure()
    plt.subplot(3, 1, 1)
    plt.plot(biocam_log["timestamp"], biocam_log["roll_deg"], label="BioCam roll")
    plt.plot(alr_log["timestamp"], alr_log["roll_at_biocam"], label="Roll from ALR, compensated for BioCam offset")
    plt.legend()
    plt.subplot(3, 1, 2)
    plt.plot(biocam_log["timestamp"], biocam_log["pitch_deg"], label="BioCam pitch")
    plt.plot(alr_log["timestamp"], alr_log["pitch_at_biocam"], label="Pitch from ALR, compensated for BioCam offset")
    plt.legend()
    plt.subplot(3, 1, 3)
    plt.plot(biocam_log["timestamp"], biocam_log["yaw_deg"], label="BioCam heading")
    plt.plot(alr_log["timestamp"], alr_log["AUV_heading"], label="ALR heading")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("BioCam_IMU", help="Path to BioCam IMU csv log")
    parser.add_argument("ALR_engineering_log", help="Path to (time-corrected) ALR engineering log")
    parser.add_argument("-t", "--shift_auv_time_by", help="Shift AUV time by this many seconds (add)", type=float, default=0.0)
    parser.add_argument("-r", "--biocam_roll_offset_deg", help="Offset BioCam roll by this many degrees", type=float, default=0.0)
    parser.add_argument("-p", "--biocam_pitch_offset_deg", help="Offset BioCam pitch by this many degrees", type=float, default=0.0)
    args = parser.parse_args()
    main(args.BioCam_IMU, args.ALR_engineering_log, args.shift_auv_time_by, args.biocam_roll_offset_deg, args.biocam_pitch_offset_deg)


# Example usage:
# Original BioCam IMU log and ALR engineering log corrected for time drift based on messages over serial only and applying offsets to time, roll and pitch to make the BioCam and ALR redings to line up:
# python ./compare_biocam_to_alr_orientation.py D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20220923_130737_alr_bc4k15c_mapping/20220923_125146_imu.csv D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20220923_130737_alr_bc4k15c_mapping/corrected_engineering_log.csv -t -1.6 -r 1.9 -p -0.5
# python ./compare_biocam_to_alr_orientation.py D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20221004_153010_alr_bc4k15c_mapping/20221004_150501_imu.csv D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20221004_153010_alr_bc4k15c_mapping/engineering_log_corrected.csv -t -1.6 -r 1.9 -p -0.5
# python ./compare_biocam_to_alr_orientation.py D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20221006_095110_alr_bc4k15c_mapping/20221006_092720_imu.csv D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20221006_095110_alr_bc4k15c_mapping/engineering_log_corrected.csv -t -1.6 -r 1.9 -p -0.5

# After correcting engineering log for time and orientation offsets with apply_offsets_to_engineering_log.py (using the values found above). Files now line up, so no offsets are needed:
# python ./compare_biocam_to_alr_orientation.py D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20220923_130737_alr_bc4k15c_mapping/20220923_125146_imu.csv D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20220923_130737_alr_bc4k15c_mapping/engineering_log_corrected_2.csv
# python ./compare_biocam_to_alr_orientation.py D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20221004_153010_alr_bc4k15c_mapping/20221004_150501_imu.csv D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20221004_153010_alr_bc4k15c_mapping/engineering_log_corrected_2.csv
# python ./compare_biocam_to_alr_orientation.py D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20221006_095110_alr_bc4k15c_mapping/20221006_092720_imu.csv D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20221006_095110_alr_bc4k15c_mapping/engineering_log_corrected_2.csv

# After correcting engineering log for time and orientation offsets in opposite direction (for testing) with apply_offsets_to_engineering_log.py (turns out to be wrong - don't use these.)
# python ./compare_biocam_to_alr_orientation.py D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20220923_130737_alr_bc4k15c_mapping/20220923_125146_imu.csv D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20220923_130737_alr_bc4k15c_mapping/engineering_log_corrected_3_minus_1_9_roll.csv
# python ./compare_biocam_to_alr_orientation.py D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20221004_153010_alr_bc4k15c_mapping/20221004_150501_imu.csv D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20221004_153010_alr_bc4k15c_mapping/engineering_log_corrected_3_minus_1_9_roll.csv
# python ./compare_biocam_to_alr_orientation.py D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20221006_095110_alr_bc4k15c_mapping/20221006_092720_imu.csv D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20221006_095110_alr_bc4k15c_mapping/engineering_log_corrected_3_minus_1_9_roll.csv
