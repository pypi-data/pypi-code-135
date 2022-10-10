from AudioAugmentation import AudioAugmentation


class Audio_K(AudioAugmentation):

    def __init__(self, file_path: str, save: str = None, grafica: bool = False):
        super().__init__(audio_file=file_path, save=save, graph=grafica)

    def aumentar(self):
        all_data = [
            self.get_original(),
            self.add_noise(factor_ruido=0.05),
            self.add_noise2(),
            self.stretch(rate_stretch=0.8),
            self.shift(),
            self.add_crop(),
            self.loudness(),
            self.speed(),
            self.normalizer(),
            self.polarizer()
        ]

        return all_data