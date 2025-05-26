import io
from typing import Iterator

class LastLinesReader:
    """
    Serviço para leitura reversa das linhas de um arquivo.

    Args:
        filepath (str): Caminho do arquivo.
        buffer_size (int): Tamanho do buffer para leitura.

    Raises:
        TypeError: Se filepath não for string ou buffer_size não for inteiro positivo.
        FileNotFoundError: Se o arquivo não for encontrado.
        IOError: Se houver erro ao ler o arquivo.
    """

    def __init__(self, filepath: str, buffer_size: int = io.DEFAULT_BUFFER_SIZE) -> None:
        if not isinstance(filepath, str):
            raise TypeError("filepath deve ser uma string.")
        if not isinstance(buffer_size, int) or buffer_size <= 0:
            raise ValueError("buffer_size deve ser um inteiro positivo.")
        self._filepath = filepath
        self._buffer_size = buffer_size

    def read(self) -> Iterator[str]:
        """
        Lê as linhas do arquivo em ordem reversa.

        Returns:
            Iterator[str]: Iterador sobre as linhas do arquivo, do final para o início.

        Raises:
            FileNotFoundError: Se o arquivo não for encontrado.
            IOError: Em caso de erro de leitura.
        """
        try:
            with open(self._filepath, 'rb') as file:
                file.seek(0, io.SEEK_END)
                position = file.tell()
                buffer = b''

                while position > 0:
                    read_size = min(self._buffer_size, position)
                    position -= read_size
                    file.seek(position)
                    buffer = file.read(read_size) + buffer

                    while b'\n' in buffer:
                        buffer, line = buffer.rsplit(b'\n', 1)
                        if line:  # evita linha vazia
                            yield line.decode('utf-8') + '\n'

                if buffer:
                    decoded_line = buffer.decode('utf-8')
                    if decoded_line:  # evita linha vazia
                        if not decoded_line.endswith('\n'):
                            decoded_line += '\n'
                        yield decoded_line

        except FileNotFoundError as e:
            raise FileNotFoundError(f"O arquivo {self._filepath} não foi encontrado.") from e
        except IOError as e:
            raise IOError(f"Erro ao ler o arquivo: {e}") from e
