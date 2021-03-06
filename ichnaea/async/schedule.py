from datetime import timedelta

from celery.schedules import crontab


CELERYBEAT_SCHEDULE = {
    'histogram-cell-yesterday': {
        'task': 'ichnaea.content.tasks.cell_histogram',
        'schedule': crontab(hour=0, minute=3),
        'args': (1, ),
    },
    'histogram-wifi-yesterday': {
        'task': 'ichnaea.content.tasks.wifi_histogram',
        'schedule': crontab(hour=0, minute=4),
        'args': (1, ),
    },
    'histogram-unique-cell-yesterday': {
        'task': 'ichnaea.content.tasks.unique_cell_histogram',
        'schedule': crontab(hour=0, minute=5),
        'args': (1, ),
    },
    'histogram-unique-wifi-yesterday': {
        'task': 'ichnaea.content.tasks.unique_wifi_histogram',
        'schedule': crontab(hour=0, minute=6),
        'args': (1, ),
    },
    'cell-location-update-1': {
        'task': 'ichnaea.tasks.cell_location_update',
        'schedule': timedelta(seconds=299),  # 13*23
        'args': (1, 10, 5000),
        'options': {'expires': 290},
    },
    'cell-location-update-10': {
        'task': 'ichnaea.tasks.cell_location_update',
        'schedule': timedelta(seconds=305),  # 5*61
        'args': (10, 1000, 1000),
        'options': {'expires': 295},
    },
    'cell-location-update-1000': {
        'task': 'ichnaea.tasks.cell_location_update',
        'schedule': timedelta(seconds=323),  # 17*19
        'args': (1000, 1000000, 100),
        'options': {'expires': 310},
    },
    'wifi-location-update-1': {
        'task': 'ichnaea.tasks.wifi_location_update',
        'schedule': timedelta(seconds=301),  # 7*43
        'args': (1, 10, 5000),
        'options': {'expires': 290},
    },
    'wifi-location-update-10': {
        'task': 'ichnaea.tasks.wifi_location_update',
        'schedule': timedelta(seconds=319),  # 11*29
        'args': (10, 1000, 1000),
        'options': {'expires': 310},
    },
    'wifi-location-update-1000': {
        'task': 'ichnaea.tasks.wifi_location_update',
        'schedule': timedelta(seconds=329),  # 7*47
        'args': (1000, 1000000, 100),
        'options': {'expires': 320},
    },
    'continuous-cell-scan-lacs': {
        'task': 'ichnaea.tasks.scan_lacs',
        'schedule': timedelta(seconds=3607),  # about an hour
        'args': (1000, ),
        'options': {'expires': 3511},
    },

    # TODO: start scheduling this once we handled the backlog
    # 'backfill-celltower-info': {
    #     'task': 'ichnaea.backfill.tasks.do_backfill',
    #     'schedule': crontab(hour=0, minute=15),
    # }

    's3-schedule-cellmeasure-archival': {
        'task': 'ichnaea.backup.tasks.schedule_cellmeasure_archival',
        'args': (100, 1000000),
        'schedule': crontab(hour=0, minute=7),
        'options': {'expires': 43200},
    },
    's3-write-cellbackups': {
        'task': 'ichnaea.backup.tasks.write_cellmeasure_s3_backups',
        'args': (100, 10000, 300),
        'schedule': crontab(hour=1, minute=7),
        'options': {'expires': 43200},
    },

    's3-schedule-wifimeasures-archival': {
        'task': 'ichnaea.backup.tasks.schedule_wifimeasure_archival',
        'args': (100, 1000000),
        'schedule': crontab(hour=0, minute=17),
        'options': {'expires': 43200},
    },
    's3-write-wifibackups': {
        'task': 'ichnaea.backup.tasks.write_wifimeasure_s3_backups',
        'args': (100, 10000, 300),
        'schedule': crontab(hour=1, minute=17),
        'options': {'expires': 43200},
    },

    's3-delete-wifimeasures': {
        'task': 'ichnaea.backup.tasks.delete_wifimeasure_records',
        'args': (100, 2, 300),
        'schedule': crontab(hour=2, minute=17),
        'options': {'expires': 43200},
    },
    's3-delete-cellmeasures': {
        'task': 'ichnaea.backup.tasks.delete_cellmeasure_records',
        'args': (100, 2, 300),
        'schedule': crontab(hour=2, minute=27),
        'options': {'expires': 43200},
    },
    'nightly-cell-unthrottle-messages': {
        'task': 'ichnaea.backup.tasks.cell_unthrottle_measures',
        'schedule': crontab(hour=3, minute=17),
        'args': (10000, 1000),
        'options': {'expires': 43200},
    },
    'nightly-wifi-unthrottle-messages': {
        'task': 'ichnaea.backup.tasks.wifi_unthrottle_measures',
        'schedule': crontab(hour=3, minute=27),
        'args': (10000, 1000),
        'options': {'expires': 43200},
    },

}
