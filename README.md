# Weather App

A desktop weather application built with PyQt5 that provides real-time weather information with a clean, modern interface.

## Features

- **Real-time Weather Data**: Fetches current weather from OpenWeatherMap API
- **Visual Weather Indicators**: Dynamic emoji display based on weather conditions
- **Temperature Display**: Shows temperature in Celsius with automatic conversion
- **Professional UI**: Custom fonts, styling, and hover effects
- **Comprehensive Error Handling**: Handles network issues and invalid inputs gracefully

## Technical Implementation

- **GUI Framework**: PyQt5 for cross-platform desktop interface
- **API Integration**: OpenWeatherMap API with proper authentication
- **Error Management**: Comprehensive HTTP status code handling
- **Custom Styling**: CSS-like styling with custom fonts and responsive design
- **Weather Mapping**: Intelligent emoji selection based on weather condition IDs

## Installation

```bash
pip install PyQt5 requests
```

## Usage

```bash
python main.py
```



<p align="center">
  <img src="https://github.com/user-attachments/assets/59011653-3c71-4a15-94c0-09e759eb66eb" alt="weatherapp_gui" width="300"/>
</p>

1. Enter a city name in the input field
2. Click "Get Weather" to fetch current conditions
3. View temperature, description, and weather emoji

## Key Features

### Weather Condition Mapping
- Thunderstorms ⛈️
- Rain 🌧️
- Snow ❄️  
- Clear skies ☀️
- Clouds ☁️
- And more weather conditions

### Error Handling
- Network connectivity issues
- Invalid city names
- API rate limiting
- Server errors

## Dependencies

- PyQt5: GUI framework
- requests: HTTP requests for API calls
- OpenWeatherMap API: Weather data source

This project demonstrates desktop GUI development, API integration, and professional error handling in Python.
