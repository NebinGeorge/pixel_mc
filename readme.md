# HEPMC and Analysis files for pixel analysis in EIC-dRICH (mc version)

Analysis done by Nebin George 

Total files:581 hepmc files & 571 analysis files

The HEPMC filenames have the format PID_MOMENTUM_ETABIN_PHIBIN.hepmc.Each file has 200 events. 

The Analysis filenames have the format PID_MOMENTUM_ETABIN_PHI.root.Each file has 200 events.

The HEPMC and Analysis files are generated for the follwing PID, MOMENTUM, ETA and PHI values.

Mometum values are:  [5,15,25,35,45,55] in Gev/C.In the code, internally momentum is smeared between +/- 0.1 GeV.

PID's are: [211(Pion),321(Kaon),2212(Proton)] 

ETABIN : [5, 10, 15, 20], corresponding ETA VALUE: [2, 2.5, 3, 3.5].

{1.999, 2.001}, //etaBin 5   
{2.499, 2.501}, //etaBin 10    
{2.999, 3.001}, //etaBin 15    
{3.499, 3.501}  //etaBin 20  

PHI BIN : [0,1,2,3,4,5,6,7], corresponding PHI VALUE: [0, 45, 90, 135, 180, 225, 270, 315] in degrees.








