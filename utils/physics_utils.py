

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