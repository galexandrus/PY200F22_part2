import unittest
from turbine import SteamTurbine


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.test_power = 100
        self.test_pressure = 127.5
        self.test_type = "Р"
        self.test_pk = 3
        self.turbine = SteamTurbine(self.test_power, self.test_pressure, self.test_type, self.test_pk)
        # self.turbine = SteamTurbine(100, 127.5, "Р", 3)

    def test_repr(self):
        test_string = f"{self.turbine.__class__.__name__}" \
                      f"({self.test_power}, {self.test_pressure}, \"{self.test_type}\", {self.test_pk})"
        self.assertEqual(repr(self.turbine), test_string, "method __repr__ don't work correctly")

    def test_type_getter(self):
        self.assertEqual(self.turbine.type_, self.test_type, "method type getter don't work correctly")

    def test_check_type(self):
        testing_string = "234"
        self.assertRaises(ValueError, self.turbine.check_type, testing_string)

    def test_check_pk(self):
        testing_pk1 = "josdf"
        with self.assertRaises(TypeError):
            self.turbine.check_pk(testing_pk1)
        testing_pk2 = 30
        turbine2 = SteamTurbine(self.test_power, self.test_pressure, "Т", self.test_pk)
        with self.assertRaises(ValueError):
            turbine2.check_pk(testing_pk2)

    def test_pk_getter(self):
        self.assertEqual(self.turbine.pk, self.test_pk, "method pk getter don't work correctly")

    def test_pk_setter(self):
        new_pk = self.test_pk + 5
        self.turbine.pk = new_pk
        self.assertEqual(self.turbine.pk, new_pk, "method pk setter don't work correctly")


if __name__ == '__main__':
    unittest.main()
