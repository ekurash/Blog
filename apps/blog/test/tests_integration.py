from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from selenium.webdriver.safari.webdriver import WebDriver

from apps.blog.models import Post


class ContactListIntegrationTests(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_contact_listed(self):
        User.objects.create(username='admin',
                            email='qwe@qwe.zxc', password='qwe123qwe')
        Post.objects.create(title='Lorem', content='ipsum')

        self.selenium.get('{}{}'.format(self.live_server_url, '/blog/'))
        self.assertEqual(
            self.selenium.find_elements_by_css_selector
            ('.post-title')[0].text.strip(), 'Lorem'
        )

    def test_add_contact_linked(self):
        self.selenium.get('{}{}'.format(self.live_server_url, '/blog/'))
        self.assert_(
            self.selenium.find_element_by_link_text('Add post')
        )
