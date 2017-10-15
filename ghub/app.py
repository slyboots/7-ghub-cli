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
USER_NAME = os.getenv('GITHUB_USER_NAME')
# license template list created using the github api
# https://api.github.com/licenses
LICENSES = [
    "lgpl-3.0",
    "bsd-3-clause",
    "lgpl-2.1",
    "mit",
    "apache-2.0",
    "epl-1.0",
    "unlicense",
    "agpl-3.0",
    "mpl-2.0",
    "bsd-2-clause",
    "gpl-3.0",
    "gpl-2.0"
]
# getignore template list created using the github api.
# https://api.github.com/gitignore/templates
GITIGNORES = [
    "Actionscript",
    "Ada",
    "Agda",
    "Android",
    "AppEngine",
    "AppceleratorTitanium",
    "ArchLinuxPackages",
    "Autotools",
    "C",
    "C++",
    "CFWheels",
    "CMake",
    "CUDA",
    "CakePHP",
    "ChefCookbook",
    "Clojure",
    "CodeIgniter",
    "CommonLisp",
    "Composer",
    "Concrete5",
    "Coq",
    "CraftCMS",
    "D",
    "DM",
    "Dart",
    "Delphi",
    "Drupal",
    "EPiServer",
    "Eagle",
    "Elisp",
    "Elixir",
    "Elm",
    "Erlang",
    "ExpressionEngine",
    "ExtJs",
    "Fancy",
    "Finale",
    "ForceDotCom",
    "Fortran",
    "FuelPHP",
    "GWT",
    "GitBook",
    "Go",
    "Gradle",
    "Grails",
    "Haskell",
    "IGORPro",
    "Idris",
    "Java",
    "Jboss",
    "Jekyll",
    "Joomla",
    "Julia",
    "KiCAD",
    "Kohana",
    "LabVIEW",
    "Laravel",
    "Leiningen",
    "LemonStand",
    "Lilypond",
    "Lithium",
    "Lua",
    "Magento",
    "Maven",
    "Mercury",
    "MetaProgrammingSystem",
    "Nim",
    "Node",
    "OCaml",
    "Objective-C",
    "Opa",
    "OracleForms",
    "Packer",
    "Perl",
    "Phalcon",
    "PlayFramework",
    "Plone",
    "Prestashop",
    "Processing",
    "PureScript",
    "Python",
    "Qooxdoo",
    "Qt",
    "R",
    "ROS",
    "Rails",
    "RhodesRhomobile",
    "Ruby",
    "Rust",
    "SCons",
    "Sass",
    "Scala",
    "Scheme",
    "Scrivener",
    "Sdcc",
    "SeamGen",
    "SketchUp",
    "Smalltalk",
    "SugarCRM",
    "Swift",
    "Symfony",
    "SymphonyCMS",
    "TeX",
    "Terraform",
    "Textpattern",
    "TurboGears2",
    "Typo3",
    "Umbraco",
    "Unity",
    "UnrealEngine",
    "VVVV",
    "VisualStudio",
    "Waf",
    "WordPress",
    "Xojo",
    "Yeoman",
    "Yii",
    "ZendFramework",
    "Zephir",
    "gcov",
    "nanoc",
    "opencart",
    "stella"
]


# subcommand functions
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
    if res.status_code == 201:
        print(f"Repository {args.name} successfully created at:\n"
              f"https://github.com/{USER_NAME}/{args.name}")
    print(res.json())


def rm_entry_func(args):
    '''
    entry func for the rm sub-command
    deletes a remote repository
    '''
    repo_endpoint = f"{API_URL}/repos/{USER_NAME}/{args.name}"
    res = requests.delete(repo_endpoint)
    res.raise_for_status()
    if res.status_code == 204:
        print(f"Repository {args.name} successfully deleted!")
    else:
        print(res.json())


# argparse code
PARSER = ArgParser(
    prog='ghub',
    description='a simple cli for managing github repos.'
)
SUBPARSERS = PARSER.add_subparsers(help='sub-command help')

# new repository sub-command
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


RM_SUBPARSER = SUBPARSERS.add_parser(
    'rm', help='delete a remote repo'
)
RM_SUBPARSER.add_argument(
    'name',
    help='name of the remote repo'
)
RM_SUBPARSER.set_defaults(func=rm_entry_func)


# main entry func
def entry_func():
    try:
        if ACCESS_TOKEN is None:
            raise EnvironmentError
        if USER_NAME is None:
            raise EnvironmentError
        ARGS = PARSER.parse_args()
        ARGS.func(ARGS)
    except EnvironmentError:
        print("ERROR: Missing required environment variables.\n"
              "Are GITHUB_ACCESS_TOKEN and GITHUB_USER_NAME set?")
    except AttributeError as atr_err:
        print(f"ERROR: {atr_err}")
        PARSER.print_help()
    except Exception as err:
        print(f"unknown error: {err}")


if __name__ == '__main__':
    entry_func()
