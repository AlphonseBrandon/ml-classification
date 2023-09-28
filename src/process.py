# """
# This is the demo code that uses hydra to access the parameters in under the directory config.

# Author: Khuyen Tran
# """

# import hydra
# from omegaconf import DictConfig


# @hydra.main(config_path="../config", config_name="main", version_base=None)
# def process_data(config: DictConfig):
#     """Function to process the data"""

#     print(f"Process data using {config.data.raw}")
# #     print(f"Columns used: {config.process.use_columns}")

# # def printHello():
# #     print("Hello world")


# if __name__ == "__main__":
#     process_data()

from hydra import compose, initialize

with initialize(version_base=None, config_path="../config/"):
    cfg = compose(config_name="main.yaml")
    print(f"Process data using {cfg.data.raw}")


def hello():
    pass
