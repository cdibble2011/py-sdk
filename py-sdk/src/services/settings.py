"""
Settings Service

Source: https://github.com/pocketbase/js-sdk/blob/master/src/services/Settings.ts
"""


"""
import BaseService from '@/services/utils/BaseService';
"""
from .utils import BaseService

class Settings(BaseService):
    """
    export default class Settings extends BaseService {}
    """
    def get_all(self, query_params: dict = {}):
        """
        Fetch all available app settings.
        
        getAll(queryParams = {}): Promise<{ [key: string]: any }> {
            return this.client.send('/api/settings', {
                'method': 'GET',
                'params': queryParams,
            }).then((responseData) => responseData || {});
        }
        """
        return self.client.send('/api/settings', {
            'method': 'GET',
            'params': query_params,
        }).then(lambda response_data: response_data or {})

    def update(self, body_params: dict = {}, query_params: dict = {}):
        """
        Bulk updates app settings.
        
        update(bodyParams = {}, queryParams = {}): Promise<{ [key: string]: any }> {
            return this.client.send('/api/settings', {
                'method': 'PATCH',
                'params': queryParams,
                'body':   bodyParams,
            }).then((responseData) => responseData || {});
        }
        """
        return self.client.send('/api/settings', {
            'method': 'PATCH',
            'params': query_params,
            'body':   body_params,
        }).then(lambda response_data: response_data or {})

    def test_s3(self, query_params: dict = {}):
        """
        Performs a S3 storage connection test.
        
        testS3(queryParams = {}): Promise<boolean> {
            return this.client.send('/api/settings/test/s3', {
                'method': 'POST',
                'params': queryParams,
            }).then(() => true);
        }
        """
        return self.client.send('/api/settings/test/s3', {
            'method': 'POST',
            'params': query_params,
        }).then(lambda _: True)

    def test_email(self, to_email: str, email_template: str, query_params: dict = {}):
        """
        Sends a test email.
        
        The possible `emailTemplate` values are:
        - verification
        - password-reset
        - email-change
        
        testEmail(toEmail: string, emailTemplate: string, queryParams = {}): Promise<boolean> {
            const bodyParams = {
                'email':    toEmail,
                'template': emailTemplate,
            };

            return this.client.send('/api/settings/test/email', {
                'method': 'POST',
                'params': queryParams,
                'body':   bodyParams,
            }).then(() => true);
        }
        """
        body_params = {
            'email':    to_email,
            'template': email_template,
        }

        return self.client.send('/api/settings/test/email', {
            'method': 'POST',
            'params': query_params,
            'body':   body_params,
        }).then(lambda _: True)