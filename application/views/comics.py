from flask.views import MethodView
from flask import request


class SearchComic(MethodView):
    def get(self):
        # Library import
        from application.utils.comics import Comics
        from application.utils.characters import Characters

        # Default Values
        response_dict = {
        }

        list_characters = ['character', 'characters']
        list_comics = ['comic', 'comics']

        # Get params
        keyword_param = request.args.get(key='keyword', default='')
        type_param = request.args.get(key='type', default='')

        # Get Characters
        if type_param in list_characters or not type_param:
            params = ''
            if keyword_param:
                params = f'nameStartsWith={keyword_param}'
            response_dict['characters'] = Characters.get_characters(
                params=params
            )

        # Get Comics
        if type_param in list_comics or not type_param:
            params = ''
            if keyword_param:
                params = f'title={keyword_param}'
            response_dict['comics'] = Comics.get_comics(
                params=params
            )
        has_content = response_dict['comics'] or response_dict['characters']
        code = 200 if has_content else 404

        return response_dict, code
