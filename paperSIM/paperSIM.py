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
    
    while traci.simulation.getMinExpectedNumber()>0:  # Run for 30 simulation steps (30 seconds)
        traci.simulationStep()
        
        #30km/h = 8.33 m/s
        #35km/h = 9.72 m/s
        #40km/h = 11.11 m/s
        #45km/h = 12.5 m/s
        #50km/h = 13.89 m/s
    
        setSpeed("PTW") #PTW
        setSpeed("VEH") #VEH
        

   
def setSpeed(veh_id):
    if veh_id in traci.vehicle.getIDList():
       traci.vehicle.setSpeedMode(veh_id,96)
       traci.vehicle.setSpeed(veh_id,13.89)
    	   
   

if __name__ == "__main__":
    sumo_config_path = "/home/ulas/sumofork/sumo/paperSIM/paperSIM.sumocfg"  # Update with your actual file path
    start_sumo_gui(sumo_config_path)  # Start SUMO-GUI
    try:
        run_simulation()  # Run the simulation
    finally:
        traci.close()  # Ensure SUMO closes properly
