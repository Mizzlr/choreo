from triton.client import TritonClient
import math


def test_basic():
    client = TritonClient()
    result = client.submit('math.sqrt', 5)
    assert result.get() == math.sqrt(5)
