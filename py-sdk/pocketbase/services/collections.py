"""
pocketbase/services/collections.py

declare class Collections extends CrudService<Collection> {
    /**
     * @inheritdoc
     */
    decode(data: {
        [key: string]: any;
    }): Collection;
    /**
     * @inheritdoc
     */
    baseCrudPath(): string;
    /**
     * Imports the provided collections.
     *
     * If `deleteMissing` is `true`, all local collections and schema fields,
     * that are not present in the imported configuration, WILL BE DELETED
     * (including their related records data)!
     */
    import(collections: Array<Collection>, deleteMissing?: boolean, queryParams?: {}): Promise<true>;
}
"""

from typing import Optional, Dict, Any, List

from ..abstracts import CrudService
from ..models import Collection

class Collections(CrudService):
    def decode(self, data: Dict[str, Any]) -> Collection:
        return self._decode(data, 'Collection')

    def base_crud_path(self) -> str:
        return 'collections'

    def import_collections(self, collections: List[Collection], delete_missing: Optional[bool] = None, query_params: Optional[Dict[str, Any]] = None) -> bool:
        """
        Imports the provided collections.
        
        If `deleteMissing` is `true`, all local collections and schema fields,
        that are not present in the imported configuration, WILL BE DELETED
        (including their related records data)!
        """
        return self._post('import', None, bool, query_params, collections, delete_missing)