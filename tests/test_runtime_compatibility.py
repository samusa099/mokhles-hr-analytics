from __future__ import annotations

import unittest

import pandas as pd

from mokhles_hr_analytics import list_csv_tables, load_csv_table, load_master_sheet


class RuntimeCompatibilityTests(unittest.TestCase):
    """Verify the installed package can read its supported dataset formats."""

    def test_csv_catalog_contains_employee_master(self) -> None:
        tables = list_csv_tables()

        self.assertIn("01_Employee_Master_FY2025.csv", tables)
        self.assertGreaterEqual(len(tables), 13)

    def test_employee_csv_loads_with_expected_schema(self) -> None:
        frame = load_csv_table("01_Employee_Master_FY2025.csv", nrows=5)

        self.assertIsInstance(frame, pd.DataFrame)
        self.assertFalse(frame.empty)
        self.assertIn("Employee ID", frame.columns)
        self.assertIn("Department", frame.columns)

    def test_master_workbook_loads_with_openpyxl(self) -> None:
        frame = load_master_sheet("Employee Master", nrows=5)

        self.assertIsInstance(frame, pd.DataFrame)
        self.assertFalse(frame.empty)
        self.assertIn("Employee ID", frame.columns)

    def test_csv_path_traversal_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            load_csv_table("../requirements.txt")


if __name__ == "__main__":
    unittest.main()
