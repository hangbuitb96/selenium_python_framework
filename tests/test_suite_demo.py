import unittest
from tests.home.test_login import LoginTests
from tests.courses.test_register_course_csv_data import RegisterCourseCSVDataTests

# Get all tests from the test classes

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCourseCSVDataTests)

# Create a test suite combining all test classes
smoke_test = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smoke_test)