from pyramid import testing

class TestViewClass():
    def setup_method(self, method):
        self.config = testing.setUp()

    def teardown_method(self, method):
        testing.tearDown()

    def test_my_view(self):
        from box.views import my_view
        request = testing.DummyRequest()
        info = my_view(request)
        assert info['project'] == 'box'
