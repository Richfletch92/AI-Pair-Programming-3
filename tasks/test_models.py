from django.test import TestCase
from .models import Category, Task
from datetime import date

class TaskModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Work")
        self.task = Task.objects.create(
            title="Complete project",
            due_date=date.today(),
            completed=False,
            category=self.category
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, "Complete project")
        self.assertEqual(self.task.due_date, date.today())
        self.assertEqual(self.task.completed, False)
        self.assertEqual(self.task.category, self.category)

    def test_task_str(self):
        self.assertEqual(str(self.task), "Complete project")

    def test_task_due_date(self):
        self.assertEqual(self.task.due_date, date.today())

    def test_task_completed(self):
        self.assertEqual(self.task.completed, False)

    def test_task_category(self):
        self.assertEqual(self.task.category, self.category)
        self.assertEqual(self.category.task_set.first(), self.task)
        self.assertEqual(self.category.task_set.count(), 1)

    # generate a unit test taht checks for an error if the title is longer than 100 characters
    # def test_task_title_length(self):
    #     with self.assertRaises(ValueError):
    #         Task.objects.create(
    #             title="A" * 101,
    #             due_date=date.today(),
    #             completed=False,
    #             category=self.category
    #         )