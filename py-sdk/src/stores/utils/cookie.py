"""
Cookie Stores

Source https://github.com/pocketbase/js-sdk/blob/master/src/stores/utils/cookie.ts

--------------------------------------------------------------------
| Simple cookie parse and serialize utilities mostly based on the  |
| node module https://github.com/jshttp/cookie.                    |
--------------------------------------------------------------------
"""
import math
from datetime import datetime
import urllib
import six
""" 
const fieldContentRegExp = /^[\u0009\u0020-\u007e\u0080-\u00ff]+$/;
"""
fieldContentRegExp = "/^[\u0009\u0020-\u007e\u0080-\u00ff]+$/"


def parse_options(val):
    """
    export interface ParseOptions{ decode?: (val: string) => string, }
    """
    if val is None:
        return {}
    if isinstance(val, dict):
        return val
    return cookie_parse(val)



def cookie_parse(string, options=None):
    """
    Parses the given cookie header string into an object
    The object has the various cookies as keys(names) => values
    
    export function cookieParse(str: string, options?: ParseOptions): { [key: string]: any }  {
        const result: { [key: string]: any } = {};

        if (typeof str !== 'string') { return result; }

        const opt    = Object.assign({}, options || {});
        const decode = opt.decode || defaultDecode;

        let index = 0;
        while (index < str.length) {
            const eqIdx = str.indexOf('=', index);

            // no more cookie pairs
            if (eqIdx === -1) { break; }

            let endIdx = str.indexOf(';', index);

            if (endIdx === -1) {
                endIdx = str.length;
            } else if (endIdx < eqIdx) {
                // backtrack on prior semicolon
                index = str.lastIndexOf(';', eqIdx - 1) + 1;
                continue;
            }

            const key = str.slice(index, eqIdx).trim();

            // only assign once
            if (undefined === result[key]) {
                let val = str.slice(eqIdx + 1, endIdx).trim();

                // quoted values
                if (val.charCodeAt(0) === 0x22) { val = val.slice(1, -1); }

                try { result[key] = decode(val); } catch (_) {
                    result[key] = val; // no decoding
                }
            }
            index = endIdx + 1;
        }

        return result;
    };
    """
    result = {}
    if not isinstance(string, str):
        return result
    opt = dict(options or {})
    decode = opt.get('decode', default_decode)
    index = 0
    while index < len(string):
        eq_idx = string.find('=', index)
        if eq_idx == -1:
            break
        end_idx = str.find(';', index)
        if end_idx == -1:
            end_idx = len(string)
        elif end_idx < eq_idx:
            index = string.rfind(';', eq_idx - 1) + 1
            continue
        key = string[index:eq_idx].strip()
        if key not in result:
            val = string[eq_idx + 1:end_idx].strip()
            if val[0] == '"':
                val = val[1:-1]
            try:
                result[key] = decode(val)
            except:
                result[key] = val
        index = end_idx + 1
    return result




def serialize_options(val):
    """
    export interface SerializeOptions{
        encode?:   (val: string | number | boolean) => string,
        maxAge?:   number,
        domain?:   string,
        path?:     string,
        expires?:  Date,
        httpOnly?: boolean,
        secure?:   boolean,
        priority?: string,
        sameSite?: boolean|string,
    }
    """
    if val is None:
        return {}
    if isinstance(val, dict):
        return val
    return cookie_serialize(val)

def default_decode(val):
    """
    Default URL-decode string value function.
    Optimized to skip native call when no `%`.
    
    function defaultDecode(val: string): string {
        return val.indexOf('%') !== -1
            ? decodeURIComponent(val)
            : val;
    }
    """
    return val if val.find('%') == -1 else urllib.parse.unquote(six.text_type(val))


def default_encode(val):
    """
    Default URL-encode value function.
    
    function defaultEncode(val: string | number | boolean): string { return encodeURIComponent(val); }
    """
    return urllib.parse.quote(val, safe='~()*!\'')

def is_date(val) -> bool:
    """
    Determines if value is a Date.
    
    function isDate(val: any): boolean {
        return (
            Object.prototype.toString.call(val) === '[object Date]' ||
            val instanceof Date
        );
    }
    """
    return isinstance(val, [datetime, str])



def cookie_serialize(name, val, options=None):
    """
    Serialize data into a cookie header.
    
    Serialize the a name value pair into a cookie string suitable for
    http headers. An optional options object specified cookie parameters.
    ```js
    cookieSerialize('foo', 'bar', { httpOnly: true }) // "foo=bar; httpOnly"
    ```
    
    export function cookieSerialize(name: string, val: string, options?: SerializeOptions): string {
        const opt    = Object.assign({}, options || {});
        const encode = opt.encode || defaultEncode;

        if (!fieldContentRegExp.test(name)) {
            throw new TypeError('argument name is invalid');
        }

        const value = encode(val);

        if (value && !fieldContentRegExp.test(value)) {
            throw new TypeError('argument val is invalid');
        }

        let result = name + '=' + value;

        if (opt.maxAge != null) {
            const maxAge = opt.maxAge - 0;

            if (isNaN(maxAge) || !isFinite(maxAge)) {
                throw new TypeError('option maxAge is invalid');
            }

            result += '; Max-Age=' + Math.floor(maxAge);
        }

        if (opt.domain) {
            if (!fieldContentRegExp.test(opt.domain)) {
                throw new TypeError('option domain is invalid');
            }

            result += '; Domain=' + opt.domain;
        }

        if (opt.path) {
            if (!fieldContentRegExp.test(opt.path)) {
                throw new TypeError('option path is invalid');
            }

            result += '; Path=' + opt.path;
        }

        if (opt.expires) {
            if (!isDate(opt.expires) || isNaN(opt.expires.valueOf())) {
                throw new TypeError('option expires is invalid');
            }

            result += '; Expires=' + opt.expires.toUTCString();
        }

        if (opt.httpOnly) {
            result += '; HttpOnly';
        }

        if (opt.secure) {
            result += '; Secure';
        }

        if (opt.priority) {
            const priority = typeof opt.priority === 'string' ? opt.priority.toLowerCase() : opt.priority;

            switch (priority) {
                case 'low':
                    result += '; Priority=Low';
                    break;
                case 'medium':
                    result += '; Priority=Medium';
                    break;
                case 'high':
                    result += '; Priority=High';
                    break;
                default:
                    throw new TypeError('option priority is invalid');
            }
        }

        if (opt.sameSite) {
            const sameSite = typeof opt.sameSite === 'string' ? opt.sameSite.toLowerCase() : opt.sameSite;

            switch (sameSite) {
                case true:
                    result += '; SameSite=Strict';
                    break;
                case 'lax':
                    result += '; SameSite=Lax';
                    break;
                case 'strict':
                    result += '; SameSite=Strict';
                    break;
                case 'none':
                    result += '; SameSite=None';
                    break;
                default:
                    throw new TypeError('option sameSite is invalid');
            }
        }

        return result;
    };
    """
    opt = dict(options or {})
    encode = opt.get('encode', default_encode)
    if not fieldContentRegExp.test(name):
        raise TypeError('argument name is invalid')
    value = encode(val)
    if value and not fieldContentRegExp.test(value):
        raise TypeError('argument val is invalid')
    result = name + '=' + value
    if opt.get('maxAge') is not None:
        max_age = opt['maxAge'] - 0
        if math.isnan(max_age) or not math.isfinite(max_age):
            raise TypeError('option maxAge is invalid')
        result += '; Max-Age=' + math.floor(max_age)
    if opt.get('domain'):
        if not fieldContentRegExp.test(opt['domain']):
            raise TypeError('option domain is invalid')
        result += '; Domain=' + opt['domain']
    if opt.get('path'):
        if not fieldContentRegExp.test(opt['path']):
            raise TypeError('option path is invalid')
        result += '; Path=' + opt['path']
    if opt.get('expires'):
        if not is_date(opt['expires']) or math.isnan(opt['expires'].valueOf()):
            raise TypeError('option expires is invalid')
        result += '; Expires=' + opt['expires'].toUTCString()
    if opt.get('httpOnly'):
        result += '; HttpOnly'
    if opt.get('secure'):
        result += '; Secure'
    if opt.get('priority'):
        priority = opt['priority'].lower() if isinstance(opt['priority'], str) else opt['priority']
        if priority == 'low':
            result += '; Priority=Low'
        elif priority == 'medium':
            result += '; Priority=Medium'
        elif priority == 'high':
            result += '; Priority=High'
        else:
            raise TypeError('option priority is invalid')
    if opt.get('sameSite'):
        same_site = opt['sameSite'].lower() if isinstance(opt['sameSite'], str) else opt['sameSite']
        if same_site is True:
            result += '; SameSite=Strict'
        elif same_site == 'lax':
            result += '; SameSite=Lax'
        elif same_site == 'strict':
            result += '; SameSite=Strict'
        elif same_site == 'none':
            result += '; SameSite=None'
        else:
            raise TypeError('option sameSite is invalid')
    return result

