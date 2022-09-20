"""
Admin Model

Source: https://github.com/pocketbase/js-sdk/blob/master/src/models/Admin.ts

import BaseModel from '@/models/utils/BaseModel';
"""
from .utils import BaseModel

class Admin(BaseModel):
    """
    export default class Admin extends BaseModel {
        avatar!:          number;
        email!:           string;
        lastResetSentAt!: string;
    }
    """
    def __init__(self, data: dict = {}):
        self.load(data)
        
    def __repr__(self):
        return f'<Admin avatar={self.avatar} \
                        email={self.email} \
                        last_reset_sent_at={self.last_reset_sent_at}>'

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.avatar == other.avatar and \
               self.email == other.email and \
               self.last_reset_sent_at == other.last_reset_sent_at

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.avatar, self.email, self.last_reset_sent_at))

    def to_dict(self) -> dict:
        super().to_dict()
        return {
            'avatar': self.avatar,
            'email': self.email,
            'lastResetSentAt': self.last_reset_sent_at,
            **self._base_dict
        }

    @classmethod
    def from_dict(cls, data: dict):
        data['avatar'] = data.get('avatar', 0)
        data['email'] = data.get('email', '')
        data['lastResetSentAt'] = data.get('lastResetSentAt', '')
        return cls(data)

    def load(self, data: dict):
        """
        load(data: { [key: string]: any }) {
            super.load(data);

            this.avatar = typeof data.avatar === 'number' ? data.avatar : 0;
            this.email  = typeof data.email  === 'string' ? data.email  : '';
            this.lastResetSentAt = typeof data.lastResetSentAt === 'string' ? data.lastResetSentAt : '';
        }
        """
        super().load(data)
        self.avatar = data.get('avatar', 0)
        self.email = data.get('email', '')
        self.last_reset_sent_at = data.get('lastResetSentAt', '')
        
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
        