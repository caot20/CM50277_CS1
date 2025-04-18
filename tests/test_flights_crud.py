
import unittest
from src import db_handler as h
from src import db_flights_crud as c
from datetime import datetime, timedelta

class TestDbFlightsCrud(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        h.create_tables()
        h.seed_tables()

    @classmethod
    def tearDownClass(cls):
        h.drop_tables()

    def test_validate_insert_input(self):
        origin_date = datetime.now().isoformat()
        destination_date = (datetime.now() + timedelta(minutes=60)).isoformat()

        errors \
         , flight_number \
         , origin_id \
         , origin_scheduled_departure_time_utc \
         , destination_id \
         , destination_scheduled_arrival_time_utc \
         , scheduled_pilot_1 \
         , scheduled_pilot_2 = c.validate_insert_input( flight_number="TEST0"
                                                      , origin_id=1
                                                      , origin_scheduled_departure_time_utc=origin_date
                                                      , destination_id=2
                                                      , destination_scheduled_arrival_time_utc=destination_date
                                                      , scheduled_pilot_1=1
                                                      , scheduled_pilot_2=2
                                                      )
        self.assertEqual(errors, [])
        self.assertEqual(flight_number, "TEST0")
        self.assertEqual(origin_id, 1)
        self.assertEqual(origin_scheduled_departure_time_utc, origin_date)
        self.assertEqual(destination_id, 2)
        self.assertEqual(destination_scheduled_arrival_time_utc, destination_date)
        self.assertEqual(scheduled_pilot_1, 1)
        self.assertEqual(scheduled_pilot_2, 2)

    def test_validate_update_input(self):
        origin_date = datetime.now().isoformat()
        destination_date = (datetime.now() + timedelta(minutes=50)).isoformat()

        errors \
         , flight_id \
         , flight_number \
         , origin_id \
         , origin_scheduled_departure_time_utc \
         , destination_id \
         , destination_scheduled_arrival_time_utc \
         , scheduled_pilot_1 \
         , scheduled_pilot_2 = c.validate_update_input( flight_id=1
                                                      , flight_number="TEST1"
                                                      , origin_id=1
                                                      , origin_scheduled_departure_time_utc=origin_date
                                                      , destination_id=2
                                                      , destination_scheduled_arrival_time_utc=destination_date
                                                      , scheduled_pilot_1=1
                                                      , scheduled_pilot_2=2
                                                      )
        self.assertEqual(errors, [])
        self.assertEqual(flight_id, 1)
        self.assertEqual(flight_number, "TEST1")
        self.assertEqual(origin_id, 1)
        self.assertEqual(origin_scheduled_departure_time_utc, origin_date)
        self.assertEqual(destination_id, 2)
        self.assertEqual(destination_scheduled_arrival_time_utc, destination_date)
        self.assertEqual(scheduled_pilot_1, 1)
        self.assertEqual(scheduled_pilot_2, 2)

    def test_validate_get_flight_input(self):
        errors, flight_id = c.validate_get_flight_input(flight_id=1)
        
        self.assertEqual(errors, [])
        self.assertEqual(flight_id, 1)

    # def test_validate_get_flight_input_out_of_range(self):
    #     with self.assertRaises(ValueError):
    #         errors , flight_id = c.validate_get_flight_input(flight_id=99999)
    #     # Raise error if does not fail
    #     self.fail("Expected ValueError was not raised")

    def test_create_and_get_flight(self):
        origin_date = datetime.now().isoformat()
        destination_date = (datetime.now() + timedelta(minutes=50)).isoformat()
    
        flight_id = c.create_flight("TEST1", 1, origin_date, 2, destination_date, 1, 2)
        flight = c.get_flight(flight_id)
        self.assertEqual(flight[0][0], flight_id)
        self.assertEqual(flight[0][1], "TEST1")
        self.assertEqual(flight[0][2], "EGGD (BRS|1)")
        self.assertEqual(flight[0][3], origin_date)
        self.assertEqual(flight[0][4], "EHAM (AMS|2)")
        self.assertEqual(flight[0][5], destination_date)
        self.assertEqual(flight[0][6], "Amelia Earhart (Captain|1)")
        self.assertEqual(flight[0][7], "Chesley Sullenberger (First Officer|2)")

    def test_create_and_update_flight(self):
        origin_date = datetime.now().isoformat()
        destination_date = (datetime.now() + timedelta(minutes=50)).isoformat()
    
        flight_id = c.create_flight("TEST2", 1, origin_date, 2, destination_date, 1, 2)
        # Update Fields
        origin_date = (datetime.now() + timedelta(minutes=120)).isoformat()
        destination_date = (datetime.now() + timedelta(minutes=180)).isoformat()

        c.update_flight(flight_id=flight_id
                 , flight_number="TEST2.1"
                 , origin_id=2
                 , origin_scheduled_departure_time_utc=origin_date
                 , destination_id=1
                 , destination_scheduled_arrival_time_utc=destination_date
                 , scheduled_pilot_1=3
                 , scheduled_pilot_2=4
                 )

        flight = c.get_flight(flight_id)
        self.assertEqual(flight[0][0], flight_id)
        self.assertEqual(flight[0][1], "TEST2.1")
        self.assertEqual(flight[0][2], "EHAM (AMS|2)")
        self.assertEqual(flight[0][3], origin_date)
        self.assertEqual(flight[0][4], "EGGD (BRS|1)")
        self.assertEqual(flight[0][5], destination_date)
        self.assertEqual(flight[0][6], "Yuri Gagarin (Captain|3)")
        self.assertEqual(flight[0][7], "Manfred von Richthofen (First Officer|4)")        

    def test_create_and_delete_flight(self):
        origin_date = datetime.now().isoformat()
        destination_date = (datetime.now() + timedelta(minutes=50)).isoformat()
    
        flight_id = c.create_flight("TEST3", 1, origin_date, 2, destination_date, 1, 2)

        c.delete_flight(flight_id=flight_id)
        flight = c.get_flight(flight_id)
        self.assertFalse(flight)

if __name__ == '__main__':
    unittest.main()
