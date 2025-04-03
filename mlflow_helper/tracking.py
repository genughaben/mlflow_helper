from dataclasses import dataclass
from typing import Optional
import mlflow
from contextlib import contextmanager

@dataclass
class RunMeta:
    project_name: str
    mlops_level: int
    stage: str
    owner: Optional[str] = None
    use_case: Optional[str] = None
    kpi_target: Optional[str] = None
    data_version: Optional[str] = None
    experiment_summary: Optional[str] = None
    toolchain: Optional[str] = None

@contextmanager
def start_logged_run(meta: RunMeta):
    experiment_name = f"Project:{meta.project_name} - {meta.stage} - Level {meta.mlops_level}"
    mlflow.set_experiment(experiment_name)

    with mlflow.start_run() as run:
        # Required tags
        mlflow.set_tag("mlops_level", str(meta.mlops_level))
        mlflow.set_tag("stage", meta.stage)
        mlflow.set_tag("project_name", meta.project_name)

        # Optional tags
        optional_tags = {
            "owner": meta.owner,
            "use_case": meta.use_case,
            "kpi_target": meta.kpi_target,
            "data_version": meta.data_version,
            "experiment_summary": meta.experiment_summary,
            "toolchain": meta.toolchain,
        }
        for key, value in optional_tags.items():
            if value is not None:
                mlflow.set_tag(key, value)

        yield run
