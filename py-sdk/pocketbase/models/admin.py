"""
pocketbase/models/admin.py

declare class Admin extends BaseModel {
    avatar: number;
    email: string;
    lastResetSentAt: string;
    /**
     * @inheritdoc
     */
    load(data: {
        [key: string]: any;
    }): void;
}
"""
from ..abstracts import BaseModel


class Admin(BaseModel):
    def __init__(self, data: dict = {}, **kwargs):
        """
        constructor(data: { [key: string]: any } = {}) { this.load(data || {}); }
        """
        self.load(data or {})

    def __repr__(self):
        return f'<Admin {self.__dict__}>'

    def __str__(self):
        return f'<Admin {self.__dict__}>'

    def load(self, data: dict):
        """
        Loads `data` into the current model.
        
        load(data: { [key: string]: any }) {
            this.avatar = typeof data.avatar !== 'undefined' ? data.avatar : 0;
            this.email = typeof data.email !== 'undefined' ? data.email : '';
            this.lastResetSentAt = typeof data.lastResetSentAt !== 'undefined' ? data.lastResetSentAt : '';
        }
        """
        self.avatar = data.get('avatar', None)
        self.email = data.get('email', None)
        self.last_reset_sent_at = data.get('lastResetSentAt', None)
        self.id = data.get('id', None)
        self.created = data.get('created', None)
        self.updated = data.get('updated', None)
        self._base_dict = {
            'avatar': self.avatar,
            'email': self.email,
            'lastResetSentAt': self.last_reset_sent_at,
            'id': self.id,
            'created': self.created,
            'updated': self.updated,
        }
        
    def clone(self):
        return Admin(self._base_dict)
    
    def export(self):
        return self._base_dict
        
    def to_dict(self):
        return self._base_dict
