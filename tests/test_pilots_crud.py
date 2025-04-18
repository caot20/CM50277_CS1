
import unittest
from src import db_handler as h
from src import db_pilots_crud as c

class TestDbPilotsCrud(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        h.create_tables()
        h.seed_tables()

    @classmethod
    def tearDownClass(cls):
        h.drop_tables()

    def test_validate_insert_input(self):
        errors \
         , position \
         , name \
         , passport_number \
         , nationality = c.validate_insert_input( position=0
                                                , name="Test 001"
                                                , passport_number="TE1234567"
                                                , nationality="Test Nationality"
                                                )
        self.assertEqual(errors, [])
        self.assertEqual(position, 0)
        self.assertEqual(name, "Test 001")
        self.assertEqual(passport_number, "TE1234567")
        self.assertEqual(nationality, "Test Nationality")


    def test_validate_update_input(self):
         errors \
         , pilot_id \
         , position \
         , name \
         , passport_number \
         , nationality = c.validate_update_input( pilot_id = 1
                                                , position=0
                                                , name="Test 001"
                                                , passport_number="TE1234567"
                                                , nationality="Test Nationality"
                                                )
         self.assertEqual(errors, [])
         self.assertEqual(pilot_id, 1)
         self.assertEqual(position, 0)
         self.assertEqual(name, "Test 001")
         self.assertEqual(passport_number, "TE1234567")
         self.assertEqual(nationality, "Test Nationality")

    def test_validate_get_pilot_input(self):
        errors, pilot_id = c.validate_get_pilot_input(pilot_id=1)
        
        self.assertEqual(errors, [])
        self.assertEqual(pilot_id, 1)

    def test_create_and_get_pilot(self):
        pilot_id = c.create_pilot(pilot_position_id=0
                                 , name="Test 001"
                                 , passport_number="TE1234567"
                                 , nationality="Test Nationality"
                                 )
        pilot = c.get_pilot(pilot_id)

        self.assertEqual(pilot[0][0], pilot_id)
        self.assertEqual(pilot[0][1], "Captain (0)")
        self.assertEqual(pilot[0][2], "Test 001")
        self.assertEqual(pilot[0][3], "TE1234567")
        self.assertEqual(pilot[0][4], "Test Nationality")

    def test_create_and_update_pilot(self):

        pilot_id = c.create_pilot(pilot_position_id=0
                                 , name="Test 002"
                                 , passport_number="TE2234567"
                                 , nationality="Test Nationality 2"
                                 )

        c.update_pilot( pilot_id=pilot_id
                      , pilot_position_id=1
                      , name="Test 003"
                      , passport_number="TE2234567"
                      , nationality="Test Nationality 3"
                 )

        pilot = c.get_pilot(pilot_id)

        self.assertEqual(pilot[0][0], pilot_id)
        self.assertEqual(pilot[0][1], "First Officer (1)")
        self.assertEqual(pilot[0][2], "Test 003")
        self.assertEqual(pilot[0][3], "TE2234567")
        self.assertEqual(pilot[0][4], "Test Nationality 3")

    def test_create_and_delete_pilot(self):
        pilot_id = c.create_pilot(pilot_position_id=1
                                 , name="Test 004"
                                 , passport_number="TE4234567"
                                 , nationality="Test Nationality 4"
                                 )
    
        c.delete_pilot(pilot_id=pilot_id)
        pilot = c.get_pilot(pilot_id)
        self.assertFalse(pilot)

if __name__ == '__main__':
    unittest.main()
