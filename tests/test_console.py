import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_create(self):
        # Test create command with valid class name
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd('create BaseModel')
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 36)  # Check if ID is printed

        # Test create command with invalid class name
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd('create InvalidClassName')
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

        # Add more test cases for create command

    def test_show(self):
        # Test show command with valid class name and ID
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd('show BaseModel {}'.format(valid_id))
            output = mock_stdout.getvalue().strip()
            self.assertIn('BaseModel', output)  # Check if correct object is printed

        # Test show command with invalid class name
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd('show InvalidClassName {}'.format(valid_id))
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

        # Add more test cases for show command

    def test_destroy(self):
        # Mocking the storage object's all method
        storage_mock = MagicMock()
        storage_mock.all.return_value = {'BaseModel.{}'.format(valid_id): MagicMock()}
        with patch('models.storage', storage_mock):
            # Test destroy command with valid class name and ID
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                self.console.onecmd('destroy BaseModel {}'.format(valid_id))
                output = mock_stdout.getvalue().strip()
                self.assertEqual(output, "")  # Check if output is empty (no confirmation message)

            # Test destroy command with invalid class name
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                self.console.onecmd('destroy InvalidClassName {}'.format(valid_id))
                output = mock_stdout.getvalue().strip()
                self.assertEqual(output, "** class doesn't exist **")

            # Add more test cases for destroy command

    def test_update(self):
        # Mocking the storage object's all method
        storage_mock = MagicMock()
        storage_mock.all.return_value = {'BaseModel.{}'.format(valid_id): MagicMock()}
        with patch('models.storage', storage_mock):
            # Test update command with valid class name, ID, attribute name, and attribute value
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                self.console.onecmd('update BaseModel {} name "New Name"'.format(valid_id))
                output = mock_stdout.getvalue().strip()
                self.assertEqual(output, "")  # Check if output is empty (no confirmation message)

            # Test update command with invalid class name
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                self.console.onecmd('update InvalidClassName {} name "New Name"'.format(valid_id))
                output = mock_stdout.getvalue().strip()
                self.assertEqual(output, "** class doesn't exist **")

            # Add more test cases for update command

    def test_all(self):
        # Mocking the storage object's all method
        storage_mock = MagicMock()
        storage_mock.all.return_value = {'BaseModel.{}'.format(valid_id): MagicMock()}
        with patch('models.storage', storage_mock):
            # Test all command with valid class name
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                self.console.onecmd('all BaseModel')
                output = mock_stdout.getvalue().strip()
                self.assertIn('BaseModel', output)  # Check if correct objects are printed

            # Test all command with invalid class name
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                self.console.onecmd('all InvalidClassName')
                output = mock_stdout.getvalue().strip()
                self.assertEqual(output, "** class doesn't exist **")

            # Add more test cases for all command

    def test_quit(self):
        # Test quit command
        with patch('sys.exit') as mock_exit:
            self.console.onecmd('quit')
            mock_exit.assert_called_once_with()

    def test_EOF(self):
        # Test EOF command
        with patch('sys.exit') as mock_exit:
            self.console.onecmd('EOF')
            mock_exit.assert_called_once_with()

    # Add more test methods as needed

if __name__ == '__main__':
    unittest.main()

