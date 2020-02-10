"""
Script that starts up the development web server with our application
"""
from src import WHM as whm

if __name__ == '__main__':
    whm.run(host='0.0.0.0', port=5001, debug=True)
