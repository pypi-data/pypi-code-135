import subprocess
import os
import sys
import shutil
import json
import csv
import SimpleITK as sitk
from glob import glob

def main():
    base_image_folder = os.path.join(os.getcwd(), 'data')
    base_output_folder = os.path.join(base_image_folder, 'local_verts')
    base_intermediate_folder = os.path.join(base_image_folder, 'tmp')
    models_folder = os.path.join(os.getcwd(), 'models')
    cropped_folder = os.path.join(base_output_folder, 'cropped')

    pipeline = sys.argv[1:] if len(sys.argv) > 1 else ['all']
    print('Using pipeline: ', pipeline)

    all_image_folders = [os.path.split(path)[-1] for path in glob(os.path.join(base_image_folder, '*')) if
                         os.path.isdir(path) and path != base_output_folder]
    for current_image_folder in sorted(all_image_folders):
        print('Processing folder ', current_image_folder)

        image_folder = os.path.join(base_image_folder, current_image_folder)
        output_folder = os.path.join(base_output_folder, current_image_folder)
        intermediate_folder = os.path.join(base_intermediate_folder, current_image_folder)

        preprocessed_image_folder = os.path.join(intermediate_folder, 'data_preprocessed')
        spine_localization_folder = os.path.join(intermediate_folder, 'spine_localization')
        spine_localization_model = os.path.join(models_folder, 'spine_localization')
        vertebrae_localization_folder = os.path.join(intermediate_folder, 'vertebrae_localization')
        vertebrae_localization_model = os.path.join(models_folder, 'vertebrae_localization')

        if 'preprocessing' in pipeline or 'all' in pipeline:
            subprocess.run(['python', 'preprocess.py',
                            '--image_folder', image_folder,
                            '--output_folder', preprocessed_image_folder,
                            '--sigma', '0.75'])
        if 'spine_localization' in pipeline or 'all' in pipeline:
            subprocess.run(['python', 'main_spine_localization.py',
                            '--image_folder', preprocessed_image_folder,
                            '--setup_folder', intermediate_folder,
                            '--model_files', spine_localization_model,
                            '--output_folder', spine_localization_folder])
        if 'vertebrae_localization' in pipeline or 'all' in pipeline:
            subprocess.run(['python', 'main_vertebrae_localization.py',
                            '--image_folder', preprocessed_image_folder,
                            '--setup_folder', intermediate_folder,
                            '--model_files', vertebrae_localization_model,
                            '--output_folder', vertebrae_localization_folder])
        if 'postprocessing' in pipeline or 'all' in pipeline:
            subprocess.run(['python', 'cp_landmark_files.py',
                            '--landmark_folder', vertebrae_localization_folder,
                            '--output_folder', output_folder])

        localization_bounding_boxes = os.path.join(spine_localization_folder, "bbs.csv")
        shutil.copyfile(localization_bounding_boxes, output_folder+"\\bbs.csv")

        shutil.copyfile(vertebrae_localization_folder + "\\" + "landmarks.csv", output_folder + "\\" + "landmarks.csv")

        with open(output_folder+"\\bbs.csv", newline='') as BBcsv:
            BBreader = csv.reader(BBcsv, delimiter=',')
            for row in BBreader:
                with open(output_folder + "\\" + "landmarks.csv", newline='') as landmarksCSV:
                    Landmarks_reader = csv.reader(landmarksCSV, delimiter=',')
                    for compare in Landmarks_reader:
                        if compare[0] == row[0]:
                            with open(output_folder + "\\" + compare[0] + ".json", 'w') as new:
                                data = [{"label": 0, "X": float(row[4]), "Y": float(row[5]), "Z": float(row[6])}]
                                vert = 0
                                for i in range(1, len(compare), 3):
                                    if compare[i] == compare[i+1] == compare[i+2] == 'nan':
                                        break
                                    else:
                                        vert += 1
                                        data.append({"label": vert, "X": float(compare[i]), "Y": float(compare[i+1]), "Z": float(compare[i+2])})
                                last = vert + 1
                                data.append({"label": last, "X": float(row[1]), "Y": float(row[2]), "Z": float(row[3])})
                                json.dump(data, new)

        for image in os.listdir(preprocessed_image_folder):
            print('Processing', image)
            volume = sitk.ReadImage(os.path.join(preprocessed_image_folder, image))
            image_size = volume.GetSize()
            nii = os.path.splitext(image)[0]
            for jsons in os.listdir(output_folder):
                image_name = os.path.splitext(nii)[0]
                if image_name == os.path.splitext(jsons)[0]:
                    f = open(output_folder + "\\" + jsons)
                    new = json.load(f)
                    size = len(new)

                    new_path = os.path.join(cropped_folder, image_name)
                    if not os.path.exists(new_path):
                        os.makedirs(new_path)

                    for i in range(1, 8):
                        vert_name = new[i]["label"]
                        lower = (int(new[0]["X"])+10, int(new[0]["Y"])+10, int(new[i+1]["Z"]))
                        true_lower = volume.TransformPhysicalPointToIndex(lower)

                        upper = (int(new[size-1]["X"])-10, int(new[size-1]["Y"])-10, int(new[i-1]["Z"]))
                        if vert_name == 1:
                            upper = (int(new[size-1]["X"])-10, int(new[size-1]["Y"])-10, int(new[i-1]["Z"])+10)

                        true_upper = volume.TransformPhysicalPointToIndex(upper)

                        vert_volume = volume[true_upper[0]:true_lower[0], true_upper[1]:true_lower[1], true_lower[2]:true_upper[2]]
                        sitk.WriteImage(vert_volume, new_path + "\\C" + str(vert_name) + ".nii.gz")

        shutil.rmtree(base_intermediate_folder)

if __name__ == '__main__':
    main()
