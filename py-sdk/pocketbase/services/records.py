"""
pocketbase/services/records.py

declare class Records extends SubCrudService<Record> {
    /**
     * @inheritdoc
     */
    decode(data: {
        [key: string]: any;
    }): Record;
    /**
     * @inheritdoc
     */
    baseCrudPath(collectionIdOrName: string): string;
    /**
     * Builds and returns an absolute record file url.
     */
    getFileUrl(record: Record, filename: string, queryParams?: {}): string;
}
"""

from typing import Optional, Dict, Any, List

from ..abstracts import SubCrudService
from ..models import Record

class Records(SubCrudService):
    def decode(self, data: Dict[str, Any]) -> Record:
        return self._decode(data, 'Collection')

    def base_crud_path(self, collection_or_id_name: str) -> str:
        return collection_or_id_name + '/' + 'records'

    def get_file_url(self, record: Record, filename: str, query_params: Optional[Dict[str, Any]] = None) -> str:
        """
        Builds and returns an absolute record file url.
        """
        return self._get_file_url(record, filename, query_params)