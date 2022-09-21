"""
pocketbase/ifaces/message_data.py

interface MessageData {
    [key: string]: any;
    action: string;
    record: Record;
}
"""
from ..models import Record

class MessageData:
    def __init__(self, action: str = '', record: Record = None):
        self.action = action
        self.record = record