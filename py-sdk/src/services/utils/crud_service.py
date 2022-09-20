"""
CRUD Service

Source: https://github.com/pocketbase/js-sdk/blob/master/src/services/utils/CrudService.ts
"""

"""
import ListResult      from '@/models/utils/ListResult';
import BaseModel       from '@/models/utils/BaseModel';
import BaseCrudService from '@/services/utils/BaseCrudService';
"""
from ...models import BaseModel, ListResult
from .base_crud_service import BaseCrudService


class CrudService(BaseCrudService, BaseModel):
    """
    export default abstract class CrudService<M extends BaseModel> extends BaseCrudService<M> {}
    """
    def __init__(self):
        super().__init__()
        """
        Base path for the crud actions (without trailing slash, eg. '/admins').
        
        abstract baseCrudPath(): string
        """
        self.base_crud_path = None

    def get_full_list(self, batch_size: int = 100, query_params: dict = {}):
        """
        Returns a promise with all list items batch fetched at once.
        
        getFullList(batchSize = 100, queryParams = {}): Promise<Array<M>> {
            return this._getFullList(this.baseCrudPath(), batchSize, queryParams);
        }
        """
        return self._get_full_list(self.base_crud_path(), batch_size, query_params)

    def get_list(self, page: int = 1, per_page: int = 30, query_params: dict = {}):
        """
        Returns paginated items list.
        
        getList(page = 1, perPage = 30, queryParams = {}): Promise<ListResult<M>> {
            return this._getList(this.baseCrudPath(), page, perPage, queryParams);
        }
        """
        return self._get_list(self.base_crud_path(), page, per_page, query_params)

    def get_one(self, id, query_params: dict = {}):
        """
        Returns single item by its id.
        
        getOne(id: string, queryParams = {}): Promise<M> {
            return this._getOne(this.baseCrudPath(), id, queryParams);
        }
        """
        return self._get_one(self.base_crud_path(), id, query_params)

    def create(self, body_params: dict = {}, query_params: dict = {}):
        """
        Creates a new item.
        
        create(bodyParams = {}, queryParams = {}): Promise<M> {
            return this._create(this.baseCrudPath(), bodyParams, queryParams);
        }
        """
        return self._create(self.base_crud_path(), body_params, query_params)

    def update(self, id, body_params: dict = {}, query_params: dict = {}):
        """
        Updates an existing item by its id.
        
        update(id: string, bodyParams = {}, queryParams = {}): Promise<M> {
            return this._update(this.baseCrudPath(), id, bodyParams, queryParams);
        }
        """
        return self._update(self.base_crud_path(), id, body_params, query_params)

    def delete(self, id, query_params: dict = {}):
        """
        Deletes an existing item by its id.
        
        delete(id: string, queryParams = {}): Promise<boolean> {
            return this._delete(this.baseCrudPath(), id, queryParams);
        }
        """
        return self._delete(self.base_crud_path(), id, query_params)