"""
Admin Service

Source: https://github.com/pocketbase/js-sdk/blob/master/src/services/Admins.ts
"""

from ..stores.utils import cookie_parse, fieldContentRegExp, parse_options, serialize_options, default_decode, default_encode, is_date, cookie_serialize
from ..stores.utils import a_to_b_polyfill, get_token_payload, is_token_expired
from ..models import Admin
from .utils import CrudService

class AdminAuthResponse:
    """
    export type AdminAuthResponse = {
        [key: string]: any,
        token: string,
        admin: Admin,
    }
    """
    def __init__(self, token: str, admin: Admin, **kwargs):
        self.token = token
        self.admin = admin
        
class Admins(CrudService):
    """
    export default class Admins extends CrudService<Admin> {
        /**
         * @inheritdoc
         */
        decode(data: { [key: string]: any }): Admin {
            return new Admin(data);
        }
    }
    """
    def __init__(self, client):
        super().__init__(client, Admin)

    def auth_response(self, response_data) -> AdminAuthResponse:
        """
        /**
         * Prepare successful authorize response.
         */
        protected authResponse(responseData: any): AdminAuthResponse {
            const admin = this.decode(responseData?.admin || {});

            if (responseData?.token && responseData?.admin) {
                this.client.authStore.save(responseData.token, admin);
            }

            return Object.assign({}, responseData, {
                // normalize common fields
                'token': responseData?.token || '',
                'admin': admin,
            });
        }
        """
        admin = self.decode(response_data.get('admin', {}))

        if response_data.get('token') and response_data.get('admin'):
            self.client.auth_store.save(response_data.get('token'), admin)

        return AdminAuthResponse(token=response_data.get('token', ''), admin=admin, **response_data)

    def base_crud_path(self) -> str:
        """
        /**
         * @inheritdoc
         */
        baseCrudPath(): string {
            return '/api/admins';
        }
        """
        return '/api/admins'

    def auth_via_email(self, email: str, password: str, body_params: dict = {}, query_params: dict = {}):
        """
        /**
         * Authenticate an admin account by its email and password
         * and returns a new admin token and data.
         *
         * On success this method automatically updates the client's AuthStore data.
         */
        authViaEmail(
            email: string,
            password: string,
            bodyParams = {},
            queryParams = {},
        ): Promise<AdminAuthResponse> {
            bodyParams = Object.assign({
                'email':    email,
                'password': password,
            }, bodyParams);

            return this.client.send(this.baseCrudPath() + '/auth-via-email', {
                'method':  'POST',
                'params':  queryParams,
                'body':    bodyParams,
                'headers': {
                    'Authorization': '',
                },
            }).then(this.authResponse.bind(this));
        }
        """
        body_params = dict({'email': email, 'password': password}, **body_params)

        return self.client.send(self.base_crud_path() + '/auth-via-email', {
            'method': 'POST',
            'params': query_params,
            'body': body_params,
            'headers': {
                'Authorization': '',
            },
        }).then(self.auth_response)

    def refresh(self, body_params: dict = {}, query_params: dict = {}):
        """
        /**
         * Refreshes the current admin authenticated instance and
         * returns a new token and admin data.
         *
         * On success this method automatically updates the client's AuthStore data.
         */
        refresh(bodyParams = {}, queryParams = {}): Promise<AdminAuthResponse> {
            return this.client.send(this.baseCrudPath() + '/refresh', {
                'method': 'POST',
                'params': queryParams,
                'body':   bodyParams,
            }).then(this.authResponse.bind(this));
        }
        """
        return self.client.send(self.base_crud_path() + '/refresh', {
            'method': 'POST',
            'params': query_params,
            'body': body_params,
        }).then(self.auth_response)

    def request_password_reset(self, email: str, body_params: dict = {}, query_params: dict = {}):
        """
        /**
         * Sends admin password reset request.
         */
        requestPasswordReset(
            email: string,
            bodyParams = {},
            queryParams = {},
        ): Promise<boolean> {
            bodyParams = Object.assign({
                'email': email,
            }, bodyParams);

            return this.client.send(this.baseCrudPath() + '/request-password-reset', {
                'method': 'POST',
                'params': queryParams,
                'body':   bodyParams,
            }).then(() => true);
        }
        """
        body_params = dict({'email': email}, **body_params)

        return self.client.send(self.base_crud_path() + '/request-password-reset', {
            'method': 'POST',
            'params': query_params,
            'body': body_params,
        }).then(lambda: True)

    def confirm_password_reset(self, password_reset_token: str, password: str, password_confirm: str, body_params: dict = {}, query_params: dict = {}):
        """
        /**
         * Confirms admin password reset request.
         */
        confirmPasswordReset(
            passwordResetToken: string,
            password: string,
            passwordConfirm: string,
            bodyParams = {},
            queryParams = {},
        ): Promise<AdminAuthResponse> {
            bodyParams = Object.assign({
                'token':           passwordResetToken,
                'password':        password,
                'passwordConfirm': passwordConfirm,
            }, bodyParams);

            return this.client.send(this.baseCrudPath() + '/confirm-password-reset', {
                'method': 'POST',
                'params': queryParams,
                'body':   bodyParams,
            }).then(this.authResponse.bind(this));
        }
        """
        body_params = dict({'token': password_reset_token, 'password': password, 'passwordConfirm': password_confirm}, **body_params)

        return self.client.send(self.base_crud_path() + '/confirm-password-reset', {
            'method': 'POST',
            'params': query_params,
            'body': body_params,
        }).then(self.auth_response)

