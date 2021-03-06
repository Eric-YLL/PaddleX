#copyright (c) 2020 PaddlePaddle Authors. All Rights Reserve.
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

import paddlelite.lite as lite
import os
import argparse


def export_lite():
    opt = lite.Opt()
    model_file = os.path.join(FLAGS.model_path, '__model__')
    params_file = os.path.join(FLAGS.model_path, '__params__')
    opt.run_optimize("", model_file, params_file, FLAGS.place, FLAGS.save_dir)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--model_path",
        type=str,
        default="",
        help="model path.",
        required=True)
    parser.add_argument(
        "--place",
        type=str,
        default="arm",
        help="preprocess config path.",
        required=True)
    parser.add_argument(
        "--save_dir",
        type=str,
        default="paddlex.onnx",
        help="Directory for storing the output visualization files.",
        required=True)
    FLAGS = parser.parse_args()
    export_lite()
