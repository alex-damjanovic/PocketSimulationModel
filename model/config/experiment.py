experimental_setups = {
    "test1": {
        "config_option_state": "Test",
        "config_option_params": "Test",
        "monte_carlo_n": 1,
        "T": 365,
    },
    "Base": {
        "config_option_state": "Base",
        "config_option_params": "Base",
        "monte_carlo_n": 1,
        "T": 365,
    },
    "BaseDynamic": {
        "config_option_state": "Base",
        "config_option_params": "BaseDynamic",
        "monte_carlo_n": 1,
        "T": 365,
    },
    "BaseEvent": {
        "config_option_state": "Base",
        "config_option_params": "BaseEvent",
        "monte_carlo_n": 1,
        "T": 365,
    },
}

for i in range(1, 28):
    experimental_setups["Test{}".format(i)] = {
        "config_option_state": "Base",
        "config_option_params": "Test{}".format(i),
        "monte_carlo_n": 30,
        "T": 365,
    }

for i in range(1, 289):
    experimental_setups["gateway_viability_sweep_ag1_{}".format(i)] = {
        "config_option_state": "Base",
        "config_option_params": "gateway_viability_sweep_ag1_{}".format(i),
        "monte_carlo_n": 1,
        "T": 365,
    }

for i in range(1, 49):
    experimental_setups["network_failures_service_ag1_{}".format(i)] = {
        "config_option_state": "Base",
        "config_option_params": "network_failures_service_ag1_{}".format(i),
        "monte_carlo_n": 1,
        "T": 365,
    }

for i in range(1, 1153):
    experimental_setups["servicer_viability_ag1_{}".format(i)] = {
        "config_option_state": "Base",
        "config_option_params": "servicer_viability_ag1_{}".format(i),
        "monte_carlo_n": 1,
        "T": 365,
    }
