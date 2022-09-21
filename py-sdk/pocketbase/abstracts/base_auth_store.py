"""
pocketbase/models/abstracts/base_auth_store.py

/**
 * Base AuthStore class that is intended to be extended by all other
 * PocketBase AuthStore implementations.
 */
declare abstract class BaseAuthStore {
    protected baseToken: string;
    protected baseModel: User | Admin | null;
    private _onChangeCallbacks;
    /**
     * Retrieves the stored token (if any).
     */
    get token(): string;
    /**
     * Retrieves the stored model data (if any).
     */
    get model(): User | Admin | null;
    /**
     * Checks if the store has valid (aka. existing and unexpired) token.
     */
    get isValid(): boolean;
    /**
     * Saves the provided new token and model data in the auth store.
     */
    save(token: string, model: User | Admin | null): void;
    /**
     * Removes the stored token and model data form the auth store.
     */
    clear(): void;
    /**
     * Parses the provided cookie string and updates the store state
     * with the cookie's token and model data.
     */
    loadFromCookie(cookie: string, key?: string): void;
    /**
     * Exports the current store state as cookie string.
     *
     * By default the following optional attributes are added:
     * - Secure
     * - HttpOnly
     * - SameSite=Strict
     * - Path=/
     * - Expires={the token expiration date}
     *
     * NB! If the generated cookie exceeds 4096 bytes, this method will
     * strip the model data to the bare minimum to try to fit within the
     * recommended size in https://www.rfc-editor.org/rfc/rfc6265#section-6.1.
     */
    exportToCookie(options?: SerializeOptions, key?: string): string;
    /**
     * Register a callback function that will be called on store change.
     *
     * Returns a removal function that you could call to "unsubscribe" from the changes.
     */
    onChange(callback: () => void): () => void;
    protected triggerChange(): void;
}
"""
from abc import ABC, abstractmethod
import json

class BaseAuthStore(ABC):
    def __init__(self):
        self.base_token = ''
        self.base_model = None
        self._on_change_callbacks = []

    @property
    def token(self):
        return self.base_token

    @property
    def model(self):
        return self.base_model

    @property
    def is_valid(self) -> bool:
        return self.base_token != '' and self.base_model != None
    
    @abstractmethod
    def save(self, token: str, model: dict):
        self.base_token = token
        self.base_model = model
        self.trigger_change()

    @abstractmethod
    def clear(self):
        self.base_token = ''
        self.base_model = None
        self.trigger_change()

    @abstractmethod
    def load_from_cookie(self, cookie: str, key: str = ''):
        pass

    @abstractmethod
    def export_to_cookie(self, options: dict = {}, key: str = ''):
        pass

    def on_change(self, callback: callable):
        self._on_change_callbacks.append(callback)
        return lambda: self._on_change_callbacks.remove(callback)

    def trigger_change(self):
        for callback in self._on_change_callbacks:
            callback()

    @abstractmethod
    def to_dict(self):
        return {
            'baseToken': self.base_token,
            'baseModel': self.base_model,
            '_onChangeCallbacks': self._on_change_callbacks
        }

    @classmethod
    def from_dict(cls, data: dict, **kwargs):
        return cls(data, **kwargs)
    
    def to_json(self):
        return json.dumps(self._base_dict)
    
    @classmethod
    def from_json(cls, json_str: str):
        return cls.from_dict(json.loads(json_str))