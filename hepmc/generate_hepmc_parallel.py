# Code to parallely generate hepmc files
# run with nohup python generate_hepmc_parallel.py &

import multiprocessing
import numpy as np
import subprocess

def get_mom_range(pid):
    if pid == 211:
        start = 3.5
    elif pid == 2212:
        start = 24
    elif pid == 321:
        start = 12.5
    else:
        raise ValueError("Invalid PID")

    return np.concatenate((np.arange(start, 31.5, 0.5), np.arange(32, 50.5, 2), np.arange(55, 60.5, 5)))

nevents=200
# bin_id_range = np.arange(0,21,1)
bin_id_range = [5,10,15,20]  #eta_bins
pid_range=[211,2212,321]
phi_range=[0,1,2,3,4,5,6,7]

print("Bin IDs: {}, {} bins".format(bin_id_range,len(bin_id_range)))

print("PID range: {}".format(pid_range))

print(f"Phi range {phi_range}")

# for pid in pid_range:
#     print(f"files for pid {pid}: {len(bin_id_range)*len(get_mom_range(pid))}, each with {nevents} events")
#     #print("Total files to be generated: {}, each with {{} events".format(len(bin_id_range)*len(mom_range)*len(pid_range),nevents))

def execute_statement(statement):
  subprocess.run(statement, shell=True)

def generate_and_execute_statements():
    print("Generating statements...")

    statements = []
    for pid in pid_range:
        #mom_range = get_mom_range(pid)
        mom_range = [5,15,25,35,45,55]
        for bin in bin_id_range:
            for mom in mom_range:
                for phi in phi_range:
                    statement = f"root -l 'drich_hepmc_writer_sp.C({nevents},{bin},{phi},{mom},{pid})'"
                    statements.append(statement)

    # Execute statements (uncomment if using multiprocessing)
    with multiprocessing.Pool() as pool:
        pool.map(execute_statement, statements)

    # Execute statements sequentially (for demonstration)
    #for statement in statements:
    #    print(f"Executing: {statement}")
    #    run(statement, shell=True)


if __name__ == "__main__":
    generate_and_execute_statements()
