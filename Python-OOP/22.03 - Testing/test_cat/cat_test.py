from unittest import TestCase, main
from test_cat.cat import Cat
class CatTests(TestCase):

    def setUp(self):
        self.cat = Cat("Pancho")


    def test_cat_name(self):
        expected_name = "Pancho"
        self.assertEqual(expected_name, self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_cat_size_increase_after_eating(self):
        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_feed_cat_when_cat_already_fet(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_sleepy_cat_sleeps_and_its_not_sleepy(self):
        self.cat.sleepy = True
        self.cat.fed = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)

    def test_hundly_cat_sleep(self):

        self.cat.fed = False

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))



if __name__ == "__main__":
    main()