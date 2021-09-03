from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})
        # form is not valid. 
        self.assertFalse(form.is_valid())
        # The error occurred on the name field 
        self.assertIn('name', form.errors.keys())
        # the specific error message is what we expect
        self.assertEqual(form.errors['name'][0], 'This field is required.')

        # field is not required
    def test_done_field_is_not_require(self):
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

        # That said we should write a test to ensure 
        # that the only fields that are displayed in the form 
        # are the name and done fields
    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
    