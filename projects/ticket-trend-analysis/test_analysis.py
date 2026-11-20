"""Run with: python -m unittest discover -s projects/ticket-trend-analysis -p 'test_*.py'"""
import unittest
from datetime import date
from pathlib import Path
from analyze_tickets import load_tickets, summarize


class TicketTrendTests(unittest.TestCase):
    def setUp(self):
        self.rows = load_tickets(Path(__file__).with_name('sample_tickets.csv'))

    def test_totals_and_recurrence(self):
        report = summarize(self.rows, as_of=date(2026, 10, 31))
        self.assertEqual(report['total'], 12)
        self.assertEqual(report['unresolved'], 8)
        self.assertIn(('Sync delayed', 3), report['repeated_symptoms'])
        self.assertEqual(report['aged_open'][0], ('T-101', 30))

    def test_empty_data(self):
        report = summarize([])
        self.assertEqual(report['total'], 0)
        self.assertEqual(report['repeated_symptoms'], [])

    def test_negative_aging_threshold(self):
        with self.assertRaises(ValueError):
            summarize([], aging_days=-1)


if __name__ == '__main__':
    unittest.main()
