from typing import List, Tuple, Optional
from datetime import datetime
import copy

class ReconcileAccountsService:
    """
    Serviço responsável por realizar a conciliação de transações entre duas listas,
    considerando tolerância de até ±1 dia nas datas.

    Args:
        transactions_1 (List[List[str]]): Lista de transações de origem.
        transactions_2 (List[List[str]]): Lista de transações de comparação.

    Raises:
        TypeError: Caso os parâmetros não sejam listas de listas de strings.
    """

    DATE_FORMAT: str = "%Y-%m-%d"

    def __init__(self, transactions_1: List[List[str]], transactions_2: List[List[str]]) -> None:
        if not isinstance(transactions_1, list) or not isinstance(transactions_2, list):
            raise TypeError("As transações devem ser listas de listas de strings.")
        self._transactions_1 = copy.deepcopy(transactions_1)
        self._transactions_2 = copy.deepcopy(transactions_2)
        self._matched_indices_2 = set()

    def reconcile(self) -> Tuple[List[List[str]], List[List[str]]]:
        """
        Executa a conciliação entre as listas de transações.

        Returns:
            Tuple[List[List[str]], List[List[str]]]: Listas de transações anotadas com 'FOUND', 'MISSING' ou 'INVALID'.
        """
        for row1 in self._transactions_1:
            if self._validate_transaction(row1):
                if self._find_match(row1):
                    row1.append('FOUND')
                else:
                    row1.append('MISSING')
            else:
                row1.append('INVALID')

        for idx, row2 in enumerate(self._transactions_2):
            if self._validate_transaction(row2):
                status = 'FOUND' if idx in self._matched_indices_2 else 'MISSING'
                row2.append(status)
            else:
                row2.append('INVALID')

        return self._transactions_1, self._transactions_2

    def _find_match(self, row1: List[str]) -> bool:
        """
        Busca correspondência na lista de comparação com tolerância de ±1 dia.

        Args:
            row1 (List[str]): Transação a ser conciliada.

        Returns:
            bool: True se encontrado, False caso contrário.
        """
        date1 = self._parse_date(row1[0])
        if date1 is None:
            return False

        for idx, row2 in enumerate(self._transactions_2):
            if idx in self._matched_indices_2:
                continue

            date2 = self._parse_date(row2[0])
            if date2 is None:
                continue

            if self._is_match(date1, row1[1:], date2, row2[1:]):
                self._matched_indices_2.add(idx)
                return True
        return False

    def _parse_date(self, date_str: str) -> Optional[datetime]:
        """
        Converte uma string de data para objeto datetime.

        Args:
            date_str (str): Data em string.

        Returns:
            Optional[datetime]: Objeto datetime ou None em caso de falha.
        """
        try:
            return datetime.strptime(date_str, self.DATE_FORMAT)
        except (ValueError, TypeError):
            return None

    def _is_match(self, date1: datetime, data1: List[str], date2: datetime, data2: List[str]) -> bool:
        """
        Verifica correspondência entre duas transações.

        Args:
            date1 (datetime): Data da transação de origem.
            data1 (List[str]): Demais campos da transação de origem.
            date2 (datetime): Data da transação de comparação.
            data2 (List[str]): Demais campos da transação de comparação.

        Returns:
            bool: True se as transações correspondem, False caso contrário.
        """
        return abs((date1 - date2).days) <= 1 and data1 == data2

    def _validate_transaction(self, transaction: List[str]) -> bool:
        """
        Valida se a transação possui ao menos 4 campos.

        Args:
            transaction (List[str]): Transação.

        Returns:
            bool: True se válida, False caso contrário.
        """
        return isinstance(transaction, list) and len(transaction) >= 4
