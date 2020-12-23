from django.test import TestCase
from app.models import Student

class Test_Student_Model(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Student.objects.create(sid = '1', name = "abcd", phone_number = "98746321", email = "abcd@abcd.com", standard = "12")
    
    #sid
    def test_sid_label(self):
        student = Student.objects.get(sid = '1')
        field_label = Student._meta.get_field('sid').verbose_name
        self.assertEqual(field_label, 'sid')
       
    def test_sid_length(self):
        student = Student.objects.get(sid = '1')
        max_length = Student._meta.get_field('sid').max_length
        self.assertEqual(max_length, 100)


    #name
    def test_name_label(self):
        student = Student.objects.get(sid = '1')
        field_label = Student._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')
       
    def test_name_length(self):
        student = Student.objects.get(sid = '1')
        max_length = Student._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)
    

    #phone_number
    def test_phone_number_label(self):
        student = Student.objects.get(sid = '1')
        field_label = Student._meta.get_field('phone_number').verbose_name
        self.assertEqual(field_label, 'phone number')
       
    def test_phone_number_length(self):
        student = Student.objects.get(sid = '1')
        max_length = Student._meta.get_field('phone_number').max_length
        self.assertEqual(max_length, 100)

    #email
    def test_email_label(self):
        student = Student.objects.get(sid = '1')
        field_label = Student._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')
       
    

    #standard
    def test_standard_label(self):
        student = Student.objects.get(sid = '1')
        field_label = Student._meta.get_field('standard').verbose_name
        self.assertEqual(field_label, 'standard')
       
    def test_standard_length(self):
        student = Student.objects.get(sid = '1')
        max_length = Student._meta.get_field('standard').max_length
        self.assertEqual(max_length, 6)