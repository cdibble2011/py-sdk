"""
pocketbase/models/list_result.py

declare class ListResult<M extends BaseModel> {
    page: number;
    perPage: number;
    totalItems: number;
    totalPages: number;
    items: Array<M>;
    constructor(page: number, perPage: number, totalItems: number, totalPages: number, items: Array<M>);
}
"""
from ..abstracts import BaseModel

class ListResult(BaseModel):
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
        self.load(data or {})

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
            this.page = typeof data.page !== 'undefined' ? data.page : 1;
            this.perPage = typeof data.perPage !== 'undefined' ? data.perPage : 0;
            this.totalItems = typeof data.totalItems !== 'undefined' ? data.totalItems : 0;
            this.totalPages = typeof data.totalPages !== 'undefined' ? data.totalPages : 0;
            this.items = typeof data.items !== 'undefined' ? data.items : [];
        }
        """
        self.id = data.get('id', None)
        self.created = data.get('created', None)
        self.updated = data.get('updated', None)
        self.page = data.get('page', 1)
        self.per_page = data.get('perPage', 0)
        self.total_items = data.get('totalItems', 0)
        self.total_pages = data.get('totalPages', 0)
        self.items = data.get('items', [])
        self._base_dict = {
            'page': self.avatar,
            'perPage': self.email,
            'totalItems': self.last_reset_sent_at,
            'totalPages': self.last_reset_token,
            'items': self.items,
            'id': self.id,
            'created': self.created,
            'updated': self.updated,
        }

    def clone(self):
        return ListResult(self._base_dict)
    
    def export(self):
        return self._base_dict
        
    def to_dict(self):
        return self._base_dict
    
    

    
    


