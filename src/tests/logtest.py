
if __name__ == '__main__':
	
	import logging, sys
	FORMAT = '%(asctime)-15s %(message)s'
	logging.basicConfig(format=FORMAT, stream=sys.stderr)
	logging.getLogger("log.test").setLevel(logging.DEBUG)

	log = logging.getLogger("log.test")
	
	log.debug("isto eh um debug!")
	
	log.info("isto eh um info!")
	
	log.warning("isto eh um warning!")
	
	log.error("isto eh um error!")
	
	log.critical("isto eh um critical!")
