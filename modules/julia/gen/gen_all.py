#!/usr/bin/python

# This file is part of OpenCV project.
# It is subject to the license terms in the LICENSE file found in the top-level directory
# of this distribution and at http://opencv.org/license.html
# Copyright (C) 2020 by Archit Rungta

import sys
import subprocess
import os

mod_path = sys.argv[1]


hdr_list = [
    f"{mod_path}/core/include/opencv2/core.hpp",
    f"{mod_path}/core/include/opencv2/core/base.hpp",
    f"{mod_path}/core/include/opencv2/core/bindings_utils.hpp",
    f"{mod_path}/core/include/opencv2/core/optim.hpp",
    f"{mod_path}/core/include/opencv2/core/persistence.hpp",
    f"{mod_path}/core/include/opencv2/core/types.hpp",
    f"{mod_path}/core/include/opencv2/core/utility.hpp",
]

for module in sys.argv[2:]:
    if module == 'opencv_calib3d':
        hdr_list.append(f"{mod_path}/calib3d/include/opencv2/calib3d.hpp")

    elif module == 'opencv_dnn':
        hdr_list.append(f"{mod_path}/dnn/include/opencv2/dnn/dnn.hpp")
    elif module == 'opencv_highgui':
        hdr_list.append(f"{mod_path}/highgui/include/opencv2/highgui.hpp")
    elif module == 'opencv_imgcodecs':
        hdr_list.append(f"{mod_path}/imgcodecs/include/opencv2/imgcodecs.hpp")
    elif module == 'opencv_imgproc':
        hdr_list.append(f"{mod_path}/imgproc/include/opencv2/imgproc.hpp")
    elif module == 'opencv_videoio':
        hdr_list.append(f"{mod_path}/videoio/include/opencv2/videoio.hpp")
if not os.path.exists('autogen_cpp'):
    os.makedirs('autogen_cpp')
    os.makedirs('autogen_jl')

subprocess.call([sys.executable, 'gen3_cpp.py', ';'.join(hdr_list)])
subprocess.call([sys.executable, 'gen3_julia_cxx.py', ';'.join(hdr_list)])
subprocess.call([sys.executable, 'gen3_julia.py', ';'.join(hdr_list)])
