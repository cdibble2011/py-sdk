"""
pocketbase/services/users.py

declare class Users extends CrudService<User> {
    /**
     * @inheritdoc
     */
    decode(data: {
        [key: string]: any;
    }): User;
    /**
     * @inheritdoc
     */
    baseCrudPath(): string;
    /**
     * Prepare successful authorization response.
     */
    protected authResponse(responseData: any): UserAuthResponse;
    /**
     * Returns all available application auth methods.
     */
    listAuthMethods(queryParams?: {}): Promise<AuthMethodsList>;
    /**
     * Authenticate a user via its email and password.
     *
     * On success, this method also automatically updates
     * the client's AuthStore data and returns:
     * - new user authentication token
     * - the authenticated user model record
     */
    authViaEmail(email: string, password: string, bodyParams?: {}, queryParams?: {}): Promise<UserAuthResponse>;
    /**
     * Authenticate a user via OAuth2 client provider.
     *
     * On success, this method also automatically updates
     * the client's AuthStore data and returns:
     * - new user authentication token
     * - the authenticated user model record
     * - the OAuth2 user profile data (eg. name, email, avatar, etc.)
     */
    authViaOAuth2(provider: string, code: string, codeVerifier: string, redirectUrl: string, bodyParams?: {}, queryParams?: {}): Promise<UserAuthResponse>;
    /**
     * Refreshes the current user authenticated instance and
     * returns a new token and user data.
     *
     * On success this method also automatically updates the client's AuthStore data.
     */
    refresh(bodyParams?: {}, queryParams?: {}): Promise<UserAuthResponse>;
    /**
     * Sends user password reset request.
     */
    requestPasswordReset(email: string, bodyParams?: {}, queryParams?: {}): Promise<boolean>;
    /**
     * Confirms user password reset request.
     */
    confirmPasswordReset(passwordResetToken: string, password: string, passwordConfirm: string, bodyParams?: {}, queryParams?: {}): Promise<UserAuthResponse>;
    /**
     * Sends user verification email request.
     */
    requestVerification(email: string, bodyParams?: {}, queryParams?: {}): Promise<boolean>;
    /**
     * Confirms user email verification request.
     */
    confirmVerification(verificationToken: string, bodyParams?: {}, queryParams?: {}): Promise<UserAuthResponse>;
    /**
     * Sends an email change request to the authenticated user.
     */
    requestEmailChange(newEmail: string, bodyParams?: {}, queryParams?: {}): Promise<boolean>;
    /**
     * Confirms user new email address.
     */
    confirmEmailChange(emailChangeToken: string, password: string, bodyParams?: {}, queryParams?: {}): Promise<UserAuthResponse>;
    /**
     * Lists all linked external auth providers for the specified user.
     */
    listExternalAuths(userId: string, queryParams?: {}): Promise<Array<ExternalAuth>>;
    /**
     * Unlink a single external auth provider from the specified user.
     */
    unlinkExternalAuth(userId: string, provider: string, queryParams?: {}): Promise<boolean>;
}
"""
from typing import Optional, Dict, Any

from ..abstracts import CrudService
from ..models import User, ExternalAuth
from ..types import UserAuthResponse

class Users(CrudService):
    def decode(self, data: Dict[str, Any]) -> User:
        return User(**data)

    def base_crud_path(self) -> str:
        return '/users'

    def auth_response(self, response_data: Dict[str, Any]) -> UserAuthResponse:
        """
        Prepare successful authorization response.
        """
        return UserAuthResponse(**response_data)

    def list_auth_methods(self, query_params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Returns all available application auth methods.
        """
        return self.request('GET', '/auth/methods', query_params=query_params)

    def auth_via_email(self, email: str, password: str, body_params: Optional[Dict[str, Any]] = None, query_params: Optional[Dict[str, Any]] = None) -> UserAuthResponse:
        """
        Authenticate a user via its email and password.
        On success, this method also automatically updates
        the client's AuthStore data and returns:
         - new user authentication token
         - the authenticated user model record
        """
        body_params = body_params or {}
        body_params['email'] = email
        body_params['password'] = password
        response_data = self.request('POST', '/auth/email', body_params=body_params, query_params=query_params)
        return self.auth_response(response_data)

    def auth_via_oauth2(self, provider: str, code: str, code_verifier: str, redirect_url: str, body_params: Optional[Dict[str, Any]] = None, query_params: Optional[Dict[str, Any]] = None) -> UserAuthResponse:
        """
        Authenticate a user via OAuth2 client provider.
        
        On success, this method also automatically updates
        the client's AuthStore data and returns:
         - new user authentication token
         - the authenticated user model record
         - the OAuth2 user profile data (eg. name, email, avatar, etc.)
        """
        body_params = body_params or {}
        body_params['code'] = code
        body_params['codeVerifier'] = code_verifier
        body_params['redirectUrl'] = redirect_url
        response_data = self.request('POST', '/auth/oauth2/' + provider, body_params=body_params, query_params=query_params)
        return self.auth_response(response_data)

    def refresh(self, body_params: Optional[Dict[str, Any]] = None, query_params: Optional[Dict[str, Any]] = None) -> UserAuthResponse:
        """
        Refreshes the current user authenticated instance and
        returns a new token and user data.
     
        On success this method also automatically updates the client's AuthStore data.
        """
        response_data = self.request('POST', '/auth/refresh', body_params=body_params, query_params=query_params)
        return self.auth_response(response_data)

    def request_password_reset(self, email: str, body_params: Optional[Dict[str, Any]] = None, query_params: Optional[Dict[str, Any]] = None) -> bool:
        """
        Sends user password reset request.
        """
        body_params = body_params or {}
        body_params['email'] = email
        return self.request('POST', '/auth/password-reset', body_params=body_params, query_params=query_params)

    def confirm_password_reset(self, password_reset_token: str, password: str, password_confirm: str, body_params: Optional[Dict[str, Any]] = None, query_params: Optional[Dict[str, Any]] = None) -> UserAuthResponse:
        """
        Confirms user password reset request.
        """
        body_params = body_params or {}
        body_params['password'] = password
        body_params['passwordConfirm'] = password_confirm
        response_data = self.request('POST', '/auth/password-reset/' + password_reset_token, body_params=body_params, query_params=query_params)
        return self.auth_response(response_data)
    
    def request_verification(self, email: str, body_params: Optional[Dict[str, Any]] = None, query_params: Optional[Dict[str, Any]] = None) -> bool:
        """
        Sends user verification email request.
        """
        body_params = body_params or {}
        body_params['email'] = email
        return self.request('POST', '/auth/request-verification', body_params=body_params, query_params=query_params)
    
    def confirm_verification(self, verification_token: str, body_params: Optional[Dict[str, Any]] = None, query_params: Optional[Dict[str, Any]] = None) -> UserAuthResponse:
        """
        Confirms user email verification request.
        """
        body_params = body_params or {}
        body_params['verificationToken'] = verification_token
        return self.request('POST', '/auth/confirm-verification', body_params=body_params, query_params=query_params)
    
    def request_email_change(self, new_email: str, body_params: Optional[Dict[str, Any]] = None, query_params: Optional[Dict[str, Any]] = None) -> bool:
        """
        Sends user email change request.
        """
        body_params = body_params or {}
        body_params['newEmail'] = new_email
        return self.request('POST', '/auth/request-email-change', body_params=body_params, query_params=query_params)
    
    def confirm_email_change(self, email_change_token: str, body_params: Optional[Dict[str, Any]] = None, query_params: Optional[Dict[str, Any]] = None) -> UserAuthResponse:
        """
        Confirms user email change request.
        """
        body_params = body_params or {}
        body_params['emailChangeToken'] = email_change_token
        return self.request('POST', '/auth/confirm-email-change', body_params=body_params, query_params=query_params)
    
    def list_external_auths(self, user_id: str, query_params: Optional[Dict[str, Any]] = None) -> ExternalAuth:
        """
        List all external authentication methods linked to the user.
        """
        return self.request('GET', '/' + user_id + '/auth/external-auths', query_params=query_params)
    
    def unlink_external_auth(self, user_id: str, external_auth_id: str, query_params: Optional[Dict[str, Any]] = None) -> bool:
        """
        Unlink an external authentication method from the user.
        """
        return self.request('DELETE', '/' + user_id + '/auth/external-auths/' + external_auth_id, query_params=query_params)