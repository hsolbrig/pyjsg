# Copyright (c) 2017, Mayo Clinic
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this
#     list of conditions and the following disclaimer.
#
#     Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#     Neither the name of the Mayo Clinic nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.
import os
import unittest
import types
from typing import Optional
import requests
from jsonasobj import loads as jao_loads
from dict_compare import compare_dicts

from jsglib.jsg import loads as jsg_loads
from jsglib.logger import Logger
from parser_impl.generate_python import parse
from tests.memlogger import MemLogger
import ShExJ

shexJSGSource = "https://api.github.com/repos/shexSpec/shexTest/contents/doc/ShExJ.jsg"
shexTestRepository = "https://api.github.com/repos/shexSpec/shexTest/contents/schemas"

# If there is a path here, we use the local ShExJ.jsg rather than the one on the github site
LOCAL_PARSER_IMAGE = os.path.join('jsg', 'ShExJ.jsg')
USE_STATIC_SHEXJ = True


def compare_json(j1: str, j2: str, log: Logger) -> bool:
    """ Compare two JSON strings """
    d1 = jao_loads(j1)
    d2 = jao_loads(j2)
    return compare_dicts(d1._as_dict, d2._as_dict, file=log)


def validate_shexj_json(json_str: str, input_fname: str, module: types.ModuleType) -> bool:
    """
    Validate json_str against ShEx Schema
    :param json_str: String to validate
    :param input_fname: Name of source file for error reporting
    :return: True if pass
    """
    log = MemLogger('\t')
    logger = Logger(log)
    shex_obj = jsg_loads(json_str, module)
    if not shex_obj._is_valid(logger):
        print("File: {} - ".format(input_fname))
        print(log.log)
        return False
    elif not compare_json(json_str, shex_obj._as_json, logger):
        print("File: {} - ".format(input_fname))
        print(log.log)
        return False
    return True


def validate_file(download_url: str, module: types.ModuleType) -> bool:
    print("Downloading {}".format(download_url))
    resp = requests.get(download_url)
    if resp.ok:
        return validate_shexj_json(resp.text, download_url, module)
    else:
        print("Error {}: {}".format(resp.status_code, resp.reason))
        return False


def download_github_file(github_url: str) -> Optional[str]:
    """
    Download the file in github_url
    :param github_url: github url to download
    :return: file contents if success, None otherwise
    """
    print("Downloading {}".format(github_url))
    resp = requests.get(github_url)
    if resp.ok:
        resp = requests.get(resp.json()['download_url'])
        if resp.ok:
            return resp.text
    print("Error {}: {}".format(resp.status_code, resp.reason))
    return None


def validate_shex_schemas(module: types.ModuleType) -> bool:
    resp = requests.get(shexTestRepository)
    if resp.ok:
        return all([validate_file(f['download_url'], module) for f in resp.json() if f['name'].endswith('.json')])

    print("Error {}: {}".format(resp.status_code, resp.reason))
    return False


def download_shex_parser() -> Optional[types.ModuleType]:
    """
    Download the ShExJ definition and transform it into python
    :return: ShExJ module if success
    """
    if LOCAL_PARSER_IMAGE:
        shexj_jsg = open(LOCAL_PARSER_IMAGE).read()
    else:
        shexj_jsg = download_github_file(shexJSGSource)
    if shexj_jsg is not None:
        shexj_py = parse(shexj_jsg, shexJSGSource)
        if shexj_py is not None:
            with open("ShExJ.py", 'w') as shexj_src:
                shexj_src.write(shexj_py)
            shex_module = types.ModuleType("<ShExJ>")
            exec(shexj_py, shex_module.__dict__)
            return shex_module
    return None


class ShExJValidationTestCase(unittest.TestCase):

    def test_shex_schema(self):
        if not USE_STATIC_SHEXJ:
            module = download_shex_parser()
        else:
            module = ShExJ
        if module is not None:
            self.assertTrue(validate_shex_schemas(module))

if __name__ == '__main__':
    unittest.main()
