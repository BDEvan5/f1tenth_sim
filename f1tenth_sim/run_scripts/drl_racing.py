from f1tenth_sim.run_scripts.testing_functions import *
import numpy as np 
import torch
from f1tenth_sim.simulator import F1TenthSim_TrueLocation, F1TenthSim
from f1tenth_sim.drl_racing.EndToEndAgent import EndToEndAgent, TrainEndToEndAgent

# from f1tenth_sim.drl_racing.agents import TrainingAgent, TestingAgent
from f1tenth_sim.data_tools.specific_plotting.plot_drl_training import plot_drl_training


def seed_randomness(random_seed):
    np.random.seed(random_seed)
    torch.use_deterministic_algorithms(True)
    torch.manual_seed(random_seed)
    


def train_and_test_agents():
    seed_randomness(10)
    train_map = "mco"
    # train_map = "gbr" # test_id is the training map.
    # test_id = "TestTD3"
    test_id = "TestSAC2"

    training_agent = TrainEndToEndAgent(train_map, test_id)
    simulate_training_steps(training_agent, train_map, test_id)
    plot_drl_training(training_agent.name, test_id)

    testing_agent = EndToEndAgent(test_id)
    test_mapless_all_maps(testing_agent, test_id)


train_and_test_agents()


