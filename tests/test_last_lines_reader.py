import unittest
import tempfile
import os
from models.last_lines_reader import LastLinesReader

class TestLastLinesReader(unittest.TestCase):
    """
    Testes para o serviço LastLinesReader.
    """

    def setUp(self) -> None:
        """
        Configura um arquivo temporário para testes.
        """
        # Arrange: Criar arquivo temporário com conteúdo conhecido
        self.test_file = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8')
        self.test_file.write("Line 1\nLine 2\nLine 3\n")
        self.test_file.close()

    def tearDown(self) -> None:
        """
        Remove o arquivo temporário após os testes.
        """
        os.unlink(self.test_file.name)

    def test_read_last_lines(self) -> None:
        """
        Testa se as linhas são lidas em ordem reversa, mantendo '\n'.
        """
        # Arrange
        reader = LastLinesReader(self.test_file.name)

        # Act
        lines = list(reader.read())

        # Assert
        expected_lines = ['Line 3\n', 'Line 2\n', 'Line 1\n']
        self.assertEqual(lines, expected_lines)

    def test_file_not_found(self) -> None:
        """
        Testa se FileNotFoundError é lançado para arquivo inexistente.
        """
        # Arrange
        reader = LastLinesReader("arquivo_inexistente.txt")

        # Act & Assert
        with self.assertRaises(FileNotFoundError):
            list(reader.read())

    def test_invalid_filepath_type(self) -> None:
        """
        Testa se TypeError é lançado quando filepath não é string.
        """
        # Arrange, Act & Assert
        with self.assertRaises(TypeError):
            LastLinesReader(123)

    def test_invalid_buffer_size(self) -> None:
        """
        Testa se ValueError é lançado para buffer_size inválido.
        """
        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            LastLinesReader(self.test_file.name, buffer_size=-1)

if __name__ == "__main__":
    unittest.main()
