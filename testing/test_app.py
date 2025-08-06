from os import path

def test_app_py_exists():
    assert path.exists("lib/app.py")
