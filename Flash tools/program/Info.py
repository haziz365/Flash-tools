from Config.Util import *
from Config.Config import *
try:
    import webbrowser
except Exception as e:
   ErrorModule(e)

Title("Info")

try:
    print(f"\n{BEFORE + current_time_hour() + AFTER} {WAIT} Information Recovery..{reset}")

    Slow(f"""
    {INFO_ADD} Name Tool     :  {white}{name_tool}
    {INFO_ADD} Type Tool     :  {white}{type_tool}
    {INFO_ADD} Version       :  {white}{version_tool}
    {INFO_ADD} Copyright     :  {white}{copyright}
    {INFO_ADD} Coding        :  {white}{coding_tool}
    {INFO_ADD} Language      :  {white}{language_tool}
    {INFO_ADD} Creator       :  {white}{creator}
    {INFO_ADD} Platform      :  {white}{platform}
    {INFO_ADD} Discord  [W]  :  {white}https://{discord_server}
    {INFO_ADD} Site     [W]  :  {white}https://{website}
    {INFO_ADD} GitHub   [W]  :  {white}https://{github_tool}
    {INFO_ADD} Telegram [W]  :  {white}https://{telegram}
    {reset}""")

    license_read = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Open 'LICENSE' ? (y/n) -> {reset}")
    if license_read in ['y', 'Y', 'Yes', 'yes', 'YES']:
        webbrowser.open_new_tab(license)
    else:
        pass
    Continue()
    Reset()
except Exception as e:
    Error(e)