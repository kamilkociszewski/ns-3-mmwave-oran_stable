/**
 * \defgroup topology Topology Input Readers
 *
 * \section topologyOverview Topology Input Readers Overview
 *
 * The topology modules aim at reading a topology file generated by an automatic topology generator.
 *
 * The process is divided in two steps:
 * - running a topology generator to build a topology file
 * - reading the topology file and build a ns-3 simulation
 *
 * Hence, model is focused on being able to read correctly the various topology formats.
 *
 * Currently there are three models:
 * - ns3::OrbisTopologyReader for Orbis 0.7 traces (http://sysnet.ucsd.edu/~pmahadevan/topo_research/topo.html)
 * - ns3::InetTopologyReader for Inet 3.0 traces (http://topology.eecs.umich.edu/inet/)
 * - ns3::RocketfuelTopologyReader for Rocketfuel traces (http://www.cs.washington.edu/research/networking/rocketfuel/)
 *
 * See the ns-3 modules manual for further information.
 *
 * Examples can be found in the directory src/topology-read/examples/
 */
