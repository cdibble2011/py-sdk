"""
Sub CRUD Service

Source: https://github.com/pocketbase/js-sdk/blob/master/src/services/utils/SubCrudService.ts

import BaseModel       from '@/models/utils/BaseModel';
import ListResult      from '@/models/utils/ListResult';
import BaseCrudService from '@/services/utils/BaseCrudService';
"""

from typing import Any, Dict, List, Optional, Union
from pocketbase.api.models import BaseModel, ListResult
from .base_crud_service import BaseCrudService

class SubCrudService(BaseCrudService, BaseModel):
    """
    export default abstract class SubCrudService<M extends BaseModel> extends BaseCrudService<M> {}
    """
    def __init__(self):
        super().__init__()
        """
        /**
         * Base path for the crud actions (without trailing slash, eg. '/collections/{:sub}/records').
         */
        abstract baseCrudPath(sub: string): string
        """
        self.base_crud_path = None

    def getFullList(self, sub, batch_size: int = 100, query_params: dict = {}):
        """
        /**
         * Returns a promise with all list items batch fetched at once.
         */
        getFullList(sub: string, batchSize = 100, queryParams = {}): Promise<Array<M>> {
            return this._getFullList(this.baseCrudPath(sub), batchSize, queryParams);
        }
        """
        return self._getFullList(self.base_crud_path(sub), batch_size, query_params)

    def getList(self, sub, page: int = 1, per_page: int = 30, query_params: dict = {}):
        """
        /**
         * Returns paginated items list.
         */
        getList(sub: string, page = 1, perPage = 30, queryParams = {}): Promise<ListResult<M>> {
            return this._getList(this.baseCrudPath(sub), page, perPage, queryParams);
        }
        """
        return self._getList(self.base_crud_path(sub), page, per_page, query_params)

    def getOne(self, sub, id, query_params: dict = {}):
        """
        /**
         * Returns single item by its id.
         */
        getOne(sub: string, id: string, queryParams = {}): Promise<M> {
            return this._getOne(this.baseCrudPath(sub), id, queryParams);
        }
        """
        return self._getOne(self.base_crud_path(sub), id, query_params)

    def create(self, sub, body_params: dict = {}, query_params: dict = {}):
        """
        /**
         * Creates a new item.
         */
        create(sub: string, bodyParams = {}, queryParams = {}): Promise<M> {
            return this._create(this.baseCrudPath(sub), bodyParams, queryParams);
        }
        """
        return self._create(self.base_crud_path(sub), body_params, query_params)

    def update(self, sub, id, body_params: dict = {}, query_params: dict = {}):
        """
        /**
         * Updates an existing item by its id.
         */
        update(sub: string, id: string, bodyParams = {}, queryParams = {}): Promise<M> {
            return this._update(this.baseCrudPath(sub), id, bodyParams, queryParams);
        }
        """
        return self._update(self.base_crud_path(sub), id, body_params, query_params)
    
    
