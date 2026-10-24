import logging

logging.basicConfig(
    level=logging.INFO,
                    format=" %(asctime)s %(levelname)s %(message)s"
                    )

row_count =5000
file_path ="roaster_file.csv"

logging.info("Read %d rows from %s file",row_count,file_path)
logging.error("Read %d rows from %s file",row_count,file_path)

# logging.warning("Files are not available in pathe")
# logging.info("Files are not available in pathe")
# logging.debug("Start Debugging")
# logging.error("failed")
# logging.critical("database connection lost")