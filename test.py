import unittest
from main import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_solve_endpoint(self):
        test_data = {'a': '100000', 'b': '20000', 'c': '5', 'd': '0.05'} # Пример значений для теста
        response = self.app.post('/solve', data=test_data)
        self.assertEqual(response.status_code, 200)
    def test_solve_endpoint1(self):
        test_data = {'a': '1000', 'b': '20000', 'c': '5', 'd': '0.05'} # Пример значений для теста
        response = self.app.post('/solve', data=test_data)
        self.assertEqual(response.status_code, 200)
    def test_solve_endpoint2(self):
        test_data = {'a': 'ddd', 'b': '20000', 'c': '5', 'd': '0.05'} # Пример значений для теста
        response = self.app.post('/solve', data=test_data)
        self.assertEqual(response.status_code, 200)
    def test_solve_endpoint3(self):
        test_data = {'a': '10000', 'b': 'ghh', 'c': '5', 'd': '0.05'} # Пример значений для теста
        response = self.app.post('/solve', data=test_data)
        self.assertEqual(response.status_code, 200)
    def test_solve_endpoint4(self):
        test_data = {'a': '1000', 'b': '20000', 'c': 'f', 'd': '0.05'} # Пример значений для теста
        response = self.app.post('/solve', data=test_data)
        self.assertEqual(response.status_code, 200)
    def test_solve_endpoint5(self):
        test_data = {'a': 'ddd', 'b': '20000', 'c': '5', 'd': '555'} # Пример значений для теста
        response = self.app.post('/solve', data=test_data)
        self.assertEqual(response.status_code, 200)




if __name__ == '__main__':
    unittest.main()