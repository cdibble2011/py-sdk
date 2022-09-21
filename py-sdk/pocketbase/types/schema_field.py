"""
pocketbase/types/schema_field.py

declare class SchemaField {
    id: string;
    name: string;
    type: string;
    system: boolean;
    required: boolean;
    unique: boolean;
    options: {
        [key: string]: any;
    };
    constructor(data?: {
        [key: string]: any;
    });
    /**
     * Loads `data` into the field.
     */
    load(data: {
        [key: string]: any;
    }): void;
}
"""

import json
class SchemaField:
    def __init__(self, data: dict = None, **kwargs):
        self.id = ''
        self.name = ''
        self.type = ''
        self.system = False
        self.required = False
        self.unique = False
        self.options = {}
        if data:
            self.load(data)
        self.__dict__.update(kwargs)

    def load(self, data: dict):
        """
        Loads `data` into the field.

        load(data: { [key: string]: any }) {
            this.id = typeof data.id !== 'undefined' ? data.id : '';
            this.name = typeof data.name !== 'undefined' ? data.name : '';
            this.type = typeof data.type !== 'undefined' ? data.type : '';
            this.system = typeof data.system !== 'undefined' ? data.system : false;
            this.required = typeof data.required !== 'undefined' ? data.required : false;
            this.unique = typeof data.unique !== 'undefined' ? data.unique : false;
            this.options = typeof data.options !== 'undefined' ? data.options : {};
        }
        """
        self.id = data.get('id', '')
        self.name = data.get('name', '')
        self.type = data.get('type', '')
        self.system = data.get('system', False)
        self.required = data.get('required', False)
        self.unique = data.get('unique', False)
        self.options = data.get('options', {})

    def __repr__(self):
        return json.dumps(self.__dict__)

    def __str__(self):
        return json.dumps(self.__dict__)

    def to_dict(self):
        return self.__dict__
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(data)