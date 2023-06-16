# Convert raw colour imges to RGB

# BioCam4000_15C

#input_folder='D:/raw/2022/insite_subsampled/20221004_153010_alr_bc4k15c_mapping_selection/'
#image_filename=20221005_115709_169039_20221005_115706_389281_pcoc.tif
#output_folder='D:/processed/2022/insite_subsampled/20221004_153010_alr_bc4k15c_mapping_selection2/'

input_folder='J:/raw/2022/insite/alr/biocam_data_subsampled/20221006_095110_alr_bc4k15c_mapping/cam61008269_strobe/'
output_folder='D:/processed/2022/insite_subsampled/20221006_095110_alr_bc4k15c_mapping/'

parameters='0.022 0.015 0.025 1200 1200 1200'

image_path=${input_folder}${image_filename}

# # Single image for adjusting demosaic parameters (-d)
#image_conversion -i ${image_path} -o $output_folder -f png -d $parameters -w

# Process entire folder
image_conversion -i ${input_folder} -o $output_folder -f png -d $parameters

printf "Demosaic parameters [cr, cg, cb, sr, sg, sb]:\n%s\n" "$parameters" > ${output_folder}parameters.txt
