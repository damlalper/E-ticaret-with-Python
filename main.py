from product import Product
from cart import Cart
from customer import Customer
from order import Order


def main():
    products = {
        "Çilek": Product("Çilek", 15, 30),
        "Erik": Product("Erik", 20, 35),
        "Karpuz": Product("Karpuz", 10, 25)
    }

    customer_name = input("müşteri adınızı girin: ")
    customer_email = input("E-Postanızı girin: ")
    customer = Customer(customer_name, customer_email)

    cart = Cart()

    while True:
        print("\nYapmak İstediğiniz İşlemi Seçiniz:")
        print("1. Ürün ekle")
        print("2. Ürün çıkar")
        print("3. Sepeti görüntüle")
        print("4. Siparişi Tamamla")
        print("5. Çıkış")

        choice = input("seçiminiz: ")

        if choice == "1":
            print("mevcut ürünler:")
            for product in products.values():
                print(product)
            product_name = input("ekleyeceğiniz ürünün adı: ")
            if product_name in products:
                quantity = int(input("kaç tane eklemek istersiniz?: "))
                cart.add_product(products[product_name], quantity)
                print(f"{quantity} adet {product_name} sepete eklendi")
            else:
                print("ürün bulunamadı")

        elif choice == "2":
            product_name = input("çıkaracağınız ürünün adı: ")
            cart.remove_product(product_name)
            print(f"{product_name} sepetten çıkarıldı")

        elif choice == "3":
            print("\nsepetiniz:")
            cart.display_cart()
            print(f"toplam tutar: {cart.get_total()} TL")

        elif choice == "4":
            order = Order(customer, cart)
            order.place_order()
            break

        elif choice == "5":
            print("çıkış yapılıyor...")
            break

        else:
            print("geçersiz seçim, tekrar deneyin")


if __name__ == "__main__":
    main()
