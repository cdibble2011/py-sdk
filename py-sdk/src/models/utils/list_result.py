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
    def __init__(self, page: int, per_page: int, total_items: int, total_pages: int, items: list = []):
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
        if page > 0:
            self.page = page
        else:
            self.page = 1
        if per_page >= 0:
            self.per_page = per_page
        else:
            self.per_page = 0
        if total_items >= 0:
            self.total_items = total_items
        else:
            self.total_items = 0
        if total_pages >= 0:
            self.total_pages = total_pages
        else:
            self.total_pages = 0
        self.items = items

    def __repr__(self):
        return f'<ListResult page={self.page} per_page={self.per_page} total_items={self.total_items} total_pages={self.total_pages} items={self.items}>'

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.page == other.page and self.per_page == other.per_page and self.total_items == other.total_items and self.total_pages == other.total_pages and self.items == other.items

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.page, self.per_page, self.total_items, self.total_pages, self.items))

    def to_dict(self):
        return {
            'page': self.page,
            'per_page': self.per_page,
            'total_items': self.total_items,
            'total_pages': self.total_pages,
            'items': self.items,
        }

    @classmethod
    def from_dict(cls, d):
        return cls(
            d['page'],
            d['per_page'],
            d['total_items'],
            d['total_pages'],
            d['items'],
        )