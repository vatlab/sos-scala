#!/usr/bin/env python3
#
# Copyright (c) Bo Peng and the University of Texas MD Anderson Cancer Center
# Distributed under the terms of the 3-clause BSD License.

import os
import pandas as pd
from tempfile import TemporaryDirectory
from textwrap import dedent
from sos.utils import env

class sos_scala:
    supported_kernels = {'Scala': ['scala', 'spylon_kernel']}
    background_color = '#D59D87'
    options = {}
    #cd_command = "cd {dir}"

    def __init__(self, sos_kernel, kernel_name='scala'):
        self.sos_kernel = sos_kernel
        self.kernel_name = kernel_name
        self.init_statements = ''

    def get_vars(self, names):
        pass
        #
        # get variables with names from env.sos_dict and create
        # them in the subkernel. The current kernel should be scala
#         for name in names:
#             var = env.sos_dict[name]
#             # https://www.scala.com/help.cgi?data+types
#             if isinstance(var, (int, float)):
#                 # byte, int, long
#                 self.sos_kernel.run_cell(f'local {name} {var}', True, False,
#                     on_error=f'Failed to put variable {name} to scala')
#             elif isinstance(var, str):
#                 # string L (L is length)
#                 # we are using local var = "str"
#                 # to send string to Scala, but I am not sure how to handle " and \n etc
#                 var = var.replace('\n', '')
#                 self.sos_kernel.run_cell(f'local {name} {var}', True, False,
#                     on_error=f'Failed to put variable {name} to scala')
#             elif isinstance(var, pd.DataFrame):
#                 # convert dataframe to scala
#                 with TemporaryDirectory() as temp_dir:
#                     filename = os.path.join(temp_dir, f'{name}.dta')
#                     env.sos_dict[name].to_scala(filename)
#                     self.sos_kernel.run_cell(f'use {filename}', True, False,
#                         on_error=f'Failed to put variable {name} to scala')
#             else:
#                 #if self.sos_kernel._debug_mode:
#                 self.sos_kernel.warn(f'Cannot transfer object {name} of type {var.__class__.__name__} to scala')#


    def put_vars(self, items, to_kernel=None):
        return {}
        # put scala dataset to Python as dataframe
#         response = self.sos_kernel.get_response('macro list', ('stream'))
#         response = [x[1]['text'].split(':', 1) for x in response if ':' in x[1]['text']]
#         res = {}
#         for x,y in response:
#             if x.startswith('_sos'):
#                 res[x[1:]] = y.strip()
#             elif x.startswith('sos') and x not in res:
#                 res[x] = y.strip()
#             elif x.startswith('_') and x[1:] in items:
#                 res[x[1:]] = y.strip()
#             elif x in items and x not in res:
#                 res[x] = y.strip()
# 
#         remaining = [x for x in items if x not in res]
# 
#         if not remaining:
#             return res
# 
#         # first, get a list of global macros
#         with TemporaryDirectory() as temp_dir:
#             for idx, item in enumerate(remaining):
#                 try:
#                     code = f'''\
#                         local _olddir : pwd
#                         cd {temp_dir}
#                         save data_{idx}.dta
#                         cd `_olddir'
#                     '''
#                     # run the code to save file
#                     self.sos_kernel.run_cell(dedent(code), True, False,
#                         on_error=f"Failed to get data set {item} from scala")
#                     # check if file exists
#                     saved_file = os.path.join(temp_dir, f'data_{idx}.dta')
#                     if not os.path.isfile(saved_file):
#                         self.sos_kernel.warn(f'Failed to save dataset to {saved_file}')
#                         continue
#                     # now try to read it with Python
#                     df = pd.read_scala(saved_file)
#                     res[item] = df
#                 except Exception as e:
#                     self.sos_kernel.warn(f'Failed to get dataset {item} from scala: {e}')
#         return res

#    def preview(self, item):
#        # put scala dataset to Python as dataframe
#         res = self.sos_kernel.get_response(f'macro list {item}', ('stream'))[0][1]['text']
#         if ':' in res:
#             return f'macro', res.split(':', 1)[-1].strip()
#         else:
#             return 'Unknown macro', ''


#    def sessioninfo(self):
#        # return information of the kernel
#        return self.sos_kernel.get_response('version', ('stream',))[0][1]['text']
