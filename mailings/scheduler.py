from apscheduler.schedulers.background import BackgroundScheduler

from mailings.utils import send_mailing


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_mailing, 'interval', seconds=10)
    scheduler.start()
