```python
# test_pnucleus.py: Unit Tests for P-Nucleus Core
import unittest
import sqlite3
from src.pnucleus_core import PNucleus

class TestPNucleus(unittest.TestCase):
    """Unit tests for P-Nucleus functionality."""
    
    def setUp(self):
        """Initialize P-Nucleus for testing."""
        self.nucleus = PNucleus(db_path="test_memory.db")
    
    def test_inference(self):
        """Test inference generates non-empty response."""
        response = self.nucleus.inference("Test input", max_length=20)
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0, "Inference response is empty")
    
    def test_memory_storage(self):
        """Test input/output is stored in memory database."""
        input_text = "Optimize route"
        self.nucleus.inference(input_text, max_length=20)
        
        with sqlite3.connect("test_memory.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT input_text FROM memory WHERE input_text = ?", (input_text,))
            result = cursor.fetchone()
            self.assertIsNotNone(result, "Input not stored in memory")
            self.assertEqual(result[0], input_text)
    
    def test_personality_update(self):
        """Test personality updates within valid range."""
        feedback = {"empathy": 0.2, "creativity": -0.1}
        updated = self.nucleus.update_personality(feedback)
        
        self.assertAlmostEqual(updated["empathy"], 0.9, places=2)
        self.assertAlmostEqual(updated["creativity"], 0.5, places=2)
        self.assertTrue(0.0 <= updated["empathy"] <= 1.0, "Empathy out of range")
    
    def tearDown(self):
        """Clean up test database."""
        import os
        if os.path.exists("test_memory.db"):
            os.remove("test_memory.db")

if __name__ == "__main__":
    unittest.main()
```