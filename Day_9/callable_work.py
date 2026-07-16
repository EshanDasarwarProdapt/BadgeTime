'''
Case study: Food delivery application
Imagine you're developing a food delivery app
The app can run in three envs

Development
Testing 
Production
'''

class Devconfig:
    database = "sqlite.db"
    debug = True

class Testconfig:
    database = "test.db"
    debug = True

class prodconfig:
    database = "prod.db"
    debug = False


#step2 - define a configuration factory

def getconfig(environment):
    if environment == "development":
        return Devconfig()
    elif environment == "testing":
        return Testconfig()
    elif environment == "production":
        return prodconfig()
    else:
        raise ValueError("Invalid environment specified")
    
env = "production"

config = getconfig(env)

print(f"Database: {config.database}, Debug: {config.debug}")