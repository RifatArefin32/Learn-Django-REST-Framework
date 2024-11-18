# Authentication
- Super class of all authentication is `BaseAuthentication`

## Types of Authentication Classes
- BasicAuthentication: validating username and password
- SessionAuthentication: validating sessions whether logged in
- TokenAuthentication: Auth by passing token key
- RemoteUserAuthentication: Remote auth

## Setting Authentication
- Globally for all views (at settings.py)
- Specific view (at class based view)
- Specific view (at function based view - decorator)

## Token Authentication Steps
- First add `'rest_framework.authtoken'` to the `INSTALLED_APPS` array. The `rest_framework.authtoken` app provides Django database migrations.
- Run a migration for differnet authentication 
- 
- 
