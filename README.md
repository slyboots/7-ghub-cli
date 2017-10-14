# ghub cli #
*A simple cli for managing github repos*

## Overview ##
The primary goal of this project is to make the information for all of my other project more immediately available to me.
Up until recently, I didn't mind clicking through all of github to start a new repo, but now that I'm trying to create something each week my initial workflow has become a bunch of annoying steps and I'm lazy.

### The annoying process of starting a project on github: ###
- Navigate to github.com and fill out the log in form.
- Wait for the two factor authentication text to be sent to my phone.
- Type the code in
- Better retype it just to make sure I got it right so I dont have to wait for a new code
- Fill out the forms to create the repo(s) on github.com
- Grab the url after watching the page to reload so I can clone it locally
- Manually transfer over any brainstorming I'd done while messing around in to the new project folder
- start the whole project setup process (This isnt to bad with scaffolding tools)
- Eventually have to manually copy project info to my blog
- Start editing and formatting it for the blog post
- meh...

__I want to:__
- Create a remote repo for a project without leaving the terminal I'm brainstorming in
- Delete those repos just as fast if the idea doesnt come together as hoped
- Grab project info thats ready to be used while editing my blog without leaving my text editor
- Hike the Appalachian Trail and become friends with a bear.

I should be able to get at least 3/4 easy.

## Details ##

### Requirements ###
- [Python 3.6](python.org)
- [Requests](http://docs.python-requests.org/en/master/)

### Installation ###
1. clone the repo
2. cd into the project directory
3. install using something similar to: `pip3 install --editable . --user`
4. confirm installation by running: `ghub -h` in your terminal

And you're done. If you get to step 4 and it doesn't work, you're on your own!
### Usage ### 
In a termial run: `ghub -h` or `ghub new -h`

### Examples ###
- Help text for __ghub__ command:

    ```
    usage: ghub [-h] {new} ...
    
    a simple cli for managing github repos.
    
    positional arguments:
      {new}       sub-command help
        new       create a new remote repository
    
    optional arguments:
      -h, --help  show this help message and exit
    ```
- Help text for __ghub new__ command:
    ```
    usage: ghub new [-h] [-d DESCRIPTION] [-u URL] [-p] [-I] [-J] [-W] [-a]
                    [-gi GITIGNORE] [-li LICENSE]
                    name
    
    positional arguments:
      name                  name of the remote repo
    
    optional arguments:
      -h, --help            show this help message and exit
      -d DESCRIPTION, --description DESCRIPTION
                            short description of the repo
      -u URL, --url URL     A URL with more info about the repo
      -p, --private         Pass to create a private repo
      -I, --noissues        Disable issues for the repo
      -J, --noprojects      Disable projects for the repo
      -W, --nowiki          Disable wiki for repo
      -a, --autoinit        Create repo with empty README commited
      -gi GITIGNORE, --gitignore GITIGNORE
                            Choose one of these .gitignore templates for the
                            project: Actionscript, Ada, Agda, Android,     AppEngine,
                            AppceleratorTitanium, ArchLinuxPackages, Autotools,     C,
                            C++, CFWheels, CMake, CUDA, CakePHP, ChefCookbook,
                            Clojure, CodeIgniter, CommonLisp, Composer,     Concrete5,
                            Coq, CraftCMS, D, DM, Dart, Delphi, Drupal,     EPiServer,
                            Eagle, Elisp, Elixir, Elm, Erlang,     ExpressionEngine,
                            ExtJs, Fancy, Finale, ForceDotCom, Fortran,     FuelPHP,
                            GWT, GitBook, Go, Gradle, Grails, Haskell, IGORPro,
                            Idris, Java, Jboss, Jekyll, Joomla, Julia, KiCAD,
                            Kohana, LabVIEW, Laravel, Leiningen, LemonStand,
                            Lilypond, Lithium, Lua, Magento, Maven, Mercury,
                            MetaProgrammingSystem, Nim, Node, OCaml,     Objective-C,
                            Opa, OracleForms, Packer, Perl, Phalcon,
                            PlayFramework, Plone, Prestashop, Processing,
                            PureScript, Python, Qooxdoo, Qt, R, ROS, Rails,
                            RhodesRhomobile, Ruby, Rust, SCons, Sass, Scala,
                            Scheme, Scrivener, Sdcc, SeamGen, SketchUp,     Smalltalk,
                            SugarCRM, Swift, Symfony, SymphonyCMS, TeX,     Terraform,
                            Textpattern, TurboGears2, Typo3, Umbraco, Unity,
                            UnrealEngine, VVVV, VisualStudio, Waf, WordPress,
                            Xojo, Yeoman, Yii, ZendFramework, Zephir, gcov,     nanoc,
                            opencart, stella
      -li LICENSE, --license LICENSE
                            Choose one of these license templates for the     project:
                            mit, apache-2.0, agpl-3.0, lgpl-2.1, bsd-3-clause,
                            gpl-2.0, mpl-2.0, gpl-3.0, bsd-2-clause, lgpl-3.0,
                            unlicense, epl-1.0
    ```
