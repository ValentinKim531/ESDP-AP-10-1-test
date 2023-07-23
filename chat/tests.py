from accounts.models import Account
from unittest.mock import patch
from django.test import TestCase
from django.contrib.auth import get_user_model
from chat.models import ChatRoom, ChatType, ChatMessage, ChatRoomMembership

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
