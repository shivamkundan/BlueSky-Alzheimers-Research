import os
from typing import Union

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp, sp
from kivy.properties import (
    BooleanProperty,
    BoundedNumericProperty,
    ColorProperty,
    DictProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
    VariableListProperty,
)
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.weakproxy import WeakProxy

# from kivymd import uix_path
# from kivymd.color_definitions import text_colors
# from kivymd.font_definitions import theme_font_styles
# from kivymd.material_resources import (
#     FLOATING_ACTION_BUTTON_M2_ELEVATION,
#     FLOATING_ACTION_BUTTON_M2_OFFSET,
#     FLOATING_ACTION_BUTTON_M3_ELEVATION,
#     FLOATING_ACTION_BUTTON_M3_OFFSET,
#     FLOATING_ACTION_BUTTON_M3_SOFTNESS,
#     RAISED_BUTTON_OFFSET,
#     RAISED_BUTTON_SOFTNESS,
# )
# from kivymd.theming import ThemableBehavior
# from kivymd.uix.behaviors import (
#     CommonElevationBehavior,
#     DeclarativeBehavior,
#     RectangularRippleBehavior,
#     RotateBehavior,
# )
# from kivymd.uix.label import MDLabel
# from kivymd.uix.tooltip import MDTooltip

with open(
    os.path.join( "button.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


theme_text_color_options = (
    "Primary",
    "Secondary",
    "Hint",
    "Error",
    "Custom",
    "ContrastParentBackground",
)


class BaseButton(
    # DeclarativeBehavior,
    # RectangularRippleBehavior,
    # ThemableBehavior,
    # ButtonBehavior,
    # AnchorLayout,
):
    """
    Base class for all buttons.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.DeclarativeBehavior` and
    :class:`~kivymd.uix.behaviors.RectangularRippleBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivy.uix.behaviors.ButtonBehavior` and
    :class:`~kivy.uix.anchorlayout.AnchorLayout`
    classes documentation.
    """

    padding = VariableListProperty([dp(16), dp(8), dp(16), dp(8)])
    """
    Padding between the widget box and its children, in pixels:
    [padding_left, padding_top, padding_right, padding_bottom].

    padding also accepts a two argument form [padding_horizontal,
    padding_vertical] and a one argument form [padding].

    .. versionadded:: 1.0.0

    :attr:`padding` is a :class:`~kivy.properties.VariableListProperty`
    and defaults to [16dp, 8dp, 16dp, 8dp].
    """

    halign = OptionProperty("center", options=("left", "center", "right"))
    """
    Horizontal anchor.

    .. versionadded:: 1.0.0

    :attr:`anchor_x` is an :class:`~kivy.properties.OptionProperty`
    and defaults to 'center'. It accepts values of 'left', 'center' or 'right'.
    """

    valign = OptionProperty("center", options=("top", "center", "bottom"))
    """
    Vertical anchor.

    .. versionadded:: 1.0.0

    :attr:`anchor_y` is an :class:`~kivy.properties.OptionProperty`
    and defaults to 'center'. It accepts values of 'top', 'center' or 'bottom'.
    """

    text = StringProperty("")
    """
    Button text.

    :attr:`text` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    icon = StringProperty("")
    """
    Button icon.

    :attr:`icon` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    # font_style = OptionProperty("Body1", options=theme_font_styles)
    # """
    # Button text font style.

    # Available vanilla font_style are: `'H1'`, `'H2'`, `'H3'`, `'H4'`, `'H5'`,
    # `'H6'`, `'Subtitle1'`, `'Subtitle2'`, `'Body1'`, `'Body2'`, `'Button'`,
    # `'Caption'`, `'Overline'`, `'Icon'`.

    # :attr:`font_style` is a :class:`~kivy.properties.StringProperty`
    # and defaults to `'Body1'`.
    # """

    # theme_text_color = OptionProperty(None, options=theme_text_color_options)
    # """
    # Button text type. Available options are: (`"Primary"`, `"Secondary"`,
    # `"Hint"`, `"Error"`, `"Custom"`, `"ContrastParentBackground"`).

    # :attr:`theme_text_color` is an :class:`~kivy.properties.OptionProperty`
    # and defaults to `None` (set by button class).
    # """

    # theme_icon_color = OptionProperty(None, options=theme_text_color_options)
    # """
    # Button icon type. Available options are: (`"Primary"`, `"Secondary"`,
    # `"Hint"`, `"Error"`, `"Custom"`, `"ContrastParentBackground"`).

    # .. versionadded:: 1.0.0

    # :attr:`theme_icon_color` is an :class:`~kivy.properties.OptionProperty`
    # and defaults to `None` (set by button subclass).
    # """

    text_color = ColorProperty(None)
    """
    Button text color in (r, g, b, a) or string format.

    :attr:`text_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    icon_color = ColorProperty(None)
    """
    Button icon color in (r, g, b, a) or string format.

    :attr:`icon_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    font_name = StringProperty()
    """
    Button text font name.

    :attr:`font_name` is a :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    font_size = NumericProperty("14sp")
    """
    Button text font size.

    :attr:`font_size` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `14sp`.
    """

    icon_size = NumericProperty()
    """
    Icon font size.
    Use this parameter as the font size, that is, in sp units.

    .. versionadded:: 1.0.0

    :attr:`icon_size` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `None`.
    """

    line_width = NumericProperty(1)
    """
    Line width for button border.

    :attr:`line_width` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `1`.
    """

    line_color = ColorProperty(None)
    """
    Line color in (r, g, b, a) or string format for button border.

    :attr:`line_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    line_color_disabled = ColorProperty(None)
    """
    Disabled line color in (r, g, b, a) or string format for button border.

    .. versionadded:: 1.0.0

    :attr:`line_color_disabled` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    md_bg_color = ColorProperty(None)
    """
    Button background color in (r, g, b, a) or string format.

    :attr:`md_bg_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    md_bg_color_disabled = ColorProperty(None)
    """
    The background color in (r, g, b, a) or string format of the button when
    the button is disabled.

    :attr:`md_bg_color_disabled` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    disabled_color = ColorProperty(None)
    """
    The color of the text and icon when the button is disabled,
    in (r, g, b, a) or string format.

    .. versionadded:: 1.0.0

    :attr:`disabled_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `None`.
    """

    rounded_button = BooleanProperty(False)
    """
    Should the button have fully rounded corners (e.g. like M3 buttons)?

    .. versionadded:: 1.0.0

    :attr:`rounded_button` is a :class:`~kivy.properties.BooleanProperty`
    and defaults to `False`.
    """

    # Note - _radius must be > 0 to avoid rendering issues.
    _radius = BoundedNumericProperty(dp(4), min=0.0999, errorvalue=0.1)
    # Properties used for rendering.
    _disabled_color = ColorProperty([0.0, 0.0, 0.0, 0.0])
    _md_bg_color = ColorProperty([0.0, 0.0, 0.0, 0.0])
    _md_bg_color_disabled = ColorProperty([0.0, 0.0, 0.0, 0.0])
    _line_color = ColorProperty([0.0, 0.0, 0.0, 0.0])
    _line_color_disabled = ColorProperty([0.0, 0.0, 0.0, 0.0])
    _theme_text_color = OptionProperty(None, options=theme_text_color_options)
    _theme_icon_color = OptionProperty(None, options=theme_text_color_options)
    _text_color = ColorProperty(None)
    _icon_color = ColorProperty(None)

    # Defaults which can be overridden in subclasses
    _min_width = NumericProperty(dp(64))
    _min_height = NumericProperty(dp(36))

    # Default colors - set to None to use primary theme colors
    _default_md_bg_color = [0.0, 0.0, 0.0, 0.0]
    _default_md_bg_color_disabled = [0.0, 0.0, 0.0, 0.0]
    _default_line_color = [0.0, 0.0, 0.0, 0.0]
    _default_line_color_disabled = [0.0, 0.0, 0.0, 0.0]
    _default_theme_text_color = StringProperty("Primary")
    _default_theme_icon_color = StringProperty("Primary")
    _default_text_color = ColorProperty(None)
    _default_icon_color = ColorProperty(None)

    _animation_fade_bg = ObjectProperty(None, allownone=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.theme_cls.bind(
            primary_palette=self.set_all_colors,
            theme_style=self.set_all_colors,
        )
        self.bind(
            md_bg_color=self.set_button_colors,
            md_bg_color_disabled=self.set_button_colors,
            line_color=self.set_button_colors,
            line_color_disabled=self.set_button_colors,
            theme_text_color=self.set_text_color,
            text_color=self.set_text_color,
            theme_icon_color=self.set_icon_color,
            icon_color=self.set_icon_color,
            disabled_color=self.set_disabled_color,
            rounded_button=self.set_radius,
            height=self.set_radius,
        )
        Clock.schedule_once(self.set_all_colors)
        Clock.schedule_once(self.set_radius)

    def set_disabled_color(self, *args):
        """
        Sets the color for the icon, text and line of the button when button
        is disabled.
        """

        if self.disabled:
            disabled_color = (
                self.disabled_color
                if self.disabled_color
                else self.theme_cls.disabled_hint_text_color
            )
            self._disabled_color = disabled_color
            # Button icon color.
            if "lbl_ic" in self.ids:
                self.ids.lbl_ic.disabled_color = disabled_color
            # Button text color.
            if "lbl_txt" in self.ids:
                self.ids.lbl_txt.disabled_color = disabled_color
        else:
            self._disabled_color = self._line_color

    def set_all_colors(self, *args) -> None:
        """Set all button colours."""

        self.set_button_colors()
        self.set_text_color()
        self.set_icon_color()

    def set_button_colors(self, *args) -> None:
        """Set all button colours (except text/icons)."""

        # Set main color
        _md_bg_color = (
            self.md_bg_color
            or self._default_md_bg_color
            or self.theme_cls.primary_color
        )

        # Set disabled color
        _md_bg_color_disabled = (
            self.md_bg_color_disabled
            or (
                [sum(self.md_bg_color[0:3]) / 3.0] * 3
                + [0.38 if self.theme_cls.theme_style == "Light" else 0.5]
                if self.md_bg_color
                else None
            )
            or self._default_md_bg_color_disabled
            or self.theme_cls.disabled_primary_color
        )

        # Set line color
        _line_color = (
            self.line_color
            or self._default_line_color
            or self.theme_cls.primary_color
        )

        # Set disabled line color
        _line_color_disabled = (
            self.line_color_disabled
            or (
                [sum(self.line_color[0:3]) / 3.0] * 3
                + [0.38 if self.theme_cls.theme_style == "Light" else 0.5]
                if self.line_color
                else None
            )
            or self._default_line_color_disabled
            or self.theme_cls.disabled_primary_color
        )

        if self.theme_cls.theme_style_switch_animation:
            Animation(
                _md_bg_color=_md_bg_color,
                _md_bg_color_disabled=_md_bg_color_disabled,
                _line_color=_line_color,
                _line_color_disabled=_line_color_disabled,
                d=self.theme_cls.theme_style_switch_animation_duration,
                t="linear",
            ).start(self)
        else:
            self._md_bg_color = _md_bg_color
            self._md_bg_color_disabled = _md_bg_color_disabled
        self._line_color = _line_color
        self._line_color_disabled = _line_color_disabled

    def set_text_color(self, *args) -> None:
        """
        Set _theme_text_color and _text_color based on defaults and options.
        """

        self._theme_text_color = (
            self.theme_text_color or self._default_theme_text_color
        )
        if self._default_text_color == "PrimaryHue":
            default_text_color = text_colors[self.theme_cls.primary_palette][
                self.theme_cls.primary_hue
            ]
        elif self._default_text_color == "Primary":
            default_text_color = self.theme_cls.primary_color
        else:
            default_text_color = self.theme_cls.text_color
        self._text_color = self.text_color or default_text_color

    def set_icon_color(self, *args) -> None:
        """
        Set _theme_icon_color and _icon_color based on defaults and options.
        """

        self._theme_icon_color = (
            (self.theme_icon_color or self._default_theme_icon_color)
            if not self.disabled
            else "Custom"
        )
        if self._default_icon_color == "PrimaryHue":
            default_icon_color = text_colors[self.theme_cls.primary_palette][
                self.theme_cls.primary_hue
            ]
        elif self._default_icon_color == "Primary":
            default_icon_color = self.theme_cls.primary_color
        else:
            default_icon_color = self.theme_cls.text_color
        self._icon_color = self.icon_color or default_icon_color

    def set_radius(self, *args) -> None:
        """
        Set the radius, if we are a rounded button, based on the
        current height.
        """

        if self.rounded_button:
            self._radius = self.height / 2

    # Touch events that cause transparent buttons to fade to background
    def on_touch_down(self, touch):
        """
        Animates fade to background on press, for buttons with no
        background color.
        """

        if touch.is_mouse_scrolling:
            return False
        elif not self.collide_point(touch.x, touch.y):
            return False
        elif self in touch.ud:
            return False
        elif self.disabled:
            return False
        else:
            if self._md_bg_color[3] == 0.0:
                self._animation_fade_bg = Animation(
                    duration=0.5, _md_bg_color=[0.0, 0.0, 0.0, 0.1]
                )
                self._animation_fade_bg.start(self)
            return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        """Animates return to original background on touch release."""

        if not self.disabled and self._animation_fade_bg:
            self._animation_fade_bg.stop_property(self, "_md_bg_color")
            self._animation_fade_bg = None
            md_bg_color = (
                self.md_bg_color
                or self._default_md_bg_color
                or self.theme_cls.primary_color
            )
            Animation(duration=0.05, _md_bg_color=md_bg_color).start(self)
        return super().on_touch_up(touch)

    def on_disabled(self, instance_button, disabled_value: bool) -> None:
        if hasattr(super(), "on_disabled"):
            if self.disabled is True:
                Animation.cancel_all(self, "elevation")
            super().on_disabled(instance_button, disabled_value)
        Clock.schedule_once(self.set_disabled_color)

