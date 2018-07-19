import os
import unittest
from contextlib import redirect_stdout
from io import StringIO
from typing import Optional, TextIO, cast

import requests
from dict_compare import compare_dicts
from jsonasobj import loads as jao_loads
from jsonasobj.jsonobj import as_dict, as_json

from pyjsg.validate_json import JSGPython

shexJSGSource = ""
# shexTestRepository = "https://api.github.com/repos/shexSpec/shexTest/contents/schemas?ref=master"
shexTestRepository = os.path.expanduser('~/Development/git/shexSpec/shexTest/schemas')

shexTestJson = ""

# If there is a path here, we use the local ShExJ.jsg rather than the one on the github site
LOCAL_PARSER_IMAGE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'jsg', 'ShExJ.jsg')

# You can't debug if you compile inline -- change to a static image if you have to test
# LOCAL_PARSER_IMAGE = None


STOP_ON_ERROR = False

# Files to skip until we reintroduce a manifest reader
skip = ['coverage.json', 'manifest.json']


def compare_json(j1: str, j2: str, log: TextIO) -> bool:
    """ Compare two JSON strings """
    d1 = jao_loads(j1)
    d2 = jao_loads(j2)
    return compare_dicts(as_dict(d1), as_dict(d2), file=log)


def validate_shexj_json(json_str: str, input_fname: str, parser: JSGPython) -> bool:
    """Validate json_str against ShEx Schema

    :param json_str: String to validate
    :param input_fname: Name of source file for error reporting
    :param parser: JSGPython parser
    :return: True if pass
    """
    rslt = parser.conforms(json_str, input_fname)
    if not rslt.success:
        print("File: {} - ".format(input_fname))
        print(str(rslt.fail_reason))
        return False
    else:
        log = StringIO()
        if not compare_json(json_str, as_json(parser.json_obj), cast(TextIO, log)):
            print("File: {} - ".format(input_fname))
            print(log.getvalue())
            print(as_json(parser.json_obj))
            return False
    return True


class FileValidator:
    def __init__(self):
        self.nvalidated = 0
        self.nskipped = 0

    def validate_file(self, download_file: str, parser: JSGPython) -> bool:
        fname = download_file.rsplit('/', 1)[1]
        if fname not in skip and 'futureWork' not in download_file:
            if '://' in download_file:
                resp = requests.get(download_file)
                if resp.ok:
                    text = resp.text
                else:
                    print("Error {}: {}".format(resp.status_code, resp.reason))
                    return False
            else:
                with open(download_file) as f:
                    text = f.read()
            self.nvalidated += 1
            return validate_shexj_json(text, download_file, parser)
        print("Skipping {}".format(download_file))
        self.nskipped += 1
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


def validate_shex_schemas(parser: JSGPython, validator: FileValidator) -> bool:
    if not shexTestJson:
        filelist = []
        if '://' in shexTestRepository:
            resp = requests.get(shexTestRepository)
            if resp.ok:
                filelist = [f['download_url'] for f in resp.json() if f['name'].endswith('.json')]
            else:
                print("Error {}: {}".format(resp.status_code, resp.reason))
                return False
        else:
            for dirpath, _, filenames in os.walk(shexTestRepository):
                filelist += [os.path.join(dirpath, f) for f in filenames if f.endswith('.json')]
        if STOP_ON_ERROR:
            return all(validator.validate_file(f, parser) for f in filelist)
        else:
            return all([validator.validate_file(f, parser) for f in filelist])
    else:
        return validator.validate_file(shexTestJson, parser)


class ShExJValidationTestCase(unittest.TestCase):

    @unittest.skipIf(False, "Schema tests disabled -- do not commit in this state")
    def test_shex_schema(self):
        parser = JSGPython(LOCAL_PARSER_IMAGE if LOCAL_PARSER_IMAGE else shexJSGSource)
        log_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'logs', 'test_shex_schema.log')
        validator = FileValidator()
        with open(log_path, 'w') as logf:
            with redirect_stdout(logf):
                self.assertTrue(validate_shex_schemas(parser, validator), f"See {log_path} for reasons")
        print(f"{validator.nvalidated} files validated - {validator.nskipped} skipped")


if __name__ == '__main__':
    unittest.main()
