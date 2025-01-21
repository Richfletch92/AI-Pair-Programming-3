from django.test import TestCase
from .forms import TaskForm
from .models import Category, Task
from datetime import date

class TaskFormTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Work")
        self.valid_data = {
            'title': 'Complete project',
            'due_date': date.today(),
            'category': self.category.id,
        }
        self.invalid_data = {
            'title': '',
            'due_date': '',
            'category': '',
        }

    def test_task_form_valid(self):
        form = TaskForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_task_form_invalid(self):
        form = TaskForm(data=self.invalid_data)
        self.assertFalse(form.is_valid())

    def test_task_form_due_date_field(self):
        form = TaskForm()
        self.assertEqual(form.fields['due_date'].widget.attrs.get('type'), 'date')

    # def test_task_form_category_field(self):
    #     form = TaskForm()
    #     self.assertEqual(form.fields['category'].queryset.first(), self.category)
    #     self.assertEqual(form.fields['category'].queryset.count(), 1)
    #     self.assertEqual(form.fields['category'].queryset.get(id=self.category.id), self.category)