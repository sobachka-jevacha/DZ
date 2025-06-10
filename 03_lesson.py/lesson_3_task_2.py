from smartphone import Smartphone
catalog = [
    Smartphone("Apple", "iPhone 13 Pro Max", "+79876543210"),
    Smartphone("Samsung", "Galaxy S22 Ultra", "+79876543211"),
    Smartphone("Xiaomi", "Redmi Note 10S", "+79876543212"),
    Smartphone("Huawei", "P40 Lite", "+79876543213"),
    Smartphone("Google", "Pixel 6A", "+79876543214")
]

for item in catalog:
    print(item.phone_brand, "-", item.phone_model, ".", item.number)