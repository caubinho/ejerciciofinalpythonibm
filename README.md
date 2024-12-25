Ejercicio Final - Enunciado
Descripción: Crea una aplicación en Python para la gestión de un inventario de productos, usando programación orientada a objetos (POO). El sistema debe permitir agregar, actualizar, eliminar y mostrar productos en un inventario, cada uno de los cuales es representado como un objeto de la clase Producto.

Requisitos:
1.Clases y Objetos:
  Implementar una clase Producto con los siguientes atributos:
      ▪nombre: El nombre del producto.
      ▪categoria: La categoría a la que pertenece el producto.
      ▪precio: El precio del producto (debe ser mayor que 0).
      ▪cantidad: La cantidad en stock (debe ser mayor o igual que 0).
   Implementar una clase Inventario que maneje una lista de productos y permita las siguientes operaciones:

  1.Agregar un producto: Verificar que el producto no exista previamente en el inventario.
  2.Actualizar un producto: Modificar el precio o la cantidad en stock de un producto ya existente.
  3.Eliminar un producto: Quitar un producto del inventario.
  4.Mostrar inventario: Listar todos los productos disponibles.
  5.Buscar un producto: Permitir buscar un producto por nombre.

2.Validaciones:
  El precio debe ser siempre mayor que 0.
  La cantidad debe ser mayor o igual que 0.
  Manejar correctamente las excepciones y validar entradas (evitar que el usuario ingrese datos no válidos).

3.Funciones y Métodos:
  Todos los atributos deben ser privados, utilizando getters y setters para acceder y modificar los valores.
  Deben implementarse métodos para cada una de las funcionalidades mencionadas (agregar, actualizar, eliminar, etc.).
