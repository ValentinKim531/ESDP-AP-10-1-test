from os.path import basename
from accounts.models import Account
from unittest.mock import patch
from django.test import TestCase
from django.contrib.auth import get_user_model
from chat.models import ChatRoom, ChatType, ChatMessage, ChatRoomMembership, File
from django.core.files.uploadedfile import SimpleUploadedFile

User = get_user_model()


class ChatRoomModelTestCase(TestCase):
    def setUp(self):
        self.user = Account.objects.create_user(username='testuser', password='testpass')
        self.room_private = ChatRoom.objects.create(name='Private Room', chat_type=ChatType.PRIVATE.name)
        self.room_group = ChatRoom.objects.create(name='Group Room', chat_type=ChatType.GROUP.name)

    def test_is_group_chat(self):
        self.assertFalse(self.room_private.is_group_chat())
        self.assertTrue(self.room_group.is_group_chat())

    def test_get_user_list(self):
        self.room_private.users.add(self.user)
        user_list = self.room_private.get_user_list()
        self.assertEqual(user_list, ['testuser'])


class ChatRoomMembershipModelTestCase(TestCase):
    def setUp(self):
        self.user = Account.objects.create_user(username='testuser', password='testpass')
        self.room = ChatRoom.objects.create(name='Test Room', chat_type=ChatType.PRIVATE.name)

    @patch('chat.models.logger.debug')
    def test_chatroommembership_creation_log(self, mock_debug):
        ChatRoomMembership.objects.create(user=self.user, chat_room=self.room)
        mock_debug.assert_called_once()


class ChatMessageModelTestCase(TestCase):
    def setUp(self):
        self.user = Account.objects.create_user(username='testuser', password='testpass')
        self.room = ChatRoom.objects.create(name='Test Room', chat_type=ChatType.PRIVATE.name)
        self.message = ChatMessage.objects.create(user=self.user, room=self.room, message='Hello, World!')

    def test_display_timestamp(self):
        format_timestamp = self.message.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        self.assertEqual(self.message.display_timestamp(), format_timestamp)


class FileModelTestCase(TestCase):
    def setUp(self):
        self.user = Account.objects.create_user(email='testuser@test.com', password='testpass2', username='testuser')
        self.room = ChatRoom.objects.create(name='Test Room 2', chat_type=ChatType.PRIVATE.name)

        dummy_file = SimpleUploadedFile("file.txt", b"file_content", content_type="text/plain")
        self.file_instance = File.objects.create(file=dummy_file, user=self.user, room=self.room)

    def test_file_upload(self):
        self.assertTrue(self.file_instance.file)
        self.assertEqual(self.file_instance.user, self.user)
        self.assertEqual(self.file_instance.room, self.room)

    def test_file_creation_time(self):
        self.assertIsNotNone(self.file_instance.uploaded_at)

    def test_file_string_representation(self):
        actual_filename = basename(self.file_instance.file.name)
        self.assertEqual(actual_filename, actual_filename)

    def test_related_files_with_chat_message(self):
        chat_message = ChatMessage.objects.create(user=self.user, room=self.room, message="Hello with a file!")
        chat_message.related_files.add(self.file_instance)
        self.assertIn(self.file_instance, chat_message.related_files.all())
