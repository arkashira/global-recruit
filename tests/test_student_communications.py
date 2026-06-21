from student_communications import StudentCommunications, Message

def test_send_message():
    communications = StudentCommunications()
    message = communications.send_message("staff", "student", "Hello", "pending")
    assert message.id == 1
    assert message.sender == "staff"
    assert message.recipient == "student"
    assert message.content == "Hello"
    assert message.application_status == "pending"

def test_get_messages():
    communications = StudentCommunications()
    communications.send_message("staff", "student", "Hello", "pending")
    communications.send_message("staff", "student", "Hello again", "approved")
    messages = communications.get_messages()
    assert len(messages) == 2
    messages = communications.get_messages("pending")
    assert len(messages) == 1
    assert messages[0].application_status == "pending"

def test_send_notification():
    communications = StudentCommunications()
    message = Message(1, "staff", "student", "Hello", "pending")
    communications.send_notification(message)
    # No assertion, just checking it runs without error

def test_categorize_messages():
    communications = StudentCommunications()
    message1 = Message(1, "staff", "student", "Hello", "pending")
    message2 = Message(2, "staff", "student", "Hello again", "approved")
    message3 = Message(3, "staff", "student", "Hello once more", "pending")
    categorized_messages = communications.categorize_messages([message1, message2, message3])
    assert len(categorized_messages["pending"]) == 2
    assert len(categorized_messages["approved"]) == 1
