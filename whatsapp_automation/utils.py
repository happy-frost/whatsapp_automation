from re import fullmatch
import  whatsapp_automation.exceptions as exceptions

def check_number(phone_no: str):
    if not fullmatch(r"^\+?[0-9]{2,4}\s?[0-9]{8,15}", phone_no):
        raise exceptions.InvalidPhoneNumber(phone_no)