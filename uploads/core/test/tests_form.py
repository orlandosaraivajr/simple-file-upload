from django.test import TestCase, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from uploads.core.forms import DocumentForm

TINY_GIF = b'GIF89a\x01\x00\x01\x00\x00\xff\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x00;'

@override_settings(DEFAULT_FILE_STORAGE='inmemorystorage.InMemoryStorage')
class TestFormImage(TestCase):
    def setUp(self):
        self.data = {}
        self.data['description'] = 'Tiny Image'
        self.files = {}
        self.files['document'] = SimpleUploadedFile('file.txt', b"file_content")
        self.files['image'] = SimpleUploadedFile('tiny.gif', TINY_GIF)

        self.form = DocumentForm(self.data, self.files)
        self.form.is_valid()

    def test_valid_form(self):
        self.assertEqual(True, self.form.is_valid())

    def test_saved_document(self):
        self.assertEqual(self.files['document'], self.form.cleaned_data['document'])

    def test_saved_image(self):
        self.assertEqual(self.files['image'], self.form.cleaned_data['image'])