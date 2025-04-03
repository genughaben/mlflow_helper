# mlflow_helpers

`mlflow_helpers` provides utility functions to standardize and simplify MLflow experiment tracking, including setting up experiments with consistent naming conventions and tagging.

## Installation

Install the package using pip:

```bash
pip install mlflow_helpers

## Usage example:

from mlflow_helpers import RunMeta, start_logged_run
import mlflow

# Define the metadata for the run
meta = RunMeta(
    project_name="Example Project",
    mlops_level=1,
    stage="development",
    owner="your_name",
    use_case="classification",
    kpi_target="Accuracy > 90%",
    data_version="v1.0.0",
    experiment_summary="Initial development run with baseline model",
    toolchain="scikit-learn"
)

# Start the logged run
with start_logged_run(meta):
    # Your ML code here
    mlflow.log_param("param1", 0.5)
    mlflow.log_metric("accuracy", 0.92)
    mlflow.log_artifact("path/to/artifact")