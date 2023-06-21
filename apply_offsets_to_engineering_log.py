import pandas as pd
import argparse


def main(input_path, output_path, offset_s, offset_roll_rad, offset_pitch_rad):
    df = pd.read_csv(input_path)
    df["corrected_timestamp"] += offset_s
    df["AUV_roll"] += offset_roll_rad
    df["AUV_pitch"] += offset_pitch_rad
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", type=str)
    parser.add_argument("output_path", type=str)
    parser.add_argument("offset_s", type=float)
    parser.add_argument("offset_roll_rad", type=float)
    parser.add_argument("offset_pitch_rad", type=float)
    args = parser.parse_args()
    main(args.input_path, args.output_path, args.offset_s, args.offset_roll_rad, args.offset_pitch_rad)


# Example usage:
# Applying time, roll and pitch offset found using compare_biocam_to_alr_orientation.py
'''
python ./apply_offsets_to_engineering_log.py D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20220923_130737_alr_bc4k15c_mapping/corrected_engineering_log.csv D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20220923_130737_alr_bc4k15c_mapping/engineering_log_corrected_2.csv -1.6 0.033161 -0.008727
python ./apply_offsets_to_engineering_log.py D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20221004_153010_alr_bc4k15c_mapping/engineering_log_corrected.csv D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20221004_153010_alr_bc4k15c_mapping/engineering_log_corrected_2.csv -1.6 0.033161 -0.008727
python ./apply_offsets_to_engineering_log.py D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20221006_095110_alr_bc4k15c_mapping/engineering_log_corrected.csv D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20221006_095110_alr_bc4k15c_mapping/engineering_log_corrected_2.csv -1.6 0.033161 -0.008727
'''

# Applying time, roll and pitch offset found using compare_biocam_to_alr_orientation.py, but apply the inverse of the roll and pitch offsets for testing (turns out this does not make sense indeed - don't use this!)
'''
python ./apply_offsets_to_engineering_log.py D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20220923_130737_alr_bc4k15c_mapping/corrected_engineering_log.csv D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20220923_130737_alr_bc4k15c_mapping/engineering_log_corrected_3_minus_1_9_roll.csv -1.6 -0.033161 0.008727
python ./apply_offsets_to_engineering_log.py D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20221004_153010_alr_bc4k15c_mapping/engineering_log_corrected.csv D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20221004_153010_alr_bc4k15c_mapping/engineering_log_corrected_3_minus_1_9_roll.csv -1.6 -0.033161 0.008727
python ./apply_offsets_to_engineering_log.py D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20221006_095110_alr_bc4k15c_mapping/engineering_log_corrected.csv D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20221006_095110_alr_bc4k15c_mapping/engineering_log_corrected_3_minus_1_9_roll.csv -1.6 -0.033161 0.008727
'''
