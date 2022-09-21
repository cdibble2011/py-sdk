"""
pocketbase/types/auth_response.py

type AdminAuthResponse = {
    [key: string]: any;
    token: string;
    admin: Admin;
};

type UserAuthResponse = {
    [key: string]: any;
    token: string;
    user: User;
};

type AuthProviderInfo = {
    name: string;
    state: string;
    codeVerifier: string;
    codeChallenge: string;
    codeChallengeMethod: string;
    authUrl: string;
};

type AuthMethodsList = {
    [key: string]: any;
    emailPassword: boolean;
    authProviders: Array<AuthProviderInfo>;
};
"""
from typing import List
from ..models import Admin, User

class AdminAuthResponse:
    def __init__(self, token: str, admin: Admin):
        self.token = token
        self.admin = admin

class UserAuthResponse:
    def __init__(self, token: str, user: User):
        self.token = token
        self.user = user

class AuthProviderInfo:
    def __init__(self, name: str, state: str, code_verifier: str, code_challenge: str, code_challenge_method: str, auth_url: str):
        self.name = name
        self.state = state
        self.code_verifier = code_verifier
        self.code_challenge = code_challenge
        self.code_challenge_method = code_challenge_method
        self.auth_url = auth_url
        
class AuthMethodsList:
    def __init__(self, email_password: bool, auth_providers: List[AuthProviderInfo]):
        self.email_password = email_password
        self.auth_providers = auth_providers

