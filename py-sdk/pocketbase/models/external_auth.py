"""
pocketbase/models/external_auth.py

declare class ExternalAuth extends BaseModel {
    userId: string;
    provider: string;
    providerId: string;
    /**
     * @inheritdoc
     */
    load(data: {
        [key: string]: any;
    }): void;
}
"""
from ..abstracts import BaseModel

class ExternalAuth(BaseModel):
    def __init__(self, data: dict = None):
        """
        constructor(data: { [key: string]: any } = {}) { this.load(data || {}); }
        """
        self.load(data or {})
    def __repr__(self):
        return f'<ExternalAuth {self.__dict__}>'
    def __str__(self):
        return f'<ExternalAuth {self.__dict__}>'
    
    def load(self, data: dict):
        """
        Loads `data` into the current model.
        
        load(data: { [key: string]: any }) {
            this.userId = typeof data.userId !== 'undefined' ? data.userId : '';
            this.provider = typeof data.provider !== 'undefined' ? data.provider : '';
            this.providerId = typeof data.providerId !== 'undefined' ? data.providerId : '';
        }
        """
        self.user_id = data.get('userId', None)
        self.provider = data.get('provider', None)
        self.provider_id = data.get('providerId', None)
        self.id = data.get('id', None)
        self.created = data.get('created', None)
        self.updated = data.get('updated', None)
        self._base_dict = {
            'userId': self.user_id,
            'provider': self.provider,
            'providerId': self.provider_id,
            'id': self.id,
            'created': self.created,
            'updated': self.updated,
        }
        
    def clone(self):
        return ExternalAuth(self._base_dict)
    
    def export(self):
        return self._base_dict
        
    def to_dict(self):
        return self._base_dict
        
