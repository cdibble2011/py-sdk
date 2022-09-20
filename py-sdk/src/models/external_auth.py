"""
External Auth Model

Source: https://github.com/pocketbase/js-sdk/blob/master/src/models/ExternalAuth.ts
"""

"""
import BaseModel from '@/models/utils/BaseModel';
"""
from .utils import BaseModel

class ExternalAuth(BaseModel):
    """
    export default class ExternalAuth extends BaseModel {
        userId!:     string;
        provider!:   string;
        providerId!: string;    
    }
    """
    def __init__(self, data: dict = {}): # user_id: str, provider: str, provider_id: str):
        self.load(data)

    def __repr__(self):
        return f'<ExternalAuth user_id={self.user_id} \
                               provider={self.provider} \
                               provider_id={self.provider_id}>'

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.user_id == other.user_id and \
               self.provider == other.provider and \
               self.provider_id == other.provider_id

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.user_id, self.provider, self.provider_id))

    def to_dict(self) -> dict:
        super().to_dict()
        return {
            'userId': self.user_id,
            'provider': self.provider,
            'providerId': self.provider_id,
            **self._base_dict
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        data['userId'] = data.get('userId', ''),
        data['provider'] = data.get('provider', ''),
        data['providerId'] = data.get('providerId', ''),
        return cls(data)
    
    def load(self, data: dict):
        """
        load(data: { [key: string]: any }) {
            super.load(data);

            this.userId     = typeof data.userId === 'string'     ? data.userId     : '';
            this.provider   = typeof data.provider === 'string'   ? data.provider   : '';
            this.providerId = typeof data.providerId === 'string' ? data.providerId : '';
        }
        """
        super().load(data)

        self.user_id = data.get('userId', '')
        self.provider = data.get('provider', '')
        self.provider_id = data.get('providerId', '')
        
    def clone(self) -> dict:
        """
        Robust deep clone of a model.
        clone(): BaseModel { return new (this.constructor as any)(JSON.parse(JSON.stringify(this))); }
        """
        return self.to_dict()

    def export(self) -> dict:
        """
        Exports all model properties as a new plain object.
        
        export(): { [key: string]: any } { return Object.assign({}, this); }
        """
        return self.to_dict()