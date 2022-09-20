"""
Base Crud Service

Source: https://github.com/pocketbase/js-sdk/blob/master/src/services/utils/BaseCrudService.ts
"""


"""
import BaseModel   from '@/models/utils/BaseModel';
import ListResult  from '@/models/utils/ListResult';
import BaseService from '@/services/utils/BaseService';
"""
from .base_service import BaseService
from ...models.utils import ListResult
from ...models.utils.base_model import BaseModel

class BaseCrudService(BaseService, BaseModel):
    """
    export default abstract class BaseCrudService<M extends BaseModel> extends BaseService {}
    """
    def __init__(self):
        super().__init__()
        """
        Response data decoder.
        
        abstract decode(data: { [key: string]: any }): M
        """
        self.decode = None

    def _get_full_list(self, base_path: str, batch_size: int = 100, query_params: dict = {}):
        """
        Returns a promise with all list items batch fetched at once.
        
        protected _getFullList(basePath: string, batchSize = 100, queryParams = {}): Promise<Array<M>> {
            var result: Array<M> = [];

            let request = async (page: number): Promise<Array<any>> => {
                return this._getList(basePath, page, batchSize, queryParams).then((list) => {
                    const castedList = (list as ListResult<M>);
                    const items = castedList.items;
                    const totalItems = castedList.totalItems;

                    result = result.concat(items);

                    if (items.length && totalItems > result.length) { return request(page + 1); }
                    return result;
                });
            }
            return request(1);
        }
        """
        result = []

        async def request(page=1):
            _list = await self._get_list(base_path, page, batch_size, query_params)
            casted_list = _list
            items = casted_list.items
            total_items = casted_list.total_items

            result = result + items

            if items and total_items > len(result):
                return await request(page + 1)

            return result

        return request(1)

    async def _get_list(self, base_path: str, page: int = 1, per_page: int = 30, query_params: dict = {}):
        """
        Returns paginated items list.
        
        protected _getList(basePath: string, page = 1, perPage = 30, queryParams = {}): Promise<ListResult<M>> {
            queryParams = Object.assign({
                'page':    page,
                'perPage': perPage,
            }, queryParams);

            return this.client.send(basePath, {
                'method': 'GET',
                'params': queryParams,
            }).then((responseData: any) => {
                const items: Array<M> = [];
                if (responseData?.items) {
                    responseData.items = responseData.items || [];
                    for (const item of responseData.items) {
                        items.push(this.decode(item));
                    }
                }

                return new ListResult<M>(
                    responseData?.page || 1,
                    responseData?.perPage || 0,
                    responseData?.totalItems || 0,
                    responseData?.totalPages || 0,
                    items,
                );
            });
        }
        """
        query_params = {
            'page': page,
            'perPage': per_page,
            **query_params
        }

        response_data = await self.client.send(base_path, {
            'method': 'GET',
            'params': query_params,
        })

        items = []
        if response_data.get('items'):
            response_data['items'] = response_data.get('items', [])
            for item in response_data['items']:
                items.append(self.decode(item))
                
        return ListResult(data = {
            'page': response_data.get('page', 1),
            'perPage': response_data.get('perPage', 0),
            'totalItems': response_data.get('totalItems', 0),
            'totalPages': response_data.get('totalPages', 0),
            'items': items,
        })

    async def _get_one(self, base_path: str, id, query_params: dict = {}):
        """
        Returns single item by its id.
        
        protected _getOne(basePath: string, id: string, queryParams = {}): Promise<M> {
            return this.client.send(basePath + '/' + encodeURIComponent(id), {
                'method': 'GET',
                'params': queryParams
            }).then((responseData: any) => this.decode(responseData));
        }
        """
        response_data = await self.client.send(base_path + '/' + id, {
            'method': 'GET',
            'params': query_params
        })
        return self.decode(response_data)

    async def _create(self, base_path: str, body_params: dict = {}, query_params: dict = {}):
        """
        Creates a new item.
        
        protected _create(basePath: string, bodyParams = {}, queryParams = {}): Promise<M> {
            return this.client.send(basePath, {
                'method': 'POST',
                'params': queryParams,
                'body':   bodyParams,
            }).then((responseData: any) => this.decode(responseData));
        }
        """
        response_data = await self.client.send(base_path, {
            'method': 'POST',
            'params': query_params,
            'body': body_params,
        })
        return self.decode(response_data)

    async def _update(self, base_path: str, id, body_params: dict = {}, query_params: dict = {}):
        """
        Updates an existing item by its id.
        
        protected _update(basePath: string, id: string, bodyParams = {}, queryParams = {}): Promise<M> {
            return this.client.send(basePath + '/' + encodeURIComponent(id), {
                'method': 'PATCH',
                'params': queryParams,
                'body':   bodyParams,
            }).then((responseData: any) => this.decode(responseData));
        }
        """
        response_data = await self.client.send(base_path + '/' + id, {
            'method': 'PATCH',
            'params': query_params,
            'body': body_params,
        })
        return self.decode(response_data)

    async def _delete(self, base_path: str, id, query_params: dict = {}):
        """
        Deletes an existing item by its id.
        
        protected _delete(basePath: string, id: string, queryParams = {}): Promise<boolean> {
            return this.client.send(basePath + '/' + encodeURIComponent(id), {
                'method': 'DELETE',
                'params': queryParams,
            }).then(() => true);
        }
        """
        await self.client.send(base_path + '/' + id, {
            'method': 'DELETE',
            'params': query_params,
        })
        return True
    
    def to_dict(self):
        raise NotImplementedError(f'{__class__}.to_dict() is not implemented!')

    def load(self):
        raise NotImplementedError(f'{__class__}.load() is not implemented!')

    def clone(self):
        raise NotImplementedError(f'{__class__}.clone() is not implemented!')
    
    def export(self):
        raise NotImplementedError(f'{__class__}.export() is not implemented!')
    