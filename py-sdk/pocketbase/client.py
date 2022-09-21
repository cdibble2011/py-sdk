"""
pocketbase/client.py

/**
 * PocketBase JS Client.
 */
declare class Client {
    /**
     * The base PocketBase backend url address (eg. 'http://127.0.0.1.8090').
     */
    baseUrl: string;
    /**
     * Hook that get triggered right before sending the fetch request,
     * allowing you to inspect/modify the request config.
     *
     * Returns the new modified config that will be used to send the request.
     *
     * For list of the possible options check https://developer.mozilla.org/en-US/docs/Web/API/fetch#options
     *
     * Example:
     * ```js
     * client.beforeSend = function (url, reqConfig) {
     *     reqConfig.headers = Object.assign({}, reqConfig.headers, {
     *         'X-Custom-Header': 'example',
     *     });
     *
     *     return reqConfig;
     * };
     * ```
     */
    beforeSend?: (url: string, reqConfig: {
        [key: string]: any;
    }) => {
        [key: string]: any;
    };
    /**
     * Hook that get triggered after successfully sending the fetch request,
     * allowing you to inspect/modify the response object and its parsed data.
     *
     * Returns the new Promise resolved `data` that will be returned to the client.
     *
     * Example:
     * ```js
     * client.afterSend = function (response, data) {
     *     if (response.status != 200) {
     *         throw new ClientResponseError({
     *             url:      response.url,
     *             status:   response.status,
     *             data:     data,
     *         });
     *     }
     *
     *     return data;
     * };
     * ```
     */
    afterSend?: (response: Response, data: any) => any;
    /**
     * Optional language code (default to `en-US`) that will be sent
     * with the requests to the server as `Accept-Language` header.
     */
    lang: string;
    /**
     * A replaceable instance of the local auth store service.
     */
    authStore: BaseAuthStore;
    /**
     * An instance of the service that handles the **Settings APIs**.
     */
    readonly settings: Settings;
    /**
     * An instance of the service that handles the **Admin APIs**.
     */
    readonly admins: Admins;
    /**
     * An instance of the service that handles the **User APIs**.
     */
    readonly users: Users;
    /**
     * An instance of the service that handles the **Collection APIs**.
     */
    readonly collections: Collections;
    /**
     * An instance of the service that handles the **Record APIs**.
     */
    readonly records: Records;
    /**
     * An instance of the service that handles the **Log APIs**.
     */
    readonly logs: Logs;
    /**
     * An instance of the service that handles the **Realtime APIs**.
     */
    readonly realtime: Realtime;
    private cancelControllers;
    constructor(baseUrl?: string, lang?: string, authStore?: BaseAuthStore | null);
    /**
     * @deprecated Legacy alias for `this.authStore`.
     */
    get AuthStore(): BaseAuthStore;
    /**
     * @deprecated Legacy alias for `this.settings`.
     */
    get Settings(): Settings;
    /**
     * @deprecated Legacy alias for `this.admins`.
     */
    get Admins(): Admins;
    /**
     * @deprecated Legacy alias for `this.users`.
     */
    get Users(): Users;
    /**
     * @deprecated Legacy alias for `this.collections`.
     */
    get Collections(): Collections;
    /**
     * @deprecated Legacy alias for `this.records`.
     */
    get Records(): Records;
    /**
     * @deprecated Legacy alias for `this.logs`.
     */
    get Logs(): Logs;
    /**
     * @deprecated Legacy alias for `this.realtime`.
     */
    get Realtime(): Realtime;
    /**
     * Cancels single request by its cancellation key.
     */
    /**
     * Cancels single request by its cancellation key.
     */
    cancelRequest(cancelKey: string): Client;
    /**
     * Cancels all pending requests.
     */
    /**
     * Cancels all pending requests.
     */
    cancelAllRequests(): Client;
    /**
     * Sends an api http request.
     */
    /**
     * Sends an api http request.
     */
    send(path: string, reqConfig: {
        [key: string]: any;
    }): Promise<any>;
    /**
     * Builds a full client url by safely concatenating the provided path.
     */
    /**
     * Builds a full client url by safely concatenating the provided path.
     */
    buildUrl(path: string): string;
    /**
     * Serializes the provided query parameters into a query string.
     */
    /**
     * Serializes the provided query parameters into a query string.
     */
    private serializeQueryParams;
}
export { Client as default };
"""
from typing import Optional, Dict, Any
from .abstracts import BaseAuthStore
from .models import Admin, Collection, ExternalAuth, ListResult, LogRequest, Record, User
from .services import Admins, Collections, Logs, Records, Settings, Users

class Client:
    def __init__(self, base_url: str = 'http://127.0.0.1:8090', lang: str = 'en-us'):
        self.base_url = base_url
        self.lang = lang
        self.auth_store = BaseAuthStore
        self.settings = Settings
        self.admins = Admins
        self.collections = Collections
        self.logs = Logs
        self.records = Records
        self.users = Users
        
    def cancel_request(self, cancel_key: str) -> Client:
        pass

    def cancel_all_requests(self) -> Client:
        pass

    def send(self, path: str, req_config: Dict[str, Any]) -> Any:
        pass

    def build_url(self, path: str) -> str:
        pass
    
    def serialize_query_params(self):
        pass
        
    