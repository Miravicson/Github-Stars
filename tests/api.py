import unittest
from repos.api import create_query



class CreateQueryTest(unittest.TestCase):


    def test_create_query(self):
        """
        Test that 
        """
        test_languages = ["Java", "Elixir"]
        min_stars = "20"

        expected_query = "stars:>20 language:Java language:Elixir"
        self.assertEqual(
            create_query(test_languages, min_stars),
            expected_query, "Expects query to be built from the language list and the number of stars" )