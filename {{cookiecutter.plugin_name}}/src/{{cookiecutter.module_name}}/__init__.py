{% if cookiecutter.use_git_tags_for_versioning == 'y' %}
try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"
{% else -%}
__version__ = "0.0.1"
{% endif -%}

{% if cookiecutter.include_controller == 'y' %}
from .{{cookiecutter.module_name}}Controller import *
{% endif %}{% if cookiecutter.include_widget_plugin == 'y' -%}
from .{{cookiecutter.module_name}}Widget import *
{% endif %}{% if cookiecutter.include_manager_plugin == 'y' -%}
from .{{cookiecutter.module_name}}Manager import *
{% endif %}{% if cookiecutter.include_info_plugin == 'y' -%}
from .{{cookiecutter.module_name}}Info import *
{% endif %}
__all__ = (
)
