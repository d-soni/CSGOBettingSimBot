from mySettings import *
from databses import *
from reddit import *
from checkResults import *
from sqlalchemy.orm import sessionmaker

def main():
	engine = createEngine()
	createTables(engine)
	session = sessionmaker(bind=engine)

	processCommands(crawlSubmissions(), session)
	adjust(getToBeAdjusted(session), session)
