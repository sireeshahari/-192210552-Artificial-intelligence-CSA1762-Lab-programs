def water_jug_problem():
    jug_a = 0
    jug_b = 0
    target = 2
    print(f"Initial state: Jug A={jug_a} liters, Jug B={jug_b} liters")
    jug_b = 4
    print(f"Fill Jug B: Jug A={jug_a} liters, Jug B={jug_b} liters")
    jug_a = 3
    jug_b = 1
    print(f"Pour Jug B into Jug A: Jug A={jug_a} liters, Jug B={jug_b} liters")
    jug_a = 0
    print(f"Empty Jug A: Jug A={jug_a} liters, Jug B={jug_b} liters")
    jug_a = 1
    jug_b = 0
    print(f"Pour Jug B into Jug A: Jug A={jug_a} liters, Jug B={jug_b} liters")
    jug_b = 4
    print(f"Fill Jug B: Jug A={jug_a} liters, Jug B={jug_b} liters")
    jug_a = 3
    jug_b = 2
    print(f"Pour Jug B into Jug A: Jug A={jug_a} liters, Jug B={jug_b} liters")
    if jug_b == target:
        print(f"Goal achieved! Jug B has exactly {target} liters.")
    else:
        print("Goal not achieved.")
water_jug_problem()
