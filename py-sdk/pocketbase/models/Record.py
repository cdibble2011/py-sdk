"""
pocketbase/models/record.py

declare class Record extends BaseModel {
    [key: string]: any;
    "@collectionId": string;
    "@collectionName": string;
    "@expand": {
        [key: string]: any;
    };
    /**
     * @inheritdoc
     */
    load(data: {
        [key: string]: any;
    }): void;
}
"""
from ..abstracts import BaseModel

class Record(BaseModel):
    def __init__(self, data: dict = {}):
        """
        constructor(data: { [key: string]: any } = {}) { this.load(data || {}); }
        """
        self.load(data or {})

    def __repr__(self):
        return f'<Record {self.__dict__}>'

    def __str__(self):
        return f'<Record {self.__dict__}>'

    def load(self, data: dict):
        """
        Loads `data` into the current model.
        
        load(data: { [key: string]: any }) {
            this.id = typeof data.id !== 'undefined' ? data.id : '';
            this.created = typeof data.created !== 'undefined' ? data.created : '';
            this.updated = typeof data.updated !== 'undefined' ? data.updated : '';
        }
        """
        self.collection_id = data.get('@collectionId', None)
        self.collection_name = data.get('@collectionName', None)
        self.expand = data.get('@expand', None)
        self.id = data.get('id', None)
        self.created = data.get('created', None)
        self.updated = data.get('updated', None)
        self._base_dict = {
            '@collectionId': self.collection_id,
            '@collectionName': self.collection_name,
            '@expand': self.expand,
            'id': self.id,
            'created': self.created,
            'updated': self.updated,
        }

    def clone(self):
        return Record(self._base_dict)
    
    def export(self):
        return self._base_dict
        
    def to_dict(self):
        return self._base_dict

    