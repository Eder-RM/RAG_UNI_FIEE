import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from text_processor import tokenize_and_count

def test_tokenize_and_count_basic():
    text = "hola fiee!"
    count = tokenize_and_count(text)
    assert count == 3, "Debe contar 3 tokens: 'hola', 'fiee', '!'"
