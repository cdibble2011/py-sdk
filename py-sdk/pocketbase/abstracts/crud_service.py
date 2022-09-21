"""
pocketbase/models/abstracts/crud_service.py

declare abstract class CrudService<M extends BaseModel> extends BaseCrudService<M> {
    /**
     * Base path for the crud actions (without trailing slash, eg. '/admins').
     */
    abstract baseCrudPath(): string;
    /**
     * Returns a promise with all list items batch fetched at once.
     */
    getFullList(batchSize?: number, queryParams?: {}): Promise<Array<M>>;
    /**
     * Returns paginated items list.
     */
    getList(page?: number, perPage?: number, queryParams?: {}): Promise<ListResult<M>>;
    /**
     * Returns single item by its id.
     */
    getOne(id: string, queryParams?: {}): Promise<M>;
    /**
     * Creates a new item.
     */
    create(bodyParams?: {}, queryParams?: {}): Promise<M>;
    /**
     * Updates an existing item by its id.
     */
    update(id: string, bodyParams?: {}, queryParams?: {}): Promise<M>;
    /**
     * Deletes an existing item by its id.
     */
    delete(id: string, queryParams?: {}): Promise<boolean>;
}
"""
from abc import abstractmethod
from typing import Optional, List
from .base_model import BaseModel
from .base_crud_service import BaseCrudService
from ..list_result import ListResult

class CrudService(BaseCrudService):
    @abstractmethod
    def base_crud_path(self) -> str:
        """
        Base path for the crud actions (without trailing slash, eg. '/admins').
        """
        pass
    
    @abstractmethod
    def get_full_list(self, batch_size: Optional[int] = None, query_params: Optional[dict] = None) -> List[BaseModel]:
        """
        Returns a promise with all list items batch fetched at once.
        """
        pass
    
    @abstractmethod
    def get_list(self, page: Optional[int] = None, per_page: Optional[int] = None, query_params: Optional[dict] = None) -> ListResult[BaseModel]:
        """
        Returns paginated items list.
        """
        pass
    
    @abstractmethod
    def get_one(self, id: str, query_params: Optional[dict] = None) -> List[BaseModel]:
        """
        Returns single item by its id.
        """
        pass
    
    @abstractmethod
    def create(self, body_params: Optional[dict] = None, query_params: Optional[dict] = None) -> List[BaseModel]:
        """
        Creates a new item..
        """
        pass
    
    @abstractmethod
    def update(self, id: str, body_params: Optional[dict] = None, query_params: Optional[dict] = None) -> List[BaseModel]:
        """
        Updates an existing item by its id.
        """
        pass

    @abstractmethod
    def delete(self, id: str, query_params: Optional[dict] = None) -> bool:
        """
        Deletes an existing item by its id.
        """
        pass
    
