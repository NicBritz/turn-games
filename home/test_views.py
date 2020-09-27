from django.test import TestCase


class TestHomeViews(TestCase):
    # get index page response good
    def test_get_index_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")

    # return 404 if url incorrect
    def test_get_index_page_404(self):
        response = self.client.get("/afsd")
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")
