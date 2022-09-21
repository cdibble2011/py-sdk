"""
pocketbase/models/user.py

declare class User extends BaseModel {
    email: string;
    verified: boolean;
    lastResetSentAt: string;
    lastVerificationSentAt: string;
    profile: null | Record;
    /**
     * @inheritdoc
     */
    load(data: {
        [key: string]: any;
    }): void;
}
"""
from ..abstracts import BaseModel
from .record import Record


class User(BaseModel):
    def __init__(self, data: dict = {}):
        """
        constructor(data: { [key: string]: any } = {}) { this.load(data || {}); }
        """
        self.load(data or {})

    def __repr__(self):
        return f'<User {self.__dict__}>'

    def __str__(self):
        return f'<User {self.__dict__}>'

    def load(self, data: dict):
        """
        Loads `data` into the current model.
        
        load(data: { [key: string]: any }) {
            this.id = typeof data.id !== 'undefined' ? data.id : '';
            this.created = typeof data.created !== 'undefined' ? data.created : '';
            this.updated = typeof data.updated !== 'undefined' ? data.updated : '';
        }
        """
        self.email = data.get('email', None)
        self.verified = data.get('verified', None)
        self.last_reset_sent_at = data.get('lastResetSentAt', None)
        self.last_verification_sent_at = data.get('lastVerificationSentAt', None)
        self.profile = data.get('profile', None)
        self.id = data.get('id', None)
        self.created = data.get('created', None)
        self.updated = data.get('updated', None)
        self._base_dict = {
            'email': self.email,
            'verified': self.verified,
            'lastResetSentAt': self.last_reset_sent_at,
            'lastVerificationSentAt': self.last_verification_sent_at,
            'profile': self.profile,
            'id': self.id,
            'created': self.created,
            'updated': self.updated,
        }
        
    def clone(self):
        return User(self._base_dict)
    
    def export(self):
        return self._base_dict
        
    def to_dict(self):
        return self._base_dict
    
