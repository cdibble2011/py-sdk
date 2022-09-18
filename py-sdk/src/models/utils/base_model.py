"""
Base Model

Source: https://github.com/pocketbase/js-sdk/blob/master/src/models/utils/BaseModel.ts
"""
from abc import ABC, abstractmethod

class BaseModel(ABC):
    """
    export default abstract class BaseModel {
        id!:      string;
        created!: string;
        updated!: string;
    }
    """
    def __init__(self, data: dict = {}):
        """
        constructor(data: { [key: string]: any } = {}) {
            this.load(data || {});
        }
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
        /**
         * Loads `data` into the current model.
         */
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
    @abstractmethod
    def is_new(self) -> bool:
        """
        /**
         * Returns whether the current loaded data represent a stored db record.
         */
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
        /**
         * Robust deep clone of a model.
         */
        clone(): BaseModel {
            return new (this.constructor as any)(JSON.parse(JSON.stringify(this)));
        }
        """
        return self.__class__(self.export())

    @abstractmethod
    def export(self) -> dict:
        """
        /**
         * Exports all model properties as a new plain object.
         */
        export(): { [key: string]: any } {
            return Object.assign({}, this);
        }
        """
        return self.__dict__
