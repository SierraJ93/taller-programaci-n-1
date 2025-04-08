class ExcesoVelocidadException(Exception):
    def __init__(self, mensaje="Velocidad excedida. No se pueden superar los 200 km/h (piensa en que te esperan en casa)"):
        super().__init__(mensaje)
