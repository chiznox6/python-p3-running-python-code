# testing/app_test.py
import os
from os import path
import subprocess

class TestAppPy:
    def test_app_py_exists(self):
        '''
        exists in lib directory
        '''
        assert path.exists("lib/app.py")

    def test_app_py_is_executable(self):
        '''
        is executable
        '''
        result = subprocess.run(["python3", "lib/app.py"], capture_output=True, text=True)
        assert result.returncode == 0

    def test_app_py_prints_hello_world(self):
        '''
        prints "Hello World! Pass this test, please."
        '''
        result = subprocess.run(["python3", "lib/app.py"], capture_output=True, text=True)
        assert result.stdout.strip() == "Hello World! Pass this test, please."
