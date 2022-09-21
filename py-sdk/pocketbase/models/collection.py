"""
pocketbase/models/collection.py

declare class Collection extends BaseModel {
    name: string;
    schema: Array<SchemaField>;
    system: boolean;
    listRule: null | string;
    viewRule: null | string;
    createRule: null | string;
    updateRule: null | string;
    deleteRule: null | string;
    /**
     * @inheritdoc
     */
    load(data: {
        [key: string]: any;
    }): void;
}
"""
from ..abstracts import BaseModel
from ..types import SchemaField

class Collection(BaseModel):
    def __init__(self, data: dict = {}, **kwargs):
        """
        constructor(data: { [key: string]: any } = {}) { this.load(data || {}); }
        """
        self.load(data or {})

    def __repr__(self):
        return f'<Collection {self.__dict__}>'

    def __str__(self):
        return f'<Collection {self.__dict__}>'

    def load(self, data: dict):
        """
        Loads `data` into the current model.

        load(data: { [key: string]: any }) {
            super.load(data);
            this.name = typeof data.name !== 'undefined' ? data.name : '';
            this.schema = typeof data.schema !== 'undefined' ? data.schema : [];
            this.system = typeof data.system !== 'undefined' ? data.system : false;
            this.listRule = typeof data.listRule !== 'undefined' ? data.listRule : null;
            this.viewRule = typeof data.viewRule !== 'undefined' ? data.viewRule : null;
            this.createRule = typeof data.createRule !== 'undefined' ? data.createRule : null;
            this.updateRule = typeof data.updateRule !== 'undefined' ? data.updateRule : null;
            this.deleteRule = typeof data.deleteRule !== 'undefined' ? data.deleteRule : null;
        }
        """
        super().load(data)
        self.name = data.get('name', '')
        self.schema = [SchemaField(field) for field in data.get('schema', [])]
        self.system = data.get('system', False)
        self.list_rule = data.get('listRule', None)
        self.view_rule = data.get('viewRule', None)
        self.create_rule = data.get('createRule', None)
        self.update_rule = data.get('updateRule', None)
        self.delete_rule = data.get('deleteRule', None)
        self._base_dict = {
            'name': self.name,
            'schema': self.schema,
            'listRule': self.list_rule,
            'viewRule': self.view_rule,
            'createRule': self.create_rule,
            'updateRule': self.update_rule,
            'deleteRule': self.delete_rule,
            'id': self.id,
            'created': self.created,
            'updated': self.updated,
            }
        
    def clone(self):
        return Collection(self._base_dict)
    
    def export(self):
        return self._base_dict
        
    def to_dict(self):
        return self._base_dict
