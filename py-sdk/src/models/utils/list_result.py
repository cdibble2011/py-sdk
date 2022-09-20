"""
List Result

Source: https://github.com/pocketbase/js-sdk/blob/master/src/models/utils/ListResult.ts

import BaseModel from './BaseModel';
"""

from .base_model import BaseModel

class ListResult(BaseModel):
    """
    export default class ListResult<M extends BaseModel> {
        page!: number;
        perPage!: number;
        totalItems!: number;
        totalPages!: number;
        items!: Array<M>;
    }
    """
    def __init__(self, data: dict = {}):
        """
        constructor(
            page: number,
            perPage: number,
            totalItems: number,
            totalPages: number,
            items: Array<M>,
        ) {
            this.page = page > 0 ? page : 1;
            this.perPage = perPage >= 0 ? perPage : 0;
            this.totalItems = totalItems >= 0 ? totalItems : 0;
            this.totalPages = totalPages >= 0 ? totalPages : 0;
            this.items = items || [];
        }
        """
        self.load(data)

    def __repr__(self):
        return f'<ListResult page={self.page} \
                             per_page={self.per_page} \
                             total_items={self.total_items} \
                             total_pages={self.total_pages} \
                             items={self.items}>'

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.page == other.page and \
               self.per_page == other.per_page and \
               self.total_items == other.total_items and \
               self.total_pages == other.total_pages and \
               self.items == other.items

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.page, self.per_page, self.total_items, self.total_pages, self.items))

    
    
    def load(self, data: dict):
        """
        load(data: { [key: string]: any }) {
            super.load(data);
            this.items = this.items.map((item: any) => new this.itemClass(item));
        }
        """
        super().load(data)
        self.page = data.get('page', 1)
        self.per_page = data.get('per_page', 0)
        self.total_items = data.get('total_items', 0)
        self.total_pages = data.get('total_pages', 0)
        self.items = data.get('items', [])
        
    def to_dict(self):
        return {
            'id': self.id,
            'created': self.created,
            'updated': self.updated,
            'page': self.page,
            'per_page': self.per_page,
            'total_items': self.total_items,
            'total_pages': self.total_pages,
            'items': self.items,
        }

    @classmethod
    def from_dict(cls, d: dict):
        return cls(d)
    
    def clone(self):
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
        