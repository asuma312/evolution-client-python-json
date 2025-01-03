from ..models import return_models


class InstanceService:
    def __init__(self, client):
        self.client = client

    def fetch_instances(self)->return_models.instance.FetchInstance:
        response = self.client.get('instance/fetchInstances')
        return return_models.instance.FetchInstance.from_dict(response)

    def create_instance(self, config)->return_models.instance.CreateInstance:
        response = self.client.post('instance/create', data=config.__dict__)
        return return_models.instance.CreateInstance.from_dict(response)