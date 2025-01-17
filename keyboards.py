from pyrogram.types import (CallbackGame,
                            InlineKeyboardButton,
                            InlineKeyboardMarkup,
                            LoginUrl,
                            WebAppInfo)

# noinspection PyPep8Naming
from l10n import Locale, LocaleKeys as LK, get_available_languages


class ExtendedIKB(InlineKeyboardButton):
    SELECTION_INDICATOR = '•'

    def __init__(self,
                 text: str,
                 callback_data: str | bytes = None,
                 url: str = None,
                 web_app: WebAppInfo = None,
                 login_url: LoginUrl = None,
                 user_id: int = None,
                 switch_inline_query: str = None,
                 switch_inline_query_current_chat: str = None,
                 callback_game: CallbackGame = None,
                 *,
                 translatable: bool = True,
                 selectable: bool = True):

        super().__init__(text, callback_data, url, web_app, login_url, user_id,
                         switch_inline_query, switch_inline_query_current_chat, callback_game)
        self.translatable = translatable
        self.selectable = selectable

        self.text_key = self.text
        self.url_key = None
        self.selected = False
        if self.url:
            self.url_key = self.url

    def set_localed_text(self, locale: Locale):
        if self.translatable:
            self.text = locale.get(self.text_key)
            if self.url_key:
                self.url = locale.get(self.url_key)
        else:
            self.text = self.text_key

        if self.selectable and self.selected:
            self.text = f'{self.SELECTION_INDICATOR} {self.text} {self.SELECTION_INDICATOR}'

    def localed(self, locale: Locale):
        self.set_localed_text(locale)
        return self

    def __call__(self, locale: Locale):
        return self.localed(locale)


class ExtendedIKM(InlineKeyboardMarkup):
    def update_locale(self, locale: Locale):
        for line in self.inline_keyboard:
            for button in line:
                if isinstance(button, ExtendedIKB):
                    button.set_localed_text(locale)

    def localed(self, locale: Locale):
        self.update_locale(locale)
        return self

    def __call__(self, locale: Locale):
        return self.localed(locale)

    def select_button_by_key(self, key: str):
        for line in self.inline_keyboard:
            for button in line:
                if isinstance(button, ExtendedIKB) and button.selectable:
                    if button.text_key == key or button.callback_data == key:
                        button.selected = True
                    else:
                        button.selected = False  # only one button at a time can be selected


# Back button
back_button = ExtendedIKB(LK.bot_back, LK.bot_back, selectable=False)

# Channel link for inline messages
inline_button_channel_link = ExtendedIKB(LK.bot_author_text, url=LK.bot_author_link)

markup_inline_button = ExtendedIKM([[inline_button_channel_link]])

# Default
_server_stats = ExtendedIKB(LK.bot_servers_stats, LK.bot_servers_stats)
_profile_info = ExtendedIKB(LK.bot_profile_info, LK.bot_profile_info)
_extra_features = ExtendedIKB(LK.bot_extras, LK.bot_extras)
_settings = ExtendedIKB(LK.bot_settings, LK.bot_settings)

main_markup = ExtendedIKM([
    [_server_stats],
    [_profile_info],
    [_extra_features],
    [_settings]
])

# Server Statistics
_server_status = ExtendedIKB(LK.game_status_button_title, LK.game_status_button_title)
_matchmaking = ExtendedIKB(LK.stats_matchmaking_button_title, LK.stats_matchmaking_button_title)
_dc = ExtendedIKB(LK.dc_status_title, LK.dc_status_title)

ss_markup = ExtendedIKM([
    [_server_status],
    [_matchmaking],
    [_dc],
    [back_button]
])


# Profile Information
_profile_info = ExtendedIKB(LK.user_profileinfo_title, LK.user_profileinfo_title)
_cs_stats = ExtendedIKB(LK.user_gamestats_button_title, LK.user_gamestats_button_title)

profile_markup = ExtendedIKM([
    [_profile_info],
    [_cs_stats],
    [back_button]
])

# Extra Features

_crosshair = ExtendedIKB(LK.crosshair, LK.crosshair)
_currency = ExtendedIKB(LK.exchangerate_button_title, LK.exchangerate_button_title)
_valve_hq_time = ExtendedIKB(LK.valve_hqtime_button_title, LK.valve_hqtime_button_title)
_timer = ExtendedIKB(LK.game_dropcap_button_title, LK.game_dropcap_button_title)
_game_version = ExtendedIKB(LK.game_version_button_title, LK.game_version_button_title)
_guns = ExtendedIKB(LK.gun_button_text, LK.gun_button_text)

extra_markup = ExtendedIKM([
    [_crosshair, _currency, _game_version],
    [_valve_hq_time, _timer],
    [_guns],
    [back_button]
])

# Settings

_language = ExtendedIKB(LK.settings_language_button_title, LK.settings_language_button_title)
settings_markup = ExtendedIKM([
    [_language],
    [back_button]
])

# DC

_europe = ExtendedIKB(LK.dc_europe, LK.dc_europe)
_asia = ExtendedIKB(LK.dc_asia, LK.dc_asia)
_africa = ExtendedIKB(LK.dc_africa, LK.dc_africa)
_south_america = ExtendedIKB(LK.dc_southamerica, LK.dc_southamerica)
_australia = ExtendedIKB(LK.dc_australia, LK.dc_australia)
_us = ExtendedIKB(LK.dc_us, LK.dc_us)

dc_markup = ExtendedIKM([
    [_asia, _australia, _europe],
    [_africa, _south_america, _us],
    [back_button]
])

# DC Asia

_india = ExtendedIKB(LK.dc_india, LK.dc_india)
_emirates = ExtendedIKB(LK.dc_emirates, LK.dc_emirates)
_china = ExtendedIKB(LK.dc_china, LK.dc_china)
_singapore = ExtendedIKB(LK.dc_singapore, LK.dc_singapore)
_hongkong = ExtendedIKB(LK.dc_hongkong, LK.dc_hongkong)
_japan = ExtendedIKB(LK.dc_japan, LK.dc_japan)
_south_korea = ExtendedIKB(LK.dc_southkorea, LK.dc_southkorea)

dc_asia_markup = ExtendedIKM([
    [_china, _emirates, _hongkong],
    [_south_korea, _india],
    [_japan, _singapore],
    [back_button]
])

# DC Europe

_eu_west = ExtendedIKB(LK.dc_west, LK.dc_eu_west)
_eu_east = ExtendedIKB(LK.dc_east, LK.dc_eu_east)
_eu_north = ExtendedIKB(LK.dc_north, LK.dc_eu_north)

dc_eu_markup = ExtendedIKM([
    [_eu_east, _eu_north, _eu_west],
    [back_button]
])

# DC USA

_us_northwest = ExtendedIKB(LK.dc_north, LK.dc_us_north)
_us_southwest = ExtendedIKB(LK.dc_south, LK.dc_us_south)

dc_us_markup = ExtendedIKM([
    [_us_northwest, _us_southwest],
    [back_button]
])

# Guns

_pistols = ExtendedIKB(LK.gun_pistols, LK.gun_pistols)
_heavy = ExtendedIKB(LK.gun_heavy, LK.gun_heavy)
_smgs = ExtendedIKB(LK.gun_smgs, LK.gun_smgs)
_rifles = ExtendedIKB(LK.gun_rifles, LK.gun_rifles)

guns_markup = ExtendedIKM([
    [_pistols, _heavy],
    [_smgs, _rifles],
    [back_button]
])

# Pistols

_usps = ExtendedIKB("USP-S", "usps", translatable=False)
_p2000 = ExtendedIKB("P2000", "p2000", translatable=False)
_glock = ExtendedIKB("Glock-18", "glock18", translatable=False)
_dualies = ExtendedIKB("Dual Berettas", "dualberettas", translatable=False)
_p250 = ExtendedIKB("P250", "p250", translatable=False)
_cz75 = ExtendedIKB("CZ75-Auto", "cz75auto", translatable=False)
_five_seven = ExtendedIKB("Five-SeveN", "fiveseven", translatable=False)
_tec = ExtendedIKB("Tec-9", "tec9", translatable=False)
_deagle = ExtendedIKB("Desert Eagle", "deserteagle", translatable=False)
_r8 = ExtendedIKB("R8 Revolver", "r8revolver", translatable=False)

pistols_markup = ExtendedIKM([
    [_usps, _p2000, _glock],
    [_dualies, _p250],
    [_five_seven, _tec, _cz75],
    [_deagle, _r8],
    [back_button]
])

# Heavy

_nova = ExtendedIKB("Nova", "nova", translatable=False)
_xm1014 = ExtendedIKB("XM1014", "xm1014", translatable=False)
_mag7 = ExtendedIKB("MAG-7", "mag7", translatable=False)
_sawedoff = ExtendedIKB("Sawed-Off", "sawedoff", translatable=False)
_m249 = ExtendedIKB("M249", "m249", translatable=False)
_negev = ExtendedIKB("Negev", "negev", translatable=False)

heavy_markup = ExtendedIKM([
    [_nova, _xm1014],
    [_mag7, _sawedoff],
    [_m249, _negev],
    [back_button],
])

# SMGs

_mp9 = ExtendedIKB("MP9", "mp9", translatable=False)
_mac10 = ExtendedIKB("MAC-10", "mac10", translatable=False)
_mp7 = ExtendedIKB("MP7", "mp7", translatable=False)
_mp5 = ExtendedIKB("MP5-SD", "mp5sd", translatable=False)
_ump = ExtendedIKB("UMP-45", "ump45", translatable=False)
_p90 = ExtendedIKB("P90", "p90", translatable=False)
_pp = ExtendedIKB("PP-Bizon", "ppbizon", translatable=False)

smgs_markup = ExtendedIKM([
    [_mp9, _mac10],
    [_mp7, _mp5],
    [_ump, _p90, _pp],
    [back_button]
])

# Rifles

_famas = ExtendedIKB("FAMAS", "famas", translatable=False)
_galil = ExtendedIKB("Galil AR", "galilar", translatable=False)
_m4a4 = ExtendedIKB("M4A4", "m4a4", translatable=False)
_m4a1 = ExtendedIKB("M4A1-S", "m4a1s", translatable=False)
_ak = ExtendedIKB("AK-47", "ak47", translatable=False)
_aug = ExtendedIKB("AUG", "aug", translatable=False)
_sg = ExtendedIKB("SG 553", "sg553", translatable=False)
_ssg = ExtendedIKB("SSG 08", "ssg08", translatable=False)
_awp = ExtendedIKB("AWP", "awp", translatable=False)
_scar = ExtendedIKB("SCAR-20", "scar20", translatable=False)
_g3sg1 = ExtendedIKB("G3SG1", "g3sg1", translatable=False)

rifles_markup = ExtendedIKM([
    [_famas, _galil],
    [_m4a4, _m4a1, _ak],
    [_aug, _sg],
    [_ssg, _awp],
    [_scar, _g3sg1],
    [back_button]
])

# Crosshair
_generate_crosshair = ExtendedIKB(LK.crosshair_generate, LK.crosshair_generate)
_decode_crosshair = ExtendedIKB(LK.crosshair_decode, LK.crosshair_decode)

crosshair_markup = ExtendedIKM([
    [_generate_crosshair, _decode_crosshair],
    [back_button]
])

# Language
_available_langs = get_available_languages()
columns = 3

_language_buttons = []
_row = []
for lang_code, lang_name in _available_langs.items():
    _row.append(ExtendedIKB(lang_name, lang_code, translatable=False))
    if len(_row) == columns:
        _language_buttons.append(_row)  # yes, we append lists
        _row = []
if _row:
    _language_buttons.append(_row)

_language_buttons.append([back_button])

language_settings_markup = ExtendedIKM(_language_buttons)


all_selectable_markups = (ss_markup, extra_markup, dc_markup, dc_asia_markup, dc_eu_markup, dc_us_markup,
                          pistols_markup, heavy_markup, smgs_markup, rifles_markup, language_settings_markup)
