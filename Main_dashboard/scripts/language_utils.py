def get_text(key, language):
    translations = {
        'nav_title': {
            'en': 'Mexico City Air Quality Forecast',
            'es': 'Monitor del Índice Aire y Salud de México'
        },
        'select_page': {
            'en': 'Select Page',
            'es': 'Seleccionar página'
        },
        'page1': {
            'en': 'Air and Health Index Heatmap',
            'es': 'Mapa de Calor Índice Aire y Salud'
        },
        'page2': {
            'en': 'Forecast',
            'es': 'Pronostico'
        },
        'page3': {
            'en': 'New home',
            'es': 'Nuevo Inicio'
        },
        'page4': {
            'en': 'Health Recommendations',
            'es': 'Recomendaciones de Salud'
        },
        'current_aqi': {
            'en': 'Current Air and Health Index',
            'es': 'Índice Aire y Salud Actual'
        },
        'pollutant_levels': {
            'en': 'Pollutant Levels',
            'es': 'Niveles de Contaminantes'
        },
        'station_aqi': {
            'en': 'Station Air and Health Index',
            'es': 'Niveles del Índice Aire y Salud por Estación'
        },
        'refresh_map': {
            'en': 'Refresh Map',
            'es': 'Actualizar Mapa'
        },
        'aqi_heatmap': {
            'en': 'Air and Health Index Heatmap of Mexico Monitoring Stations',
            'es': 'Mapa de Calor Índice Aire y Salud de Estaciones de Monitoreo'
        },
        # AQI Status translations
        'good': {
            'en': 'Good',
            'es': 'Bueno'
        },
        'moderate': {
            'en': 'Moderate',
            'es': 'Moderado'
        },
        'unhealthy_sensitive': {
            'en': 'Unhealthy for Sensitive Groups',
            'es': 'Poco saludable para grupos sensibles'
        },
        'unhealthy': {
            'en': 'Unhealthy',
            'es': 'Poco saludable'
        },
        'very_unhealthy': {
            'en': 'Very Unhealthy',
            'es': 'Muy poco saludable'
        },
        'hazardous': {
            'en': 'Hazardous',
            'es': 'Peligroso'
        },
        # Station translations
        'Ajusco Medio': {
            'en': 'Ajusco Medio',
            'es': 'Ajusco Medio'
        },
        'Ajusco': {
            'en': 'Ajusco',
            'es': 'Ajusco'
        },
        'Benito Juarez': {
            'en': 'Benito Juarez',
            'es': 'Benito Juárez'
        },
        'Hospital General': {
            'en': 'General Hospital',
            'es': 'Hospital General de México'
        },
        'Merced': {
            'en': 'Merced',
            'es': 'Merced'
        },
        'Miguel Hidalgo': {
            'en': 'Miguel Hidalgo',
            'es': 'Miguel Hidalgo'
        },
        'Milpa Alta': {
            'en': 'Milpa Alta',
            'es': 'Milpa Alta'
        },
        'Pedregal': {
            'en': 'Pedregal',
            'es': 'Pedregal'
        },
        'San Agustin': {
            'en': 'San Agustin',
            'es': 'San Agustín'
        },
        'Santa Fe': {
            'en': 'Santa Fe',
            'es': 'Santa Fe'
        },
        'Tlalnepantla': {
            'en': 'Tlalnepantla',
            'es': 'Tlalnepantla'
        },
        'UAM Iztapalapa': {
            'en': 'UAM Iztapalapa',
            'es': 'UAM Iztapalapa'
        },
        'Xalostoc': {
            'en': 'Xalostoc',
            'es': 'Xalostoc'
        },
        'station': {
            'en': 'Station',
            'es': 'Estación'
        },
        'select_station': {
            'en': 'Select Station',
            'es': 'Seleccionar Estación'
        },
        'All Stations': {
            'en': 'All Stations',
            'es': 'Todas las Estaciones'
        },
        'current_forecast': {
            'en': 'Air Quality Forecast',
            'es': 'Pronostico de Calidad del Aire'
        },
        'air_quality_index': {
            'en': 'Air Quality Index',
            'es': 'Índice de calidad del aire'
        },
        ''
        'humidity': {
            'en': 'Humidity',
            'es': 'Humedad'
        },
        'pressure': {
            'en': 'Pressure',
            'es': 'Presión'
        },
        'wind_speed': {
            'en': 'Wind Speed',
            'es': 'Velocidad del viento'
        },
        'o3': {
            'en': 'Ozone',
            'es': 'Ozono'
        },
        'no2': {
            'en': 'Nitrogen Dioxide',
            'es': 'Dióxido de nitrógeno'
        },
        'pm10': {
            'en': 'PM10',
            'es': 'PM10'
        },
        'pm25': {
            'en': 'PM2.5',
            'es': 'PM2.5'
        },
        'co': {
            'en': 'CO',
            'es': 'CO'
        },
        'so2': {
            'en': 'SO2',
            'es': 'SO2'
        },
        'metric': {
            'en': 'Metric',
            'es': 'Métrica de medida'
        },
        'pollutants': {
            'en': 'Pollutants',
            'es': 'Contaminantes'
        },
        'temperature': {
            'en': 'Temperature',
            'es': 'Temperatura'
        },
        'time_of_day': {
            'en': 'Time of day',
            'es': 'Hora del día'
        }
    }
    
    return translations.get(key, {}).get(language, key) 