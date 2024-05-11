import io
from contextlib import redirect_stdout

from mytests import py_gen_tests as pt

text_io = io.StringIO()
with redirect_stdout(text_io):
    pt.test_count_args(2, 3, [], "!")
    text = text_io.getvalue()
if int(text) != 4:
    raise ValueError("Expected positive value.")
