import sys
import os
import csv
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.reconcile_accounts_service import ReconcileAccountsService


def read_csv(filepath: str) -> List[List[str]]:
    """
    Lê um arquivo CSV e retorna uma lista de listas de strings.

    Args:
        filepath (str): Caminho do arquivo CSV.

    Returns:
        List[List[str]]: Lista de linhas como listas de strings.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Arquivo '{filepath}' não encontrado.")

    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        return [row for row in reader if row]  # ignora linhas vazias


if __name__ == "__main__":
    """
    Script de exemplo para testar o ReconcileAccountsService lendo arquivos CSV.
    """

    transactions_1 = read_csv('data/transactions1.csv')
    transactions_2 = read_csv('data/transactions2.csv')

    reconciler = ReconcileAccountsService(transactions_1, transactions_2)
    reconciled_1, reconciled_2 = reconciler.reconcile()

    print("Transações reconciliadas (lista 1):")
    for trans in reconciled_1:
        print(trans)

    print("\nTransações reconciliadas (lista 2):")
    for trans in reconciled_2:
        print(trans)
