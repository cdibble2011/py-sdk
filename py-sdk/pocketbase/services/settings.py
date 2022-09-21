"""
pocketbase/services/settings.py

declare class Settings extends BaseService {
    /**
     * Fetch all available app settings.
     */
    getAll(queryParams?: {}): Promise<{
        [key: string]: any;
    }>;
    /**
     * Bulk updates app settings.
     */
    update(bodyParams?: {}, queryParams?: {}): Promise<{
        [key: string]: any;
    }>;
    /**
     * Performs a S3 storage connection test.
     */
    testS3(queryParams?: {}): Promise<boolean>;
    /**
     * Sends a test email.
     *
     * The possible `emailTemplate` values are:
     * - verification
     * - password-reset
     * - email-change
     */
    testEmail(toEmail: string, emailTemplate: string, queryParams?: {}): Promise<boolean>;
}
"""
from typing import Optional, Dict, Any
from ..abstracts import BaseService

class Settings(BaseService):
    def get_all(self, query_params: Optional[dict] = None) -> Dict[Any]:
        """
        Fetch all available app settings.
        
        getAll(queryParams?: {}) {
            return this.request.get('/settings', queryParams);
        }
        """
        return self.request.get('/settings', query_params)

    def update(self, body_params: Optional[dict] = None, query_params: Optional[dict] = None) -> Dict[Any]:
        """
        Bulk updates app settings.
        
        update(bodyParams?: {}, queryParams?: {}) {
            return this.request.put('/settings', bodyParams, queryParams);
        }
        """
        return self.request.put('/settings', body_params, query_params)

    def test_S3(self, query_params: Optional[dict] = None) -> bool:
        """
        Performs a S3 storage connection test.
        
        testS3(queryParams?: {}) {
            return this.request.get('/settings/test-s3', queryParams);
        }
        """
        return self.request.get('/settings/test-s3', query_params)

    def test_email(self, to_email: str, email_template: str, query_params: Optional[dict] = None) -> bool:
        """
        Sends a test email.
        
        The possible `emailTemplate` values are:
        - verification
        - password-reset
        - email-change
        
        testEmail(toEmail: string, emailTemplate: string, queryParams?: {}) {
            return this.request.get(`/settings/test-email/${toEmail}/${emailTemplate}`, queryParams);
        }
        """
        return self.request.get(f'/settings/test-email/{to_email}/{email_template}', query_params)