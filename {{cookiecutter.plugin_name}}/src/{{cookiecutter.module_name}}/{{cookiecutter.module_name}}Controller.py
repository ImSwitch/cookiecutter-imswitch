from imswitch.imcontrol.model.managers.detectors.DetectorManager import DetectorManager, DetectorAction, DetectorNumberParameter
from imswitch.imcontrol.controller.basecontrollers import ImConWidgetController
from imswitch.imcontrol.view.ImConMainView import _DockInfo

import numpy as np
from typing import Any, Dict, List, Optional, Tuple



class {{cookiecutter.module_name}}Controller(ImConWidgetController):
    """Linked to CameraPluginWidget."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
