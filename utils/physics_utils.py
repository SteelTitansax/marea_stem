
def kinematics(v0,a,t):
    # Kinematics formula
    v = v0 + a * t
    x = v0 * t + 0.5 * a * t**2

    print(f"Velocidad final (m/s)      : {v}")
    print(f"Desplazamiento (m)         : {x}")

def dynamics(F,m):
    # Example of second Newton's law
    a = F / m
    print(f"Aceleración resultante (m/s²) : {a}")


def classic_gravity(G,m1,m2,r):
    Fg = G * m1 * m2 / r**2
    print(f"Fuerza gravitatoria (N) : {Fg}")

def coulomb(k,q1,q2,r):
    Fe = k * q1 * q2 / r**2
    print(f"Fuerza eléctrica (N) : {Fe}")


import math

def static_equilibrium(forces, moments):
    """
    forces: list of tuples (Fx, Fy)
    moments: list of moments about a reference point (N·m)
    """
    sum_fx = sum(f[0] for f in forces)
    sum_fy = sum(f[1] for f in forces)
    sum_m = sum(moments)

    return sum_fx, sum_fy, sum_m


def run_static_analysis():
    # ====== INTERACTIVE STATIC ANALYSIS ======
    print("\n--- ANÁLISIS DE ESTÁTICA ---\n")

    num_forces = int(input("Número de fuerzas aplicadas: "))
    forces = []
    moments = []

    for i in range(num_forces):
        print(f"\nFuerza {i+1}")
        F = float(input("Magnitud de la fuerza (N): "))
        angle_deg = float(input("Ángulo respecto al eje x (grados): "))
        distance = float(input("Distancia al punto de referencia (m): "))

        # Resolve force into components
        Fx = F * math.cos(math.radians(angle_deg))
        Fy = F * math.sin(math.radians(angle_deg))

        # Simple 2D moment (planar assumption)
        M = Fy * distance

        forces.append((Fx, Fy))
        moments.append(M)

    # Weight input
    weight = float(input("\nPeso del objeto (N): "))
    forces.append((0.0, -weight))

    # Compute equilibrium
    sum_fx, sum_fy, sum_m = static_equilibrium(forces, moments)

    # ====== RESULTS ======
    print("\n--- RESULTADOS DE ESTÁTICA ---")
    print(f"ΣFx = {sum_fx:.2f} N")
    print(f"ΣFy = {sum_fy:.2f} N")
    print(f"ΣM  = {sum_m:.2f} N·m")

    tolerance = 1e-3
    if abs(sum_fx) < tolerance and abs(sum_fy) < tolerance and abs(sum_m) < tolerance:
        print("✅ El sistema está en equilibrio estático")
    else:
        print("❌ El sistema NO está en equilibrio")
