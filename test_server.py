import unittest
from unittest.mock import patch, MagicMock
import sys
import io

class TestServerStartup(unittest.TestCase):
    @patch('requests.get')
    def test_callback_with_requests(self, mock_get):
        """Test that the callback is sent using requests when available."""
        # Setup mock response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        # Capture stdout to prevent print statements from cluttering test output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        try:
            # Make sure server is not already imported
            if 'server' in sys.modules:
                del sys.modules['server']
                
            # Import server which will trigger the callback
            import server
            
            # Verify the callback was made with the correct URL
            mock_get.assert_called_once_with("https://toallo.com/callback")
            
        finally:
            # Reset stdout
            sys.stdout = sys.__stdout__
    
    @patch('requests.get')
    def test_callback_error_handling(self, mock_get):
        """Test that the server continues to run even if the callback fails."""
        # Setup mock to raise an exception
        mock_get.side_effect = Exception("Network error")
        
        # Reload the server module to trigger the callback again
        if 'server' in sys.modules:
            del sys.modules['server']
        
        # Capture stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        try:
            # Import server which will trigger the callback
            import server
            
            # Verify the hello message is still printed even after callback fails
            self.assertIn("hello", captured_output.getvalue())
            
        finally:
            # Reset stdout
            sys.stdout = sys.__stdout__
    
    @patch('requests.get', side_effect=ImportError("requests not available"))
    @patch('urllib.request.urlopen')
    def test_callback_with_urllib_fallback(self, mock_urlopen, mock_get):
        """Test that the callback falls back to urllib when requests is not available."""
        # Setup mock response for urllib
        mock_response = MagicMock()
        mock_response.getcode.return_value = 200
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response
        
        # Reload the server module to trigger the callback again
        if 'server' in sys.modules:
            del sys.modules['server']
        
        # Capture stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        try:
            # Import server which will trigger the callback
            import server
            
            # Verify urllib was used with the correct URL
            mock_urlopen.assert_called_once()
            self.assertEqual(mock_urlopen.call_args[0][0], "https://toallo.com/callback")
            
        finally:
            # Reset stdout
            sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()