import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.last_lines_reader import LastLinesReader

if __name__ == "__main__":
    """
    Script de exemplo para executar a leitura reversa de um arquivo.
    """
    filepath = 'data/my_file.txt'
    reader = LastLinesReader(filepath)

    print("Linhas lidas do arquivo (em ordem reversa):")
    for line in reader.read():
        print(line, end='')
