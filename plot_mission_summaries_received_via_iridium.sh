## Run this script line by line to plot the mission summaries for each dive we have a sbd or txt file for

# Reference time: Fri Sep 23 2022 13:25:53 GMT
python D:/software/git_bash/biocam_scripts/ship_or_shore_side/biocam_summary_decoder.py D:/raw/2022/insite/alr/alr_dive_summary_via_iridium/m78/300025060108110_003738_M78.sbd
# Reference time: Fri Sep 23 2022 13:25:53 GMT. Same file as the one above, just a different name.
python D:/software/git_bash/biocam_scripts/ship_or_shore_side/biocam_summary_decoder.py "D:/raw/2022/insite/alr/alr_dive_summary_via_iridium/m78/alr-3_2022-09-24T01 45 55.573Z.txt"
# Reference time: Tue Oct 04 2022 08:26:29 GMT (no images)
python D:/software/git_bash/biocam_scripts/ship_or_shore_side/biocam_summary_decoder.py "D:/raw/2022/insite/alr/alr_dive_summary_via_iridium/alr-3_2022-10-04T14 31 59.270Z.txt"
# M93; Reference time: Tue Oct 04 2022 15:49:05 GMT
python D:/software/git_bash/biocam_scripts/ship_or_shore_side/biocam_summary_decoder.py D:/raw/2022/insite/alr/alr_dive_summary_via_iridium/m93/300025060108110_003924.sbd
# M94; Reference time: Wed Oct 05 2022 00:08:57 GMT
python D:/software/git_bash/biocam_scripts/ship_or_shore_side/biocam_summary_decoder.py D:/raw/2022/insite/alr/alr_dive_summary_via_iridium/m94/300025060108110_003931.sbd
# M95; Reference time: Wed Oct 05 2022 08:14:08 GMT
python D:/software/git_bash/biocam_scripts/ship_or_shore_side/biocam_summary_decoder.py D:/raw/2022/insite/alr/alr_dive_summary_via_iridium/m95/300025060108110_003938.sbd


# 3 dives at Miller:
# 4 transects each, starting and ending at the mid-point of the the transects!
# Mission | Unix time start - end   | Human raedable time start - end           | Altitude [m]
# --------+-------------------------+-------------------------------------------+-------------
# M93     | 1664899560 - 1664926440 | 2022/10/04 16:06:00 - 2022/10/04 23:34:00 | 5
# M94     | 1664929342 - 1664955511 | 2022/10/05 00:22:22 - 2022/10/05 07:38:31 | 4.6
# M95     | 1664960681 - 1664984768 | 2022/10/05 09:04:41 - 2022/10/05 15:46:08 | 4
