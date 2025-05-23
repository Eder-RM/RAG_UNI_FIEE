from src.tokenizer import SimpleTokenizer

def test_encode_basic():
    tokenizer = SimpleTokenizer()
    result = tokenizer.encode("Hola fiee!")
    # "hola", "fiee" y "!" son tokens separados
    assert result == [0, 1, 2], "Debe tokenizar palabras y signos como tokens separados"

def test_encode_case_insensitive():
    tokenizer = SimpleTokenizer()
    result1 = tokenizer.encode("Hola")
    result2 = tokenizer.encode("hola")
    assert result1 == result2, "Tokenización debe ser insensible a mayúsculas/minúsculas"

def test_decode_basic():
    tokenizer = SimpleTokenizer()
    # Primero codificamos para crear el vocabulario
    ids = tokenizer.encode("hola fiee !")
    text = tokenizer.decode(ids)
    assert text == "hola fiee !", "Decodificación debe reconstruir tokens separados por espacios"

def test_encode_multiple_calls():
    tokenizer = SimpleTokenizer()
    ids1 = tokenizer.encode("hola")
    ids2 = tokenizer.encode("fiee")
    # En segunda llamada "fiee" debe tener ID 1, porque "hola" fue 0
    assert ids1 == [0]
    assert ids2 == [1]

