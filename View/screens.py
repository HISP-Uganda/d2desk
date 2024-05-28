# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.


from Model.splash_screen import SplashScreenModel
from Controller.splash_screen import SplashScreenController
from Model.login_screen import LoginScreenModel
from Controller.login_screen import LoginScreenController

screens = {
    "splash screen": {
        "model": SplashScreenModel,
        "controller": SplashScreenController,
    },

    "login screen": {
        "model": LoginScreenModel,
        "controller": LoginScreenController,
    },
}