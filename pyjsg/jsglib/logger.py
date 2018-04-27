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

