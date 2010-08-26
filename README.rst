AMF dump files for PyAMF_.

The included `parse_dump.py` script tries to parse a collection of raw AMF data
files and displays their content, which is useful when testing new
functionality and bugfixes in the PyAMF library.

Usage
-----

Parse all files in 'dumps' folder: `./parse_dump.py dumps/*`
Only parse '.amf0' files: `./parse_dump.py dumps/*.amf0`

.. _PyAMF: http://pyamf.org
