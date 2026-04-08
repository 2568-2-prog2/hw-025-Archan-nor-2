import unittest
import requests

class TestAPI(unittest.TestCase):

    def test_call(self):
        url = "http://127.0.0.1:8080/roll_dice"

        data = {
            "probabilities":[0.2,0.2,0.2,0.2,0.1,0.1],
            "number_of_random":3
        }

        r = requests.get(url, json=data)

        self.assertEqual(r.status_code, 200)

        j = r.json()
        self.assertEqual(j["status"], "success")

if __name__ == "__main__":
    unittest.main()