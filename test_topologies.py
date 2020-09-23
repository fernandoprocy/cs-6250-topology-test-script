import pytest
import os
from subprocess import check_call, CalledProcessError, STDOUT

TEST_TOPOLOGIES = [
    # "BadTopo",  # Warning: It should always be []
    "SimpleTopo",
    "SimpleNegativeCycleTopo",
    "ComplexTopo",
    "SingleLoopTopo",
    # "LargeRandom",  # Warning: a bit heavy
    # "new_ComplexTopoHalfed",
    # "new_LongLoop",
    # "new_NegCycleWithBiNegLink",
    # "new_NoNegTopo",
    # "new_TailNegativeCycle",
    # "new_TailNegCycleWithBiNegLink",
    # "new_v2_SingleNode",
    # "new_v2_TwoNodesNeg",
    # "new_v2_TwoNodes",
    # "new_v2_TwoNodesUni",
    # "new_v2_VeryComplex2",
    # "new_v2_VeryComplex",
    # "new_YoutubeTopo",
    # "n_longAlternatingSeries",
    # "n_longNegSeries2",
    # "n_longNegSeries",
    # "n_longSeries",
    # "NodeDetectEarly",
    # "NodeDetectWithCycle",
    # "NoInOrOutLinks",
    # "SimpleNegativeCycle",
    # "SimpleOddLengthNegativeCycle",
    # "TwoNegCycles"
]

CURRENT_DIR = os.getcwd()
FNULL = open(os.devnull, 'w')
REFERENCE_DIR = os.getenv("REF_DIR", "reference")
REF_LOG_FILE_EXT = ".log"
RESULT_LOG_FILE_EXT = ".log"

def parse_line(line):
    # Receive raw line and return tuple (node, set(distance_vector))
    node, vectors = line.split(":")
    return (node, set(vectors.split(",")))

def read_file(filename_path):
    with open(os.path.join(CURRENT_DIR, filename_path), "r") as f:

        # Read the last output fragment only
        try:
            log = f.read().split("-----\n")[-2].splitlines()
        except: # Empty log file, probably from bad topologies
            log = []

    # Return list of (node, set(distance_vector))
    return [parse_line(line) for line in log]

def execute_algorithm(topo_name):
    try:
        check_call(["./run.sh", topo_name], stdout=FNULL, stderr=FNULL)
    except CalledProcessError:
        raise RuntimeError("Execution of algorithm on topology {} failed.".format(topo_name))


@pytest.mark.parametrize("topo_name", TEST_TOPOLOGIES)
def test_topology(topo_name):

    ## Setup phase
    execute_algorithm(topo_name)

    # Load reference and result logs
    ref_log = read_file(os.path.join(REFERENCE_DIR, topo_name + REF_LOG_FILE_EXT))
    result_log = read_file(topo_name + RESULT_LOG_FILE_EXT)

    # Then
    assert len(ref_log) == len(result_log)
    for i in range(len(ref_log)):
        node_ref, vectors_ref = ref_log[i]
        node_result, vectors_result = result_log[i]

        assert node_ref == node_result
        assert vectors_ref == vectors_result
    