

from unittest import TestCase

from contact_app_functions import create_contact, clear_contacts


class TestContactApp(TestCase):


	def test_sample(self):

		self.assertEqual(90, 90)
		self.assertTrue(True)
		self.assertFalse(False)


	def test_that_new_contact_can_be_created(self):
		clear_contacts()

		first_name ="Daniel"
		last_name ="Messiah"
		phone_number ="09012344566"
		
		contact = create_contact(first_name,last_name,phone_number)

		self.assertEqual(type(contact), list)
		self.assertEqual(len(contact), 3)
		self.assertEqual("09012344566", contact [-1])
		
	def test_that_duplicate_contact_cannot_be _created(self):

		clear_contacts()
		
		first_name ="Jam"
		last_name ="job"
		phone_number ="09012344566"
	
		create_contact(first_name,last_name,phone_number)

		first_name ="James"
		last_name ="Methew"
		phone_number ="09012344566"
		
		create_contact(first_name,last_name,phone_number)

		self.assertIsNone(contact)
