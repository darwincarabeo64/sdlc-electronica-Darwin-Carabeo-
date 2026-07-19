from fsm_demo1 import TrafficLightFSM, TrafficLightState


# Test 1: Verificar el estado inicial
def test_estado_inicial():
    fsm = TrafficLightFSM()
    assert fsm.state == TrafficLightState.RED


# Test 2: Verificar la transición RED -> GREEN
def test_transicion_red_green():
    fsm = TrafficLightFSM()
    fsm.transition()
    assert fsm.state == TrafficLightState.GREEN


# Test 3: Verificar el ciclo completo RED -> GREEN -> YELLOW -> RED
def test_ciclo_completo():
    fsm = TrafficLightFSM()

    fsm.transition()   # RED -> GREEN
    fsm.transition()   # GREEN -> YELLOW
    fsm.transition()   # YELLOW -> RED

    assert fsm.state == TrafficLightState.RED


# Test 4: Verificar el contador de transiciones
def test_conteo_ciclos():
    fsm = TrafficLightFSM()

    fsm.transition()
    fsm.transition()
    fsm.transition()

    assert fsm.cycle_count == 3