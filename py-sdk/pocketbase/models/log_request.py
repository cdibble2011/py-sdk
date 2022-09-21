"""
pocketbase/models/log_request.py

declare class LogRequest extends BaseModel {
    url: string;
    method: string;
    status: number;
    auth: string;
    remoteIp: string;
    userIp: string;
    referer: string;
    userAgent: string;
    meta: null | {
        [key: string]: any;
    };
    /**
     * @inheritdoc
     */
    load(data: {
        [key: string]: any;
    }): void;
}
"""
from ..abstracts import BaseModel

class LogRequest(BaseModel):
    def __init__(self, data: dict = {}, **kwargs):
        """
        constructor(data: { [key: string]: any } = {}) { this.load(data || {}); }
        """
        self.load(data or {})

    def __repr__(self):
        return f'<LogRequest {self.__dict__}>'

    def __str__(self):
        return f'<LogRequest {self.__dict__}>'

    def load(self, data: dict):
        """
        Loads `data` into the current model.

        load(data: { [key: string]: any }) {
            super.load(data);
            this.url = typeof data.url !== 'undefined' ? data.url : '';
            this.method = typeof data.method !== 'undefined' ? data.method : '';
            this.status = typeof data.status !== 'undefined' ? data.status : 0;
            this.auth = typeof data.auth !== 'undefined' ? data.auth : '';
            this.remoteIp = typeof data.remoteIp !== 'undefined' ? data.remoteIp : '';
            this.userIp = typeof data.userIp !== 'undefined' ? data.userIp : '';
            this.referer = typeof data.referer !== 'undefined' ? data.referer : '';
            this.userAgent = typeof data.userAgent !== 'undefined' ? data.userAgent : '';
            this.meta = typeof data.meta !== 'undefined' ? data.meta : null;
        }
        """
        super().load(data)
        self.url = data.get('url', '')
        self.method = data.get('method', '')
        self.status = data.get('status', 0)
        self.auth = data.get('auth', '')
        self.remote_ip = data.get('remoteIp', '')
        self.user_ip = data.get('userIp', '')
        self.referer = data.get('referer', '')
        self.user_agent = data.get('userAgent', '')
        self.meta = data.get('meta', None)
        self._base_dict = {
            'id': self.id,
            'created': self.created,
            'updated': self.updated,
            'url': self.url,
            'method': self.method,
            'status': self.status,
            'auth': self.auth,
            'remoteIp': self.remote_ip,
            'userIp': self.user_ip,
            'referer': self.referer,
            'userAgent': self.user_agent,
            'meta':self.meta
            }
        
    def clone(self):
        return LogRequest(self._base_dict)
    
    def export(self):
        return self._base_dict
        
    def to_dict(self):
        return self._base_dict
