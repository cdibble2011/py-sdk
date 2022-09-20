"""
Base Auth Store

Source: https://github.com/pocketbase/js-sdk/blob/master/src/stores/BaseAuthStore.ts

import { cookieParse, cookieSerialize, SerializeOptions } from '@/stores/utils/cookie';
import { isTokenExpired, getTokenPayload } from '@/stores/utils/jwt';
import User  from '@/models/User';
import Admin from '@/models/Admin';
"""


"""
import { cookieParse, cookieSerialize, SerializeOptions } from '@/stores/utils/cookie';
import { isTokenExpired, getTokenPayload } from '@/stores/utils/jwt';
import User  from '@/models/User';
import Admin from '@/models/Admin';
"""

from __future__ import annotations
from .utils import cookie_parse, cookie_serialize, serialize_options
from .utils import is_token_expired, get_token_payload
from ..models import User, Admin
from typing import Callable, List, Optional, Union
import datetime
import requests
import json


"""
const defaultCookieKey = 'pb_auth';
"""
default_cookie_key = 'pb_auth'

class OnChangeFunc:
    """
    type onChangeFunc = (token: string, model: User|Admin|null) => void;
    """
    def __init__(self, token: str, model: User or Admin or None) -> None:
        self.base_token: str = token or ''
        self.base_model: User or Admin or None = model or None
        self.change_callbacks: List[Callable] = []

class BaseAuthStore:
    """
    Base AuthStore class that is intended to be extended by all other
    PocketBase AuthStore implementations.
    
    export default abstract class BaseAuthStore {
        protected baseToken: string = '';
        protected baseModel: User|Admin|null = null;

        private _onChangeCallbacks: Array<onChangeFunc> = [];        
    }
    """
    base_token: str = ''
    base_model: Optional[Union[User, Admin]] = None

    _on_change_callbacks: List[Callable[[str, Optional[Union[User, Admin]]], None]] = []

    @property
    def token(self) -> str:
        """
        Retrieves the stored token (if any).
        
        get token(): string { return this.baseToken; }
        """
        return self.base_token

    @property
    def model(self) -> Optional[Union[User, Admin]]:
        """
        Retrieves the stored model data (if any).
        
        get model(): User|Admin|null { return this.baseModel; }
        """
        return self.base_model

    @property
    def is_valid(self) -> bool:
        """
        Checks if the store has valid (aka. existing and unexpired) token.
        
        get isValid(): boolean { return !isTokenExpired(this.token); }
        """
        return not is_token_expired(self.token)

    def save(self, token: str, model: Optional[Union[User, Admin]]) -> None:
        """
        Saves the provided new token and model data in the auth store.
        
        save(token: string, model: User|Admin|null): void {
            this.baseToken = token || '';

            // normalize the model instance
            if (model !== null && typeof model === 'object') {
                this.baseModel = (model as any)?.verified !== 'undefined' ?
                    new User(model) : new Admin(model);
            } else {
                this.baseModel = null;
            }

            this.triggerChange();
        }
        """
        self.base_token = token or ''

        if model is not None and isinstance(model, dict):
            self.base_model = User(model) if 'verified' in model else Admin(model)
        else:
            self.base_model = None

        self.trigger_change()

    def clear(self) -> None:
        """
        Removes the stored token and model data form the auth store.
        
        clear(): void {
            this.baseToken = '';
            this.baseModel = null;
            this.triggerChange();
        }
        """
        self.base_token = ''
        self.base_model = None
        self.trigger_change()

    def load_from_cookie(self, cookie: str, key: str = default_cookie_key) -> None:
        """
        Parses the provided cookie string and updates the store state
        with the cookie's token and model data.
         
        loadFromCookie(cookie: string, key = defaultCookieKey): void {
            const rawData = cookieParse(cookie || '')[key] || '';

            let data: { [key: string]: any } = {};
            try {
                data = JSON.parse(rawData);
                // normalize
                if (typeof data === null || typeof data !== 'object' || Array.isArray(data)) {
                    data = {};
                }
            } catch (_) {}

            this.save(data.token || '', data.model || {});
        }
        """
        raw_data = cookie_parse(cookie or '').get(key, '')

        data: dict = {}
        try:
            data = json.loads(raw_data)
            if data is None or not isinstance(data, dict) or isinstance(data, list):
                data = {}
        except json.JSONDecodeError:
            pass

        self.save(data.get('token', ''), data.get('model', {}))

    def export_to_cookie(self, options: Optional[serialize_options] = None, key: str = default_cookie_key) -> str:
        """
        Exports the current store state as cookie string.
        
        By default the following optional attributes are added:
        - Secure
        - HttpOnly
        - SameSite=Strict
        - Path=/
        - Expires={the token expiration date}
        
        NB! If the generated cookie exceeds 4096 bytes, this method will
        strip the model data to the bare minimum to try to fit within the
        recommended size in https://www.rfc-editor.org/rfc/rfc6265#section-6.1.
        
        exportToCookie(options?: SerializeOptions, key = defaultCookieKey): string {
            const defaultOptions: SerializeOptions = {
                secure:   true,
                sameSite: true,
                httpOnly: true,
                path:     "/",
            };

            // extract the token expiration date
            const payload = getTokenPayload(this.token);
            if (payload?.exp) {
                defaultOptions.expires = new Date(payload.exp * 1000);
            } else {
                defaultOptions.expires = new Date('1970-01-01');
            }

            // merge with the user defined options
            options = Object.assign({}, defaultOptions, options);

            const rawData = {
                token: this.token,
                model: this.model?.export() || null,
            };

            let result = cookieSerialize(key, JSON.stringify(rawData), options);

            const resultLength = typeof Blob !== 'undefined' ?
                (new Blob([result])).size : result.length;

            // strip down the model data to the bare minimum
            if (rawData.model && resultLength > 4096) {
                rawData.model = {id: rawData?.model?.id, email: rawData?.model?.email};
                if (this.model instanceof User) {
                    rawData.model.verified = this.model.verified;
                }
                result = cookieSerialize(key, JSON.stringify(rawData), options)
            }

            return result;
        }
        """
        default_options: serialize_options = {
            'secure': True,
            'sameSite': True,
            'httpOnly': True,
            'path': '/',
        }

        payload = get_token_payload(self.token)
        if payload and 'exp' in payload:
            default_options['expires'] = datetime.fromtimestamp(payload['exp'])
        else:
            default_options['expires'] = datetime.fromisoformat('1970-01-01')

        options = {**default_options, **(options or {})}

        raw_data = {
            'token': self.token,
            'model': self.model.export() if self.model else None,
        }

        result = cookie_serialize(key, json.dumps(raw_data), options)

        result_length = len(result)
        if raw_data['model'] and result_length > 4096:
            raw_data['model'] = {'id': raw_data['model'].get('id'), 'email': raw_data['model'].get('email')}
            if isinstance(self.model, User):
                raw_data['model']['verified'] = self.model.verified
            result = cookie_serialize(key, json.dumps(raw_data), options)

        return result
    
    def trigger_change(self) -> None:
        """
        protected triggerChange(): void {
            for (const callback of this._onChangeCallbacks) {
                callback && callback(this.token, this.model);
            }
        }
        
        # Triggers the change event
        triggerChange(): void {
            this.changeCallbacks.forEach((callback) => callback());
        }
        """
        for callback in self.change_callbacks:
            callback()
            
    def on_change(self, callback: Callable) -> None:
        """
        Register a callback function that will be called on store change.
        Returns a removal function that you could call to "unsubscribe" from the changes.
        
        onChange(callback: () => void): () => void {
            this._onChangeCallbacks.push(callback);

            return () => {
                for (let i = this._onChangeCallbacks.length - 1; i >= 0; i--) {
                    if (this._onChangeCallbacks[i] == callback) {
                        delete this._onChangeCallbacks[i];    // removes the function reference
                        this._onChangeCallbacks.splice(i, 1); // reindex the array
                        return;
                    }
                }
            }
        }
        """
        self.change_callbacks.append(callback)

        def remove_callback() -> None:
            for i in range(len(self.change_callbacks) - 1, -1, -1):
                if self.change_callbacks[i] == callback:
                    del self.change_callbacks[i]
                    return

        return remove_callback
    