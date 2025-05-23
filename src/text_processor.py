from tokenizer import SimpleTokenizer

def tokenize_and_count(text: str) -> int:
    tokenizer = SimpleTokenizer()
    tokens = tokenizer.encode(text)
    return len(tokens)
