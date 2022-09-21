"""
pocketbase/models/base_model.py

declare abstract class BaseModel {
    id: string;
    created: string;
    updated: string;
    constructor(data?: {
        [key: string]: any;
    });
    /**
     * Loads `data` into the current model.
     */
    load(data: {
        [key: string]: any;
    }): void;
    /**
     * Returns whether the current loaded data represent a stored db record.
     */
    get isNew(): boolean;
    /**
     * Robust deep clone of a model.
     */
    clone(): BaseModel;
    /**
     * Exports all model properties as a new plain object.
     */
    export(): {
        [key: string]: any;
    };
}
"""
from abc import ABC, abstractmethod
import json

class BaseModel(ABC):
    def __init__(self, data: dict = None, **kwargs):
        self.id = ''
        self.created = ''
        self.updated = ''
        if data:
            self.load(data)
        self.__dict__.update(kwargs)

    @abstractmethod
    def load(self, data: dict):
        """
        Loads `data` into the current model.
        
        load(data: { [key: string]: any }) {
            this.id = typeof data.id !== 'undefined' ? data.id : '';
            this.created = typeof data.created !== 'undefined' ? data.created : '';
            this.updated = typeof data.updated !== 'undefined' ? data.updated : '';
        }
        """
        self.id = data.get('id', '')
        self.created = data.get('created', '')
        self.updated = data.get('updated', '')

    @property
    def is_new(self) -> bool:
        """
        Returns whether the current loaded data represent a stored db record.
        
        get isNew(): boolean {
            return (
                // id is not set
                !this.id ||
                // zero uuid value
                this.id === '00000000-0000-0000-0000-000000000000'
            );
        }
        """
        return not self.id or self.id == '00000000-0000-0000-0000-000000000000'

    @abstractmethod
    def clone(self):
        """
        Robust deep clone of a model.
        clone(): BaseModel { return new (this.constructor as any)(JSON.parse(JSON.stringify(this))); }
        """
        return self.__class__(self.export())

    @abstractmethod
    def export(self) -> dict:
        """
        Exports all model properties as a new plain object.
        
        export(): { [key: string]: any } { return Object.assign({}, this); }
        """
        return self.__dict__

    @abstractmethod
    def to_dict(self):
        return {
            'id': self.id,
            'created': self.created,
            'updated': self.updated
        }

    @classmethod
    def from_dict(cls, data: dict, **kwargs):
        return cls(data, **kwargs)

    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id} created={self.created} updated={self.updated})'

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.id == other.id and \
               self.created

    def to_json(self):
        return json.dumps(self._base_dict)
    
    @classmethod
    def from_json(cls, json_str: str):
        return cls.from_dict(json.loads(json_str))

