class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__cantidad = cantidad

    # Métodos getters
    def get_nombre(self):
        return self.__nombre

    def get_categoria(self):
        return self.__categoria

    def get_precio(self):
        return self.__precio

    def get_cantidad(self):
        return self.__cantidad

    # Métodos setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_categoria(self, categoria):
        self.__categoria = categoria

    def set_precio(self, precio):
        self.__precio = precio

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def __str__(self):
        return f"{self.__nombre} | {self.__categoria} | €{self.__precio} | {self.__cantidad} unidades"


class Inventario:
    def __init__(self):
        self.__productos = []

    # Método para agregar un producto
    def create_producto(self, producto):
        self.__productos.append(producto)

    # Método para listar todos los productos
    def list_productos(self):
        return self.__productos

    # Método para buscar un producto por nombre
    def get_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                return producto
        return None

    # Método para modificar un producto
    def update_producto(self, nombre, nuevo_producto):
        for i, producto in enumerate(self.__productos):
            if producto.get_nombre() == nombre:
                self.__productos[i] = nuevo_producto
                return True
        return False

    # Método para eliminar un producto
    def delete_producto(self, nombre):
        producto = self.get_producto(nombre)
        if producto:
            self.__productos.remove(producto)
            return True
        return False


class Menu:
    def __init__(self, inventario):
        self.__inventario = inventario

    def mostrar_menu(self):
        while True:
            print("\n--- MENU ---")
            print("1. Listar productos")
            print("2. Crear producto")
            print("3. Buscar producto")
            print("4. Modificar producto")
            print("5. Eliminar producto")
            print("6. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.listar_productos()
            elif opcion == "2":
                self.crear_producto()
            elif opcion == "3":
                self.buscar_producto()
            elif opcion == "4":
                self.modificar_producto()
            elif opcion == "5":
                self.eliminar_producto()
            elif opcion == "6":
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def listar_productos(self):
        print("\n--- Lista de Productos ---")
        productos = self.__inventario.list_productos()
        if productos:
            for producto in productos:
                print(producto)  # Usa `__str__` de Producto
        else:
            print("No hay productos registrados.")

    def crear_producto(self):
        print("\n--- Crear Producto ---")

        while True:
            nombre = input("Nombre: ").strip()
            if not nombre:
                print('¡El campo Nombre no puede estar vacío! Intente nuevamente.')
                continue

            nombre = nombre.upper()

            if len(nombre) > 15:
                print('¡El campo Nombre no puede tener más de 15 caracteres! Intente nuevamente.')
                continue

            if len(nombre) < 3:
                print('¡El campo Nombre no puede tener menos de 3 caracteres! Intente nuevamente.')
                continue

            if any(producto.get_nombre == nombre for producto in self.__inventario.list_productos()):
                print("¡El producto ya existe en el Inventario! Intente con otro Nombre.")
                continue
            break

        while True:
            categoria = input("Categoría: ").strip()
            if not categoria:
                print('¡El campo Categoria no puede estar vacío! Intente nuevamente')
                continue

            categoria = categoria.upper()

            if len(categoria) > 15:
                print('¡El campo Categoria no puede tener más de 15 caracteres! Intente nuevamente.')
                continue

            if len(categoria) < 3:
                print('¡El campo Categoria no puede tener menos de 3 caracteres! Intente nuevamente.')
                continue

            break

        while True:
            precio = input("Precio: ")

            if not precio:
                print("¡El campo Precio no puede estar vacío! Intente nuevamente.")
                continue

            try:
                precio = float(precio)
                if precio <= 0:
                    print("¡El Precio debe ser mayor que 0! Intente nuevamente.")
                    continue
                break
            except ValueError:
                print("¡Ingrese un valor numérico válido! (Ejemplo: 99.99)!")

        while True:

            cantidad = input("Cantidad: ")
            if not cantidad:
                print("¡El campo Cantidad no puede estar vacío! Intente nuevamente.")
                continue

            try:
                cantidad = int(cantidad)
                if cantidad < 0:
                    print("¡La Cantidad deve ser zero o maior que zero! Intente nuevamente")
                    continue
                break
            except ValueError:
                print("¡Ingrese un valor numérico válido! (Example: 0-999).")

        producto = Producto(nombre, categoria, precio, cantidad)

        self.__inventario.create_producto(producto)
        print("*** Producto agregado exitosamente. ***")


    def buscar_producto(self):
        print("\n--- Buscar Producto ---")
        nombre = input("Ingrese el nombre del producto: ")
        producto = self.__inventario.get_producto(nombre)
        if producto:
            print("Producto encontrado:")
            print(producto)
        else:
            print("Producto no encontrado.")

    def modificar_producto(self):
        print("\n--- Modificar Producto ---")
        nombre = input("Ingrese el nombre del producto a modificar: ")
        producto_actual = self.__inventario.get_producto(nombre)

        if producto_actual:
            print("Ingrese los nuevos datos del producto:")


            while True:
                nuevo_nombre = input("Nuevo nombre: ")
                if not nuevo_nombre:
                    print('¡El campo Nombre no puede estar vacío! Intente nuevamente.')
                    continue

                nuevo_nombre = nuevo_nombre.upper()

                if len(nuevo_nombre) > 15:
                    print('¡El campo Nombre no puede tener más de 15 caracteres! Intente nuevamente.')
                    continue

                if len(nuevo_nombre) < 3:
                    print('¡El campo Nombre no puede tener menos de 3 caracteres! Intente nuevamente.')
                    continue

                if any(producto.get_nombre == nuevo_nombre for producto in self.__inventario.list_productos()):
                    print("¡El producto ya existe en el Inventario! Intente con otro Nombre.")
                    continue
                break

            while True:
                nueva_categoria = input("Nueva categoría: ")
                if not nueva_categoria:
                    print('¡El campo Categoria no puede estar vacío! Intente nuevamente')
                    continue

                nueva_categoria = nueva_categoria.upper()

                if len(nueva_categoria) > 15:
                    print('¡El campo Categoria no puede tener más de 15 caracteres! Intente nuevamente.')
                    continue

                if len(nueva_categoria) < 3:
                    print('¡El campo Categoria no puede tener menos de 3 caracteres! Intente nuevamente.')
                    continue
                break

            while True:
                nuevo_precio = input("Nuevo precio: ")

                if not nuevo_precio:
                    print("¡El campo Precio no puede estar vacío! Intente nuevamente.")
                    continue

                try:
                    nuevo_precio = float(nuevo_precio)
                    if nuevo_precio <= 0:
                        print("¡El Precio debe ser mayor que 0! Intente nuevamente.")
                        continue
                    break
                except ValueError:
                    print("¡Ingrese un valor numérico válido! (Ejemplo: 99.99)!")

            while True:
                nueva_cantidad = input("Nueva cantidad: ")

                if not nueva_cantidad:
                    print("¡El campo Cantidad no puede estar vacío! Intente nuevamente.")
                    continue

                try:
                    nueva_cantidad = int(nueva_cantidad)
                    if nueva_cantidad < 0:
                        print("¡La Cantidad deve ser zero o maior que zero! Intente nuevamente")
                        continue
                    break
                except ValueError:
                    print("¡Ingrese un valor numérico válido! (Example: 0-999).")


            nuevo_producto = Producto(nuevo_nombre, nueva_categoria, nuevo_precio, nueva_cantidad)
            self.__inventario.update_producto(nombre, nuevo_producto)

            print("Producto modificado exitosamente.")

        else:
            print("Producto no encontrado.")

    def eliminar_producto(self):
        print("\n--- Eliminar Producto ---")
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        if self.__inventario.delete_producto(nombre):
            print("Producto eliminado exitosamente.")
        else:
            print("Producto no encontrado.")


# Inicializar el sistema
inventario = Inventario()
menu = Menu(inventario)
menu.mostrar_menu()
