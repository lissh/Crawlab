from db.manager import db_manager
from routes.base import BaseApi
from utils import jsonify


class DeployApi(BaseApi):
    col_name = 'deploys'

    arguments = (
        ('spider_id', str),
        ('node_id', str),
    )

    def get(self, id: str = None, action: str = None) -> (dict, tuple):
        """
        GET method of DeployAPI.
        :param id: deploy_id
        :param action: action
        """
        # action by id
        if action is not None:
            if not hasattr(self, action):
                return {
                           'status': 'ok',
                           'code': 400,
                           'error': 'action "%s" invalid' % action
                       }, 400
            return getattr(self, action)(id)

        # get one node
        elif id is not None:
            return jsonify(db_manager.get('deploys', id=id))

        # get a list of items
        else:
            items = db_manager.list('deploys', {})
            deploys = []
            for item in items:
                spider_id = item['spider_id']
                spider = db_manager.get('spiders', id=str(spider_id))
                if spider is None:
                    db_manager.remove('deploys', {'spider_id':spider_id})
                item['spider_name'] = spider['name']
                deploys.append(item)
            return {
                'status': 'ok',
                'items': jsonify(deploys)
            }
