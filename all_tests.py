import io
from contextlib import redirect_stdout

from mytests import py_gen_tests as pt


text_io = io.StringIO()
with redirect_stdout(text_io):
    pt.test_count_args(*[2, 3, [], '!'])

result = text_io.getvalue()
assert int(result) == 4