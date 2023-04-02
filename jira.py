import requests
import json
from requests.auth import HTTPBasicAuth


class Jira:

    def __init__(self, site, token, email):
        self.site = site
        self.auth = HTTPBasicAuth(email, token)
        self.__headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def issue_create(self, project_key, summary, description):

        url = 'https://webdream.atlassian.net/rest/api/2/issue'

        payload = json.dumps(
            {
                "fields": {
                    "project":
                        {
                            "key": project_key
                        },
                    'summary': summary,
                    'description': description,
                    'issuetype': {
                        "name": "Task"
                    }
                }
            }
        )

        response = requests.post(url, headers=self.__headers, auth=self.auth, data=payload)
        print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

    def issue_update(self, issue_key_or_id, summary, description):

        url = f"https://webdream.atlassian.net/rest/api/2/issue/{issue_key_or_id}"

        payload = json.dumps(
            {
                "update": {
                    "summary": [
                        {
                            "set": summary
                        }
                    ],

                    "description": [
                        {
                            "set": description
                        }
                    ]
                }
            }
        )
        response = requests.request(
            'PUT',
            url,
            data=payload,
            headers=self.__headers,
            auth=self.auth
        )
        print(response.text)

    def issue_delete(self, issue_key_or_id):
        url = f"https://webdream.atlassian.net/rest/api/2/issue/{issue_key_or_id}"
        response = requests.request(
            'DELETE',
            url,
            auth=self.auth
        )
        print(response.text)

    def issue_get(self, issue_key_or_id):

        url = f"https://webdream.atlassian.net/rest/api/2/issue/{issue_key_or_id}"

        response = requests.request(
            'GET',
            url,
            headers=self.__headers,
            auth=self.auth
        )
        print(response.text)

