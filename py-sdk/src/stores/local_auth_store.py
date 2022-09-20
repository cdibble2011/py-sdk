"""
Local Auth Store

Source: https://github.com/pocketbase/js-sdk/blob/master/src/stores/LocalAuthStore.ts
"""

"""
import BaseAuthStore from '@/stores/BaseAuthStore';
import User          from '@/models/User';
import Admin         from '@/models/Admin';
"""
from curses import window
import json
from .base_auth_store import BaseAuthStore
from ..models import User, Admin

class LocalAuthStore(BaseAuthStore):
    """
    The default token store for browsers with auto fallback
    to runtime/memory if local storage is undefined (eg. in node env).
    
    export default class LocalAuthStore extends BaseAuthStore {
        private storageFallback: { [key: string]: any } = {};
        private storageKey: string  
    }
    """
    def __init__(self, storage_key = "pocketbase_auth"):
        # constructor(storageKey = "pocketbase_auth") {
        #     super();
        #     this.storageKey = storageKey;
        # }
        super().__init__()
        self.storage_key = storage_key
        self.storage_fallback = {}
        
    def get_token(self) -> str:
        # get token(): string { const data = this._storageGet(this.storageKey) || {}; return data.token || ''; }
        data = self._storage_get(self.storage_key) or {}
        return data.get('token', '')
    
    def get_model(self):
        # get model(): User|Admin|null { 
        # const data = this._storageGet(this.storageKey) || {};
        data = self._storage_get(self.storage_key) or {}
        # if ( data === null || typeof data !== 'object' || data.model === null || typeof data.model !== 'object' )
        if data is None or not isinstance(data, dict) or data.get('model') is None or not isinstance(data.get('model'), dict):
            # { return null; }
            return None
        # // admins don't have `verified` prop
        # if (typeof data.model?.verified !== 'undefined') 
        if data.get('model').get('verified') is not None:
            # { return new User(data.model); }
            return User(data.get('model'))
        # return new Admin(data.model); }
        return Admin(data.get('model'))
    
    def save(self, token, model):
        # save(token: string, model: User|Admin|null) {
        #   this._storageSet(this.storageKey, {
        self._storage_set(self.storage_key, {
            # 'token': token,
            'token': token,
            # 'model': model,
            'model': model,
        # });
        })
        # super.save(token, model); }
        super().save(token, model)
        
    def clear(self):
        # clear() { this._storageRemove(this.storageKey); super.clear(); }
        self._storage_remove(self.storage_key)
        super().clear()

    #// ---------------------------------------------------------------
    #// Internal helpers:
    #// ---------------------------------------------------------------

    def _storage_get(self, key):
        """
        Retrieves `key` from the browser's local storage
        (or runtime/memory if local storage is undefined).
        """
        # private _storageGet(key: string): any {
        # if (typeof window !== 'undefined' && window?.localStorage)
        if isinstance(window, dict) and window.get('localStorage'):
            # { const rawValue = window?.localStorage?.getItem(key) || '';
            raw_value = window.get('localStorage').get(key) or ''
            # try { return JSON.parse(rawValue); } 
            try:
                return json.loads(raw_value)
            # catch (e) { return rawValue; } // not a json }
            except Exception as e:
                return raw_value
            # return this.storageFallback[key]; // fallback }
        return self.storage_fallback.get(key)
    
    def _storage_set(self, key, value):
        """
        Stores a new data in the browser's local storage
        (or runtime/memory if local storage is undefined).
        """
        # private _storageSet(key: string, value: any) {
        # if (typeof window !== 'undefined' && window?.localStorage) // store in local storage
        if isinstance(window, dict) and window.get('localStorage'):
            # let normalizedVal = value;
            normalized_val = value
            # if (typeof value !== 'string')
            if not isinstance(value, str):
                # { normalizedVal = JSON.stringify(value); }
                normalized_val = json.dumps(value)
            # window?.localStorage?.setItem(key, normalizedVal); }
            window.get('localStorage').set(key, normalized_val)
        # else { this.storageFallback[key] = value; } // store in fallback } }
        else:
            self.storage_fallback[key] = value
            
    def _storage_remove(self, key):
        """
        Removes `key` from the browser's local storage and the runtime/memory.
        """
        # private _storageRemove(key: string) {
        # // delete from local storage
        # if (typeof window !== 'undefined') 
        if isinstance(window, dict):
            # { window?.localStorage?.removeItem(key); }
            window.get('localStorage').remove(key)
        # // delete from fallback
        # delete this.storageFallback[key]; }
        del self.storage_fallback[key]
        
    