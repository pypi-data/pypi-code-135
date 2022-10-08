class Preprocessor():
    """Generic Preprocessor for 3D medical imaging data"""

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
    
    def preprocess(self) -> None:
        pass

class CTPreprocessorNNUnet(Preprocessor):
    """Preprocessor for CT 3D medical imaging data
        nnUNet:
            - Intensity Normalization: global dataset percentile clipping & z score with global foreground mean and s.d.
            - Image Resampling Strategy: 
                if anisotropic, 
                    in-plane with third-order spline, 
                    out-of-plane with NN 
                (otherwise third-order spline)
            - Image Target Spacing
                if anisotropic: 
                    lowest resolution axis tenth percentile other axes median.
                othwerwise:
                    median spacing for each axis (computed based on spacings found in training data)
    """
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def preprocess(self) -> None:
        raise NotImplementedError("CT data not supported)")


class MRIPreprocessor(Preprocessor):
    """Preprocessor for MRI 3D medical imaging data"""
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        
    def preprocess(self) -> None:
        raise NotImplementedError("MRI data not supported")