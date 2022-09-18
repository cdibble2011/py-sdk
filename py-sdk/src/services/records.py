"""
Records Service

Source: https://github.com/pocketbase/js-sdk/blob/master/src/services/Records.ts

import SubCrudService from '@/services/utils/SubCrudService';
import Record         from '@/models/Record';
"""
from .utils import SubCrudService
from ..models import Record
from ..stores import default_decode, default_encode

from urllib.parse import urlparse

class Records(SubCrudService):
    """
    export default class Records extends SubCrudService<Record> {}
    """
    def __init__(self, client):
        super(Record, self).__init__(client)
        
    def decode(self, data):
        """
        /**
         * @inheritdoc
         */
        decode(data: { [key: string]: any }): Record {
            return new Record(data);
        }
        """
        return Record(data)
    
    def base_crud_path(self, collection_id_or_name: str):
        """
        /**
         * @inheritdoc
         */
        baseCrudPath(collectionIdOrName: string): string {
            return '/api/collections/' + encodeURIComponent(collectionIdOrName) + '/records';
        }
        """
        return '/api/collections/' + default_encode(collection_id_or_name) + '/records'
    
    def get_file_url(self, record: Record, filename: str, query_params: dict = {}) -> str:
        """
        /**
         * Builds and returns an absolute record file url.
         */
        getFileUrl(record: Record, filename: string, queryParams = {}): string {
            const parts = [];
            parts.push(this.client.baseUrl.replace(/\/+$/gm, ""))
            parts.push("api")
            parts.push("files")
            parts.push(record["@collectionId"])
            parts.push(record.id)
            parts.push(filename)
            let result = parts.join('/');

            if (Object.keys(queryParams).length) {
                const params = new URLSearchParams(queryParams);
                result += (result.includes("?") ? "&" : "?") + params;
            }

            return result
        }
        """
        parts = []
        parts.append(self.client.base_url.replace('/+$', ''))
        parts.append('api')
        parts.append('files')
        parts.append(record['@collectionId'])
        parts.append(record.id)
        parts.append(filename)
        result = '/'.join(parts)
        
        if len(query_params):
            params = urlparse(query_params)
            result += ('?' if '?' in result else '&') + params
        
        return result
        

