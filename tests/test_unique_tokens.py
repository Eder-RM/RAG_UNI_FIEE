import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from tokenizer import SimpleTokenizer

def test_unique_tokens_count():
    tokenizer = SimpleTokenizer()
    text = "hola fiee hola mundo"
    count = tokenizer.unique_token_count(text)  # Función NO implementada aún
    assert count == 3, "Debe contar 3 tokens únicos: 'hola', 'fiee', 'mundo'"
