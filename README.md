# cs-6250-topology-test-script
Simple Pytest script to test the topologies for Project 4 of the CS6250 OMSCS Fall 20 class.

# Disclaimer

This is by no means an official tool. It has been provided as an aid for students to test their code output, but getting a pass here doesn't guarantee passing the autograder. If you decide to use this piece of software, keep that in mind!

# How to use

Disclaimer: Only tested on the VM provided. Python 2.7.6 and pytest 2.5.1 are already installed on the VM.

Clone/Download the repository and extract into the project's root folder.

Run `py.test test_topologies.py` inside the project's root folder to run the tests with the default settings.

# Customizing

- If your reference files folder isn't named `reference`, you can optionally use an environment variable to set it.
e.g.: If your reference logs are in a folder called `results`, run `REF_DIR=results py.test test_topologies.py`.

- If you want to skip/add some tests, currently you will have to do it by editing the file itself. Edit the file and comment/add the lines inside the TEST_TOPOLOGIES list corresponding to the tests you want to skip or add.


# Troubleshooting

- If you're getting errors like len(ref_log) == 0, check if the file has the correct without carriage returns. If they have carriage returns, run something like `dos2unix` on the VM to remove them.