import numpy as np

deepglob_class_names = ['unknown', 'urban', 'agriculture', 'rangeland',
                        'forest', 'water', 'barren']

pallet_deepglob = np.array([[[0, 0, 0], 
                            [0, 255, 255], 
                            [255, 255, 0], 
                            [255, 0, 255],
                            [0, 255, 0], 
                            [0, 0, 255], 
                            [255, 255, 255]]],np.uint8) / 255