import unittest
from models.reconcile_accounts_service import ReconcileAccountsService

class TestReconcileAccountsService(unittest.TestCase):

    def test_conciliation_found(self):
        # Arrange
        transactions1 = [["2023-01-01", "Dep", "100", "Payee"]]
        transactions2 = [["2023-01-02", "Dep", "100", "Payee"]]
        service = ReconcileAccountsService(transactions1, transactions2)

        # Act
        result1, result2 = service.reconcile()

        # Assert
        self.assertEqual(result1[0][-1], 'FOUND')
        self.assertEqual(result2[0][-1], 'FOUND')

    def test_invalid_transaction(self):
        # Arrange
        transactions1 = [["2023-01-01"]]
        transactions2 = [["2023-01-02", "Dep", "100", "Payee"]]
        service = ReconcileAccountsService(transactions1, transactions2)

        # Act
        result1, result2 = service.reconcile()

        # Assert
        self.assertEqual(result1[0][-1], 'INVALID')

if __name__ == "__main__":
    unittest.main()
