from django.test import TestCase, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from uploads.core.models import Document

TINY_GIF = b'GIF89a\x01\x00\x01\x00\x00\xff\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x00;'

@override_settings(DEFAULT_FILE_STORAGE='inmemorystorage.InMemoryStorage')
class TestFields(TestCase):
    def test_document_field(self):
        """document is an FileField"""
        Document.objects.create(document=SimpleUploadedFile('file.txt', b"file_content"))
        self.assertTrue(Document.objects.exists())

    def test_image_field(self):
        """Picture is an ImageField"""
        Document.objects.create(image=SimpleUploadedFile('tiny.gif', TINY_GIF))
        self.assertTrue(Document.objects.exists())