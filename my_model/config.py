from os import path

import my_model

base_path = path.dirname(path.dirname(my_model.__file__))
workspace_path = path.join(base_path, 'workspace')
data_path = path.join(workspace_path, 'data')
models_path = path.join(workspace_path, 'models')
