"""
pocketbase/ifaces/serialize_options.py

interface SerializeOptions {
    encode?: (val: string | number | boolean) => string;
    maxAge?: number;
    domain?: string;
    path?: string;
    expires?: Date;
    httpOnly?: boolean;
    secure?: boolean;
    priority?: string;
    sameSite?: boolean | string;
}
"""

class SerializeOptions:
    def __init__(self, data: dict = {}):
        """
        constructor(data: { [key: string]: any } = {}) { this.load(data || {}); }
        """
        self.load(data or {})

    def __repr__(self):
        return f'<SerializeOptions {self.__dict__}>'

    def __str__(self):
        return f'<SerializeOptions {self.__dict__}>'

    def load(self, data: dict):
        """
        Loads `data` into the current model.
        
        load(data: { [key: string]: any }) {
            this.id = typeof data.id !== 'undefined' ? data.id : '';
            this.created = typeof data.created !== 'undefined' ? data.created : '';
            this.updated = typeof data.updated !== 'undefined' ? data.updated : '';
        }
        """
        self.encode = data.get('encode', None)
        self.max_age = data.get('maxAge', None)
        self.domain = data.get('domain', None)
        self.path = data.get('path', None)
        self.expires = data.get('expires', None)
        self.http_only = data.get('httpOnly', None)
        self.secure = data.get('secure', None)
        self.priority = data.get('priority', None)
        self.same_site = data.get('sameSite', None)

    def to_dict(self):
        self._base_dict = {
            'encode': self.encode,
            'maxAge': self.max_age,
            'domain': self.domain,
            'path': self.path,
            'expires': self.expires,
            'httpOnly': self.http_only,
            'secure': self.secure,
            'priority': self.priority,
            'sameSite': self.same_site,
        }
        return self._base_dict