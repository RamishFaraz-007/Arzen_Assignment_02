import unittest
import os
import subprocess


class TestLogParser(unittest.TestCase):

    def test_input_file_exists(self):
        self.assertTrue(os.path.exists("../Task_02/sample_logs.txt"))

    def test_parser_script_exists(self):
        self.assertTrue(os.path.exists("../Task_02/log_parser.py"))

    def test_parser_execution(self):

        result = subprocess.run(
            [
                "python",
                "../Task_02/log_parser.py",
                "../Task_02/sample_logs.txt"
            ],
            capture_output=True,
            text=True
        )

        self.assertEqual(result.returncode, 0)

    def test_output_csv_created(self):

        subprocess.run(
            [
                "python",
                "../Task_02/log_parser.py",
                "../Task_02/sample_logs.txt"
            ]
        )

        self.assertTrue(
            os.path.exists("../Task_02/output_parsed.csv")
        )

    def test_summary_message(self):

        result = subprocess.run(
            [
                "python",
                "../Task_02/log_parser.py",
                "../Task_02/sample_logs.txt"
            ],
            capture_output=True,
            text=True
        )

        self.assertIn(
            "Processing Complete",
            result.stdout
        )


if __name__ == "__main__":
    unittest.main()