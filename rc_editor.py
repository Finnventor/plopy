from matplotlib import rcParams
from .ui.ui_options_rc import Ui_RCOptions

print(rcParams.find_all("t"))


class RCOptions(Ui_RCOptions):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key in rcParams
