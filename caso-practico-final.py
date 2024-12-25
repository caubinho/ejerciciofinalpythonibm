#Caso Práctico Final Curso Python 2024
#Alumno Clauberson Pacheco

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
        # Mensaje inicial indicando que se va a crear un nuevo producto
        print("\n--- Crear Producto ---")

        # Solicitar y validar el nombre del producto
        while True:
            nombre = input("Nombre (mínimo 3 caracteres, máximo 30): ").strip()  # Solicitar el nombre y eliminar espacios adicionales
            if not nombre:  # Validar que el campo no esté vacío
                print('¡El campo Nombre no puede estar vacío! Intente nuevamente.')
                continue

            nombre = nombre.upper()  # Convertir el nombre a mayúsculas para consistencia

            # Validar la longitud del nombre (máximo y mínimo)
            if len(nombre) > 30:
                print('¡El campo Nombre no puede tener más de 30 caracteres! Intente nuevamente.')
                continue
            if len(nombre) < 3:
                print('¡El campo Nombre no puede tener menos de 3 caracteres! Intente nuevamente.')
                continue

            # Verificar que el nombre no exista en el inventario
            if any(producto.get_nombre() == nombre for producto in self.__inventario.list_productos()):
                print("¡El producto ya existe en el Inventario! Intente con otro Nombre.")
                continue
            break  # Salir del bucle si todas las validaciones son exitosas

        # Solicitar y validar la categoría del producto
        while True:
            categoria = input("Categoría (mínimo 3 caracteres, máximo 15): ").strip()  # Solicitar la categoría y eliminar espacios adicionales
            if not categoria:  # Validar que el campo no esté vacío
                print('¡El campo Categoria no puede estar vacío! Intente nuevamente')
                continue

            categoria = categoria.upper()  # Convertir la categoría a mayúsculas para consistencia

            # Validar la longitud de la categoría (máximo y mínimo)
            if len(categoria) > 15:
                print('¡El campo Categoria no puede tener más de 15 caracteres! Intente nuevamente.')
                continue
            if len(categoria) < 3:
                print('¡El campo Categoria no puede tener menos de 3 caracteres! Intente nuevamente.')
                continue
            break  # Salir del bucle si todas las validaciones son exitosas

        # Solicitar y validar el precio del producto
        while True:
            precio = input("Precio: ")  # Solicitar el precio
            if not precio:  # Validar que el campo no esté vacío
                print("¡El campo Precio no puede estar vacío! Intente nuevamente.")
                continue

            try:
                precio = float(precio)  # Intentar convertir el precio a un número flotante
                if precio <= 0:  # Validar que el precio sea mayor que 0
                    print("¡El Precio debe ser mayor que 0! Intente nuevamente.")
                    continue
                break  # Salir del bucle si la validación es exitosa
            except ValueError:  # Capturar errores de conversión
                print("¡Ingrese un valor numérico válido! (Ejemplo: 99.99)!")

        # Solicitar y validar la cantidad del producto
        while True:
            cantidad = input("Cantidad: ")  # Solicitar la cantidad
            if not cantidad:  # Validar que el campo no esté vacío
                print("¡El campo Cantidad no puede estar vacío! Intente nuevamente.")
                continue

            try:
                cantidad = int(cantidad)  # Intentar convertir la cantidad a un número entero
                if cantidad < 0:  # Validar que la cantidad sea cero o mayor
                    print("¡La Cantidad deve ser zero o maior que zero! Intente nuevamente")
                    continue
                break  # Salir del bucle si la validación es exitosa
            except ValueError:  # Capturar errores de conversión
                print("¡Ingrese un valor numérico válido! (Example: 0-999).")

        # Crear un objeto Producto con los datos ingresados
        producto = Producto(nombre, categoria, precio, cantidad)

        # Agregar el producto al inventario
        self.__inventario.create_producto(producto)

        # Confirmar al usuario que el producto fue agregado exitosamente
        print("¡Producto agregado exitosamente!")

    def buscar_producto(self):
        print("\n--- Buscar Producto ---")
        nombre = input("Ingrese el nombre del producto: ")

        # Convertir el nombre ingresado a mayúsculas
        nombre = nombre.upper()

        # Intentar obtener el producto del inventario
        producto = self.__inventario.get_producto(nombre)

        if producto:
            print("Producto encontrado:")
            print(producto)
        else:
            print("¡Producto no encontrado!.")

    def modificar_producto(self):
        print("\n--- Modificar Producto ---")
        nombre = input("Ingrese el nombre del producto a modificar: ")

        nombre = nombre.upper()

        producto_actual = self.__inventario.get_producto(nombre)

        if producto_actual:
            print("Ingrese los nuevos datos del producto (deje vacío para mantener el valor actual):")

            # Modificar el nombre
            while True:
                # Mostrar el nombre actual como sugerencia
                nuevo_nombre = input(f"Nuevo nombre [{producto_actual.get_nombre()}]: ").strip()
                if not nuevo_nombre:  # Mantener el valor actual si el campo está vacío
                    nuevo_nombre = producto_actual.get_nombre()

                # Convertir el nombre ingresado a mayúsculas
                nuevo_nombre = nuevo_nombre.upper()

                # Validaciones para el nuevo nombre
                if len(nuevo_nombre) > 30:
                    print('¡El campo Nombre no puede tener más de 30 caracteres! Intente nuevamente.')
                    continue

                if len(nuevo_nombre) < 3:
                    print('¡El campo Nombre no puede tener menos de 3 caracteres! Intente nuevamente.')
                    continue

                # Verificar si el nombre ya existe en el inventario (excepto el producto actual)
                if nuevo_nombre != producto_actual.get_nombre() and any(
                        producto.get_nombre() == nuevo_nombre for producto in self.__inventario.list_productos()
                ):
                    print("¡El producto ya existe en el Inventario! Intente con otro Nombre.")
                    continue
                break

            # Modificar la categoría
            while True:
                nueva_categoria = input(f"Nueva categoría [{producto_actual.get_categoria()}]: ").strip()
                if not nueva_categoria:
                    nueva_categoria = producto_actual.get_categoria()
                nueva_categoria = nueva_categoria.upper()

                if len(nueva_categoria) > 15:
                    print('¡El campo Categoria no puede tener más de 15 caracteres! Intente nuevamente.')
                    continue

                if len(nueva_categoria) < 3:
                    print('¡El campo Categoria no puede tener menos de 3 caracteres! Intente nuevamente.')
                    continue
                break

            # Modificar el precio
            while True:
                nuevo_precio = input(f"Nuevo precio [{producto_actual.get_precio()}]: ").strip()
                if not nuevo_precio:
                    nuevo_precio = producto_actual.get_precio()
                    break
                try:
                    nuevo_precio = float(nuevo_precio)
                    if nuevo_precio <= 0:
                        print("¡El Precio debe ser mayor que 0! Intente nuevamente.")
                        continue
                    break
                except ValueError:
                    print("¡Ingrese un valor numérico válido! (Ejemplo: 99.99)")

            # Modificar la cantidad
            while True:
                nueva_cantidad = input(f"Nueva cantidad [{producto_actual.get_cantidad()}]: ").strip()
                if not nueva_cantidad:
                    nueva_cantidad = producto_actual.get_cantidad()
                    break
                try:
                    nueva_cantidad = int(nueva_cantidad)
                    if nueva_cantidad < 0:
                        print("¡La Cantidad debe ser cero o mayor que cero! Intente nuevamente.")
                        continue
                    break
                except ValueError:
                    print("¡Ingrese un valor numérico válido! (Ejemplo: 0-999).")

            # Crear un nuevo objeto Producto con los datos actualizados
            nuevo_producto = Producto(nuevo_nombre, nueva_categoria, nuevo_precio, nueva_cantidad)

            # Actualizar el producto en el inventario
            self.__inventario.update_producto(nombre, nuevo_producto)

            print("¡Producto modificado exitosamente!.")

        else:
            print("¡Producto no encontrado!.")

    def eliminar_producto(self):
        print("\n--- Eliminar Producto ---")
        nombre = input("Ingrese el nombre del producto a eliminar: ")

        nombre = nombre.upper()

        if self.__inventario.delete_producto(nombre):
            print("¡Producto eliminado exitosamente!.")
        else:
            print("¡Producto no encontrado!.")


# Inicializar el sistema
inventario = Inventario()
menu = Menu(inventario)
menu.mostrar_menu()