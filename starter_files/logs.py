from azureml.core import Workspace
from azureml.core.webservice import Webservice

# Requires the config to be downloaded first to the current working directory
ws = Workspace.from_config()

# Set with the deployment name
name = "best-model-deploy"

# load existing web service
service = Webservice(name=name, workspace=ws)

# enable application insight
service.update(enable_app_insights=True)

logs = service.get_logs()

for line in logs.split('\n'):
<<<<<<< HEAD
    print(line)
=======
    print(line)

#enable app insights
service.update(enable_app_insights=True)
>>>>>>> b101e3191e3962d47a0b6daf3c5fd3ea1f7311d4
