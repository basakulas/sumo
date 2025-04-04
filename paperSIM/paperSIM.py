import traci

def start_sumo_gui(sumo_config):
    """
    Starts SUMO-GUI with the given configuration file.
    :param sumo_config: Path to the SUMO configuration file (.sumocfg)
    """
    traci.start(["sumo-gui", "-c", sumo_config])

def run_simulation():
    """
    Runs the SUMO simulation using TraCI and keeps vehicles in specified lanes.
    """
    step = 0
    while step < 50:  # Run for 30 simulation steps (30 seconds)
        traci.simulationStep()
        
        if step < 41:
            traci.vehicle.setSpeedMode("t_0",96)
            traci.vehicle.setSpeedMode("t_1",96)
            traci.vehicle.setSpeed("t_0",13)
            traci.vehicle.setSpeed("t_1",13)

        if step < 2:
            #t_0 == PTW
            #t_1 == VEH
            traci.vehicle.changeLane("t_0", 1,2)  # Keep t_0 at lane 0
            traci.vehicle.changeLane("t_1", 2,2)  # Keep t_2 at lane 1
       
        if 2 < step < 4:
        
            traci.vehicle.changeLane("t_0", 0,2)  # Keep t_0 at lane 0
            traci.vehicle.changeLane("t_1", 1,2)  # Keep t_2 at lane 1
            
        if 5 < step < 12:
        
            traci.vehicle.changeLane("t_0", 1,2)  # Keep t_0 at lane 0
            traci.vehicle.changeLane("t_1", 2,2)  # Keep t_2 at lane 1
            
        if 12 < step < 14:
        
            traci.vehicle.changeLane("t_0", 0,2)  # Keep t_0 at lane 0
            traci.vehicle.changeLane("t_1", 1,2)  # Keep t_2 at lane 1
            
        if 14 < step < 16:
            traci.vehicle.changeLane("t_0", 1,2)  # Keep t_0 at lane 0
            traci.vehicle.changeLane("t_1", 2,2)  # Keep t_2 at lane 1
        
            

        step += 1

if __name__ == "__main__":
    sumo_config_path = "/home/ulas/Desktop/paperSIM/paperSIM.sumocfg"  # Update with your actual file path
    start_sumo_gui(sumo_config_path)  # Start SUMO-GUI
    try:
        run_simulation()  # Run the simulation
    finally:
        traci.close()  # Ensure SUMO closes properly
