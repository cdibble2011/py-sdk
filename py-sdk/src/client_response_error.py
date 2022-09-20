"""
Client Response Error

Source: https://github.com/pocketbase/js-sdk/blob/master/src/ClientResponseError.ts

ClientResponseError is a custom Error class that is intended to wrap
and normalize any error thrown by `Client.send()`.
"""

class ClientResponseError(Exception):
    """
    ClientResponseError is a custom Error class that is intended to wrap
    and normalize any error thrown by `Client.send()`.
    
    export default class ClientResponseError extends Error {
        url: string                = '';
        status: number             = 0;
        data: {[key: string]: any} = {};
        isAbort:  boolean          = false;
        originalError: any         = null;    
    }
    """
    # constructor(errData?: any) { }
    def __init__(self, err_data = None):
        # super("ClientResponseError");
        super().__init__("ClientResponseError")
        # // Set the prototype explicitly.
        # // https://github.com/Microsoft/TypeScript-wiki/blob/main/Breaking-Changes.md#extending-built-ins-like-error-array-and-map-may-no-longer-work
        # Object.setPrototypeOf(this, ClientResponseError.prototype);
        self.url = ''
        self.status = 0
        self.data = {}
        self.is_abort = False
        self.original_error = None
        # if (!(errData instanceof ClientResponseError)) { this.originalError = errData; }
        if not isinstance(err_data, ClientResponseError):
            self.original_error = err_data
            
        # if (errData !== null && typeof errData === 'object') {
        #     this.url    = typeof errData.url === 'string' ? errData.url : '';
        #     this.status = typeof errData.status === 'number' ? errData.status : 0;
        #     this.data   = errData.data !== null && typeof errData.data === 'object' ? errData.data : {};
        # }
        if err_data is not None and isinstance(err_data, dict):
            self.url = err_data.get('url', '')
            self.status = err_data.get('status', 0)
            self.data = err_data.get('data', {})
            
        # if (typeof DOMException !== 'undefined' && errData instanceof DOMException) { this.isAbort = true; }
        if 'DOMException' in globals() and isinstance(err_data, Exception):
            self.is_abort = True
        # this.name = "ClientResponseError " + this.status;
        self.name = "ClientResponseError " + str(self.status)
        # this.message = this.data?.message || 'Something went wrong while processing your request.'
        self.message = self.data.get('message', 'Something went wrong while processing your request.')
        # // Make a POJO's copy of the current error class instance.
        # // @see https://github.com/vuex-orm/vuex-orm/issues/255
        # toJSON () { return { ...this }; }