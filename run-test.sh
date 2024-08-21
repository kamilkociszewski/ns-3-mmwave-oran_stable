#!/bin/bash
#set -x

N=1 # number of simulations
enableTraces=1 # enable generation of ns-3 traces 
e2lteEnabled=1 # enable e2 reports from lte macro cell
e2nrEnabled=1 # enable e2 reports from nr secondary cells
e2du=1 # enable reporting of DU PM containers
e2cuUp=1 # enable reporting of CU UP PM containers
e2cuCp=1 # enable reporting of CU CP PM containers
trafficModel=1 # Type of the traffic model at the transport layer [0,3], can generate full buffer traffic (0), half nodes in full buffer and half nodes in bursty (1), bursty traffic (2), mixed setup (3)
configuration=0 # 0: NR carrier at 850 MHz, low traffic | 1: NR carrier at 3.5 GHz, low traffic | 2: NR carrier at 28 GHz, high traffic
minSpeed=2.0 # minimum UE speed in m/s
maxSpeed=4.0 # maximum UE speed in m/s
simTime=1 # simulation time
e2TermIp="10.244.0.240" # actual E2term IP interface
basicCellId=1 # The next value will be the first cellId
ues=3 # Number of UEs for each mmWave ENB
reducedPmValues=0 # use reduced subset of pmValues
EnableE2FileLogging=1 # enable offline generation of data
controlPath="es_actions_for_ns3.csv" # full control file path

# Remove NoAuto on handover and Outage Threshold to use the Dynamic TTI HO
outageThreshold=-5.0 # use -5.0 when handover is not in NoAuto 
handoverMode="DynamicTtt"

# NS_LOG="KpmIndication"
# NS_LOG="RicControlMessage" 


for i in $(seq 1 $N); do
  echo "Running simulation $i out of $N";
  ./waf --run "scratch/scenario-one --RngRun=$i \
                                    --configuration=$configuration \
                                    --trafficModel=$trafficModel \
                                    --enableTraces=$enableTraces \
                                    --e2lteEnabled=$e2lteEnabled \
                                    --e2nrEnabled=$e2nrEnabled \
                                    --e2du=$e2du \
                                    --simTime=$simTime \
                                    --outageThreshold=$outageThreshold \
                                    --handoverMode=$handoverMode \
                                    --basicCellId=$basicCellId \
                                    --e2cuUp=$e2cuUp \
                                    --e2cuCp=$e2cuCp \
                                    --ues=$ues \
                                    --reducedPmValues=$reducedPmValues \
                                    --e2TermIp=$e2TermIp \
                                    --enableE2FileLogging=$EnableE2FileLogging \
                                    --minSpeed=$minSpeed\
                                    --maxSpeed=$maxSpeed\
                                    --ns3::LteEnbNetDevice::ControlFileName=$controlPath";# --gdb;
  sleep 1;
done
