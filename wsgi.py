#!/usr/bin/env python
import os
from flaskapp import app as application

#
# Below for testing only
#
if __name__ == '__main__':
	application.debug=True
	port = int(os.environ.get("PORT", 5000))
	application.run(host='0.0.0.0', port=port)
