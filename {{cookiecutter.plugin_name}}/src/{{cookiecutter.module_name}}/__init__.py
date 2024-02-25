{% if cookiecutter.use_git_tags_for_versioning == 'y' %}
try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"
{% else -%}
__version__ = "0.0.1"
{% endif -%}

{% if cookiecutter.include_controller == 'y' %}
from ._controller import imswitch_get_controller
{% endif %}{% if cookiecutter.include_widget_plugin == 'y' -%}
from ._widget import ExampleQWidget, ImageThreshold, threshold_autogenerate_widget, threshold_magic_widget
{% endif %}{% if cookiecutter.include_manager_plugin == 'y' -%}
from ._manager import write_multiple, write_single_image
{% endif %}
__all__ = (
    {% if cookiecutter.include_controller == 'y' -%}
    "imswitch_get_controller",
    {% endif %}{% if cookiecutter.include_manager_plugin == 'y' -%}
    "write_single_image",
    "write_multiple",
    {% endif %}{% if cookiecutter.include_widget_plugin == 'y' -%}
    "ExampleQWidget",
    "ImageThreshold",
    "threshold_autogenerate_widget",
    "threshold_magic_widget",
{% endif -%}
)
