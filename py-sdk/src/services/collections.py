"""
Collections Service

Source: https://github.com/pocketbase/js-sdk/blob/master/src/services/Collections.ts

import CrudService from '@/services/utils/CrudService';
import Collection  from '@/models/Collection';
"""
from typing import List
from .utils import CrudService
from ..models import Collection

class Collections(CrudService):
    """
    export default class Collections extends CrudService<Collection> {}
    """
    def __init__(self, client):
        super(Collections, self).__init__(client)

    def decode(self, data):
        """
        /**
         * @inheritdoc
         */
        decode(data: { [key: string]: any }): Collection {
            return new Collection(data);
        }
        """
        return Collection(data)

    def base_crud_path(self) -> str:
        """
        /**
         * @inheritdoc
         */
        baseCrudPath(): string {
            return '/api/collections';
        }
        """
        return '/api/collections'

    def import_collections(self, collections: List[Collection], delete_missing: bool = False,  query_params: dict = {}):
        """
        /**
         * Imports the provided collections.
         *
         * If `deleteMissing` is `true`, all local collections and schema fields,
         * that are not present in the imported configuration, WILL BE DELETED
         * (including their related records data)!
         */
        async import(collections: Array<Collection>, deleteMissing: boolean = false, queryParams = {}): Promise<true> {
            return this.client.send(this.baseCrudPath() + '/import', {
                'method': 'PUT',
                'params': queryParams,
                'body': {
                    'collections':  collections,
                    'deleteMissing': deleteMissing,
                }
            }).then(() => true);
        }
        """
        return self.client.send(self.base_crud_path() + '/import', {
            'method': 'PUT',
            'params': query_params,
            'body': {
                'collections':  collections,
                'deleteMissing': delete_missing,
            }
        }).then(lambda _: True)
