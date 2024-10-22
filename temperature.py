def konversisuhu(temperature, value):
    if value == 'C':
        # Mengonversi dari Fahrenheit ke Celsius
        temperaturesuhu = (temperature - 32) *5/9
        return temperaturesuhu, 'C'
    else:
        # Mengonversi dari Celsius ke Fahrenhei
        temperaturesuhu = (temperature * 9/5) + 32
        return temperaturesuhu, 'F'
 # Contoh penggunaan untuk konversi dari Celsius ke Fahrenheit   
celcius_temperature = 30
temperaturesuhu, target_value = konversisuhu(celcius_temperature, 'F')
print(f"{celcius_temperature}°C dikonversi ke Fahrenheit adalah {temperaturesuhu}°{target_value}")

# Contoh penggunaan untuk konversi dari Fahrenheit ke Celsius
fahrenheit_temperature = 86
temperaturesuhu, target_value = konversisuhu(fahrenheit_temperature, 'C')
print(f"{fahrenheit_temperature}°F dikonversi ke Celcius adalah {temperaturesuhu}°{target_value}")