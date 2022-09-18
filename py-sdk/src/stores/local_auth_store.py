"""
Local Auth Store

Source: https://github.com/pocketbase/js-sdk/blob/master/src/stores/LocalAuthStore.ts



"""

"""

import BaseAuthStore from '@/stores/BaseAuthStore';
import User          from '@/models/User';
import Admin         from '@/models/Admin';
"""
from .base_auth_store import BaseAuthStore
from ..models import User, Admin

class LocalAuthStore(BaseAuthStore):
    """
    /**
     * The default token store for browsers with auto fallback
     * to runtime/memory if local storage is undefined (eg. in node env).
     */
    export default class LocalAuthStore extends BaseAuthStore {
        private storageFallback: { [key: string]: any } = {};
        private storageKey: string

        
    }
    """
    def __init__(self, storage_key = "pocketbase_auth"):
        """
        constructor(storageKey = "pocketbase_auth") {
            super();

            this.storageKey = storageKey;
        }
        """
        super().__init__()
        self.storage_key = storage_key
        self.storage_fallback = {}
        
    def get_token(self):
        """
        /**
         * @inheritdoc
         */
        get token(): string {
            const data = this._storageGet(this.storageKey) || {};

            return data.token || '';
        }
        """
        data = self._storage_get(self.storage_key) or {}
        return data.get('token', '')
    
    def get_model(self):
        """
        /**
         * @inheritdoc
         */
        get model(): User|Admin|null {
            const data = this._storageGet(this.storageKey) || {};

            if (
                data === null ||
                typeof data !== 'object' ||
                data.model === null ||
                typeof data.model !== 'object'
            ) {
                return null;
            }

            // admins don't have `verified` prop
            if (typeof data.model?.verified !== 'undefined') {
                return new User(data.model);
            }

            return new Admin(data.model);
        }
        """
        data = self._storage_get(self.storage_key) or {}
        if data is None or not isinstance(data, dict) or data.get('model') is None or not isinstance(data.get('model'), dict):
            return None
        if data.get('model').get('verified') is not None:
            return User(data.get('model'))
        return Admin(data.get('model'))
    
    def save(self, token, model):
        """
        /**
         * @inheritdoc
         */
        save(token: string, model: User|Admin|null) {
            this._storageSet(this.storageKey, {
                'token': token,
                'model': model,
            });

            super.save(token, model);
        }
        """
        self._storage_set(self.storage_key, {
            'token': token,
            'model': model,
        })
        super().save(token, model)
        
    def clear(self):
        """
        /**
         * @inheritdoc
         */
        clear() {
            this._storageRemove(this.storageKey);

            super.clear();
        }
        """
        self._storage_remove(self.storage_key)
        super().clear()
        
    """
    // ---------------------------------------------------------------
    // Internal helpers:
    // ---------------------------------------------------------------
    """
        
    def _storage_get(self, key):
        """
        /**
         * Retrieves `key` from the browser's local storage
         * (or runtime/memory if local storage is undefined).
         */
        private _storageGet(key: string): any {
            if (typeof window !== 'undefined' && window?.localStorage) {
                const rawValue = window?.localStorage?.getItem(key) || '';
                try {
                    return JSON.parse(rawValue);
                } catch (e) { // not a json
                    return rawValue;
                }
            }

            // fallback
            return this.storageFallback[key];
        }
        """
        if isinstance(window, dict) and window.get('localStorage'):
            raw_value = window.get('localStorage').get(key) or ''
            try:
                return json.loads(raw_value)
            except Exception as e:
                return raw_value
        return self.storage_fallback.get(key)
    
    def _storage_set(self, key, value):
        """
        /**
         * Stores a new data in the browser's local storage
         * (or runtime/memory if local storage is undefined).
         */
        private _storageSet(key: string, value: any) {
            if (typeof window !== 'undefined' && window?.localStorage) {
                // store in local storage
                let normalizedVal = value;
                if (typeof value !== 'string') {
                    normalizedVal = JSON.stringify(value);
                }
                window?.localStorage?.setItem(key, normalizedVal);
            } else {
                // store in fallback
                this.storageFallback[key] = value;
            }
        }
        """
        if isinstance(window, dict) and window.get('localStorage'):
            normalized_val = value
            if not isinstance(value, str):
                normalized_val = json.dumps(value)
            window.get('localStorage').set(key, normalized_val)
        else:
            self.storage_fallback[key] = value
            
    def _storage_remove(self, key):
        """
        /**
         * Removes `key` from the browser's local storage and the runtime/memory.
         */
        private _storageRemove(key: string) {
            // delete from local storage
            if (typeof window !== 'undefined') {
                window?.localStorage?.removeItem(key);
            }

            // delete from fallback
            delete this.storageFallback[key];
        }
        """
        if isinstance(window, dict):
            window.get('localStorage').remove(key)
        del self.storage_fallback[key]
        
    