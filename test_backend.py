import os
import unittest
from dotenv import load_dotenv
from app import app

class TestASLBackendPipeline(unittest.TestCase):
    def setUp(self):
        """Initializes application environment mapping parameters."""
        load_dotenv()
        self.app = app.test_client()
        self.app.testing = True

    def test_environment_variable_loading(self):
        """Verifies key environment metrics exist within local storage bounds."""
        api_key = os.getenv("VISION_API_KEY")
        self.assertIsNotNone(api_key, "CRITICAL ERROR: 'VISION_API_KEY' environment property configuration missing.")

    def test_base_index_route(self):
        """Validates entry UI routing templates load completely with no schema breaks."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_empty_payload_rejection(self):
        """Asserts bad gateway calls return explicit validation error codes."""
        response = self.app.post('/api/translate-frame', json={})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    print("Beginning validation sequence on target repo stubs...")
    unittest.main()