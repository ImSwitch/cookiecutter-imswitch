{% if cookiecutter.use_git_tags_for_versioning == 'y' %}
try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"
{% else -%}
__version__ = "0.0.1"
{% endif -%}

{% if cookiecutter.include_controller == 'y' %}
from .{{cookiecutter.module_name}}_controller import *
{% endif %}{% if cookiecutter.include_widget_plugin == 'y' -%}
from .{{cookiecutter.module_name}}_widget import *
{% endif %}{% if cookiecutter.include_manager_plugin == 'y' -%}
from .{{cookiecutter.module_name}}_manager import *
{% endif %}
__all__ = (
)
