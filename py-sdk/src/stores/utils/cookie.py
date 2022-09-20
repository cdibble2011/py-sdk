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

# const fieldContentRegExp = /^[<left slash>u0009<left slash>u0020-<left slash>u007e<left slash>u0080-<left slash>u00ff]+$/;
field_content_reg_exp = "/^[\u0009\u0020-\u007e\u0080-\u00ff]+$/"


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

    """
    # export function cookieParse(str: string, options?: ParseOptions): { [key: string]: any }  {
        # const result: { [key: string]: any } = {};
    result = {}

        # if (typeof str !== 'string') { return result; }
    if not isinstance(string, str):
        return result
        # const opt    = Object.assign({}, options || {});
    opt = dict(options or {})
        # const decode = opt.decode || defaultDecode;
    decode = opt.get('decode', default_decode)
        # let index = 0;
    index = 0
        # while (index < str.length) {
    while index < len(string):
            # const eqIdx = str.indexOf('=', index);
        eq_idx = string.find('=', index)
            # // no more cookie pairs
            # if (eqIdx === -1) { break; }
        if eq_idx == -1:
            break
            # let endIdx = str.indexOf(';', index);
        end_idx = str.find(';', index)
            # if (endIdx === -1) {
        if end_idx == -1:
                # endIdx = str.length;
            end_idx = len(string)
            # } else if (endIdx < eqIdx) {
        elif end_idx < eq_idx:
                # // backtrack on prior semicolon
                # index = str.lastIndexOf(';', eqIdx - 1) + 1;
            index = string.rfind(';', eq_idx - 1) + 1
                # continue; }
            continue
            # const key = str.slice(index, eqIdx).trim();
        key = string[index:eq_idx].strip()
            # // only assign once
            # if (undefined === result[key]) {
        if key not in result:
            # let val = str.slice(eqIdx + 1, endIdx).trim();
            val = string[eq_idx + 1:end_idx].strip()
            # // quoted values
            # if (val.charCodeAt(0) === 0x22) { val = val.slice(1, -1); }
            if val[0] == '"':
                val = val[1:-1]
                # try { result[key] = decode(val); }  }
            try:
                result[key] = decode(val)
                # catch (_) { result[key] = val; // no decoding } }
            except:
                result[key] = val
            # index = endIdx + 1; }
        index = end_idx + 1
        # return result; }
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
    """
    # export function cookieSerialize(name: string, val: string, options?: SerializeOptions): string {
        # const opt    = Object.assign({}, options || {});
    opt = dict(options or {})
        # const encode = opt.encode || defaultEncode;
    encode = opt.get('encode', default_encode)
        # if (!fieldContentRegExp.test(name)) { throw new TypeError('argument name is invalid'); }
    if not field_content_reg_exp.test(name):
        raise TypeError('argument name is invalid')
        # const value = encode(val);
    value = encode(val)
        # if (value && !fieldContentRegExp.test(value)) { throw new TypeError('argument val is invalid'); }
    if value and not field_content_reg_exp.test(value):
        raise TypeError('argument val is invalid')
        # let result = name + '=' + value;
    result = name + '=' + value
        # if (opt.maxAge != null) { const maxAge = opt.maxAge - 0;
    if opt.get('maxAge') is not None:
        max_age = opt['maxAge'] - 0
            # if (isNaN(maxAge) || !isFinite(maxAge)) { throw new TypeError('option maxAge is invalid'); }
        if math.isnan(max_age) or not math.isfinite(max_age):
            raise TypeError('option maxAge is invalid')
            # result += '; Max-Age=' + Math.floor(maxAge); }
        result += '; Max-Age=' + math.floor(max_age)
        # if (opt.domain) {
    if opt.get('domain'):
            # if (!fieldContentRegExp.test(opt.domain)) { throw new TypeError('option domain is invalid'); }
        if not field_content_reg_exp.test(opt['domain']):
            raise TypeError('option domain is invalid')
            # result += '; Domain=' + opt.domain; }
        result += '; Domain=' + opt['domain']
        # if (opt.path) {
    if opt.get('path'):
            # if (!fieldContentRegExp.test(opt.path)) { throw new TypeError('option path is invalid'); }
        if not field_content_reg_exp.test(opt['path']):
            raise TypeError('option path is invalid')
            # result += '; Path=' + opt.path; }
        result += '; Path=' + opt['path']
        # if (opt.expires) {
    if opt.get('expires'):
            # if (!isDate(opt.expires) || isNaN(opt.expires.valueOf())) { throw new TypeError('option expires is invalid'); }
        if not is_date(opt['expires']) or math.isnan(opt['expires'].valueOf()):
            raise TypeError('option expires is invalid')
            # result += '; Expires=' + opt.expires.toUTCString(); }
        result += '; Expires=' + opt['expires'].toUTCString()
        # if (opt.httpOnly) { result += '; HttpOnly'; }
    if opt.get('httpOnly'):
        result += '; HttpOnly'
        # if (opt.secure) { result += '; Secure'; }
    if opt.get('secure'):
        result += '; Secure'
        # if (opt.priority) {
    if opt.get('priority'):
            # const priority = typeof opt.priority === 'string' ? opt.priority.toLowerCase() : opt.priority;
        priority = opt['priority'].lower() if isinstance(opt['priority'], str) else opt['priority']
            # switch (priority) {
            # case 'low':     
        if priority == 'low':
                # result += '; Priority=Low';
                # break;
            result += '; Priority=Low'
            # case 'medium': 
        elif priority == 'medium':
                # result += '; Priority=Medium';
                # break;
            result += '; Priority=Medium'
            # case 'high': 
        elif priority == 'high':
                # result += '; Priority=High';
                # break;
            result += '; Priority=High'
            # case 'none':
        elif priority == 'none':
                # result += '; SameSite=None';
                # break;
            result += '; SameSite=None'
            # default:
        else:
                # throw new TypeError('option priority is invalid');
            raise TypeError('option priority is invalid')
        # if (opt.sameSite) {
    if opt.get('sameSite'):
            # const sameSite = typeof opt.sameSite === 'string' ? opt.sameSite.toLowerCase() : opt.sameSite;
        same_site = opt['sameSite'].lower() if isinstance(opt['sameSite'], str) else opt['sameSite']
            # switch (sameSite) {
                # case true:
        if same_site is True:
                    # result += '; SameSite=Strict';
                    # break;
            result += '; SameSite=Strict'
                # case 'lax':
        elif same_site == 'lax':
                    # result += '; SameSite=Lax';
                    # break;
            result += '; SameSite=Lax'
                # case 'strict':
        elif same_site == 'strict':
                    # result += '; SameSite=Strict';
                    # break;
            result += '; SameSite=Strict'
                # case 'none':
        elif same_site == 'none':
                    # result += '; SameSite=None';
                    # break; 
            result += '; SameSite=None'
                # default:
        else:
                    # throw new TypeError('option sameSite is invalid'); } }
            raise TypeError('option sameSite is invalid')
        # return result; }
    return result

