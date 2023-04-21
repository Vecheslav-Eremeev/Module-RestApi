from django.test import TestCase
from .models import Module
from .api.serializers import ModuleSerializer


class ModuleTestCase(TestCase):
    """Test module for Module model"""

    def setUp(self):
        self.module_1 = Module.objects.create(number=1, name='Module 1', description='This first module', slug='module_1')
        self.module_2 = Module.objects.create(number=2, name='Module 2', description='This second module', slug='module_2')

    def test_modile_model(self):
        first_module = Module.objects.get(name='Module 1')
        self.assertEqual(self.module_1, first_module)
        self.assertEqual(self.module_1.number, 1)
        self.assertEqual(self.module_1.name, 'Module 1')
        self.assertEqual(self.module_1.description, 'This first module')
        self.assertEqual(self.module_1.slug, 'module_1')

    def test_module_serializer(self):
        serializer = ModuleSerializer(self.module_1)
        self.assertEqual(serializer.data['number'], 1)
        self.assertEqual(serializer.data['name'], 'Module 1')
        self.assertEqual(serializer.data['description'], 'This first module')
        self.assertEqual(serializer.data['slug'], 'module_1')

    def test_module_list_view(self):
        response = self.client.get('/api/modules/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'Module 1')

    def test_module_detail_view(self):
        response = self.client.get(f'/api/modules/{self.module_1.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Module 1')

    def test_module_create_view(self):
        data = {'number': 3, 'name': 'Module 3', 'description': 'This third module', 'slug': 'module_3'}
        response = self.client.post('/api/modules/', data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Module.objects.count(), 3)
        self.assertEqual(Module.objects.get(id=3).name, 'Module 3')

    def test_module_update_view(self):
        data = {'number': 1, 'name': 'Updated Module 1', 'description': 'This updated module', 'slug': 'module_1'}
        response = self.client.put(f'/api/modules/{self.module_1.id}/', data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Module.objects.get(id=self.module_1.id).name, 'Updated Module 1')

    def test_module_delete_view(self):
        response = self.client.delete(f'/api/modules/{self.module_1.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Module.objects.count(), 1)
