from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager

Window.size = (350, 550)

KV = """

<LoginWindow>:
    name: "main"
    GridLayout:
        cols: 1
        size_hint : 1,1
        Image :
            source : "/Users/valentinagonzalez/Documents/RIG INC/Project Tools/F11.png"
            pos_hint : {"center_x": 0.5, "center_y": 0.5}
            keep_ratio: True
            allow_stretch: True
            opacity: 0.8
            size_hint: 1, 1

        Button:
            text : "SIGN IN"
            size_hint : 1, 0.5
            bold : True
            background_color: 0.39, 0.57, 0.8, 1
            on_release:
                app.root.current = "third"
                root.manager.transition.direction = "left"
                app.add_datatable()

        Button:
            text : "CREATE AN ACCOUNT"
            size_hint : 1, 0.5
            bold: True
            background_color: 0.94, 0.98, 1, 1
            on_release:
                app.change_screen('fourth')
                root.manager.transition.direction = "left"
                app.add_datatable()

<SigninWindow>:
    name: "third"

    GridLayout:
        cols: 1
        size: root.width, root.height
        Image :
            source : "/Users/valentinagonzalez/Documents/RIG INC/Project Tools/pic2.jpg"

            allow_stretch: True
            keep_ratio: True
            size_hint_y: None
            size_hint_x: None
            width: self.parent.width
            height: self.parent.width/self.image_ratio

        GridLayout:
            cols: 1
            MDFloatingActionButton:
                icon: 'arrow-left'
                on_release: app.change_screen('main')

            Label:
                text: "Email: "
                size_hint : 1, 0.5
                bold: True
                color: 0.39, 0.57, 0.8, 1

            TextInput:
                multiline: False

            Label:
                text: "Password: "
                size_hint : 1, 0.5
                bold: True
                color: 0.39, 0.57, 0.8, 1

            TextInput:
                id: passw
                multiline : False

        Button:
            text : "SUBMIT"
            size_hint : 1, 0.5
            bold : True
            background_color: 0.25, 0.61, 0.92, 1
            on_release:
                app.root.current = "second" if passw.text == "valentina" else "third"
                root.manager.transition.direction = "left"

<CreateaccountWindow>:
    name: "fourth"

    GridLayout:
        cols: 1
        size: root.width, root.height

        Image :
            source : "/Users/valentinagonzalez/Documents/RIG INC/Project Tools/pic2.jpg"

            allow_stretch: True
            keep_ratio: True
            size_hint_y: None
            size_hint_x: None
            width: self.parent.width
            height: self.parent.width/self.image_ratio

        GridLayout:
            cols: 1
            MDFloatingActionButton:
                icon: 'arrow-left'
                on_release: app.change_screen('main')


            Label:
                text: "First Name: "
                size_hint : 1, 0.5
                bold: True
                color: 0.39, 0.57, 0.8, 1

            TextInput:
                multiline : False

            Label:
                text: "Last Name: "
                size_hint : 1, 0.5
                bold: True
                color: 0.39, 0.57, 0.8, 1

            TextInput:
                multiline : False

            Label:
                text: "Email: "
                size_hint : 1, 0.5
                bold: True
                color: 0.39, 0.57, 0.8, 1

            TextInput:
                multiline: False

            Label:
                text: "Password: "
                size_hint : 1, 0.5
                bold: True
                color: 0.39, 0.57, 0.8, 1

            TextInput:
                id: passw
                multiline : False

        Button:
            text : "SUBMIT"
            size_hint : 1, 0.5
            bold : True
            background_color: 0.39, 0.57, 0.8, 1
            on_release:
                app.root.current = "second"
                root.manager.transition.direction = "left"



<DataandhomeWindow>:
    name: "second"

    MDBoxLayout:
        orientation: 'vertical'
        padding: 1
        MDToolbar:
            title: 'Welcome'

            left_action_items: [["home", lambda x: app.navigation_draw()]]
            right_action_items: [["menu", lambda x: app.callback()]]
            elevation:5

        MDFloatingActionButton:
            icon: 'arrow-left'
            on_release: app.change_screen('main')

        AnchorLayout:
            id: data_layout

        MDBottomAppBar:
            MDToolbar:
                title: 'Help'
                left_action_items: [["doctor", lambda x: app.navigation_draw()]]
                mode: 'end'
                type : 'bottom'
                icon: 'folder'
                on_action_button: app.navigation_draw()



WindowManager:
    LoginWindow:
    DataandhomeWindow:
        id: data_scr
    SigninWindow:
    CreateaccountWindow:

"""


class LoginWindow(Screen):
    pass


class DataandhomeWindow(Screen):
    pass


class SigninWindow(Screen):
    pass


class CreateaccountWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class HomePage(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data_tables = None

    def build(self):
        return Builder.load_string(KV)

    def add_datatable(self):
        self.data_tables = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                       size_hint=(0.9, 0.6),
                                       check=True,
                                       rows_num=17,
                                       column_data=[
                                           ("No.", dp(30)),
                                           ("Symptom", dp(30)),
                                       ],
                                       row_data=[
                                           ("1", "itching"),
                                           ("2", "skin_rash"),
                                           ("3", "nodal_skin_eruptions"),
                                           ("4", "dischromic _patches"),
                                           ("5", "continuous_sneezing"),
                                           ("6", "shivering"),
                                           ("7", "watering_from_eyes"),
                                           ("8", "stomach_pain"),
                                           ("9", "acidity"),
                                           ("10", "ulcers_on_tongue"),
                                           ("11", "vomiting"),
                                           ("12", "cough"),
                                           ("13", "chest_pain"),
                                           ("14", "yellowish_skin"),
                                           ("15", "loss_of_appetite"),
                                           ("16", "abdominal_pain"),
                                           ("17", "yellowing_of_eyes"),
                                           ("18", "burning_micturition"),
                                           ("19", "spotting_ urination"),
                                           ("20", "loss_of_appetite"),
                                           ("21", "abdominal_pain"),
                                           ("22", "passage_of_gases"),
                                           ("23", "internal_itching"),
                                           ("24", "indigestion"),
                                           ("25", " yellowing_of_eyes"),
                                           ("26", " yellowing_of_eyes"),
                                       ]
                                       )
        self.root.ids.data_scr.ids.data_layout.add_widget(self.data_tables)

    def change_screen(self, screen: str):
        self.root.current = screen


if __name__ == "__main__":
    HomePage().run()

