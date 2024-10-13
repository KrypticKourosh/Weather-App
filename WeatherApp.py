from PyQt5.QtGui import QIcon, QFontDatabase, QFont
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
import requests

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)

        self.widgets_list = [self.city_label, self.city_input,
                             self.get_weather_button,
                             self.temperature_label,
                             self.emoji_label,
                             self.description_label]

        self.init_ui()

    def init_ui(self):
        #general UI:
        self.setWindowTitle("WeatherApp")
        self.setWindowIcon(QIcon("images/WindowsIcon.png"))
        self.setGeometry(700, 350, 400, 500)

        #layout & alignment:
        self.set_layout()
        self.set_alignment()

        #style_sheet:
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        #font set up
        my_font = self.set_font(path="Fonts/Fredoka_SemiCondensed-Regular.ttf")
        for w in self.widgets_list:
            w.setFont(my_font)


        self.setStyleSheet("""
        QWidget{
        font-size:50px;        
        }
        
        WeatherApp{
        background-color:hsl(200, 85%, 83%);
        }
        
        QPushButton#get_weather_button{
        background-color:hsl(200, 75%, 90%);
        }
        
        QPushButton#get_weather_button:hover{
        background-color:hsl(200, 80%, 95%);
        }
        
        QWidget#emoji_label{
        font-family: Segoe Emoji ui
        }
            
        """)

        #signals:
        self.get_weather_button.clicked.connect(self.get_weather)


    #GUI methods:
    def set_layout(self):
        vbox = QVBoxLayout()

        for widget in self.widgets_list:
            vbox.addWidget(widget)

        self.setLayout(vbox)

    def set_alignment(self):
        for widget in [w for w in self.widgets_list if not isinstance(w, QPushButton)]:
            widget.setAlignment(Qt.AlignCenter)

    def set_font(self, path):
        font_id = QFontDatabase.addApplicationFont(path)
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family)
        return my_font


    #funtionality methods:
    def get_weather(self): #going to use API
        api_key = "f45ac5892f8cecc1cd09035544542f54"
        city_name = self.city_input.text()

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"


        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request: \nPlease check your input")
                case 401:
                    self.display_error("Unauthorized: \nInvalid API key")
                case 403:
                    self.display_error("Forbidden: \nAccess denied")
                case 404:
                    self.display_error("Not Found: \ncity is not found")
                case 500:
                    self.display_error("Internal server error: \nPlease try again later")
                case 502:
                    self.display_error("Bad gateway: \nInvalid response from the server")
                case 503:
                    self.display_error("Server unavailable: \nServer is down")
                case 504:
                    self.display_error("Gateway timeout: \nNo response from the server")
                case _:
                    self.display_error(f"HTTP error occurred: \n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error: \ncheck your internet connection")

        except requests.exceptions.Timeout:
            self.display_error("Timeout error: \nThe request timed out")

        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects: \ncheck URL")

        except requests.exceptions.RequestException as req_error: #connection errors, invalid URL, etc. #last option
            self.display_error(f"Request Error: \n Error:{req_error}")



    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size:30px;")
        self.description_label.setText("") #resets des_label: invalid input after a valid input
        self.emoji_label.setText("")
        self.temperature_label.setText(message)


    def display_weather(self, data):
        #temperature_label setup:
        self.temperature_label.setStyleSheet("font-size:50px;")
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        temperature_f = (temperature_k * 9/5) - 459.67
        self.temperature_label.setText(f"{temperature_c:.0f}°C")

        #description_label setup:
        weather_description = data["weather"][0]["description"]
        self.description_label.setText(weather_description)

        #emoji_label setup:
        weather_id = data["weather"][0]["id"]
        self.emoji_label.setStyleSheet("font-family:Segoe Emoji UI;")
        emoji_symbol = self.get_weather_emoji(weather_id)
        self.emoji_label.setText(emoji_symbol)

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️" #thunderstorm
        elif 302 <= weather_id <= 321:
            return "🌦️" #Drizzle
        elif 500 <= weather_id <= 531:
            return "🌧️" #Rain
        elif 600 <= weather_id <= 622:
            return "❄️" #Snow
        elif 701 <= weather_id <= 741:
            return "🌫️" #Atmosphere like fog
        elif weather_id == 762:
            return "🌋" #volcano
        elif weather_id == 771:
            return "💨" #heavy wind
        elif weather_id == 781:
            return "🌪️" #tornado
        elif weather_id == 800:
            return "☀️" #clear sky
        elif 801 <= weather_id <= 804:
            return "☁️" #cloudy
        else:
            return ""