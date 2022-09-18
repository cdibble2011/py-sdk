"""
Record Model

Source: https://github.com/pocketbase/js-sdk/blob/master/src/models/Record.ts

import BaseModel from '@/models/utils/BaseModel';
"""
from .utils import BaseModel

class Record(BaseModel):
    """
    export default class Record extends BaseModel {
        [key: string]: any,

        '@collectionId'!:   string;
        '@collectionName'!: string;
        '@expand'!:         {[key: string]: any}; 
    }
    """
    def __init__(self, collection_id: str, collection_name: str, expand, **kwargs):
        self.collection_id = collection_id
        self.collection_name = collection_name
        self.expand = expand
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f'<Record collection_id={self.collection_id} collection_name={self.collection_name} expand={self.expand} **kwargs={self.__dict__}>'

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.collection_id == other.collection_id and self.collection_name == other.collection_name and self.expand == other.expand and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.collection_id, self.collection_name, self.expand, self.__dict__))

    def to_dict(self):
        return {
            '@collectionId': self.collection_id,
            '@collectionName': self.collection_name,
            '@expand': self.expand,
            **self.__dict__,
        }

    @staticmethod
    def from_dict(data):
        return Record(
            data.get('@collectionId', ''),
            data.get('@collectionName', ''),
            data.get('@expand', {}),
            **data,
        )

    def load(self, data: dict):
        """
        /**
         * @inheritdoc
         */
        load(data: { [key: string]: any }) {
            super.load(data);

            for (const [key, value] of Object.entries(data)) {
                this[key] = value;
            }

            // normalize common fields
            this['@collectionId']   = typeof data['@collectionId']   !== 'undefined' ? data['@collectionId']   : '';
            this['@collectionName'] = typeof data['@collectionName'] !== 'undefined' ? data['@collectionName'] : '';
            this['@expand']         = typeof data['@expand']         !== 'undefined' ? data['@expand']         : {};
        }
        """
        super().load(data)

        self.collection_id = data.get('@collectionId', '')
        self.collection_name = data.get('@collectionName', '')
        self.expand = data.get('@expand', {})