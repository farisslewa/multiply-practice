'''
pytest code for testing multiply function inside multiply_backend.py file.
'''
from multiply_frontend import getmultiply
import pytest


payload = {"param1": 4,"param2":6}
def test_getmultiply():
    assert getmultiply(payload) == {'param1':4, 'param2':6, 'result':24}

if __name__ == '__main__':
  pytest.main()
