from langgraph.graph import StateGraph, END

from src.agent.state import BenchmarkState

from src.agent.nodes.scenario_node import ScenarioNode
from src.agent.nodes.dataset_node import DatasetNode
from src.agent.nodes.noise_node import NoiseNode
from src.agent.nodes.ground_truth_node import GroundTruthNode


# =========================================================
# NODE WRAPPERS
# =========================================================

def scenario_step(state: BenchmarkState):
    node = ScenarioNode(
        "artifacts/scenarios/scenario_v1.yaml"
    )
    return node(state)


def dataset_step(state: BenchmarkState):
    node = DatasetNode()
    return node(state)


def noise_step(state: BenchmarkState):
    node = NoiseNode()
    return node(state)


def ground_truth_step(state: BenchmarkState):
    node = GroundTruthNode()
    return node(state)


# =========================================================
# GRAPH FACTORY
# =========================================================

def build_graph():

    workflow = StateGraph(BenchmarkState)

    # -----------------------------------------------------
    # Register nodes
    # -----------------------------------------------------

    workflow.add_node("scenario", scenario_step)
    workflow.add_node("dataset", dataset_step)
    workflow.add_node("noise", noise_step)
    workflow.add_node("ground_truth", ground_truth_step)

    # -----------------------------------------------------
    # Execution flow
    # -----------------------------------------------------

    workflow.set_entry_point("scenario")

    workflow.add_edge("scenario", "dataset")
    workflow.add_edge("dataset", "noise")
    workflow.add_edge("noise", "ground_truth")

    workflow.add_edge("ground_truth", END)

    return workflow.compile()


# # =========================================================
# # EXECUTION ENTRY POINT
# # =========================================================

# def run_pipeline():

#     graph = build_graph()

#     initial_state = BenchmarkState()

#     result = graph.invoke(initial_state)

#     print("\n====================================")
#     print("PIPELINE FINISHED")
#     print("====================================")

#     print(result)

#     return result


# if __name__ == "__main__":
#     run_pipeline()