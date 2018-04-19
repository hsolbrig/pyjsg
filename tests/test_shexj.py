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
import unittest
from contextlib import redirect_stdout
from io import StringIO
from typing import Optional, TextIO

import os
import requests
import types
from dict_compare import compare_dicts
from jsonasobj import loads as jao_loads

from pyjsg.jsglib.jsg import loads as jsg_loads
from pyjsg.parser_impl.generate_python import parse

shexJSGSource = ""
shexTestRepository = "https://api.github.com/repos/shexSpec/shexTest/contents/schemas?ref=master"

shexTestJson = ""
# shexTestJson = "https://raw.githubusercontent.com/shexSpec/shexTest/2.0/schemas/" \
#                "1refbnode_with_spanning_PN_CHARS_BASE1.json"


# If there is a path here, we use the local ShExJ.jsg rather than the one on the github site
LOCAL_PARSER_IMAGE = os.path.join('jsg', 'ShExJ.jsg')

# You can't debug if you compile inline -- change to a static image if you have to test
# LOCAL_PARSER_IMAGE = None
USE_EXISTING_SHEX = True

STOP_ON_ERROR = False

# Files to skip until we reintroduce a manifest reader
skip = ['coverage.json', 'manifest.json']


def compare_json(j1: str, j2: str, log: TextIO) -> bool:
    """ Compare two JSON strings """
    d1 = jao_loads(j1)
    d2 = jao_loads(j2)
    return compare_dicts(d1._as_dict, d2._as_dict, file=log)


def validate_shexj_json(json_str: str, input_fname: str, mod: types.ModuleType) -> bool:
    """
    Validate json_str against ShEx Schema
    :param json_str: String to validate
    :param input_fname: Name of source file for error reporting
    :param mod: module context
    :return: True if pass
    """
    log = StringIO()
    shex_obj = jsg_loads(json_str, mod)
    if not shex_obj._is_valid(log):
        print("File: {} - ".format(input_fname))
        print(log.read())
        return False
    elif not compare_json(json_str, shex_obj._as_json, log):
        print("File: {} - ".format(input_fname))
        print(log.getvalue())
        print(shex_obj._as_json_dumps())
        return False
    return True


def validate_file(download_url: str, mod: types.ModuleType) -> bool:
    fname = download_url.rsplit('/', 1)[1]
    if fname not in skip:
        resp = requests.get(download_url)
        if resp.ok:
            return validate_shexj_json(resp.text, download_url, mod)
        else:
            print("Error {}: {}".format(resp.status_code, resp.reason))
            return False
    print("Skipping {}".format(download_url))
    return True


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


def validate_shex_schemas(mod: types.ModuleType) -> bool:
    if not shexTestJson:
        resp = requests.get(shexTestRepository)
        if resp.ok:
            if STOP_ON_ERROR:
                return all(validate_file(f['download_url'], mod) for f in resp.json() if f['name'].endswith('.json'))
            else:
                return all([validate_file(f['download_url'], mod) for f in resp.json() if f['name'].endswith('.json')])
        else:
            print("Error {}: {}".format(resp.status_code, resp.reason))
    else:
        return validate_file(shexTestJson, mod)
    return False


def download_shex_parser() -> None:
    """
    Download the ShExJ definition and transform it into python
    :return: Success indicator
    """
    if LOCAL_PARSER_IMAGE:
        with open(LOCAL_PARSER_IMAGE) as f:
            shexj_jsg = f.read()
    else:
        shexj_jsg = download_github_file(shexJSGSource)
    if shexj_jsg is not None:
        shexj_py = parse(shexj_jsg, shexJSGSource)
        if shexj_py is not None:
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'py', "ShExJ.py"), 'w') as shexj_src:
                shexj_src.write(shexj_py)


class ShExJValidationTestCase(unittest.TestCase):

    def test_shex_schema(self):
        if not USE_EXISTING_SHEX:
            download_shex_parser()
        import tests.test_jsglib.py.ShExJ as ShExJ
        with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'logs', 'test_shex_schema.log'), 'w') as logf:
            with redirect_stdout(logf):
                self.assertTrue(validate_shex_schemas(ShExJ))


if __name__ == '__main__':
    unittest.main()
