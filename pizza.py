def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print(f"\n制作 {size} 大小的披萨")
    for topping in toppings:
        print("- " + topping)