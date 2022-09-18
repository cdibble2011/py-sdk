"""
Client

Source: https://github.com/pocketbase/js-sdk/blob/master/src/Client.ts
"""

"""
import ClientResponseError from '@/ClientResponseError';
import BaseAuthStore       from '@/stores/BaseAuthStore';
import LocalAuthStore      from '@/stores/LocalAuthStore';
import Settings            from '@/services/Settings';
import Admins              from '@/services/Admins';
import Users               from '@/services/Users';
import Collections         from '@/services/Collections';
import Records             from '@/services/Records';
import Logs                from '@/services/Logs';
import Realtime            from '@/services/Realtime';
"""
import urllib
import json
from datetime import datetime
from .client_response_error import ClientResponseError
from .stores import LocalAuthStore, BaseAuthStore
from .services import Settings, Admins, Users, Collections, Records, Logs, Realtime

class Client:
    """
    /**
     * PocketBase JS Client.
     */
    export default class Client {}

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
    beforeSend?: (url: string, reqConfig: { [key: string]: any }) => { [key: string]: any };

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

    private cancelControllers: { [key: string]: AbortController } = {}

    
    """
    def __init__(self):
        """
        constructor(
            baseUrl = '/',
            lang = 'en-US',
            authStore?: BaseAuthStore | null,
        ) {
            this.baseUrl   = baseUrl;
            this.lang      = lang;
            this.authStore = authStore || new LocalAuthStore();

            // services
            this.admins      = new Admins(this);
            this.users       = new Users(this);
            this.records     = new Records(this);
            this.collections = new Collections(this);
            this.logs        = new Logs(this);
            this.settings    = new Settings(this);
            this.realtime    = new Realtime(this);
        }
        """
        self.base_url = '/'
        self.lang = 'en-US'
        self.auth_store = LocalAuthStore()

        # services
        self.admins = Admins(self)
        self.users = Users(self)
        self.records = Records(self)
        self.collections = Collections(self)
        self.logs = Logs(self)
        self.settings = Settings(self)
        self.realtime = Realtime(self)
    """
    def auth_store(self):
        
        /**
         * @deprecated Legacy alias for `this.authStore`.
         */
        get AuthStore(): BaseAuthStore {
            return this.authStore;
        };
        
        return self.auth_store
        
    def settings(self): 
    
    /**
     * @deprecated Legacy alias for `this.settings`.
     */
    get Settings(): Settings {
        return this.settings;
    };
    
        return self.settings
    
    def admins(self): 
    /**
     * @deprecated Legacy alias for `this.admins`.
     */
    get Admins(): Admins {
        return this.admins;
    };

    return self.admins
    
    def users(self):
    
    /**
     * @deprecated Legacy alias for `this.users`.
     */
    get Users(): Users {
        return this.users;
    };
    
    return self.users

    def collections(self):
    
    /**
     * @deprecated Legacy alias for `this.collections`.
     */
    get Collections(): Collections {
        return this.collections;
    };
    
    return self.collections

    def records(Self):
    
    /**
     * @deprecated Legacy alias for `this.records`.
     */
    get Records(): Records {
        return this.records;
    };
    
    return self.records

    def logs(self):
    
    /**
     * @deprecated Legacy alias for `this.logs`.
     */
    get Logs(): Logs {
        return this.logs;
    };
    
    return self.logs
    
    def realtime(self):
    
    /**
     * @deprecated Legacy alias for `this.realtime`.
     */
    get Realtime(): Realtime {
        return this.realtime;
    };
    
    return self.realtime
    """

    def cancel_request(self, cancel_key: str):
        """
        /**
         * Cancels single request by its cancellation key.
         */
        cancelRequest(cancelKey: string): Client {
            if (this.cancelControllers[cancelKey]) {
                this.cancelControllers[cancelKey].abort();
                delete this.cancelControllers[cancelKey];
            }

            return this;
        }
        """
        if self.cancel_controllers[cancel_key]:
            self.cancel_controllers[cancel_key].abort()
            del self.cancel_controllers[cancel_key]
        
    def cancel_all_requestS(self):
        """
        /**
         * Cancels all pending requests.
         */
        cancelAllRequests(): Client {
            for (let k in this.cancelControllers) {
                this.cancelControllers[k].abort();
            }

            this.cancelControllers = {};

            return this;
        }
        """
        for k in self.cancel_controllers:
            self.cancel_controllers[k].abort()
        self.cancel_controllers = {}
        
    async def send(self, path: str, req_config: dict):
        """
        /**
         * Sends an api http request.
         */
        async send(path: string, reqConfig: { [key: string]: any }): Promise<any> {
            let config = Object.assign({ method: 'GET' } as { [key: string]: any }, reqConfig);
        """
        config = dict(method='GET', **req_config)
        """
            // serialize the body if needed and set the correct content type
            // note1: for FormData body the Content-Type header should be skipped
            // note2: we are checking the constructor name because FormData is not available natively in node
            if (config.body && config.body.constructor.name !== 'FormData') {
                if (typeof config.body !== 'string') {
                    config.body = JSON.stringify(config.body);
                }

                // add the json header (if not already)
                if (typeof config?.headers?.['Content-Type'] === 'undefined') {
                    config.headers = Object.assign({}, config.headers, {
                        'Content-Type': 'application/json',
                    });
                }
            }
        """
        # serialize the body if needed and set the correct content type
        # note1: for FormData body the Content-Type header should be skipped
        # note2: we are checking the constructor name because FormData is not available natively in node
        if config['body'] and config['body'].constructor.name != 'FormData':
            if not isinstance(config['body'], str):
                config['body'] = json.dumps(config['body'])
            # add the json header (if not already)
            if 'Content-Type' not in config.get('headers', {}):
                config['headers'] = dict(config['headers'], **{'Content-Type': 'application/json'})
        """
            // add Accept-Language header (if not already)
            if (typeof config?.headers?.['Accept-Language'] === 'undefined') {
                config.headers = Object.assign({}, config.headers, {
                    'Accept-Language': this.lang,
                });
            }

            // check if Authorization header can be added
            if (
                // has stored token
                this.authStore?.token &&
                // auth header is not explicitly set
                (typeof config?.headers?.Authorization === 'undefined')
            ) {
                let authType = 'Admin';
                if (typeof (this.authStore.model as any)?.verified !== 'undefined') {
                    authType = 'User'; // admins don't have verified
                }

                config.headers = Object.assign({}, config.headers, {
                    'Authorization': (authType + ' ' + this.authStore.token),
                });
            }
        """
        # add Accept-Language header (if not already)
        if 'Accept-Language' not in config.get('headers', {}):
            config['headers'] = dict(config['headers'], **{'Accept-Language': self.lang})
        # check if Authorization header can be added
        # has stored token          # auth header is not explicitly set
        if self.auth_store.token and 'Authorization' not in config.get('headers', {}) and self.auth_store.model:
            auth_type = 'Admin'
            if 'verified' in self.auth_store.model:
                auth_type = 'User'
            config['headers'] = dict(config['headers'], **{'Authorization': f'{auth_type} {self.auth_store.token}'})
        """
            // handle auto cancelation for duplicated pending request
            if (config.params?.$autoCancel !== false) {
                const cancelKey = config.params?.$cancelKey || ((config.method || 'GET') + path);

                // cancel previous pending requests
                this.cancelRequest(cancelKey);

                const controller = new AbortController();
                this.cancelControllers[cancelKey] = controller;
                config.signal = controller.signal;
            }
        """
        # handle auto cancelation for duplicated pending request
        if config['params'].get('$autoCancel', True):
            cancel_key = config['params'].get('$cancelKey', config['method'] + path)
            # cancel previous pending requests
            self.cancel_request(cancel_key)
            controller = AbortController()
            self.cancel_controllers[cancel_key] = controller
            config['signal'] = controller.signal
        """
            // remove the special cancellation params from the other valid query params
            delete config.params?.$autoCancel;
            delete config.params?.$cancelKey;

            // build url + path
            let url = this.buildUrl(path);

            // serialize the query parameters
            if (typeof config.params !== 'undefined') {
                const query = this.serializeQueryParams(config.params)
                if (query) {
                    url += (url.includes('?') ? '&' : '?') + query;
                }
                delete config.params;
            }
        """
        # remove the special cancellation params from the other valid query params
        del config['params']['$autoCancel']
        del config['params']['$cancelKey']
        # build url + path
        url = self.build_url(path)
        # serialize the query parameters
        if 'params' in config:
            query = self.serialize_query_params(config['params'])
            if query:
                url += ('?' if '?' in url else '&') + query
            del config['params']
            """
            if (this.beforeSend) {
                config = Object.assign({}, this.beforeSend(url, config));
            }

            // send the request
            return fetch(url, config)
                .then(async (response) => {
                    let data : any = {};

                    try {
                        data = await response.json();
                    } catch (_) {
                        // all api responses are expected to return json
                        // with the exception of the realtime event and 204
                    }

                    if (this.afterSend) {
                        data = this.afterSend(response, data);
                    }

                    if (response.status >= 400) {
                        throw new ClientResponseError({
                            url:      response.url,
                            status:   response.status,
                            data:     data,
                        });
                    }

                    return data;
                }).catch((err) => {
                    // wrap to normalize all errors
                    throw new ClientResponseError(err);
                });
        }
        """
        if self.before_send:
            config = dict(config, **self.before_send(url, config))
            # send the request
            return fetch(url, config).then(
                lambda response: self.handle_response(response)
            ).catch(
                lambda err: self.handle_error(err)
            )

    def build_url(self, path: str):
        """
        /**
         * Builds a full client url by safely concatenating the provided path.
         */
        buildUrl(path: string): string {
            let url = this.baseUrl + (this.baseUrl.endsWith('/') ? '' : '/');
            if (path) {
                url += (path.startsWith('/') ? path.substring(1) : path);
            }
            return url;
        }
        """
        url = self.base_url + ('' if self.base_url.endswith('/') else '/')
        if path:
            url += path[1:] if path.startswith('/') else path
        return url
    
    def serialize_parameters(self, params: dict):
        """
        /**
         * Serializes the provided query parameters into a query string.
         */
        private serializeQueryParams(params: {[key: string]: any}): string {
            const result: Array<string> = [];
            for (const key in params) {
                if (params[key] === null) {
                    // skip null query params
                    continue;
                }

                const value = params[key];
                const encodedKey = encodeURIComponent(key);

                if (Array.isArray(value)) {
                    // "repeat" array params
                    for (const v of value) {
                        result.push(encodedKey + "=" + encodeURIComponent(v));
                    }
                } else if (value instanceof Date) {
                    result.push(encodedKey + "=" + encodeURIComponent(value.toISOString()));
                } else if (typeof value !== null && typeof value === 'object') {
                    result.push(encodedKey + "=" + encodeURIComponent(JSON.stringify(value)));
                } else {
                    result.push(encodedKey + "=" + encodeURIComponent(value));
                }
            }

            return result.join('&');
        }
        """
        result = []
        for key, value in params.items():
            if value is None:
                continue
            encoded_key = urllib.parse.quote(key)
            if isinstance(value, list):
                for v in value:
                    result.append(f'{encoded_key}={urllib.parse.quote(v)}')
            elif isinstance(value, datetime):
                result.append(f'{encoded_key}={urllib.parse.quote(value.isoformat())}')
            elif isinstance(value, dict):
                result.append(f'{encoded_key}={urllib.parse.quote(json.dumps(value))}')
            else:
                result.append(f'{encoded_key}={urllib.parse.quote(value)}')
        return '&'.join(result)
        