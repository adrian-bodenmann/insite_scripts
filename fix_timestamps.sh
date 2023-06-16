#!/bin/bash

# Run this from a POSIX bash shell, e.g. Linux or Linux on WSL. MINGW64 will not work as fix_timestamps.sh needs `bc`, which MINGW64 doesn't have
# Because bash on Linux is used
# - It wants LF line endings (Linux) not CRLF (Windows) in fix_timestamps.sh. -> make sure fix_timestamps.sh is saved with LF line endings.
# - Paths need to be indicates in WSL way on windows. It will not find D:/


FIX_TIME=/mnt/d/software/git_python/oplab_pipeline/src/scripts/dy152_alr_fixtime.sh
# Fix timestamps for engineering log
#${FIX_TIME} -s /mnt/d/raw/2022/insite/alr/log/20221004/20221004_150503_auv_serial_message.log -e "/mnt/w/media/ssd/adrian/raw/2022/insite/alr/20221004_153010_alr_bc4k15c_mapping/nav/alr_log/engineering_log_sensors_cropped_to_Miller.csv" -o "/mnt/d/raw/2022/insite/alr/M92 to M97/engineering_log_corrected.csv"
#${FIX_TIME} -s /mnt/d/raw/2022/insite/alr/log/20221006/20221006_092722_auv_serial_message.log -e "/mnt/w/media/ssd/adrian/raw/2022/insite/alr/20221006_095110_alr_bc4k15c_mapping/nav/alr_log/engineering_log_sensors_cropped_to_Braemar_Pockmarks.csv" -o "/mnt/d/raw/2022/insite/alr/M92 to M97/engineering_log_corrected.csv"
# Fix timestamps for sensor data
${FIX_TIME} -s /mnt/d/raw/2022/insite/alr/log/20221004/20221004_150503_auv_serial_message.log -e "/mnt/d/raw/2022/insite/alr/M77 to M82/franatech_mets.csv" -o "/mnt/d/raw/2022/insite/alr/M77 to M82/franatech_mets_time_corrected_20220923.csv"
${FIX_TIME} -s /mnt/d/raw/2022/insite/alr/log/20221004/20221004_150503_auv_serial_message.log -e "/mnt/d/raw/2022/insite/alr/M77 to M82/chelsea_pah_plus_format_fixed.csv" -o "/mnt/d/raw/2022/insite/alr/M77 to M82/chelsea_pah_plus_format_fixed_time_corrected_20220923.csv"
#${FIX_TIME} -s /mnt/d/raw/2022/insite/alr/log/20221004/20221004_150503_auv_serial_message.log -e "/mnt/d/raw/2022/insite/alr/M92 to M97/franatech_mets.csv" -o "/mnt/d/raw/2022/insite/alr/M92 to M97/franatech_mets_time_corrected_20221004.csv"
#${FIX_TIME} -s /mnt/d/raw/2022/insite/alr/log/20221004/20221004_150503_auv_serial_message.log -e "/mnt/d/raw/2022/insite/alr/M92 to M97/chelsea_pah_plus_format_fixed.csv" -o "/mnt/d/raw/2022/insite/alr/M92 to M97/chelsea_pah_plus_format_fixed_time_corrected_20221004.csv"
#${FIX_TIME} -s /mnt/d/raw/2022/insite/alr/log/20221006/20221006_092722_auv_serial_message.log -e "/mnt/d/raw/2022/insite/alr/M92 to M97/franatech_mets.csv" -o "/mnt/d/raw/2022/insite/alr/M92 to M97/franatech_mets_time_corrected_20221006.csv"
#${FIX_TIME} -s /mnt/d/raw/2022/insite/alr/log/20221006/20221006_092722_auv_serial_message.log -e "/mnt/d/raw/2022/insite/alr/M92 to M97/chelsea_pah_plus_format_fixed.csv" -o "/mnt/d/raw/2022/insite/alr/M92 to M97/chelsea_pah_plus_format_fixed_time_corrected_20221006.csv"
