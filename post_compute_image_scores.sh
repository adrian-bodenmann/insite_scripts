RAW=B:/Data/raw/2022/insite/alr/
PROCESSED=D:/processed/2022/insite/alr/

cd D:/software/git_bash/biocam_scripts/ship_or_shore_side/

echo "[$(date +%Y/%m/%d\ %H:%M:%S)] Start batch..."
start=$SECONDS
python post_compute_image_score.py ${RAW}20220923_130737_alr_bc4k15c_mapping/image/cam61008269_strobe/ ${PROCESSED}20220923_130737_alr_bc4k15c_mapping/cam61008269_strobe_image_scores_post_computed.csv
python post_compute_image_score.py ${RAW}20220923_130737_alr_bc4k15c_mapping/image/cam61008031_laser/  ${PROCESSED}20220923_130737_alr_bc4k15c_mapping/cam61008031_laser_image_scores_post_computed.csv
python post_compute_image_score.py ${RAW}20221004_153010_alr_bc4k15c_mapping/image/cam61008269_strobe/ ${PROCESSED}20221004_153010_alr_bc4k15c_mapping/cam61008269_strobe_image_scores_post_computed.csv
python post_compute_image_score.py ${RAW}20221004_153010_alr_bc4k15c_mapping/image/cam61008031_laser/  ${PROCESSED}20221004_153010_alr_bc4k15c_mapping/cam61008031_laser_image_scores_post_computed.csv
python post_compute_image_score.py ${RAW}20221006_095110_alr_bc4k15c_mapping/image/cam61008269_strobe/ ${PROCESSED}20221006_095110_alr_bc4k15c_mapping/cam61008269_strobe_image_scores_post_computed.csv
python post_compute_image_score.py ${RAW}20221006_095110_alr_bc4k15c_mapping/image/cam61008031_laser/  ${PROCESSED}20221006_095110_alr_bc4k15c_mapping/cam61008031_laser_image_scores_post_computed.csv
elapsed_s=$((SECONDS - start))
TZ=UTC0 elapsed_string="$((elapsed_s/(24*60*60))) day(s) $(printf '%(%H h %M min %S s)T\n' "$elapsed_s")"
echo "[$(date +%Y/%m/%d\ %H:%M:%S)] ... done processing batch in $elapsed_string."