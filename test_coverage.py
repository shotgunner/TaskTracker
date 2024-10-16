import unittest
import coverage
from tests import TestTaskCLI

def run_tests_with_coverage():
    # Create a coverage object
    cov = coverage.Coverage()

    # Start measuring coverage
    cov.start()

    # Run the tests
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTaskCLI)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # Stop measuring coverage
    cov.stop()

    # Generate a report
    cov.report()

    # Optionally, generate an HTML report
    cov.html_report(directory='htmlcov')

if __name__ == '__main__':
    run_tests_with_coverage()
