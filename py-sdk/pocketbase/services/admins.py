"""
pocketbase/services/admins.py

declare class Admins extends CrudService<Admin> {
    /**
     * @inheritdoc
     */
    decode(data: {
        [key: string]: any;
    }): Admin;
    /**
     * @inheritdoc
     */
    baseCrudPath(): string;
    /**
     * Prepare successful authorize response.
     */
    protected authResponse(responseData: any): AdminAuthResponse;
    /**
     * Authenticate an admin account by its email and password
     * and returns a new admin token and data.
     *
     * On success this method automatically updates the client's AuthStore data.
     */
    authViaEmail(email: string, password: string, bodyParams?: {}, queryParams?: {}): Promise<AdminAuthResponse>;
    /**
     * Refreshes the current admin authenticated instance and
     * returns a new token and admin data.
     *
     * On success this method automatically updates the client's AuthStore data.
     */
    refresh(bodyParams?: {}, queryParams?: {}): Promise<AdminAuthResponse>;
    /**
     * Sends admin password reset request.
     */
    requestPasswordReset(email: string, bodyParams?: {}, queryParams?: {}): Promise<boolean>;
    /**
     * Confirms admin password reset request.
     */
    confirmPasswordReset(passwordResetToken: string, password: string, passwordConfirm: string, bodyParams?: {}, queryParams?: {}): Promise<AdminAuthResponse>;
}
"""
from typing import Optional, Dict, Any

from ..abstracts import CrudService
from ..models import Admin
from ..types import AdminAuthResponse

class Admins(CrudService):
    def decode(self, data: Dict[str, Any]) -> Admin:
        return self._decode(data, 'Admin')

    def base_crud_path(self) -> str:
        return 'admins'

    def auth_via_email(self, email: str, password: str, body_params: Optional[Dict[str, Any]] = None, query_params: Optional[Dict[str, Any]] = None) -> AdminAuthResponse:
        """
        Authenticate an admin account by its email and password
        and returns a new admin token and data.
        
        On success this method automatically updates the client's AuthStore data.
        """
        return self._post('auth/email', body_params, query_params)

    def refresh(self, body_params: Optional[Dict[str, Any]] = None, query_params: Optional[Dict[str, Any]] = None) -> AdminAuthResponse:
        """
        Refreshes the current admin authenticated instance and
        returns a new token and admin data.
        
        On success this method automatically updates the client's AuthStore data.
        """
        return self._post('auth/refresh', body_params, query_params)

    def request_password_reset(self, email: str, body_params: Optional[Dict[str, Any]] = None, query_params: Optional[Dict[str, Any]] = None) -> bool:
        """
        Sends admin password reset request.
        """
        return self._post('auth/password-reset/request', body_params, query_params)

    def confirm_password_reset(self, password_reset_token: str, password: str, password_confirm: str, body_params: Optional[Dict[str, Any]] = None, query_params: Optional[Dict[str, Any]] = None) -> AdminAuthResponse:
        """
        Confirms admin password reset request.
        """
        return self._post('auth/password-reset/confirm', body_params, query_params)

    def auth_response(self, response_data: Dict[str, Any]) -> AdminAuthResponse:
        """
        Prepare successful authorize response.
        """
        return self._decode(response_data, 'AdminAuthResponse')
    