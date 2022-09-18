"""
External Auth Model

Source: https://github.com/pocketbase/js-sdk/blob/master/src/models/ExternalAuth.ts

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
    def __init__(self, user_id: str, provider: str, provider_id: str):
        self.user_id = user_id
        self.provider = provider
        self.provider_id = provider_id

    def __repr__(self):
        return f'<ExternalAuth user_id={self.user_id} provider={self.provider} provider_id={self.provider_id}>'

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.user_id == other.user_id and self.provider == other.provider and self.provider_id == other.provider_id

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.user_id, self.provider, self.provider_id))

    def to_dict(self):
        return {
            'userId': self.user_id,
            'provider': self.provider,
            'providerId': self.provider_id,
        }

    @staticmethod
    def from_dict(data):
        return ExternalAuth(
            data.get('userId', ''),
            data.get('provider', ''),
            data.get('providerId', ''),
        )
    
    def load(self, data: dict):
        """
        /**
         * @inheritdoc
         */
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