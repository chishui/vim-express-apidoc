import re
from functools import wraps

doc = '''@api {%s} %s
  @apiName
  @apiGroup

  @apiPermission Authorized User

  @apiParam
  @apiParamExample {JSON} Request Body Example:
      {
      }

  @apiSuccessExample Success-Response:
      HTTP/1.1 200 OK
      {
          "error": 0,
          "data": {}
      }

  @apiError (error code) 14 "Unauthorized request"

  @apiErrorExample Error-Response:
      HTTP/1.1 200 OK
      {
      }

 @apiExample {curl} Example usage:
      curl -H "Content-Type: application/json" \\
      -d { \\
      }\\
      -X %s http://localhost:3000/api/v1%s
'''

def add_js_comment(func):
    @wraps(func)
    def wrapper():
        doc = func()
        lines = doc.split('\n')
        lines = ['* ' + i for i in lines]
        return '/**\n' + '\n'.join(lines) + '*/'
    return wrapper

@add_js_comment
def get_doc():
    global doc
    return doc

def normal(str):
    vim.command("normal "+str)

def get_http_method(line):
    r = re.search(r'router.(get|put|post|patch|delete)', line)
    if r and len(r.groups()) >= 1:
        return r.groups()[0].upper()
    return None

def get_url(line):
    r = re.search(r'\'(/[:a-z/\\\+\(\)]+)\'', line)
    if r and len(r.groups()) >= 1:
        return r.groups()[0]
    return None

def main():
    try:
        import vim
        import string
        line = vim.current.line
        pos = vim.current.buffer.range(vim.current.range.start - 1, vim.current.range.end)

        method = get_http_method(line)
        url = get_url(line)
        if method and url:
            doc = get_doc()
            newdoc = doc % (method, url, method, url)
            pos.append(newdoc.split('\n'))

    except ImportError, e:
        print 'error'

