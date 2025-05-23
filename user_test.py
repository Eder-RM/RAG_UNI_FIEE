import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from tokenizer import SimpleTokenizer

def main():
    tokenizer = SimpleTokenizer()
    print("Bienvenido al Tokenizer Simple CLI")
    while True:
        text = input("\nIngrese un texto para tokenizar (o 'salir' para terminar): ")
        if text.lower() == 'salir':
            print("Gracias por usar el tokenizer. ¡Hasta luego!")
            break
        ids = tokenizer.encode(text)
        unique_count = tokenizer.unique_token_count(text)
        decoded = tokenizer.decode(ids)
        print(f"IDs: {ids}")
        print(f"Cantidad de tokens únicos: {unique_count}")
        print(f"Texto reconstruido: {decoded}")

if __name__ == "__main__":
    main()

