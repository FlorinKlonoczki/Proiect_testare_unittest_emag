import unittest
import HtmlTestRunner
from project_emag import test_emag_class


class MyTestSuite(unittest.TestCase):
    def test_suite(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(test_emag_class.TestEmag),
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Raport Test',
            report_name='raport teste',
        )
        runner.run(smoke_test)
