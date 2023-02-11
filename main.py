import datetime
import calendar
from random import random

from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, ListProperty
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, Line, Ellipse

from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList, OneLineAvatarIconListItem
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.font_definitions import fonts
from kivymd.icon_definitions import md_icons
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.button import MDRectangleFlatIconButton



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
                                
                                MDBoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"
                                    MDRectangleFlatIconButton:
                                        icon: 'android'
                                        text: 'BUTTON1'
                                        theme_text_color: 'Custom'
                                        text_color: 1, 1, 1, 1
                                        line_color: 0, 0, 0, 0
                                        icon_color: 1, 0, 0, 1
                                        mg_bg_color: 0.1, 0.1, 0.1, 1
                                        adaptive_width: True
                                        on_release: app.calc_table(*args)

                            
                        Tab:
                            id: tab2
                            name: 'tab2'
                            title: r"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['calculator-variant']}[/size][/font] Table"
                            
                            MDBoxLayout:
                                orientation: 'vertical'
                                padding: '10dp'
                                
                                MDScrollView:
                                    MDList:
                                        id: table_list

                        Tab:
                            id: tab3
                            name: 'tab3'
                            title: r"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-areaspline']}[/size][/font] Graph"
                            
                            MDBoxLayout:
                                orientation: 'vertical'
                                padding: '10dp'
                                
                                MDBoxLayout:
                                    orientation: 'vertical'
                                    padding: '10dp'
                                    size_hint_x: 1
                                    size_hint_y: None
                                    height: 50
                                
                                    canvas:
                                        Color:
                                            rgba: 0.2, 0.2, 0.2, 0.1
                                        Rectangle:
                                            size: self.size
                                            pos: self.pos
                                    MDLabel:
                                        text: 'Payment'
                                        halign: 'center'
                                        font_style: 'H5'
                                        height: '48dp'
                                    
                                MDBoxLayout:
                                    orientation: 'vertical'
                                    padding: '10dp'
                                    id: graph
                                    
                                    canvas:
                                        Color:
                                            rgba: 1, 0, 1, .6
                                        Rectangle:
                                            size: self.size
                                            pos: self.pos
                                
                                MDBoxLayout:
                                    orientation: 'horizontal'
                                    padding: '10dp'
                                    size_hint_x: 1
                                    size_hint_y: None
                                    height: 50
                                    
                                    MDIcon:
                                        icon: 'checkbox-blank'
                                        halign: 'right'
                                        color: 0, 0, 1, 1
                                        
                                    MDLabel:
                                        text: 'Interest'
                                        halign: 'left'
                                        font_style: 'H6'
                                        height: '48dp'
                                        
                                    MDIcon:
                                        icon: 'checkbox-blank'
                                        halign: 'right'
                                        color: 1, 0, 0, 1
                                    
                                    MDLabel:
                                        text: 'Principal'
                                        halign: 'left'
                                        font_style: 'H6'
                                        height: '48dp'
                                    
                                    
                        Tab:
                            id: tab4
                            name: 'tab4'
                            title: r"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-pie']}[/size][/font] Chart"
                            
                            MDBoxLayout:
                                orientation: 'vertical'
                                padding: '10dp'
                                
                                MDBoxLayout:
                                    orientation: 'vertical'
                                    padding: '10dp'
                                    size_hint_x: 1
                                    size_hint_y: None
                                    height: 50
                                    
                                    canvas:
                                        Color:
                                            rgba: 0.2, 0.2, 0.2, 0.1
                                        Rectangle:
                                            size: self.size
                                            pos: self.pos
                                
                                    MDLabel:
                                        text: 'Total payments'
                                        halign: 'center'
                                        font_style: 'H5'
                                        height: '48dp'
                            
                                MDBoxLayout:
                                    orientation: 'vertical'
                                    padding: '10dp'
                                    id: chart
                                    
                                    canvas:
                                        Color:
                                            rgba: 1, 1, 1, 1
                                        Rectangle:
                                            size: self.size
                                            pos: self.pos
                                
                                MDBoxLayout:
                                    orientation: 'horizontal'
                                    padding: '10dp'
                                    size_hint_x: 1
                                    size_hint_y: None
                                    height: 50
                                    
                                    MDIcon:
                                        icon: 'checkbox-blank'
                                        halign: 'right'
                                        color: 0, 0, 1, 1
                                        
                                    MDLabel:
                                        text: 'Interest'
                                        halign: 'left'
                                        font_style: 'H6'
                                        height: '48dp'
                                        
                                    MDIcon:
                                        icon: 'checkbox-blank'
                                        halign: 'right'
                                        color: 1, 0, 0, 1
                                    
                                    MDLabel:
                                        text: 'Principal'
                                        halign: 'left'
                                        font_style: 'H6'
                                        height: '48dp'
                            
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

<ItemTable>:
    size_hint_y: None
    height: '42dp'
    
    canvas:
        Color:
            rgba: root.color
        Rectangle:
            size: self.size
            pos: self.pos
    MDLabel:
        text: root.num
        halign: 'center'
        
    MDLabel:
        text: root.date
        halign: 'center'
        
    MDLabel:
        text: root.payment
        halign: 'center'
    
    MDLabel:
        text: root.interest
        halign: 'center'
    
    MDLabel:
        text: root.principal
        halign: 'center'
    
    MDLabel:
        text: root.debt
        halign: 'center'
        
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


class ItemTable(MDBoxLayout):
    num = StringProperty()
    date = StringProperty()
    payment = StringProperty()
    interest = StringProperty()
    principal = StringProperty()
    debt = StringProperty()
    color = ListProperty()


# https://stackoverflow.com/questions/2249956/how-to-get-the-same-day-of-next-month-of-a-given-day-in-python-using-datetime
def next_month_date(d):
    _year = d.year + (d.month // 12)
    _month = 1 if (d.month // 12) else d.month + 1
    next_month_len = calendar.monthrange(_year, _month)[1]
    next_month = d
    if d.day > next_month_len:
        next_month = next_month.replace(day=next_month_len)
    next_month = next_month.replace(year=_year, month=_month)
    return next_month


# https://kivy.org/doc/stable/examples/gen__canvas__canvas_stress__py.html
def show_canvas_stress(wid):
    with wid.canvas:
        for x in range(10):
            Color(random(), 1, 1, mode='hsv')
            Rectangle(pos=(random() * wid.width + wid.x, random() * wid.height + wid.y), size=(20, 20))


def draw_graph(wid, start_date, loan, months, interest, payment_type):
    with wid.canvas:
        Color(.2, .2, .2, 1)
        Line(rectangle=(wid.x, wid.y, wid.width, wid.height), width=1)
    graph_height = wid.height
    delta_width = wid.width / months

    percent = interest / 100 / 12
    monthly_payment = loan * (percent + percent / ((1 + percent) ** months - 1))
    debt_end_month = loan
    for i in range(0, months):
        repayment_of_interest = debt_end_month * percent
        repayment_of_loan_body = monthly_payment - repayment_of_interest
        debt_end_month = debt_end_month - repayment_of_loan_body
        delta_height_interest = int(repayment_of_interest * graph_height / monthly_payment)
        delta_height_loan = int(repayment_of_loan_body * graph_height / monthly_payment)
        # print("####: ", delta_height_loan, delta_height_loan)
        # print(monthly_payment, repayment_of_interest, repayment_of_loan_body, debt_end_month)
        with wid.canvas:
            Color(1, 0, 0, 1)
            Rectangle(pos=(wid.x + int(i * delta_width), wid.y), size=(int(delta_width), delta_height_loan))
            Color(0, 0, 1, 1)
            Rectangle(pos=(wid.x + int(i * delta_width), wid.y + delta_height_loan),
                      size=(int(delta_width), delta_height_interest))


def draw_chart(wid, total_amount_of_payments, loan):
    interest_chart = ((total_amount_of_payments - loan) * 360) / total_amount_of_payments
    circle_width = wid.width
    center_x = 0
    center_y = wid.height // 2 - circle_width // 2
    if (wid.width > wid.height):
        circle_width = wid.height
        center_x = wid.width // 2 - circle_width // 2
        center_y = 0
    # print(wid.x, wid.y)
    with wid.canvas:
        Color(0, 0, 1, 1)
        Ellipse(pos=(wid.x + center_x, wid.y + center_y), size=(circle_width, circle_width),
                angle_start=360 - int(interest_chart), angle_end=360)
        Color(1, 0, 0, 1)
        Ellipse(pos=(wid.x + center_x, wid.y + center_y), size=(circle_width, circle_width), angle_start=0,
                angle_end=360 - int(interest_chart))


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
        self.screen.ids.start_date.text = datetime.date.today().strftime("%d-%m-%Y")
        self.screen.ids.loan.text = "5000000"
        self.screen.ids.months.text = "120"
        self.screen.ids.interest.text = "9.5"
        self.screen.ids.payment_type.text = "annuity"

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''
        self.screen.ids.start_date.text = str(datetime.date.today().strftime("%d-%m-%Y"))

    def show_date_picker(self):
        date_dialog = MDDatePicker(
            min_date=datetime.date.today(),
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

    def calc_table(self, *args):
        print('Button1 pressed')
        start_date = self.screen.ids.start_date.text
        loan = self.screen.ids.loan.text
        months = self.screen.ids.months.text
        interest = self.screen.ids.interest.text
        payment_type = self.screen.ids.payment_type.text
        print(start_date + " " + loan + " " + months + " " + interest + " " + payment_type)
        # convert to date object, float, and so on
        start_date = datetime.datetime.strptime(self.screen.ids.start_date.text, "%d-%m-%Y").date()
        loan = float(loan)
        months = int(months)
        interest = float(interest)

        row_data_for_tab = []
        # annuity payment
        # https://temabiz.com/finterminy/ap-formula-i-raschet-annuitetnogo-platezha.html
        percent = interest / 100 / 12
        monthly_payment = loan * (percent + percent / ((1 + percent) ** months - 1))
        print(monthly_payment)

        debt_end_month = loan
        for i in range(0, months):
            repayment_of_interest = debt_end_month*percent
            repayment_of_loan_body = monthly_payment - repayment_of_interest
            debt_end_month = debt_end_month - repayment_of_loan_body
            # print(monthly_payment, repayment_of_interest, repayment_of_loan_body, debt_end_month)

        total_amount_of_payments = monthly_payment * months
        overpayment_loan = total_amount_of_payments - loan
        effective_interest_rate = ((total_amount_of_payments / loan - 1) / (months / 12)) * 100
        # print(total_amount_of_payments, overpayment_loan, effective_interest_rate)

        self.screen.ids.table_list.clear_widgets()
        self.screen.ids.table_list.add_widget(
            ItemTable(
                color=(0.2, 0.2, 0.2, 0.5),
                num='№',
                date='Date',
                payment='Payment',
                interest='Interest',
                principal='Principal',
                debt='Debt'
            )
        )
        debt_end_month = loan
        for i in range(0, months):
            row_color = (1, 1, 1, 1)
            if i % 2:
                 row_color = (0.2, 0.2, 0.2, 0.2)
            repayment_of_interest = debt_end_month * percent
            repayment_of_loan_body = monthly_payment - repayment_of_interest
            debt_end_month = debt_end_month - repayment_of_loan_body

            self.screen.ids.table_list.add_widget(
                ItemTable(
                    color=row_color,
                    num=str(i + 1),
                    date=start_date.strftime("%d-%m-%Y"),
                    payment=str(round(monthly_payment, 2)),
                    interest=str(round(repayment_of_interest, 2)),
                    principal=str(round(repayment_of_loan_body, 2)),
                    debt=str(round(debt_end_month, 2))
                )
            )
            start_date = next_month_date(start_date)

            # show_canvas_stress(self.screen.ids.graph)
            # show_canvas_stress(self.screen.ids.chart)

            self.screen.ids.graph.canvas.clear()
            draw_graph(self.screen.ids.graph, start_date, loan, months, interest, payment_type)

            self.screen.ids.chart.canvas.clear()
            draw_chart(self.screen.ids.chart, total_amount_of_payments, loan)

            pass


MorCalcApp().run()
