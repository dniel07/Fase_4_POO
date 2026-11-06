"""Ejecución demostrativa con pruebas válidas e inválidas."""
from .clientes import Cliente
from .servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from .reservas import Reserva
from .excepciones import SoftwareFJError
from .logs import obtener_logger

def ejecutar_demostracion():
    logger = obtener_logger()
    clientes, servicios, reservas = [], [], []
    contador = 0

    def registrar(mensaje):
        nonlocal contador
        contador += 1
        print(f"\n[OPERACIÓN {contador}] {mensaje}")
        logger.info(mensaje)

    # 1. Cliente válido.
    c1 = Cliente("C001", "Laura Gómez", "laura@example.com", "3001234567")
    clientes.append(c1); registrar("Cliente creado: " + c1.describir())

    # 2. Cliente inválido.
    try:
        Cliente("C002", "", "correo-malo", "123")
    except SoftwareFJError as error:
        registrar("Cliente inválido controlado: " + str(error))

    # 3. Segundo cliente válido.
    c2 = Cliente("C003", "Carlos Ruiz", "carlos@example.com", "3105550101")
    clientes.append(c2); registrar("Segundo cliente creado: " + c2.describir())

    # 4. Servicio de sala.
    sala = ReservaSala("S001", "Sala de reuniones", 50000)
    servicios.append(sala); registrar(sala.describir())

    # 5. Servicio con tarifa negativa.
    try:
        ReservaSala("S002", "Sala inválida", -100)
    except SoftwareFJError as error:
        registrar("Servicio inválido controlado: " + str(error))

    # 6 y 7. Servicios adicionales.
    equipo = AlquilerEquipo("S003", "Alquiler de portátil", 80000)
    asesoria = AsesoriaEspecializada("S004", "Asesoría técnica", 120000)
    servicios.extend([equipo, asesoria])
    registrar(equipo.describir()); registrar(asesoria.describir())

    # 8. Reserva válida.
    r1 = Reserva("R001", c1, sala, 2, impuesto=0.19, descuento=0.10)
    reservas.append(r1); registrar("Reserva creada: " + r1.describir())

    # 9. Reserva con cliente inexistente.
    try:
        Reserva("R002", None, equipo, 1)
    except SoftwareFJError as error:
        registrar("Reserva inválida controlada: " + str(error))

    # 10. Confirmación y procesamiento.
    r1.confirmar()
    registrar(f"Reserva procesada por ${r1.procesar():.2f}")

    # 11. Cancelación prohibida.
    try:
        r1.cancelar()
    except SoftwareFJError as error:
        registrar("Cancelación bloqueada: " + str(error))

    # 12. Cantidad incorrecta.
    try:
        sala.calcular_costo(-2)
    except SoftwareFJError as error:
        registrar("Cálculo inválido controlado: " + str(error))

    # 13. Cálculo con impuestos y descuento.
    registrar(f"Equipo por 3 días: ${equipo.calcular_costo(3, 0.19, 0.05):.2f}")

    # 14. Reserva cancelada.
    r2 = Reserva("R003", c2, asesoria, 1)
    reservas.append(r2); r2.cancelar()
    try:
        r2.confirmar()
    except SoftwareFJError as error:
        registrar("Estado inválido controlado: " + str(error))

    # 15. Ejemplo de try/except/else/finally y encadenamiento.
    try:
        encontrado = next(c for c in clientes if c.identificador == "C001")
    except StopIteration as error:
        raise LookupError("No existe el cliente solicitado.") from error
    else:
        registrar("Consulta correcta: " + encontrado.nombre)
    finally:
        logger.info("La consulta terminó.")

    print(f"\nFin: {contador} operaciones; {len(clientes)} clientes, "
          f"{len(servicios)} servicios y {len(reservas)} reservas.")

if __name__ == "__main__":
    ejecutar_demostracion()
