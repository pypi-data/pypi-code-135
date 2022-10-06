import os

okIcon_file=os.path.join(os.path.dirname(__file__),"icons/ok.svg")
errorIcon_file=os.path.join(os.path.dirname(__file__),"icons/error.svg")
warnIcon_file=os.path.join(os.path.dirname(__file__),"icons/warn.svg")
loadingMovie_file = os.path.join(os.path.dirname(__file__),"icons/load.svg")
voidsvg_file = os.path.join(os.path.dirname(__file__),"icons/void.svg")

sym_template = os.path.abspath(os.path.join(os.path.dirname(__file__),"resources/sym_brain.nii.gz"))
protocol_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),"resources/dti_protocols"))
