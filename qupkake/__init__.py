"""Predict micro-pKa of organic molecules"""

# Add imports here
from ._version import get_versions
from .qupkake import *

__version__ = get_versions()["version"]

import os
import shutil
import subprocess

# Priority for xTB location:
# 1. XTBPATH environment variable (explicit user setting)
# 2. System xTB found in PATH
# 3. Bundled xTB (may not work on all architectures)
XTB_LOCATION = None

# First check XTBPATH environment variable
if os.environ.get("XTBPATH"):
    XTB_LOCATION = os.environ.get("XTBPATH")
    if not os.path.exists(XTB_LOCATION):
        raise RuntimeError(f'xTB executable in XTBPATH: "{XTB_LOCATION}" does not exist.')
else:
    # Try to find xTB in system PATH
    system_xtb = shutil.which("xtb")
    if system_xtb:
        XTB_LOCATION = system_xtb
    else:
        # Fall back to bundled xTB
        bundled_xtb = os.path.join(os.path.dirname(__file__), "xtb-641/bin/xtb")
        if os.path.exists(bundled_xtb):
            XTB_LOCATION = bundled_xtb
        else:
            raise RuntimeError(
                'xTB not found. Please install xTB and either:\n'
                '  1. Add it to your PATH, or\n'
                '  2. Set the XTBPATH environment variable to the xTB executable path.\n'
                'Install with: conda install -c conda-forge xtb'
            )
