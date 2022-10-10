import torchio as tio
import os

def plot(*images):
    subject = tio.Subject(temp=tio.ScalarImage(images[0]))
    if len(images) > 1:
        for img in images:
            subject.add_image(tio.ScalarImage(img), os.path.basename(img).replace(".nii.gz", ""))
    else:
        subject.add_image(tio.ScalarImage(images[0]), os.path.basename(images[0]).replace(".nii.gz", ""))

    subject.remove_image("temp")
    subject.plot()