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
# Applying time, roll and pitch offset found using compare_biocam_to_alr_orientation.py to insite datasets
'''
python ./apply_offsets_to_engineering_log.py D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20220923_130737_alr_bc4k15c_mapping/corrected_engineering_log.csv D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20220923_130737_alr_bc4k15c_mapping/engineering_log_corrected_2.csv -1.6 0.033161 -0.008727
python ./apply_offsets_to_engineering_log.py D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20221004_153010_alr_bc4k15c_mapping/engineering_log_corrected.csv D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20221004_153010_alr_bc4k15c_mapping/engineering_log_corrected_2.csv -1.6 0.033161 -0.008727
python ./apply_offsets_to_engineering_log.py D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20221006_095110_alr_bc4k15c_mapping/engineering_log_corrected.csv D:/cruises/2022/insite/comparison_attitude_BioCam-ALR/20221006_095110_alr_bc4k15c_mapping/engineering_log_corrected_2.csv -1.6 0.033161 -0.008727
'''

# Applying time, roll and pitch offset found using compare_biocam_to_alr_orientation.py to DY152 mapping datasets
'''
python ./apply_offsets_to_engineering_log.py J:/raw/2022/dy152/alr/20220712_213257_alr_bc4k15c_mapping/nav/alr_log/corrected_engineering_log_m47.csv J:/raw/2022/dy152/alr/20220712_213257_alr_bc4k15c_mapping/nav/alr_log/corrected_engineering_log_m47_2.csv -1.8 0.0279253 -0.008727
python ./apply_offsets_to_engineering_log.py J:/raw/2022/dy152/alr/20220713_073311_alr_bc4k15c_mapping/nav/alr_log/corrected_engineering_log_m48.csv J:/raw/2022/dy152/alr/20220713_073311_alr_bc4k15c_mapping/nav/alr_log/corrected_engineering_log_m48_2.csv -1.8 0.0279253 -0.008727
python ./apply_offsets_to_engineering_log.py J:/raw/2022/dy152/alr/20220714_131120_alr_bc4k15c_mapping/nav/alr_log/corrected_engineering_log_m50.csv J:/raw/2022/dy152/alr/20220714_131120_alr_bc4k15c_mapping/nav/alr_log/corrected_engineering_log_m50_2.csv -1.8 0.0279253 -0.008727
python ./apply_offsets_to_engineering_log.py J:/raw/2022/dy152/alr/20220714_204123_alr_bc4k15c_mapping/nav/alr_log/corrected_engineering_log_m51.csv J:/raw/2022/dy152/alr/20220714_204123_alr_bc4k15c_mapping/nav/alr_log/corrected_engineering_log_m51_2.csv -1.8 0.0279253 -0.008727
python ./apply_offsets_to_engineering_log.py J:/raw/2022/dy152/alr/20220719_175749_alr_bc4k15c_mapping/nav/alr_log/corrected_engineering_log_m64.csv J:/raw/2022/dy152/alr/20220719_175749_alr_bc4k15c_mapping/nav/alr_log/corrected_engineering_log_m64_2.csv -1.8 0.0279253 -0.008727
python ./apply_offsets_to_engineering_log.py J:/raw/2022/dy152/alr/20220720_094049_alr_bc4k15c_mapping/nav/alr_log/corrected_engineering_log_m65.csv J:/raw/2022/dy152/alr/20220720_094049_alr_bc4k15c_mapping/nav/alr_log/corrected_engineering_log_m65_2.csv -1.8 0.0279253 -0.008727
python ./apply_offsets_to_engineering_log.py J:/raw/2022/dy152/alr/20220720_200914_alr_bc4k15c_mapping/nav/alr_log/corrected_engineering_log_m66.csv J:/raw/2022/dy152/alr/20220720_200914_alr_bc4k15c_mapping/nav/alr_log/corrected_engineering_log_m66_2.csv -1.8 0.0279253 -0.008727
'''
