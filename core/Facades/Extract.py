#---------------------------------------------------------#
# Update Script Path                                      #
#---------------------------------------------------------#

from os.path import abspath, join, dirname
import sys

project_directory = abspath(join(dirname(__file__), '../../'))
if project_directory not in sys.path:
    sys.path.insert(0, project_directory)

#---------------------------------------------------------#
# Facade ETL Extract                                      #
# Last Modification: 05-02-2024                           #
# Developers:                                             #
# -------------    Raul Mauricio Uñate Castro             #
#---------------------------------------------------------#

# Module Imports
from core.Clarity.Logger import Logger

# Facade Extract execution
class Extract:
    
    # ----------------------------------------------------------------------------------------------------#
    # Execute Command Without Reponse                                                                     #
    # ----------------------------------------------------------------------------------------------------#
    def __init__(self, etlprocessclass):
        
        # Log Registration
        Logger().info(f"Extract Classs Executed: {etlprocessclass.__class__.__name__}")
        
        # Ejecucion del Metodo del Proceso.
        self.data = etlprocessclass.handle()
    
    # ----------------------------------------------------------------------------------------------------#
    # Reponse Data Las Process                                                                            #
    # ----------------------------------------------------------------------------------------------------#
    def response(self):
        return self.data
        