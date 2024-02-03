import subprocess
import os
import glob

from steps.bdd_test_util import cli_call

from steps.coverage import saveCoverageFiles, createCoverageAggregate

def coverageEnabled(context):
    """
    Check if code coverage is enabled
    Args:
        context: Context object containing configuration
    Returns:
        bool: True if coverage is enabled, False otherwise
    Checks the "coverage" key in the userdata configuration to determine if coverage is enabled or not.
    """
    
    return context.config.userdata.get("coverage", "false") == "true"


def getDockerComposeFileArgsFromYamlFile(compose_yaml):
    """
    Extract docker-compose file arguments from a yaml file
    Args:
        compose_yaml: Path to docker-compose yaml file
    Returns:
        args: List of docker-compose command line arguments extracted from yaml file
    Processing Logic:
    - Split yaml file path on spaces to extract multiple file paths
    - Iterate over file paths and append "-f" flag followed by file path to args list
    - Return args list containing "-f" flags and file paths
    """
    
    parts = compose_yaml.split()
    args = []
    for part in parts:
        args = args + ["-f"] + [part]
    return args

def after_scenario(context, scenario):
    """
    Get logs and decompose composition after scenario
    Args:
        context: The behave context
        scenario: Information about the executed scenario
    Returns:
        None
    - Get logs from peer and chaincode containers if scenario failed or logs forced
    - Skip decomposition if tagged or if coverage is enabled
    - Stop containers to allow coverage file creation
    - Save coverage files before decomposing composition
    """
    
    get_logs = context.config.userdata.get("logs", "N")
    if get_logs.lower() == "force" or (scenario.status == "failed" and get_logs.lower() == "y" and "compose_containers" in context):
        print("Scenario {0} failed. Getting container logs".format(scenario.name))
        file_suffix = "_" + scenario.name.replace(" ", "_") + ".log"
        # get logs from the peer containers
        for containerData in context.compose_containers:
            with open(containerData.containerName + file_suffix, "w+") as logfile:
                sys_rc = subprocess.call(["docker", "logs", containerData.containerName], stdout=logfile, stderr=logfile)
                if sys_rc !=0 :
                    print("Cannot get logs for {0}. Docker rc = {1}".format(containerData.containerName,sys_rc))
        # get logs from the chaincode containers
        cc_output, cc_error, cc_returncode = \
            cli_call(["docker",  "ps", "-f",  "name=dev-", "--format", "{{.Names}}"], expect_success=True)
        for containerName in cc_output.splitlines():
            namePart,sep,junk = containerName.rpartition("-")
            with open(namePart + file_suffix, "w+") as logfile:
                sys_rc = subprocess.call(["docker", "logs", containerName], stdout=logfile, stderr=logfile)
                if sys_rc !=0 :
                    print("Cannot get logs for {0}. Docker rc = {1}".format(namepart,sys_rc))
    if 'doNotDecompose' in scenario.tags:
        if 'compose_yaml' in context:
            print("Not going to decompose after scenario {0}, with yaml '{1}'".format(scenario.name, context.compose_yaml))
    elif 'composition' in context:
        if coverageEnabled(context):
            # First stop the containers to allow for coverage files to be created.
            context.composition.issueCommand(["stop"])
            #Save the coverage files for this scenario before removing containers
            containerNames = [containerData.containerName for  containerData in context.compose_containers]
            saveCoverageFiles("coverage", scenario.name.replace(" ", "_"), containerNames, "cov")
        context.composition.decompose()


# stop any running peer that could get in the way before starting the tests
def before_all(context):
        """Stops the peer node before all tests
        Args:
            context: Context object for test framework
        Returns:
            None: Does not return anything
        - Calls the peer node stop command to shutdown the peer before tests
        - Uses the cli_call function from the test framework to execute the command
        - Passes expect_success=False since the command may fail if node is already stopped
        - Stops the peer node to reset the environment before running each test"""
        
        cli_call(["../build/bin/peer", "node", "stop"], expect_success=False)

# stop any running peer that could get in the way before starting the tests
def after_all(context):
    """Checks if any tests failed and aggregates coverage if enabled
    Args:
        context: Context object containing test run information
    Returns:
        None: Does not return anything, just prints status and aggregates coverage
    - Checks the context.failed attribute to see if any tests failed
    - If coverage is enabled, aggregates coverage data across all tests
    """
    
    print("context.failed = {0}".format(context.failed))

    if coverageEnabled(context):
        createCoverageAggregate()
