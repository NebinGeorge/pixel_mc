# HEPMC and Analysis files for pixel analysis in EIC-dRICH (mc version)
Pixel size analysis of EIC-dRICH SiPMs was studied by obtaining photon hit positions from digitized(includes pixel size uncertainity) and undigitized hits (actual coordinates, independent of pixel size). The following files were generated for undigitized hits(MC version):
Analysis done by Nebin George 

Total files:581 hepmc files & 577 analysis files

The HEPMC filenames have the format PID_MOMENTUM_ETABIN_PHIBIN.hepmc. Each file has 200 events. 

The Analysis filenames have the format PID_MOMENTUM_ETABIN_PHI.root. Each file has 200 events.

The HEPMC and Analysis files are generated for the following PID, MOMENTUM, ETA and PHI values.

Mometum values are: [5,15,25,35,45,55] in Gev/C.In the code, internally momentum is smeared between +/- 0.1 GeV/C.

PID's are: [211(Pion),321(Kaon),2212(Proton)] 

ETABIN : [5, 10, 15, 20], corresponding ETA VALUE: [2, 2.5, 3, 3.5].

| **Eta Bin** | **Range**         |
|-------------|-------------------|
| 5           | {1.999, 2.001}   |
| 10          | {2.499, 2.501}   |
| 15          | {2.999, 3.001}   |
| 20          | {3.499, 3.501}   |


PHI BIN : [0,1,2,3,4,5,6,7], corresponding PHI VALUE: [0, 45, 90, 135, 180, 225, 270, 315] in degrees.
| **Phi Bin** | **Phi Value(degrees)**         |
|-------------|-------------------|
| 0           | 0   |
| 1           | 45  |
| 2           | 90  |
| 3           | 135 |
| 4           | 180 |
| 5           | 225 |
| 6           | 270 |
| 7           | 315 |
Link for digitized hits files: https://github.com/NebinGeorge/pixel










