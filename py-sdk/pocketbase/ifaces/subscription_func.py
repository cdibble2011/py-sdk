"""
pocketbase/ifaces/subscription_func.py

interface SubscriptionFunc {
    (data: MessageData): void;
}
"""
from .message_data import MessageData

class SubscriptionFunc:
    def __init__(self, data: MessageData):
        self.data = data