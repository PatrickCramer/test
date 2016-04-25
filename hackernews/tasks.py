from celery.task.schedules import crontab
from celery.decorators import periodic_task
from hackernews import hnapi
from celery.utils.log import get_task_logger
from scraper import scrape

logger = get_task_logger(__name__)

# A periodic task that will run every minute (the symbol "*" means every)
@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def fetch_hnapi():
    logger.info("Start task : Get info from hackernews")
    hnapi.index()
    logger.info("Task : Get info from hackernews - finished")

@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def fetch_scraper():
    logger.info("Start task : Scraping volkskrant")
    scrape.scrape_vk()
    logger.info("Task : Scraping volkskrant - finished")

@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def fetch_scraper_parool():
    logger.info("Start task : Scraping Parool")
    scrape.scrape_parool()
    logger.info("Task : Scraping Parool - finished")



