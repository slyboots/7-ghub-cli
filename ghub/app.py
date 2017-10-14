import os
import sys
import json
import argparse
from argparse import ArgumentParser as ArgParser
from argparse import _SubParsersAction as SubParsers

import requests

# configuration variable definitions
API_URL = 'https://api.github.com'
ACCESS_TOKEN = os.getenv('GITHUB_ACCESS_TOKEN')

# utility functions


def get_gitignores():
    '''get list of github .gitignore templates'''
    return requests.get(f"{API_URL}/gitignore/templates").json()


def get_licenses():
    '''get list of github license templates'''
    accept_header = {'Accept': 'application/vnd.github.drax-preview+json'}
    licenses = requests.get(f"{API_URL}/licenses",
                            headers=accept_header).json()
    return [l['key'] for l in licenses]


def new_entry_func(args):
    '''
    entry func for new sub-command
    creates dictionary using values supplied
    and POSTs to the /user/repos endpoint.
    creating repos for organization accounts isnt supported because I'm lazy
    '''
    repo_endpoint = f"{API_URL}/user/repos"
    req_header = {
        'Accept': "application/json",
        'Authorization': f"token {ACCESS_TOKEN}"
    }
    new_repo_data = json.dumps({
        'name': args.name,
        'description': args.description,
        'homepage': args.url,
        'private': args.private,
        'has_issues': args.noissues,
        'has_projects': args.noprojects,
        'has_wiki': args.nowiki,
        'auto_init': args.autoinit,
        'gitignore_template': args.gitignore,
        'license_template': args.license
    })
    res = requests.post(repo_endpoint, data=new_repo_data, headers=req_header)
    res.raise_for_status()
    print(res.json())


# argparse code
PARSER = ArgParser(
    prog='ghub',
    description='a simple cli for managing github repos.'
)
SUBPARSERS = PARSER.add_subparsers(help='sub-command help')

# new repository sub-command
GITIGNORES = get_gitignores()
LICENSES = get_licenses()

NEW_SUBPARSER = SUBPARSERS.add_parser(
    'new', help='create a new remote repository'
)
NEW_SUBPARSER.add_argument(
    'name',
    help='name of the remote repo'
)
NEW_SUBPARSER.add_argument(
    '-d', '--description',
    help='short description of the repo'
)
NEW_SUBPARSER.add_argument(
    '-u', '--url',
    help='A URL with more info about the repo'
)
NEW_SUBPARSER.add_argument(
    '-p', '--private',
    help='Pass to create a private repo',
    action='store_true'
)
NEW_SUBPARSER.add_argument(
    '-I', '--noissues',
    help='Disable issues for the repo',
    action='store_false'
)
NEW_SUBPARSER.add_argument(
    '-J', '--noprojects',
    help='Disable projects for the repo',
    action='store_false'
)
NEW_SUBPARSER.add_argument(
    '-W', '--nowiki',
    help='Disable wiki for repo',
    action='store_false'
)
NEW_SUBPARSER.add_argument(
    '-a', '--autoinit',
    help='Create repo with empty README commited',
    action='store_true'
)
NEW_SUBPARSER.add_argument(
    '-gi', '--gitignore',
    help=f"""Choose one of these .gitignore templates for the project:
    {', '.join(GITIGNORES)}""",
    choices=GITIGNORES,
    metavar='GITIGNORE'
)
NEW_SUBPARSER.add_argument(
    '-li', '--license',
    help=f"""Choose one of these license templates for the project:
    {', '.join(LICENSES)}""",
    choices=LICENSES,
    metavar='LICENSE'
)
NEW_SUBPARSER.set_defaults(func=new_entry_func)

# main entry func


def entry_func():
    try:
        if ACCESS_TOKEN is None:
            raise EnvironmentError
        ARGS = PARSER.parse_args()
        ARGS.func(ARGS)
    except EnvironmentError:
        print("ERROR: No value for github access token.\n"
              "Is the GITHUB_ACCESS_TOKEN environment variable set?")
    except AttributeError as atr_err:
        print(f"ERROR: {atr_err}")
        PARSER.print_help()
    except Exception as err:
        print(f"unknown error: {err}")


if __name__ == '__main__':
    entry_func()
