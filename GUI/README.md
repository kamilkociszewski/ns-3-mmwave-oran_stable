Running the project:

Step 1 - Clone the project 
    git clone <project link>
    
Step 2 - Start up the project with env variables present
    NS3_HOST=''' NS3_PASSWORD='' NS3_SCRIPT_PATH=''' NS3_USER='' docker-compose up --build
    Where ns3_host is hostname where the ns3_sim is located, ns3_script path is path on the host to the
    stop_ns3.py and run_simulation.sh scripts and finally user and password are credential for user with
    privilages to run said scripts
    
Step 3 - Copy sim_data_pusher.py to the ns3 folder. Edit database host (if running on the same machine it's going to
    localhost:8086)
    
Step 4 - GUI is going to be available on port 8000 of localhost from the host machine


