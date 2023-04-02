from jira import Jira
import os
from dotenv import load_dotenv
load_dotenv()


jira_token = os.getenv('jira_token')
jira_email = os.getenv('jira_email')

jira = Jira('https://webdream.atlassian.net', jira_token, jira_email)

jira.issue_create('WEB', 'jira summary 2', 'jira_manger description')

jira.issue_update('WEB-121', 'SUMMARY FIELD', 'description that')

jira.issue_delete('WEB-120')

jira.issue_get('WEB-122')
