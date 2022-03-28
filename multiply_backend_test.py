'''
pytest code for testing multiply function inside multiply_backend.py file.
'''
from multiply_backend import multiply
import pytest

def test_multiply():
    assert multiply(3,4) == {'param1': 3, 'param2': 4, 'result': 12}

if __name__ == '__main__':
  pytest.main()
