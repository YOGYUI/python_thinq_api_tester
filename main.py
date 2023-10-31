import sys
from Include import ThinqAPI, ThinqGUI
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    country_code = "KR"
    language_code = "ko-KR"
    api_key = "replace to your api key"
    api_client_id = "replace to your api cliend it"
    refresh_token = "replace to your thinq refresh token"
    oauth_secret_key = "replace to your oauth secret key"
    app_client_id = "replace to your application client id"
    app_key = "replace to your application key"

    thinq = ThinqAPI(
        country_code=country_code,
        language_code=language_code,
        api_key=api_key,
        api_client_id=api_client_id,
        refresh_token=refresh_token,
        oauth_secret_key=oauth_secret_key,
        app_client_id=app_client_id,
        app_key=app_key,
        log_mqtt_message=True
    )

    app = QApplication(sys.argv)
    wnd = ThinqGUI(parent=None)
    wnd.setThinqApiInstance(thinq)
    wnd.show()
    app.exec_()
