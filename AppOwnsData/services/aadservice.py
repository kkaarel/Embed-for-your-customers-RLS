# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

from flask import current_app as app
import msal

class AadService:

    def get_access_token():
        '''Generates and returns Access token

        Returns:
            string: Access token
        '''

        response = None
        try:

            if app.config['AUTHENTICATION_MODE'].lower() == 'serviceprincipal':
                authority = app.config['AUTHORITY_URL'].replace('organizations', app.config['TENANT_ID'])
                clientapp = msal.ConfidentialClientApplication(app.config['CLIENT_ID'], client_credential=app.config['CLIENT_SECRET'], authority=authority)

                # Make a client call if Access token is not available in cache
                response = clientapp.acquire_token_for_client(scopes=app.config['SCOPE_BASE'])

            try:
                return response['access_token']
            except KeyError:
                raise Exception(response['error_description'])

        except Exception as ex:
            raise Exception('Error retrieving Access token\n' + str(ex))