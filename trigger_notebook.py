import os
from azure.identity import ClientSecretCredential
from azureml.core import Workspace
from azureml.core.compute import ComputeTarget
from azureml.core import Experiment
from azureml.core.run import Run

tenant_id = "ee10b4ad-568d-4026-9cca-3f47d86d0d04"
client_id = "c8533615-50a1-4b7b-87a3-0e1655b2c357"
client_secret = "QxC8Q~b_m1EYYfKMuSkRRjhzp-5L9ZlEJTjhZdsc"
subscription_id = "89932198-e74d-4f28-b227-95f2729192c0"
resource_group = "rg-dp100-labs"
workspace_name = "mlw-dp100-labs"

credentials = ClientSecretCredential(
tenant_id = tenant_id,
client_id = client_id,
client_secret = client_secret)

ws = Workspace(
subscription_id = subscription_id,
resource_group = resource_group,
workspace_name = workspace_name,
auth = credentials)

compute_target = ComputeTarget(worspace = ws, name = 'trial-compute')

run = experiment.submit(
script = 'Users/shudharsananm.1989/my_own_code/github_actions_testing.py',
compute_target = compute_target)


print(f'Notebbook execution triggered with run ID: {run_id}')
