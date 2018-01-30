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
from io import StringIO

from abc import ABC, abstractmethod
from typing import Optional, List, cast, IO, TextIO


class Logger:
    """
    Basic error recording utility.  Used for validation routines where callers may simply wish to know whether something
    is or isn't valid or, in other circumstances, may wish to see the detail of all of the violations.  The mode is
    controlled by the presence of logfile.  If it is present, errors are logged and all errors are recorded.  If
    absent, the fact that the error exists is noted.
    """
    def __init__(self, logfile: Optional[TextIO] = None):
        """
        Construct a logging instance
        :param logfile: File to log to.  If absent, no messages are recorded
        """
        self.nerrors = 0
        self._logfile = logfile

    def log(self, txt: str) -> bool:
        """
        Log txt (if any) to the log file (if any). Return value indicates whether it is ok to terminate on the first
        error or whether we need to continue processing.
        :param txt: text to log.
        :return: True if we aren't logging, False if we are.
        """
        self.nerrors += 1
        if self._logfile is not None:
            print(txt, file=self._logfile)
        return not self.logging

    @property
    def logging(self):
        """
        Return logging status
        :return: True if logging is occurring (meaning we want all errors) or False if we just want to find an error
        """
        return self._logfile is not None

