"""
"""

import sys


def _open_or_stdin(path):
    """Returns a file named by 'path' opened for reading.
    If path is '-', stdin is returned.

    :param str path:
    :return: file opened for reading
    """
    if path == '-':
        return sys.stdin
    return open(path)

def _open_or_stdout(path):
    """Returns a file named by 'path' opened for writing.
    If path is '-', stdout is returned.
    
    :param str path:
    :return: file opened for writing
    """
    if path == '-':
        return sys.stdout
    return open(path, 'w')


class PyCat:
    """A simple cat replacement in python.
    """
    
    def __init__(self, files, number, nonblank, show_end, show_tabs):
        """
        :param List[str] files:
        :param bool number:
        :param bool nonblank:
        :param bool show_end:
        :param bool show_tabs:
        """
        if len(files) == 0:
            self.files = [sys.stdin]
        else:
            self.files = [_open_or_stdin(f) for f in files]
            
        self.number = number
        self.nonblank = nonblank
        self.end = '$\n' if show_end else '\n'
        self.show_tabs = show_tabs
        self.lineno = 0

    def _dump(self, stream_in, stream_out):
        """Dumps stream_in to stream_out while applying options
        to the output.

        :param file stream_in:
        :param file stream_out:
        :return" None
        """
        
        for line in stream_in.readlines():
            
            line = line.strip()
            blank = len(line) == 0
            
            if not blank and self.nonblank:
                self.lineno += 1
                
            if self.number and not self.nonblank:
                self.lineno += 1
            
            if self.show_tabs:
                line = line.replace('\t', '^I')

            if self.number or (not blank and self.nonblank):
                line = f"{self.lineno:6d}  {line}"

            print(line, file=stream_out, end=self.end)


    def __iter__(self):
        """Returns a iterator over a list of files opened for reading.
        """
        self.lineno = 0
        return iter(self.files)

    def __call__(self, output='-'):
        """Write all files to output.

        :param str output: 
        """

        output = _open_or_stdout(output)

        for file_ in self:
            self._dump(file_, output)
            
            
        
        
