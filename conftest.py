import sys, os, json
if os.path.isdir("./.venv/lib/"):
    sys.path.append('null/site-packages')
def pytest_addoption(parser):
    parser.addoption("--stdin", action="append", default=[],
        help="json with the stdin to pass to test functions")
def pytest_generate_tests(metafunc):
    if 'stdin' in metafunc.fixturenames:
        metafunc.parametrize("stdin",metafunc.configuration.getoption('stdin'))
    if 'app' in metafunc.fixturenames:
        try:
          sys.path.append('.learn/dist')
          import cached_app
          metafunc.parametrize("app",[cached_app.execute_app])
        except SyntaxError:
          metafunc.parametrize("app",[lambda : None])
        except ImportError:
          metafunc.parametrize("app",[cached_app])
        except AttributeError:
          metafunc.parametrize("app",[cached_app])
    if 'configuration' in metafunc.fixturenames:
        metafunc.parametrize("configuration", [json.loads('{"port":3000,"address":"https://df46c42a-4704-499c-8b9f-48cf264a1cba.ws-us02.gitpod.io","editor":{"mode":"gitpod","version":"1.0.1"},"dirPath":"./.learn","configPath":"bc.json","outputPath":".learn/dist","publicPath":"/preview","exercisesPath":"./exercises","webpackTemplate":null,"actions":["build","test","reset"]}')])
