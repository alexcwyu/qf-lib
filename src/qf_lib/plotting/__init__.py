#     Copyright 2016-present CERN – European Organization for Nuclear Research
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

def _setup_matplotlib_config():
    from os.path import join, dirname

    import matplotlib.pyplot as plt
    this_dir = dirname(__file__)
    style_path = join(this_dir, "stylelib", "qfstyle.mplstyle")
    # Load the bundled style through the public API instead of mutating
    # Matplotlib's deprecated private style registry.
    plt.style.use(style_path)


_setup_matplotlib_config()
