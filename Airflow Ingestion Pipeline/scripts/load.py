import os
import rasterio

folder_path = '/Users/annanya/airflow/outputs/outdir_new_TF/'
file_extension = ".tif"
search_string = ["VV","HV","HH","VH"]

# Get a list of all files in the folder
all_files = os.listdir(folder_path)
print(all_files)

# Filter the list to only include files with the correct extension and containing the search string
for i in range(len(search_string)):
    matching_files = [filename for filename in all_files if filename.endswith(file_extension) and search_string[i] in filename]
    if(len(matching_files)!=0):
        break
                
                    
                
# Print the matching files
print(matching_files)
            
                
name=folder_path+matching_files[0]
d=rasterio.open(name)
vv=d.read(1, masked=True)
print(vv)