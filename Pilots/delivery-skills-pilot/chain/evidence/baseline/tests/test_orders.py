import unittest

from src.orders import count_pending


class CountPendingTests(unittest.TestCase):
    def test_counts_legacy_pending_orders(self):
        self.assertEqual(count_pending([{'status': 'pending'}]), 1)

    def test_preserves_exact_status_matching(self):
        self.assertEqual(count_pending([{'status': 'closed'}, {'status': 'Pending'}]), 0)

    def test_empty_list(self):
        self.assertEqual(count_pending([]), 0)
