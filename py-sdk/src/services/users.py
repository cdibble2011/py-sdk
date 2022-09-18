"""
Users Service

Source: https://github.com/pocketbase/js-sdk/blob/master/src/services/Users.ts


"""

"""
import CrudService  from '@/services/utils/CrudService';
import User         from '@/models/User';
import ExternalAuth from '@/models/ExternalAuth';
"""
from .utils import CrudService
from ..models import User, ExternalAuth

class UserAuthResponse:
    """
    export type UserAuthResponse = {
        [key: string]: any,
        token:         string,
        user:          User,
    }
    """
    def __init__(self, token: str, user: User):
        self.token = token
        self.user = user


class AuthProviderInfo:
    """
    export type AuthProviderInfo = {
        name:                string,
        state:               string,
        codeVerifier:        string,
        codeChallenge:       string,
        codeChallengeMethod: string,
        authUrl:             string,
    }
    """
    def __init__(self, name: str, state: str, code_verifier: str, code_challenge: str, code_challenge_method: str, auth_url: str):
        self.name = name
        self.state = state
        self.code_verifier = code_verifier
        self.code_challenge = code_challenge
        self.code_challenge_method = code_challenge_method
        self.auth_url = auth_url
        
class AuthMethodsList:
    """
    export type AuthMethodsList = {
        [key: string]: any,
        emailPassword: boolean,
        authProviders: Array<AuthProviderInfo>,
    }
    """
    def __init__(self, email_password: bool, auth_providers: list):
        self.email_password = email_password
        self.auth_providers = auth_providers
        
class UsersService(CrudService):
    """
    export default class Users extends CrudService<User> {}
    """
    def decode(self, data):
        """
        /**
         * @inheritdoc
         */
        decode(data: { [key: string]: any }): User {
            return new User(data);
        }
        """
        return User(data)
    
    def auth_response(self, data):
        """
        /**
         * Handles user authentication response.
         */
        authResponse(data: { [key: string]: any }): UserAuthResponse {
            const response = new UserAuthResponse(data);

            this.client.authStore.update(response);

            return response;
        }
        """
        response = UserAuthResponse(data)
        self.client.auth_store.update(response)
        return response
    
    def base_crud_path(self):
        """
        /**
         * @inheritdoc
         */
        baseCrudPath(): string {
            return '/api/users';
        }
        """
        return '/api/users'
    
    def auth_response(self, response_data):
        """
        /**
         * Prepare successful authorization response.
         */
        protected authResponse(responseData: any): UserAuthResponse {
            const user = this.decode(responseData?.user || {});

            if (responseData?.token && responseData?.user) {
                this.client.authStore.save(responseData.token, user);
            }

            return Object.assign({}, responseData, {
                // normalize common fields
                'token': responseData?.token || '',
                'user':  user,
            });
        }
        """
        user = self.decode(response_data.get('user', {}))
        if response_data.get('token') and response_data.get('user'):
            self.client.auth_store.save(response_data.get('token'), user)
        return UserAuthResponse(response_data.get('token', ''), user)
    
    def auth_via_oauth2(self, provider: str, code: str, code_verifier: str, redirect_url: str, body_params: dict = {}, query_params: dict = {}):
        """
        /**
         * Authenticate a user via OAuth2 client provider.
         *
         * On success, this method also automatically updates
         * the client's AuthStore data and returns:
         * - new user authentication token
         * - the authenticated user model record
         * - the OAuth2 user profile data (eg. name, email, avatar, etc.)
         */
        authViaOAuth2(
            provider: string,
            code: string,
            codeVerifier: string,
            redirectUrl: string,
            bodyParams = {},
            queryParams = {},
        ): Promise<UserAuthResponse> {
            bodyParams = Object.assign({
                'provider':     provider,
                'code':         code,
                'codeVerifier': codeVerifier,
                'redirectUrl':  redirectUrl,
            }, bodyParams);

            return this.client.send(this.baseCrudPath() + '/auth-via-oauth2', {
                'method':  'POST',
                'params':  queryParams,
                'body':    bodyParams,
                'headers': {
                    'Authorization': '',
                },
            }).then(this.authResponse.bind(this));
        }
        """
        body_params = dict({
            'provider': provider,
            'code': code,
            'codeVerifier': code_verifier,
            'redirectUrl': redirect_url,
        }, **body_params)
        return self.client.send(self.base_crud_path() + '/auth-via-oauth2', {
            'method': 'POST',
            'params': query_params,
            'body': body_params,
            'headers': {
                'Authorization': '',
            },
        }).then(self.auth_response)

    def request_password_reset(self, email: str, body_params: dict = {}, query_params: dict = {}):
        """
        /**
         * Sends user password reset request.
         */
        requestPasswordReset(
            email: string,
            bodyParams  = {},
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
        body_params = dict({
            'email': email,
        }, **body_params)
        return self.client.send(self.base_crud_path() + '/request-password-reset', {
            'method': 'POST',
            'params': query_params,
            'body': body_params,
        }).then(lambda: True)
    
    def request_email_change(self,new_email: str, body_params: dict = {}, query_params: dict = {}):
        """
        /**
         * Sends an email change request to the authenticated user.
         */
        requestEmailChange(
            newEmail: string,
            bodyParams = {},
            queryParams = {},
        ): Promise<boolean> {
            bodyParams = Object.assign({
                'newEmail': newEmail,
            }, bodyParams);

            return this.client.send(this.baseCrudPath() + '/request-email-change', {
                'method': 'POST',
                'params': queryParams,
                'body':   bodyParams,
            }).then(() => true);
        }
        """
        body_params = dict({
            'newEmail': new_email,
        }, **body_params)
        return self.client.send(self.base_crud_path() + '/request-email-change', {
            'method': 'POST',
            'params': query_params,
            'body': body_params,
        }).then(lambda: True)

    def confirm_password_reset(self, password_reset_token: str, password: str, password_confirm: str, body_params: dict = {}, query_params: dict = {}):
        """
        /**
         * Confirms user password reset request.
         */
        confirmPasswordReset(
            passwordResetToken: string,
            password: string,
            passwordConfirm: string,
            bodyParams = {},
            queryParams = {},
        ): Promise<UserAuthResponse> {
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
        body_params = dict({
            'token': password_reset_token,
            'password': password,
            'passwordConfirm': password_confirm,
        }, **body_params)
        return self.client.send(self.base_crud_path() + '/confirm-password-reset', {
            'method': 'POST',
            'params': query_params,
            'body': body_params,
        }).then(self.auth_response)

    def request_verification(self, email: str, body_params: dict = {}, query_params: dict = {}):
        """
        /**
         * Sends user verification email request.
         */
        requestVerification(
            email: string,
            bodyParams = {},
            queryParams = {},
        ): Promise<boolean> {
            bodyParams = Object.assign({
                'email': email,
            }, bodyParams);

            return this.client.send(this.baseCrudPath() + '/request-verification', {
                'method': 'POST',
                'params': queryParams,
                'body':   bodyParams,
            }).then(() => true);
        }
        """
        body_params = dict({
            'email': email,
        }, **body_params)
        return self.client.send(self.base_crud_path() + '/request-verification', {
            'method': 'POST',
            'params': query_params,
            'body': body_params,
        }).then(lambda: True)
        
    def confirm_verification(self, verification_token_string: str, body_params: dict = {}, query_params: dict = {}):
        """
        /**
         * Confirms user email verification request.
         */
        confirmVerification(
            verificationToken: string,
            bodyParams  = {},
            queryParams = {},
        ): Promise<UserAuthResponse> {
            bodyParams = Object.assign({
                'token': verificationToken,
            }, bodyParams);

            return this.client.send(this.baseCrudPath() + '/confirm-verification', {
                'method': 'POST',
                'params': queryParams,
                'body':   bodyParams,
            }).then(this.authResponse.bind(this));
        }
        """
        body_params = dict({
            'token': verification_token_string,
        }, **body_params)
        return self.client.send(self.base_crud_path() + '/confirm-verification', {
            'method': 'POST',
            'params': query_params,
            'body': body_params,
        }).then(self.auth_response)

    def confirm_email_change(self, email_change_token: str, password: str, body_params: dict = {}, query_params: dict = {}):
        """
        /**
         * Confirms user new email address.
         */
        confirmEmailChange(
            emailChangeToken: string,
            password: string,
            bodyParams  = {},
            queryParams = {},
        ): Promise<UserAuthResponse> {
            bodyParams = Object.assign({
                'token': emailChangeToken,
                'password': password,
            }, bodyParams);

            return this.client.send(this.baseCrudPath() + '/confirm-email-change', {
                'method': 'POST',
                'params': queryParams,
                'body':   bodyParams,
            }).then(this.authResponse.bind(this));
        }
        """
        body_params = dict({
            'token': email_change_token,
            'password': password,
        }, **body_params)
        return self.client.send(self.base_crud_path() + '/confirm-email-change', {
            'method': 'POST',
            'params': query_params,
            'body': body_params,
        }).then(self.auth_response)
    
    def auth_via_email(self, email: str, password: str, body_params: dict = {}, query_params: dict = {}):
        """
        /**
         * Authenticate a user via its email and password.
         *
         * On success, this method also automatically updates
         * the client's AuthStore data and returns:
         * - new user authentication token
         * - the authenticated user model record
         */
        authViaEmail(
            email: string,
            password: string,
            bodyParams = {},
            queryParams = {},
        ): Promise<UserAuthResponse> {
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
        body_params = dict(body_params, email=email, password=password)
        return self.client.send(self.base_crud_path() + '/auth-via-email', {
            'method': 'POST',
            'params': query_params,
            'body': body_params,
            'headers': {
                'Authorization': '',
            }
        }).then(self.auth_response)

    def list_external_auths(self, user_id: str, query_params: dict = {}):
        """
        /**
         * Lists all linked external auth providers for the specified user.
         */
        listExternalAuths(
            userId: string,
            queryParams = {}
        ): Promise<Array<ExternalAuth>> {
            return this.client.send(this.baseCrudPath() + '/' + encodeURIComponent(userId) + '/external-auths', {
                'method': 'GET',
                'params': queryParams,
            }).then((responseData) => {
                const items: Array<ExternalAuth> = [];

                if (Array.isArray(responseData)) {
                    for (const item of responseData) {
                        items.push(new ExternalAuth(item));
                    }
                }

                return items;
            });
        }
        """
        return self.client.send(self.base_crud_path() + '/' + user_id + '/external-auths', {
            'method': 'GET',
            'params': query_params,
        }).then(lambda response_data: [ExternalAuth(item) for item in response_data])

    
    def refresh(self, body_params: dict = {}, query_params: dict = {}):
        """
        /**
         * Refresh user authentication token.
         *
         * On success, this method also automatically updates
         * the client's AuthStore data and returns:
         * - new user authentication token
         * - the authenticated user model record
         */
        refresh(bodyParams = {}, queryParams = {}): Promise<UserAuthResponse> {
            return this.client.send(this.baseCrudPath() + '/refresh', {
                'method':  'POST',
                'params':  queryParams,
                'body':    bodyParams,
                'headers': {
                    'Authorization': '',
                },
            }).then(this.authResponse.bind(this));
        }
        """
        return self.client.send(self.base_crud_path() + '/refresh', {
            'method': 'POST',
            'params': query_params,
            'body': body_params,
            'headers': {
                'Authorization': '',
            }
        }).then(self.auth_response)
    
    def unlink_external_auth(self, user_id: str, provider: str, query_params: dict = {}):
        """
        /**
         * Unlink a single external auth provider from the specified user.
         */
        unlinkExternalAuth(
            userId: string,
            provider: string,
            queryParams = {}
        ): Promise<boolean> {
            return this.client.send(this.baseCrudPath() + '/' + encodeURIComponent(userId) + '/external-auths/' + encodeURIComponent(provider), {
                'method': 'DELETE',
                'params': queryParams,
            }).then(() => true);
        }
        """
        return self.client.send(self.base_crud_path() + '/' + user_id + '/external-auths/' + provider, {
            'method': 'DELETE',
            'params': query_params,
        }).then(lambda _: True)
    
    def list_auth_methods(self, query_params: dict = {}):
        """
        /**
         * Returns all available application auth methods.
         */
        listAuthMethods(queryParams = {}): Promise<AuthMethodsList> {
            return this.client.send(this.baseCrudPath() + '/auth-methods', {
                'method': 'GET',
                'params': queryParams,
            }).then((responseData: any) => {
                return Object.assign({}, responseData, {
                    // normalize common fields
                    'emailPassword':  !!responseData?.emailPassword,
                    'authProviders': Array.isArray(responseData?.authProviders) ? responseData?.authProviders : [],
                });
            });
        }
        """
        return self.client.send(self.base_crud_path() + '/auth-methods', {
            'method': 'GET',
            'params': query_params,
        }).then(AuthMethodsList(bool(response_data.get('emailPassword')), response_data.get('authProviders', []))
        )
    