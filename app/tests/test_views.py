from django.test import TestCase
from django.urls import reverse
from app.models import Student

class StudentShowViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Student.objects.create(sid = '6', name = "abcd", phone_number = "987463210", email = "abcd@abcd.com", standard = "12")

    #show
    def test_show_by_view_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_show_by_view_name(self):
        response = self.client.get(reverse('show'))
        self.assertEqual(response.status_code, 200)

    def test_show_by_view_template(self):
        response = self.client.get(reverse('show'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'show.html')


    #create_get
    def test_create_by_view_location_get(self):
        response = self.client.get('/create')
        self.assertEqual(response.status_code, 200)

    def test_create_by_view_name_get(self):
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 200)

    def test_create_by_view_template_get(self):
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create.html')

    #create_post
    def test_create_by_view_location_post(self):
        response = self.client.post('/create', {"sid" : '6', "name" : "abcd", "phone_number" : "987463210", "email" : "abcd@abcd.com", "standard" : "12"})
        self.assertEqual(response.status_code, 302)

    def test_create_by_view_name_post(self):
        response = self.client.post(reverse('create'), {"sid" : '6', "name" : "abcd", "phone_number" : "987463210", "email" : "abcd@abcd.com", "standard" : "12"})
        self.assertEqual(response.status_code, 302)

    def test_create_by_view_template_post(self):
        response = self.client.post(reverse('create'), {"sid" : '6', "name" : "abcd", "phone_number" : "987463210", "email" : "abcd@abcd.com", "standard" : "12"})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')


    #edit_get
    def test_edit_by_view_location_get(self):
        response = self.client.get('/edit')
        self.assertEqual(response.status_code, 200)

    def test_edit_by_view_name_get(self):
        response = self.client.get(reverse('edit'))
        self.assertEqual(response.status_code, 200)

    def test_edit_by_view_template_get(self):
        response = self.client.get(reverse('edit'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update.html')

    
    #edit_post
    def test_edit_by_view_location_post(self):
        response = self.client.post('/edit', {"sid" : "6"})
        self.assertEqual(response.status_code, 200)

    def test_edit_by_view_name_post(self):
        response = self.client.post(reverse('edit'), {"sid" : "6"})
        self.assertEqual(response.status_code, 200)

    def test_edit_by_view_template_post(self):
        response = self.client.post(reverse('edit'), {"sid" : "6"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit.html')

    #update
    def test_update_by_view_location(self):
        response = self.client.get('/update/6')
        self.assertEqual(response.status_code, 200)

    def test_update_by_view_name(self):
        response = self.client.get(reverse('update', args = ["6"]))
        self.assertEqual(response.status_code, 200)

    def test_update_by_view_template(self):
        response = self.client.get(reverse('update',  args = ["6"]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit.html')


    
    #delete_get
    def test_delete_by_view_location_get(self):
        response = self.client.get('/delete')
        self.assertEqual(response.status_code, 200)

    def test_delete_by_view_name_get(self):
        response = self.client.get(reverse('delete'))
        self.assertEqual(response.status_code, 200)

    def test_delete_by_view_template_get(self):
        response = self.client.get(reverse('delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete.html')

    
    #delete_post
    def test_delete_by_view_location_post(self):
        response = self.client.post('/delete', {"sid" : "6"})
        self.assertEqual(response.status_code, 302)

    def test_delete_by_view_name_post(self):
        response = self.client.post(reverse('delete'), {"sid" : "6"})
        self.assertEqual(response.status_code, 302)

    def test_delete_by_view_template_post(self):
        response = self.client.post(reverse('delete'), {"sid" : "6"})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
