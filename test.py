import unittest


class TestBasic(unittest.TestCase):
    def setUp(self):
        # Load test data
        self.app = App(database='customers.json')

    def test_customer_count(self):
        self.assertEqual(len(self.app.customers), 100)

    def test_existence_of_customer(self):
        customer = self.app.get_customer(id='cfcd208495d565ef')
        self.assertEqual(customer.owner_name, "Leah")
        self.assertEqual(customer.owner_surname, "Yeskey")


if __name__ == '__main__':
    unittest.main()