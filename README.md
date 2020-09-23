# cs-6250-topology-test-script
Simple Pytest script to test the topologies for Project 4 of the CS6250 OMSCS Fall 20 class.

# How to use

Disclaimer: Only tested on the VM provided. Python 2.7.6 and pytest 2.5.1 are already installed on the VM.

Clone/Download the repository and extract into the project's root folder.

Run `py.test test_topologies.py` to run the tests with the default settings.

# Customizing

- If your reference files folder isn't named `reference`, you can optionally use an environment variable to set it.
e.g.: If your reference logs are in a folder called `results`, run `REF_DIR=results py.test test_topologies.py`.

- If you want to skip/add some tests, currently you will have to do it by editing the file itself. Edit the file and comment/add the lines inside the @pytest.mark.parametrize decorator corresponding to the tests you want to skip or add.