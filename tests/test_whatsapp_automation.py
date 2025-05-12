import pytest 

from dotenv import load_dotenv
from pathlib import Path
import os
from time import sleep
from random import randint

from whatsapp_automation import Whatsapp

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

phone_number = os.getenv("PHONE_NUMBER")
group_id = "E6ln4qel6EoKrZy6S6Vg9k"

document_path = os.getenv("DOCUMENT_PATH")
image_path = os.getenv("IMAGE_PATH")

@pytest.fixture(scope="session")
def whatsapp():
    whatsapp = Whatsapp()
    assert whatsapp.login()
    yield whatsapp
    whatsapp.exit()

def test_go_to_group(whatsapp):
    sleep(randint(10,30))
    success = whatsapp.go_to_chat(group_id)
    sleep(randint(10,30))
    assert success is True

def test_send_message_group(whatsapp):
    sleep(randint(10,30))
    success = whatsapp.go_to_chat(group_id)
    success = whatsapp.send_message("Test message")
    sleep(randint(10,30))
    assert success is True

def test_send_document_group(whatsapp):
    sleep(randint(10,30))
    success = whatsapp.go_to_chat(group_id)
    success = whatsapp.send_document(document_path,"caption")
    sleep(randint(10,30))
    assert success is True

def test_send_image_group(whatsapp):
    sleep(randint(10,30))
    success = whatsapp.go_to_chat(group_id)
    success = whatsapp.send_photo_or_video(image_path,"caption")
    sleep(randint(10,30))
    assert success is True

# def test_go_to_phone_number(whatsapp):
#     sleep(randint(10,30))
#     success = whatsapp.go_to_chat(phone_number)
#     sleep(randint(10,30))
#     assert success is True

# def test_send_message_phone_number(whatsapp):
#     sleep(randint(10,30))
#     success = whatsapp.go_to_chat(phone_number)
#     success = whatsapp.send_message("Test message")
#     sleep(randint(10,30))
#     assert success is True

# def test_send_document_phone_number(whatsapp):
#     sleep(randint(10,30))
#     success = whatsapp.go_to_chat(phone_number)
#     success = whatsapp.send_document(document_path,"caption")
#     sleep(randint(10,30))
#     assert success is True

# def test_send_image_phone_number(whatsapp):
#     sleep(randint(10,30))
#     success = whatsapp.go_to_chat(phone_number)
#     success = whatsapp.send_photo_or_video(image_path,"caption")
#     sleep(randint(10,30))
#     assert success is True