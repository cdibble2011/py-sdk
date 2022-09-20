"""
Collection Model

Source: https://github.com/pocketbase/js-sdk/blob/master/src/models/Collection.ts
"""

"""
import BaseModel   from '@/models/utils/BaseModel';
import SchemaField from '@/models/utils/SchemaField';
"""
from .utils import BaseModel, SchemaField

class Collection(BaseModel):
    """
    export default class Collection extends BaseModel {
        name!:       string;
        schema!:     Array<SchemaField>;
        system!:     boolean;
        listRule!:   null|string;
        viewRule!:   null|string;
        createRule!: null|string;
        updateRule!: null|string;
        deleteRule!: null|string;  
    }
    """
    def __init__(self, data: dict = {}):
        self.load(data)

    def load(self, data: dict):
        """
        load(data: { [key: string]: any }) {
            super.load(data);

            this.name   = typeof data.name === 'string' ? data.name : '';
            this.system = !!data.system;

            // rules
            this.listRule   = typeof data.listRule   === 'string' ? data.listRule   : null;
            this.viewRule   = typeof data.viewRule   === 'string' ? data.viewRule   : null;
            this.createRule = typeof data.createRule === 'string' ? data.createRule : null;
            this.updateRule = typeof data.updateRule === 'string' ? data.updateRule : null;
            this.deleteRule = typeof data.deleteRule === 'string' ? data.deleteRule : null;

            // schema
            data.schema = Array.isArray(data.schema) ? data.schema : [];
            this.schema = [];
            for (let field of data.schema) {
                this.schema.push(new SchemaField(field));
            }
        }
        """
        super().load(data)

        self.name = data.get('name', '')
        self.system = bool(data.get('system', False))

        # rules
        self.list_rule = data.get('listRule', None)
        self.view_rule = data.get('viewRule', None)
        self.create_rule = data.get('createRule', None)
        self.update_rule = data.get('updateRule', None)
        self.delete_rule = data.get('deleteRule', None)

        # schema
        self.schema = []
        for field in data.get('schema', []):
            self.schema.append(SchemaField(field))

    def to_dict(self) -> dict:
        super().to_dict()
        return {
            'name': self.name,
            'system': self.system,
            'listRule': self.list_rule,
            'viewRule': self.view_rule,
            'createRule': self.create_rule,
            'updateRule': self.update_rule,
            'deleteRule': self.delete_rule,
            'schema': [field.to_dict() for field in self.schema],
            **self._base_dict
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(data)

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