
import unittest
import sqlite3
from src import db_handler as h
from src import db_countries_crud as c

class TestDbCountriesCrud(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        h.create_tables()
        h.seed_tables()

    @classmethod
    def tearDownClass(cls):
        h.drop_tables()

    def test_create_and_get_country(self):
        country_code_id = c.create_country(376, "IL", "ISR", "Israel")
        country = c.get_country(country_code_id)
        self.assertEqual(country[0][0], 376)
        self.assertEqual(country[0][1], "IL")
        self.assertEqual(country[0][2], "ISR")
        self.assertEqual(country[0][3], "Israel")

    def test_create_incomplete_country(self):
        with self.assertRaises(sqlite3.IntegrityError):
            c.create_country(country_code_id=None
                            , alpha_2=None
                            , alpha_3=None
                            , country=None
                            )     

    def test_validate_input(self):
        with self.assertRaises(ValueError):
            c.validate_input(country_code_id=None
                            , alpha_2=None
                            , alpha_3=None
                            , country=None
                            )
    
    def test_get_countries(self):
        countries = c.get_countries()
        self.assertGreaterEqual(len(countries), 8)

    def test_insert_duplicate_record_expect_failure(self):
        dupe = c.create_country(826, 'GB', 'GBR', 'United Kingdom of Great Britain and Northern Ireland (the)')
        self.assertEqual(dupe, 826)

    def test_update_record_expect_IntegrityError(self):
        with self.assertRaises(sqlite3.IntegrityError):
            c.update_country(country_code_id=826
                            , alpha_2="GBR"
                            , alpha_3=None
                            , country=None
                            )
            
    def test_update_incomplete_country_expect_IntegrityError(self):
        with self.assertRaises(sqlite3.IntegrityError):
            c.update_country(country_code_id=826
                             , alpha_2=None
                             , alpha_3=None
                             , country=None
                             )   
                             
    def test_update_duplicate_record_expect_failure(self):
        with self.assertRaises(sqlite3.IntegrityError):
            # Update UK to France
            c.update_country(826, 'FR', 'FRA', 'France')
            # If no error occurred, fail the test
            self.fail("Expected sqlite3.IntegrityError was not raised")

    def test_delete_country(self):
        country_code_id = c.create_country(710, "ZA", "ZAF", "South Africa")
        d = c.delete_country(country_code_id)
        country = c.get_country(d)
        self.assertFalse(country)


if __name__ == '__main__':
    unittest.main()
