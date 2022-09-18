"""
JWT Stores

Source https://github.com/pocketbase/js-sdk/blob/master/src/stores/utils/jwt.ts
"""
import base64
import json
import time

def a_to_b_polyfill(atob):
    """
    let atobPolyfill: Function;
    if (typeof atob === 'function') {
        atobPolyfill = atob
    } else {
        atobPolyfill = (a: any) => Buffer.from(a, 'base64').toString('binary');
    }
    """
    if isinstance(atob, str):
        return base64.b64decode(atob).decode('utf-8')
    else:
        return None

def get_token_payload(token: str):
    """
    /**
     * Returns JWT token's payload data.
     */
    export function getTokenPayload(token: string): { [key: string]: any } {
        if (token) {
            try {

                let base64 = decodeURIComponent(atobPolyfill(token.split('.')[1]).split('').map(function (c: string) {
                    return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
                }).join(''));

                return JSON.parse(base64) || {};
            } catch (e) {
            }
        }

        return {};
    }
    """
    if isinstance(token, str):
        try:
            base64 = a_to_b_polyfill(token.split('.')[1])
            return json.loads(base64)
        except:
            pass
    return {}

def is_token_expired(token: str, expiration_threshold: int = 0) -> bool:
    """
    /**
     * Checks whether a JWT token is expired or not.
     * Tokens without `exp` payload key are considered valid.
     * Tokens with empty payload (eg. invalid token strings) are considered expired.
     *
     * @param token The token to check.
     * @param [expirationThreshold] Time in seconds that will be subtracted from the token `exp` property.
     */
    export function isTokenExpired(token: string, expirationThreshold = 0): boolean {
        let payload = getTokenPayload(token);

        if (
            Object.keys(payload).length > 0 &&
            (!payload.exp || (payload.exp - expirationThreshold) > (Date.now() / 1000))
        ) {
            return false;
        }

        return true;
    }
    """
    payload = get_token_payload(token)
    if len(payload) > 0 and ('exp' not in payload or (payload['exp'] - expiration_threshold) > (time.time() / 1000)):
        return False
    return True