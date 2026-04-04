class Message:
    message_counter = 1  # Class variable to track ID numbers

    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.id = Message.message_counter
        Message.message_counter += 1  # Increment counter for the next message

    def __str__(self):
        # Defines how the message looks when printed
        return f"({self.id}) {self.sender.username}: {self.content}"


class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []     # List to track users currently in the room
        self.messages = []  # List to store message history

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)

    def broadcast(self, sender, content):
        # Create a new Message object
        message = Message(sender, content)
        self.messages.append(message)
        print(message)  # "Broadcast" implies showing it to everyone right now

    def show_chat_history(self):
        print(f"\nChat History of {self.name}:")
        for msg in self.messages:
            print(msg)
        print()


class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None  # User starts with no chatroom

    def join_chatroom(self, chatroom):
        if self.chatroom:
            print(f"{self.username} is already in a chatroom.")
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"{self.username} joined {chatroom.name}")

    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.username} is not in any chatroom.")
        else:
            self.chatroom.remove_user(self)
            print(f"{self.username} left {self.chatroom.name}")
            self.chatroom = None

    def send_message(self, content):
        if not self.chatroom:
            print(f"{self.username} cannot send a message (not in a chatroom).")
        else:
            # Delegate the sending task to the chatroom
            self.chatroom.broadcast(self, content)


# --- Example Usage ---
if __name__ == "__main__":
    room = ChatRoom("Python Lounge")
    
    u1 = User("Alice")
    u2 = User("Bob")
    u3 = User("Charlie")

    u1.join_chatroom(room)
    u2.join_chatroom(room)

    u1.send_message("Hello everyone!")
    u2.send_message("Hi Alice!")

    u3.join_chatroom(room)
    u3.send_message("Hey guys, what's up?")

    room.show_chat_history()

    u1.leave_chatroom()
    u2.leave_chatroom()
    u3.leave_chatroom()