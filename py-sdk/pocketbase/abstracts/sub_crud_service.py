"""
pocketbase/models/abstracts/sub_crud_service.py

declare abstract class SubCrudService<M extends BaseModel> extends BaseCrudService<M> {
    /**
     * Base path for the crud actions (without trailing slash, eg. '/collections/{:sub}/records').
     */
    abstract baseCrudPath(sub: string): string;
    /**
     * Returns a promise with all list items batch fetched at once.
     */
    getFullList(sub: string, batchSize?: number, queryParams?: {}): Promise<Array<M>>;
    /**
     * Returns paginated items list.
     */
    getList(sub: string, page?: number, perPage?: number, queryParams?: {}): Promise<ListResult<M>>;
    /**
     * Returns single item by its id.
     */
    getOne(sub: string, id: string, queryParams?: {}): Promise<M>;
    /**
     * Creates a new item.
     */
    create(sub: string, bodyParams?: {}, queryParams?: {}): Promise<M>;
    /**
     * Updates an existing item by its id.
     */
    update(sub: string, id: string, bodyParams?: {}, queryParams?: {}): Promise<M>;
    /**
     * Deletes an existing item by its id.
     */
    delete(sub: string, id: string, queryParams?: {}): Promise<boolean>;
}
"""
from abc import abstractmethod
from typing import Optional, List
from .base_model import BaseModel
from .base_crud_service import BaseCrudService
from ..list_result import ListResult

class SubCrudService(BaseCrudService):
    @abstractmethod
    def base_crud_path(self) -> str:
        """
        Base path for the crud actions (without trailing slash, eg. '/collections/{:sub}/records').
        """
        pass
    
    @abstractmethod
    def get_full_list(self, sub: str, batch_size: Optional[int] = None, query_params: Optional[dict] = None) -> List[BaseModel]:
        """
        Returns a promise with all list items batch fetched at once.
        """
        pass
    
    @abstractmethod
    def get_list(self, sub: str, page: Optional[int] = None, per_page: Optional[int] = None, query_params: Optional[dict] = None) -> ListResult[BaseModel]:
        """
        Returns paginated items list.
        """
        pass
    
    @abstractmethod
    def get_one(self, sub: str, id: str, query_params: Optional[dict] = None) -> List[BaseModel]:
        """
        Returns single item by its id.
        """
        pass
    
    @abstractmethod
    def create(self, sub: str, body_params: Optional[dict] = None, query_params: Optional[dict] = None) -> List[BaseModel]:
        """
        Creates a new item..
        """
        pass
    
    @abstractmethod
    def update(self, sub: str, id: str, body_params: Optional[dict] = None, query_params: Optional[dict] = None) -> List[BaseModel]:
        """
        Updates an existing item by its id.
        """
        pass

    @abstractmethod
    def delete(self, sub: str, id: str, query_params: Optional[dict] = None) -> bool:
        """
        Deletes an existing item by its id.
        """
        pass
    
