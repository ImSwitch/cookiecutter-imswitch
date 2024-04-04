# cookiecutter-napari-plugin

[Cookiecutter] template for authoring ([npe2]-based) [napari] plugins.

**NOTE: This repo is not meant to be cloned/forked directly! Please read "Getting Started" below**

## Getting Started

### Create your plugin package

Install [Cookiecutter] and generate a new imswitch plugin project:

```bash
pip install cookiecutter
cookiecutter https://github.com/openUC2/cookiecutter-imswitch/
```

Cookiecutter prompts you for information regarding your plugin
(A new folder will be created in your current working directory):

```bash
(imswitch) (base) MacBook-Pro-43:imswitch-sim bene$ cookiecutter https://github.com/openUC2/cookiecutter-imswitch/
You've downloaded /Users/bene/.cookiecutters/cookiecutter-imswitch before. Is it okay to delete and re-download 
it? [y/n] (y): y
  [1/14] full_name (ImSwitch Developer): Benedict Diederich
  [2/14] email (yourname@example.com): benedict.diederich@leibniz-ipht.de
  [3/14] github_username_or_organization (githubuser): openuc2
  [4/14] plugin_name (imswitch-foobar): imswitch-sim
  [5/14] Select github_repository_url
    1 - https://github.com/openuc2/imswitch-sim
    2 - provide later
    Choose from [1/2] (1): 1
  [6/14] module_name (imswitch_sim): 
  [7/14] display_name (FooBar Camera): ImSwitch SIM
  [8/14] short_description (A simple plugin to use a camera from XYZ within ImSwitch): This plugin will organize image acquisition and reconstruction of structured illumination microscopy data. 
  [9/14] include_controller (y): 
  [10/14] include_manager_plugin (y): 
  [11/14] include_widget_plugin (y): 
  [12/14] use_git_tags_for_versioning (n): 
  [13/14] install_precommit (n): 
  [14/14] Select license
    1 - BSD-3
    2 - MIT
    3 - Mozilla Public License 2.0
    4 - Apache Software License 2.0
    5 - GNU LGPL v3.0
    6 - GNU GPL v3.0
    Choose from [1/2/3/4/5/6] (1): 2
```

Then the following message appears: 

```
b"\xe2\x9c\x94 Manifest for 'ImSwitch SIM' valid!"
Switched to a new branch 'main'

Your plugin template is ready!  Next steps:

1. `cd` into your new directory

     cd imswitch-sim
     # you probably want to install your new package into your env
     pip install -e .
2. Create a github repository with the name 'imswitch-sim':
   https://github.com/openuc2/imswitch-sim.git

3. Add your newly created github repo as a remote and push:

     git remote add origin https://github.com/openuc2/imswitch-sim.git
     git push -u origin main

4. The following default URLs have been added to `setup.cfg`:

    Bug Tracker = https://github.com/openuc2/imswitch-sim/issues
    Documentation = https://github.com/openuc2/imswitch-sim#README.md
    Source Code = https://github.com/openuc2/imswitch-sim
    User Support = https://github.com/openuc2/imswitch-sim/issues

    These URLs will be displayed on your plugin's imswitch hub page.
    You may wish to change these before publishing your plugin!
5. Read the README for more info: https://github.com/imswitch/cookiecutter-imswitch-plugin

6. We've provided a template description for your plugin page on the imswitch hub at `.imswitch-hub/DESCRIPTION.md`.
   You'll likely want to edit this before you publish your plugin.

7. Consider customizing the rest of your plugin metadata for display on the imswitch hub:
   https://github.com/chanzuckerberg/imswitch-hub/blob/main/docs/customizing-plugin-listing.md
```

You just created a minimal imswitch plugin, complete with tests and ready for automatic deployment!

For more detailed information on each prompt see the [prompts reference](./PROMPTS.md).

```no-highlight
napari-growth-cone-finder/
│
├── .github
│   └── workflows
│      └── test_and_deploy.yml
├── LICENSE
├── MANIFEST.in
├── napari_growth_cone_finder
│   ├── __init__.py
│   ├── _widget.py
│   ├── _controller.py
│   ├── napari.yaml
│   └── _tests
│       ├── __init__.py
│       ├── test_widget.py
│       └── test_controller.py
├── pyproject.toml
├── README.md
├── setup.cfg
└── tox.ini
```

### Initialize a git repository in your package

NOTE: This is important not only for version management, but also if you want to
pip install your package locally for testing with `pip install -e .`. (because
the version of your package is managed using git tags,
[see below](#automatic-deployment-and-version-management))

```bash
cd napari-growth-cone-finder
git init
git add .
git commit -m 'initial commit'
```

### Upload it to github

1. Create a [new github repository]

2. Add your newly created github repo as a remote and push:

   ```bash
   # here, continuing with the example above...
   # but replace with your own username and repo name

   git remote add origin https://github.com/openuc2/imswitch-sim.git
   git push -u origin main
   ```

### Monitor testing and coverage

The repository should already be setup to run your tests each time you push an
update (configuration is in `.github/workflows/test_and_deploy.yml`). You can
monitor them in the "Actions" tab of your github repository. If you're
following along, go have a look... they should be running right now!

When the tests are done, test coverage will be viewable at
[codecov.io](https://codecov.io/) (assuming your repository is public):
`https://codecov.io/gh/<your-github-username>/<your-package-name>`

You will need to enable the [codecov](https://github.com/apps/codecov) github app
for this to work. See [here](https://github.com/apps/codecov/installations/new)
to install the codecov github app and give it access to your imswitch plugin repository.

### Set up automatic deployments

Your new package is also nearly ready to automatically deploy to [PyPI]
(whenever you create a tagged release), so that your users can simply `pip install` your package. You just need to create an [API token to authenticate
with PyPi](https://pypi.org/help/#apitoken), and then add it to your github
repository:

1. If you don't already have one, [create an
   account](https://pypi.org/account/register/) at [PyPI]
2. Verify your email address with PyPI, (if you haven't already)
3. Generate an [API token](https://pypi.org/help/#apitoken) at PyPi: In your
   [account settings](https://pypi.org/manage/account/) go to the API tokens
   section and select "Add API token". Make sure to copy it somewhere safe!
4. [Create a new encrypted
   secret](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets#creating-encrypted-secrets)"
   in your github repository with the name "TWINE_API_KEY", and paste in your
   API token.

You are now setup for automatic deployment!

### Automatic deployment and version management

Each time you want to deploy a new version, you just need to create a tagged
commit, and push it to your main branch on github. Your package is set up to
use [setuptools_scm](https://github.com/pypa/setuptools_scm) for version
management, meaning you don't need to hard-code your version anywhere in your
package. It will be inferred from the tag each time you release.

```bash
# the tag will be used as the version string for your package
# make it meaningful: https://semver.org/
git tag -a v0.1.0 -m "v0.1.0"

# make sure to use follow-tags so that the tag also gets pushed to github
git push --follow-tags
```

> Note: as of git 2.4.1, you can set `follow-tags` as default with
> `git config --global push.followTags true`

Monitor the "actions" tab on your github repo for progress... and when the
"deploy" step is finished, your new version should be visible on pypi:

`https://pypi.org/project/<your-package-name>/`

and available for pip install with:

```bash
# for example
pip install imswitch-sim
```

### Running tests locally

Tests are automatically setup to run on github when you push to your repository.

You can run your tests locally with [pytest](https://docs.pytest.org/en/7.1.x/).
You'll need to make sure that your package is installed in your environment,
along with testing requirements (specified in the setup.cfg `extras_require` section):

```bash
pip install -e ".[testing]"
pytest
```

### Create your documentation

Documentation generation is not included in this template.
We recommend following the getting started guides for one of the following 
documentation generation tools:

1. [Sphinx]
2. [MkDocs]
3. [JupyterBook]

### Pre-commit

This template includes a default yaml configuration for [pre-commit](https://pre-commit.com/).
Among other things, it includes checks for best practices in napari plugins.
You may edit the config at `.pre-commit-config.yaml`

To use it run:

```bash
pip install pre-commit
pre-commit install
```

You can also have these checks run automatically for you when you push to github
by installing [pre-commit ci](https://pre-commit.ci/) on your repository.

## Features

- Installable [PyPI] package
- [tox] test suite, testing various python versions and platforms.
- `README.md` file that contains useful information about your plugin
- Continuous integration configuration for [github actions] that handles testing
  and deployment of tagged releases
- git-tag-based version management with [setuptools_scm]
- Choose from several licenses, including [BSD-3], [MIT], [MPL v2.0], [Apache
  v2.0], [GNU GPL v3.0], or [GNU LGPL v3.0]

## Resources

Please consult the [napari plugin
docs](https://napari.org/stable/plugins/index.html) for more information on
how to create a plugin.

Details on why this plugin template is using the `src` layout can be found [here](https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure) and [here](https://hynek.me/articles/testing-packaging/)

## Issues

If you encounter any problems with this cookiecutter template, please [file an
issue] along with a detailed description.

## License

Distributed under the terms of the [BSD-3] license, `cookiecutter-napari-plugin`
is free and open source software.

[napari organization]: https://github.com/napari/
[gitter_badge]: https://badges.gitter.im/Join%20Chat.svg
[gitter]: https://gitter.im/napari/cookiecutter-napari-plugin?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge "Join Chat on Gitter.im"
[travis_badge]: https://travis-ci.org/napari/cookiecutter-napari-plugin.svg?branch=main
[travis]: https://travis-ci.org/napari/cookiecutter-napari-plugin "See Build Status on Travis CI"
[docs_badge]: https://readthedocs.org/projects/cookiecutter-napari-plugin/badge/?version=latest
[documentation]: https://cookiecutter-napari-plugin.readthedocs.io/en/latest/ "Documentation"
[cookiecutter]: https://github.com/audreyr/cookiecutter
[napari]: https://github.com/napari/napari
[npe2]: https://github.com/napari/npe2
[pypi]: https://pypi.org/
[tox]: https://tox.readthedocs.io/en/latest/
[file an issue]: https://github.com/napari/cookiecutter-napari-plugin/issues
[sphinx]: https://www.sphinx-doc.org/en/master/usage/quickstart.html
[mkdocs]: https://www.mkdocs.org/getting-started/
[jupyterbook]: https://jupyterbook.org/en/stable/start/your-first-book.html
[mit]: http://opensource.org/licenses/MIT
[mpl v2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[bsd-3]: http://opensource.org/licenses/BSD-3-Clause
[gnu gpl v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[gnu lgpl v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[apache v2.0]: http://www.apache.org/licenses/LICENSE-2.0
[travis ci]: https://travis-ci.com/
[appveyor]: http://www.appveyor.com/
[pypa code of conduct]: https://www.pypa.io/en/latest/code-of-conduct/
[shortbread]: https://github.com/audreyr/cookiecutter/releases/tag/1.4.0
[osi_certified]: https://opensource.org/trademarks/osi-certified/web/osi-certified-120x100.png
[osi]: https://opensource.org/
[github actions]: https://github.com/features/actions
[new github repository]: https://help.github.com/en/github/getting-started-with-github/create-a-repo
[setuptools_scm]: https://github.com/pypa/setuptools_scm
