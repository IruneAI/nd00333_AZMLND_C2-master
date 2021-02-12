from azureml.core import Workspace
from azureml.core.webservice import Webservice

# Requires the config to be downloaded first to the current working directory
ws = Workspace.from_config()

# Set with the deployment name
name = "bankmarketingprediction"

# load existing web service
service = Webservice(name=name, workspace=ws)
logs = service.get_logs()

for line in logs.split('\n'):
    print(line)
<<<<<<< HEAD
=======

>>>>>>> 65c84b93ec2f55d2ffed02b483ba70bac0ac6d0b
#enable app insights
service.update(enable_app_insights=True)
