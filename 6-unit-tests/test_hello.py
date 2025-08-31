from hello import hello

def test_hello():
  assert hello("Robert") == "hello, Robert"

def test_hello_default():
  assert hello() == "hello, world"