"""
pocketbase/models/abstracts/base_crud_service.py

declare abstract class BaseCrudService<M extends BaseModel> extends BaseService {
    /**
     * Response data decoder.
     */
    abstract decode(data: {
        [key: string]: any;
    }): M;
    /**
     * Returns a promise with all list items batch fetched at once.
     */
    protected _getFullList(basePath: string, batchSize?: number, queryParams?: {}): Promise<Array<M>>;
    /**
     * Returns paginated items list.
     */
    protected _getList(basePath: string, page?: number, perPage?: number, queryParams?: {}): Promise<ListResult<M>>;
    /**
     * Returns single item by its id.
     */
    protected _getOne(basePath: string, id: string, queryParams?: {}): Promise<M>;
    /**
     * Creates a new item.
     */
    protected _create(basePath: string, bodyParams?: {}, queryParams?: {}): Promise<M>;
    /**
     * Updates an existing item by its id.
     */
    protected _update(basePath: string, id: string, bodyParams?: {}, queryParams?: {}): Promise<M>;
    /**
     * Deletes an existing item by its id.
     */
    protected _delete(basePath: string, id: string, queryParams?: {}): Promise<boolean>;
}
"""
from abc import abstractclassmethod, abstractmethod
from typing import Optional, List
from .base_model import BaseModel
from .base_service import BaseService
from ..models import ListResult

class BaseCrudService(BaseModel, BaseService):
    @abstractclassmethod
    def decode(cls, data: dict):
        """
        Response data decoder.
        """
        pass
    
    @abstractmethod
    def _get_full_list(self, base_path: str, batch_size: Optional[int], query_params: Optional[dict] = {}) -> List:
        """
        Returns a promise with all list items batch fetched at once.
        """
        pass

    @abstractmethod
    def _get_list(self, base_path: str, page: Optional[int], per_page: Optional[int], query_params: Optional[dict] = {}) -> ListResult:
        """
        Returns paginated items list.
        """
        pass

    @abstractmethod
    def _get_one(self, base_path: str, id: str, query_params: Optional[dict] = {}):
        """
        Returns single item by its id.
        """
        pass
    
    @abstractmethod
    def _create(self, base_path: str, body_params: Optional[dict] = {}, query_params: Optional[dict] = {}):
        """
        Creates a new item.
        """
        pass
    
    @abstractmethod
    def _update(self, base_path: str, id: str, body_params: Optional[dict] = {}, query_params: Optional[dict] = {}):
        """
        Updates an existing item by its id.
        """
        pass
    
    @abstractmethod
    def _delete(self, base_path: str, id: str, query_params: Optional[dict] = {}) -> bool:
        """
        Deletes an existing item by its id.
        """
        pass
    
    
