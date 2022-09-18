"""
Collection Model

Source: https://github.com/pocketbase/js-sdk/blob/master/src/models/Collection.ts

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
        self.load(data or {})

    def load(self, data: dict):
        """
        /**
         * @inheritdoc
         */
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
        self.listRule = data.get('listRule', None)
        self.viewRule = data.get('viewRule', None)
        self.createRule = data.get('createRule', None)
        self.updateRule = data.get('updateRule', None)
        self.deleteRule = data.get('deleteRule', None)

        # schema
        self.schema = []
        for field in data.get('schema', []):
            self.schema.append(SchemaField(field))

    def to_dict(self):
        return {
            'name': self.name,
            'system': self.system,
            'listRule': self.listRule,
            'viewRule': self.viewRule,
            'createRule': self.createRule,
            'updateRule': self.updateRule,
            'deleteRule': self.deleteRule,
            'schema': [field.to_dict() for field in self.schema]
        }
