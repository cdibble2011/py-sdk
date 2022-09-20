"""
Schema Fields

Source: https://github.com/pocketbase/js-sdk/blob/master/src/models/utils/SchemaField.ts
"""

from abc import ABC, abstractmethod

class SchemaField(ABC):
    """
    export default class SchemaField {
        id!:       string;
        name!:     string;
        type!:     string;
        system!:   boolean;
        required!: boolean;
        unique!:   boolean;
        options!:  { [key: string]: any };
    }
    """
    def __init__(self, data: dict = {}):
        """
        constructor(data: { [key: string]: any } = {}) { this.load(data || {}); }
        """
        self.load(data or {})

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def load(self, data: dict):
        """
        Loads `data` into the field.
        
        load(data: { [key: string]: any }) {
            this.id       = typeof data.id !== 'undefined' ? data.id : '';
            this.name     = typeof data.name !== 'undefined' ? data.name : '';
            this.type     = typeof data.type !== 'undefined' ? data.type : 'text';
            this.system   = !!data.system;
            this.required = !!data.required;
            this.unique   = !!data.unique;
            this.options  = typeof data.options === 'object' && data.options !== null ? data.options : {};
        }
        """
        self.id = data.get('id', '')
        self.name = data.get('name', '')
        self.type = data.get('type', 'text')
        self.system = bool(data.get('system', False))
        self.required = bool(data.get('required', False))
        self.unique = bool(data.get('unique', False))
        self.options = data.get('options', {})

    @abstractmethod
    def to_dict(self):
        self._base_dict = {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'system': self.system,
            'required': self.required,
            'unique': self.unique,
            'options': self.options,
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.to_dict())

    def __getitem__(self, item):
        return self.to_dict()[item]

    def __setitem__(self, key, value):
        self.to_dict()[key] = value

    def __delitem__(self, key):
        del self.to_dict()[key]

    def __iter__(self):
        return iter(self.to_dict())

    def __len__(self):
        return len(self.to_dict())

    def __contains__(self, item):
        return item in self.to_dict()

    def __copy__(self):
        return self.to_dict()

    def __deepcopy__(self, memo):
        return self.to_dict()

    def __getstate__(self):
        return self.to_dict()

    def __setstate__(self, state):
        self.load(state)

    def __getnewargs__(self):
        return (self.to_dict(),)

    def __getnewargs_ex__(self):
        return (self.to_dict(),)

    def __reduce__(self):
        return self.__class__, (self.to_dict(),)

    def __reduce_ex__(self, protocol):
        return self.__class__, (self.to_dict(),)

    def __sizeof__(self):
        return self.to_dict().__sizeof__()
    