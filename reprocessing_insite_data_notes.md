Processing Insite data
======================

### Correct images

```bash
unalias correct_images  # Not using docker

date; correct_images parse /media/hdd22/adrian/processed/2022/insite/alr/20221004_153010_alr_bc4k15c_mapping/ && date && correct_images process /media/hdd22/adrian/processed/2022/insite/alr/20221004_153010_alr_bc4k15c_mapping/ ; date
```


### Texture mappnig
```bash
alias texture_mapping='docker run --rm -it --cpus=18 --ipc=private -e USER=$(whoami) -h $HOSTNAME --user $(id -u):$(id -g) --volume /media:/media -v /etc/passwd:/etc/passwd:ro -v /etc/group:/etc/group:ro --group-add $(cat /etc/group | grep crunchers: | cut -d: -f3) --name=texture_mapping_$(whoami)_$(date +%Y%m%d_%H%M%S) texture_mapping_develop_adrian texture_mapping'
```

```bash
# until (date && correct_images process processed/2022/insite/alr/20221004_153010_alr_bc4k15c_mapping/ -F); do sleep 5; done; date

i=0; until (date && texture_mapping textureMapAndSimplify --iniFile /media/hdd22/adrian/configuration/2022/insite/alr/20220923_130737_alr_bc4k15c_mapping/texture_mapping.ini); do i=$((i+1)); echo "Command failed $i times so far"; sleep 5; done; date; echo "Done. Command failed $i times in total";

i=0; until (date && texture_mapping textureMapAndSimplify --iniFile /media/hdd22/adrian/configuration/2022/insite/alr/20221004_153010_alr_bc4k15c_mapping/texture_mapping.ini); do i=$((i+1)); echo "Command failed $i times so far"; sleep 5; done; date; echo "Done. Command failed $i times in total";

i=0; until (date && texture_mapping textureMapAndSimplify --iniFile /media/hdd22/adrian/configuration/2022/insite/alr/20221004_153010_alr_bc4k15c_mapping/texture_mapping.ini); do i=$((i+1)); echo "Command failed $i times so far"; sleep 5; done; date; echo "Done. Command failed $i times in total";
```

### Merge GeoTiffs

In `adrian@oplab-crunch2:/media/hdd22/adrian/configuration/2022/insite/alr/20221004_153010_alr_bc4k15c_mapping$` run `./batch_process_mapping_data.sh`

For 20221006_095110_alr_bc4k15c_mapping:
In `adrian@oplab-crunch2:/media/hdd22/adrian/configuration/2022/insite/alr/20221006_095110_alr_bc4k15c_mapping$` run `./merge_bathymetry.sh`


## Georef Semantic
Only use NW Hutton dataset, as others have too low visibility

### Process images
- Process images with smoothed depth maps

### Move depth maps
- Move depth maps to folder structure where script expects them

### Sample
On adrian@oplab-crunch2
```bash
cd /media/hdd22/adrian/processed/2022/insite/alr/20220923_130737_alr_bc4k15c_mapping/
python3 ../script_rgbd_image_sampling.py
```
As we are only using 1 dataset we use the version of the script that crates the sampled data within the dataset

### LGA and GeoClr (old and wrong - dont use)
Set up settings files with correct altitude bounds (setting altitude max to 5.5)

`alias georef_semantics_adrian_devel='docker run --rm -it --ipc=private -e USER=$(whoami) -h $HOSTNAME --user $(id -u):$(id -g) --volume $(pwd):/data -v /etc/passwd:/etc/passwd:ro -v /etc/group:/etc/group:ro --group-add $(cat /etc/group | grep crunchers: | cut -d: -f3) --name=georef_$(whoami)_$(date +%Y%m%d_%H%M%S) --gpus all --shm-size=16g georef_semantics:adrian_devel georef_semantics'`

`cd` into adrian@oplab-crunch2:/media/hdd22/adrian/processed/2022/insite/alr/20220923_130737_alr_bc4k15c_mapping/semantic_output

```
georef_semantics_adrian_devel train_lga -i sampled_images_depth.csv -c georef_semantics_depth.yaml -o semantic_output_depth
georef_semantics_adrian_devel train_geoclr -i sampled_images_depth.csv -c georef_semantics_depth.yaml -o semantic_output_depth
georef_semantics_adrian_devel train_lga -i sampled_images_rgb.csv -c georef_semantics_rgb.yaml -o semantic_output_rgb
georef_semantics_adrian_devel train_geoclr -i sampled_images_rgb.csv -c georef_semantics_rgb.yaml -o semantic_output_rgb
georef_semantics_adrian_devel train_lga -i sampled_images_rgbd.csv -c georef_semantics_rgbd.yaml -o semantic_output_rgbd
georef_semantics_adrian_devel train_geoclr -i sampled_images_rgbd.csv -c georef_semantics_rgbd.yaml -o semantic_output_rgbd
```

### Train
On oplab-crunch2:
Rerun sampling (done twice. imges should be the same, but check if the sampled_images.csv are the ame as well. If not those in folder 2 ar the good ones)

On crunch-laptop:
rsync from crunch2. Then:
```bash
cd ~/data/processed/2022/insite/alr/semantic_interpretation
date && \
georef_semantics train_lga -c georef_semantics_depth.yaml -o semantic_output_depth && date && \
georef_semantics train_lga -c georef_semantics_rgb.yaml -o semantic_output_rgb && date && \
georef_semantics train_lga -c georef_semantics_rgbd.yaml -o semantic_output_rgbd ; date
```

On crunch2:
```bash
cd /media/hdd22/adrian/processed/2022/insite/alr/semantic_interpretation
georef_semantics train_geoclr -c georef_semantics_rgb.yaml -o semantic_output_rgb ; date
georef_semantics train_geoclr -c georef_semantics_depth.yaml -o semantic_output_depth ; date
georef_semantics train_geoclr -c georef_semantics_rgbd.yaml -o semantic_output_rgbd ; date
```

### Cluster
On crunch2:
```bash
cd /media/hdd22/adrian/processed/2022/insite/alr/semantic_interpretation
georef_semantics cluster -c georef_semantics_rgb.yaml -o semantic_output_rgb ; date
# georef_semantics cluster -c georef_semantics_depth.yaml -o semantic_output_depth ; date
# georef_semantics cluster -c georef_semantics_rgbd.yaml -o semantic_output_rgbd ; date
```