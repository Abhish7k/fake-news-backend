import unittest
import json
import time
from app import app


class FakeNewsDetectionTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_detect_fake_news(self):
        # Prepare test data
        test_data = {
            "article": "Daniel Greenfield, a Shillman Journalism Fellow at the Freedom Center, is a New York writer focusing on radical Islam. In the final stretch of the election, Hillary Rodham Clinton has gone to war with the FBI. The word unprecedented has been thrown around so often this election that it ought to be retired. But it’s still unprecedented for the nominee of a major political party to go war with the FBI. But that’s exactly what Hillary and her people have done. Coma patients just waking up now and watching an hour of CNN from their hospital beds would assume that FBI Director James Comey is Hillary’s opponent in this election. The FBI is under attack by everyone from Obama to CNN. Hillary’s people have circulated a letter attacking Comey."
        }
        expected_result = {"result": "Fake"}

        # Send a POST request to the /detect endpoint
        response = self.app.post(
            "/detect", data=json.dumps(test_data), content_type="application/json"
        )

        # Check if response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check if response data matches expected result
        actual_result = json.loads(response.data)
        self.assertEqual(
            actual_result,
            expected_result,
            "Test Case 1 Failed: Expected Fake, but got {}".format(
                actual_result["result"]
            ),
        )

    def test_detect_real_news(self):
        # Prepare test data
        test_data = {
            "article": "Kerry to go to Paris in gesture of sympathy,U.S. Secretary of State John F. Kerry said Monday that he will stop in Paris later this week, amid criticism that no top American officials attended Sunday’s unity march against terrorism. Kerry said he expects to arrive in Paris Thursday evening, as he heads home after a week abroad. He said he will fly to France at the conclusion of a series of meetings scheduled for Thursday in Sofia, Bulgaria. He plans to meet the next day with Foreign Minister Laurent Fabius and President Francois Hollande, then return to Washington. The visit by Kerry, who has family and childhood ties to the country and speaks fluent French, could address some of the criticism that the United States snubbed France in its darkest hour in many years."
        }
        expected_result = {"result": "Real"}

        # Send a POST request to the /detect endpoint
        response = self.app.post(
            "/detect", data=json.dumps(test_data), content_type="application/json"
        )

        # Check if response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check if response data matches expected result
        actual_result = json.loads(response.data)
        self.assertEqual(
            actual_result,
            expected_result,
            "Test Case 2 Failed: Expected Real, but got {}".format(
                actual_result["result"]
            ),
        )

    def test_invalid_input(self):
        # Send a POST request with invalid input
        response = self.app.post(
            "/detect", data=json.dumps({}), content_type="application/json"
        )

        # Check if response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check if response data contains "Something went wrong"
        self.assertIn(
            b"Something went wrong",
            response.data,
            "Test Case 3 Failed: Invalid input didn't return correct error message",
        )


if __name__ == "__main__":
    # Use the built-in test runner to display results
    print("Starting Tests...\n")
    start_time = time.time()

    test_suite = unittest.TestLoader().loadTestsFromTestCase(FakeNewsDetectionTest)
    test_runner = unittest.TextTestRunner(verbosity=2)
    results = test_runner.run(test_suite)

    end_time = time.time()

    # Display summary of test results
    print("\nTest Results Summary:")
    print(
        "Ran", results.testsRun, "tests in", round(end_time - start_time, 4), "seconds."
    )
    print("Successful:", results.testsRun - len(results.failures) - len(results.errors))
    print("Failures:", len(results.failures))
    print("Errors:", len(results.errors))
