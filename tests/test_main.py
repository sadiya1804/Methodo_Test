import unittest
from unittest.mock import patch
from datetime import datetime
from src.main import is_palindrome, say_goodbye, say_hello, main

class TestMainFunctions(unittest.TestCase):
    
    def test_palindrome_detection(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("kayak"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw"))
        
        self.assertFalse(is_palindrome("bonjour"))
        self.assertFalse(is_palindrome("python"))

    @patch('main.datetime')
    def test_greetings(self, mock_datetime):
        # Test morning greeting
        mock_datetime.now.return_value = datetime(2024, 1, 1, 9, 0)
        self.assertEqual(say_hello(), "Bonjour!")
        
        # Test afternoon greeting
        mock_datetime.now.return_value = datetime(2024, 1, 1, 19, 0)
        self.assertEqual(say_hello(), "Bonsoir!")
      
    @patch('builtins.input', side_effect=['hello', 'exit'])
    @patch('builtins.print')
    def test_mirror_feature(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("Vous avez écrit: hello")
          
    @patch('main.datetime')
    def test_goodbyes(self, mock_datetime):
        # Test morning goodbye
        mock_datetime.now.return_value = datetime(2024, 1, 1, 9, 0)
        self.assertEqual(say_goodbye(), "Bonne journée!")
        
        # Test afternoon goodbye
        mock_datetime.now.return_value = datetime(2024, 1, 1, 14, 0)
        self.assertEqual(say_goodbye(), "Bon aprés midi!")
        
        # Test evening goodbye
        mock_datetime.now.return_value = datetime(2024, 1, 1, 19, 0)
        self.assertEqual(say_goodbye(), "Bonne soirée!")
        
        # Test night goodbye
        mock_datetime.now.return_value = datetime(2024, 1, 1, 22, 0)
        self.assertEqual(say_goodbye(), "Bonne nuit!")

if __name__ == '__main__':
    unittest.main()
