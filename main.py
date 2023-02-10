import datetime

from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, ListProperty
from kivy.clock import Clock

from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.font_definitions import fonts
from kivymd.icon_definitions import md_icons
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker



KV = f'''
#https://stackoverflow.com/questions/65698145/kivymd-tab-name-containing-icons-and-text
# this import will prevent disappear tabs through some clicks on them
# :import md_icons kivymd.icon_definitions.md_icons
# :import fonts kivymd.font_definitions.fonts
# Menu item in the DrawerList list.

<IconListItem>
    IconLeftWidget:
        icon: root.icon
        
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "data/logo/kivy-icon-256.png"

    MDLabel:
        text: app.title
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: app.by_who
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:
        DrawerList:
            id: md_list


MDScreen:
    MDNavigationLayout:
        MDScreenManager:
            MDScreen:
                MDBoxLayout:
                    orientation: 'vertical'
                    
                    MDTopAppBar:
                        title: app.title
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [['star-outline', lambda x: app.on_star_click()]]
                        md_bg_color: 0, 0, 0, 1
                    
                    MDTabs:
                        id: tabs
                        on_tab_switch: app.on_tab_switch(*args) 
                        height: '48dp'
                        tab_indicator_anim: False
                        background_color: 0.1, 0.1, 0.1, 1
                        tab_hint_x: True
                        
                        Tab:
                            id: tab1
                            name: 'tab1'
                            title: r"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['calculator-variant']}[/size][/font] input"
                            
                            MDBoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"

                                MDBoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "calendar-month"

                                    MDTextField:
                                        id: start_date
                                        hint_text: 'Start date'
                                        on_focus: if self.focus: app.show_date_picker()
                                        color_mode: 'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1
                                        text_hint_color: 0,0,1,1

                                MDBoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "cash"

                                    MDTextField:
                                        id: loan
                                        name: 'loan'
                                        hint_text: 'Loan'
                                        color_mode: 'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1
                                        input_filter: 'float'
                                        helper_text_mode: "on_focus"

                                MDBoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "clock-time-five-outline"

                                    MDTextField:
                                        id: months
                                        name: 'months'
                                        hint_text: 'Months'
                                        color_mode: 'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1
                                        input_filter: 'int'
                                        helper_text_mode: "on_focus"


                                MDBoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "bank"

                                    MDTextField:
                                        id: interest
                                        name: 'interest'
                                        hint_text: 'Interest'
                                        color_mode: 'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1
                                        input_filter: 'float'
                                        helper_text_mode: "on_focus"

                                    MDTextField:
                                        id: payment_type
                                        name: 'payment_type'
                                        hint_text: 'Payment type'
                                        text: 'annuity'
                                        on_focus: if self.focus: app.menu.open()
                                        color_mode: 'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1


                                MDBoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"

                                    MDLabel:
                                        text: 'Monthly payment'

                                    MDTextField:
                                        id: payment_label
                                        hint_text: ""
                                        disabled: True

                                MDBoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"

                                    MDLabel:
                                        text: 'Total interest'

                                    MDTextField:
                                        id: overpayment_loan_label
                                        hint_text: ""
                                        disabled: True

                                MDBoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"

                                    MDLabel:
                                        text: 'Total payments'

                                    MDTextField:
                                        id: total_amount_of_payments_label
                                        hint_text: ""
                                        disabled: True

                                MDBoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"

                                    MDLabel:
                                        text: 'Effective'

                                    MDTextField:
                                        id: effective_interest_rate_label
                                        hint_text: ""
                                        disabled: True
                                        text_hint_color:[0,0,1,1]

                            
                        Tab:
                            id: tab2
                            name: 'tab2'
                            title: r"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['calculator-variant']}[/size][/font] Table"
                             
                        Tab:
                            id: tab3
                            name: 'tab3'
                            title: r"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-areaspline']}[/size][/font] Graph"
                            
                        Tab:
                            id: tab4
                            name: 'tab4'
                            title: r"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-pie']}[/size][/font] Chart"
                            
                        Tab:
                            id: tab5
                            name: 'tab5'
                            title: r"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['book-open-variant']}[/size][/font] Sum"
            
           
        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            ContentNavigationDrawer:
                id: content_drawer
                nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(MDBoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class Tab(MDFloatLayout, MDTabsBase):
    pass


class IconListItem(OneLineIconListItem):
    icon = StringProperty()


class MorCalcApp(MDApp):
    title = 'MorCalc'
    by_who = 'by Тёма'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        menu_items = [
            {
                "viewclass": "IconListItem",
                "icon": "format-text-rotation-angle-up",
                "text": "annuity",
                "on_release": lambda x="annuity": self.set_item(x),
            },
            {
                "viewclass": "IconListItem",
                "icon": "format-text-rotation-angle-down",
                "text": "differentiated",
                "on_release": lambda x="differentiated": self.set_item(x),
            }
        ]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.payment_type,
            items=menu_items,
            position="auto",
            width_mult=4,
            max_height=dp(100)
        )

    def set_item(self, instance_menu):
        def set_item(interval):
            self.screen.ids.payment_type.text = instance_menu
            self.menu.dismiss()
        Clock.schedule_once(set_item, 0.5)

    def on_save(self, instance, value, date_range):
        # if value < datetime.date.today():
        #     self.screen.ids.start_date.text = str(datetime.date.today())
        # self.screen.ids.start_date.text = str(value)
        self.screen.ids.start_date.text = datetime.date.today().strftime("%d -%m -%Y")
        self.screen.ids.loan.text = "5000000"
        self.screen.ids.months.text = "120"
        self.screen.ids.interest.text = "9.5"
        self.screen.ids.payment_type.text = "annuity"

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''
        self.screen.ids.start_date.text = str(datetime.date.today().strftime("%d -%m -%Y"))

    def show_date_picker(self):
        date_dialog = MDDatePicker(
            min_date=datetime.date.today()
        )
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def build(self):
        # self.theme_cls.theme_style = "Light" # "Dark"
        # return Builder.load_string(KV)
        return self.screen

    def on_start(self):
        icons_item_menu_lines = {
            "account-cowboy-hat": "About author",
            "youtube": "My YouTube",
            "coffee": "Donate author",
            "github": "Source code",
            "share-variant": "Share app",
            "shield-sun": "Dark/Light",
        }

        icons_item_menu_tabs = {
            'calculator-variant': 'Input',
            'table-large': 'Table',
            'chart-areaspline': 'Graph',
            'chart-pie': 'Chart',
            'book-open-variant': 'Sum'
        }

        for icon_name in icons_item_menu_lines.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item_menu_lines[icon_name])
            )

        # Auto create tabs
        # for icon_name, name_tab in icons_item_menu_tabs.items():
        #     self.root.ids.tabs.add_widget(
        #         Tab(title=f"[ref={name_tab}][font={fonts[-1]['fn_regular']}]{md_icons[icon_name]}[/font][/ref] {name_tab}")
        #     )

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        print('tab clicked! '+tab_text)

    def on_star_click(self):
        pass



MorCalcApp().run()
